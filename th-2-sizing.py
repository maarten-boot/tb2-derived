# Thunderbird 2 redesign - rough first-order sizing model (see th-2-re-design-ideas.md sections 8-10)
# Run: python3 th-2-sizing.py   - edit the calls at the bottom to try variants.
import math
g, R_AIR = 9.81, 287.05
RHO0 = 1.225
RANGE_KM, HOVER_MIN, RESERVE = 1500, 4, 0.10

def rho(h, t_c):
    """Air density at altitude h [m] and actual temperature t_c [degC]."""
    p = 101325*(1-2.25577e-5*h)**5.25588
    return p/(R_AIR*(t_c+273.15))

CONDITIONS = [  # (label, altitude m, temperature degC) - includes warming margin
    ("Sea level 15 C (ISA)",            0, 15),
    ("Sahel / desert SL 50 C",          0, 50),
    ("E-Africa highlands 2,500 m 40 C", 2500, 40),
    ("Andes altiplano 4,000 m 25 C",    4000, 25),
    ("Himalaya 5,000 m 15 C",           5000, 15),
]

def hover_power(W, r, A):          # W in kg; ducted fans, expanded wake, 80 % eff., 1.15 thrust margin
    T = 1.15*W*g
    return T**1.5/(2*math.sqrt(r*A))/0.80

def run(name, W_t, fans, struct_frac, jets, LD, cruise, sto_gain, design=("SL ISA", 0, 15), quiet=False, hold_t=0.0):
    W = W_t*1000
    nf = len(fans)
    A = sum(math.pi*(d/2)**2 for d in fans)
    r_d = rho(design[1], design[2]); sig_d = r_d/RHO0
    P_inst = 1.2*hover_power(W, r_d, A)/sig_d      # SL rating so that 1.2x hover power remains at design point
    v = math.sqrt(1.15*W*g/(RHO0*A))
    # fan-out capability: 6+ fans in 3 lengthwise pairs, middle pair at CG -> worst fans need 1.5x nominal
    k = 1.5*1.05/1.15 if nf >= 6 else 1.0
    m_shaft = P_inst/1000/8*1.3
    # engines are flat-rated: turbines sized for thin/hot air (P_inst), but the gearboxes only
    # carry the shaft power actually needed at the design point (1.2 x hover power there)
    P_shaft = 1.2*hover_power(W, r_d, A)
    m_drive = 0.22*P_shaft/1000*(0.5+0.5*k**1.5) + 0.015*W*(nf/4)**0.5
    m_fans  = 20.0*A*(nf/4)**0.25*(k**0.5)         # ducted fan + duct ~20 kg per m2 of disk
    W_sto = W*(1+sto_gain)
    m_struct = 0.04*W_sto + (struct_frac-0.04)*W*(max(2.5*W, 2.0*W_sto)/(2.5*W))**0.6
    m_sys = 0.07*W + 3000
    m_hold = hold_t*1000                           # extra floor + corridor walls for a maximised hold (notes §14)
    m_jets, Tjet = 0, 0
    if jets:
        Tjet = 0.9*W*g/LD/jets['lapse']*1.3
        m_jets = Tjet/(4.5*g)
    hover_fuel = hover_power(W, RHO0, A)/1000*0.27*HOVER_MIN/60
    W0 = W - hover_fuel
    K = cruise*LD/(0.6/3600) if jets else 0.75*LD/(g*0.28/3.6e6)
    fuel = (hover_fuel + W0*(1-math.exp(-RANGE_KM*1000/K)))*(1+RESERVE)
    fuel_sto = W_sto*(1-math.exp(-RANGE_KM*1000/K))*(1+RESERVE)
    empty = m_shaft+m_drive+m_fans+m_struct+m_sys+m_jets+m_hold
    pay = W-empty-fuel; pay_sto = W_sto-empty-fuel_sto
    res = {'empty':empty/1000,'pay':pay/1000,'pay_sto':pay_sto/1000,'P':P_inst/1e6,'hot':{}}
    for lab,h,t in CONDITIONS:
        r = rho(h,t); P_av = min(P_inst*(r/RHO0), P_shaft)/1.2   # engine lapse, gearbox limit
        Wmax = (P_av*2*math.sqrt(r*A)*0.80)**(2/3)/(1.15*g)
        res['hot'][lab] = (min(Wmax,W)-empty-fuel)/1000
    if not quiet:
        print(f"\n== {name}: {W_t} t VTOL, {nf} fans x {fans[0]} m ({A:.0f} m2), power sized for {design[0]}")
        print(f"  installed {P_inst/1e6:.0f} MW (SL) | downwash {v:.0f} m/s | fan-out capable: {'yes' if nf>=6 else 'NO'}")
        print(f"  shafts {m_shaft/1e3:.1f} | drive {m_drive/1e3:.1f} | fans {m_fans/1e3:.1f} | struct {m_struct/1e3:.1f} | sys {m_sys/1e3:.1f} | jets {m_jets/1e3:.1f} | hold {m_hold/1e3:.1f}  -> EMPTY {empty/1e3:.1f} t")
        print(f"  fuel {fuel/1e3:.1f} t | PAYLOAD VTOL {pay/1e3:.1f} t | STO {W_sto/1e3:.0f} t: {pay_sto/1e3:.1f} t | cruise {cruise*1.944:.0f} kn")
        for lab,p in res['hot'].items():
            print(f"    VTOL payload at {lab:32s} {p:6.1f} t")
    return res

if __name__ == "__main__":
    MID = ("2,500 m 40 C", 2500, 40)   # current design point (see notes §10.4)
    for rng in (1500, 300):            # long-range mission vs. VTOL shuttle from a strip
        RANGE_KM = rng
        print(f"\n############ mission {rng} km + {HOVER_MIN} min hover + {RESERVE:.0%} reserve ############")
        run("TB2-H Heavy (B+D, fans only)", 200, [14]*6, 0.29, None, 10, 170, 0.35, MID, hold_t=9.0)
        run("TB2-F Fast (A+C, feathered fans + cruise jets)", 100, [10]*6, 0.27, {'lapse':0.32}, 11, 217, 0.25, MID, hold_t=4.0)

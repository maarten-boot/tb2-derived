# TB2 redesign - rough first-order sizing model (see th-2-re-design-ideas.md sections 8-14, 18, 19)
# Run: python3 th-2-sizing.py   - edit VARIANTS (shared with th-2-strip.py) to try variants.
import math
g, R_AIR = 9.81, 287.05
RHO0 = 1.225
HOVER_MIN, RESERVE = 4, 0.10
THRUST_MARGIN = 1.15   # hover thrust kept in hand for control / gusts
POWER_RESERVE = 1.20   # power kept in hand for fan-out (one fan lost, neighbours at 1.5x)
MISSIONS_KM = (1500, 300)   # long-range mission vs. VTOL shuttle from a strip

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

# Current design (notes §0). Single source of truth for both scripts.
# L/D: cut from 10 for the ladder frame in cruise (4 rails + 6 ducts add ~30 % wetted area, notes §18).
# rails: (count, length m) from the drawing; gear_extra_t: soft-field flotation beyond normal gear.
# CLS (wing+body lift x area, flaps), f (flat-plate drag, incl. rails), span: used by th-2-strip.py only.
VARIANTS = {
    "TB2-H Heavy": dict(desc="B+D, fans only", W_t=200, fans=[14]*6, struct_frac=0.29, jets=None,
                        LD=9.0, cruise=170, sto_gain=0.35, design=("2,500 m 40 C", 2500, 40),
                        hold_t=9.0, rails=(4, 72), gear_extra_t=2.0, CLS=2560, f=52, span=66),
    # TB2-F Fast dropped 2026-10-14 (notes §19). Its last entry, for comparison runs:
    # "TB2-F Fast": dict(desc="A+C, feathered fans + cruise jets", W_t=100, fans=[10]*6, struct_frac=0.27,
    #                    jets={'lapse': 0.32}, LD=9.5, cruise=217, sto_gain=0.25, design=("2,500 m 40 C", 2500, 40),
    #                    hold_t=4.0, rails=(4, 66), gear_extra_t=0.0, CLS=1205, f=22, span=62),
}

def hover_power(W, r, A):          # W in kg; ducted fans, expanded wake, 80 % eff., THRUST_MARGIN included
    T = THRUST_MARGIN*W*g
    return T**1.5/(2*math.sqrt(r*A))/0.80

def disk_area(fans): return sum(math.pi*(d/2)**2 for d in fans)

def powerplant(W, fans, design):
    """Installed SL power (flat-rated turbines) and gearbox shaft limit, both in W."""
    A = disk_area(fans)
    r_d = rho(design[1], design[2])
    P_shaft = POWER_RESERVE*hover_power(W, r_d, A)   # gearboxes carry what the design point needs
    P_inst = P_shaft/(r_d/RHO0)                      # turbines sized for thin/hot air
    return A, P_inst, P_shaft

def max_vtol_weight(A, P_inst, P_shaft, r):
    """Heaviest weight [kg] that still hovers with THRUST_MARGIN and POWER_RESERVE kept in hand."""
    P_av = min(P_inst*(r/RHO0), P_shaft)/POWER_RESERVE   # engine lapse, gearbox limit
    return (P_av*2*math.sqrt(r*A)*0.80)**(2/3)/(THRUST_MARGIN*g)

def rail_mass(W, nf, rails):
    """Ladder-frame rails: carbon box beams between the wing rungs; each fan pivots on 2 rails.
    Per-metre mass scales with the pivot load under fan-out (1.5x), plus pivot fittings. [kg]"""
    n, L = rails
    F_kN = THRUST_MARGIN*W*g/nf*1.5/2/1000          # load per rail pivot, kN
    return n*L*(12 + 0.12*F_kN) + 2*nf*0.5*F_kN

def run(name, W_t, fans, struct_frac, jets, LD, cruise, sto_gain, design=("SL ISA", 0, 15), quiet=False,
        hold_t=0.0, rails=(0, 0), gear_extra_t=0.0, range_km=1500, desc="", **_):
    W = W_t*1000
    nf = len(fans)
    A, P_inst, P_shaft = powerplant(W, fans, design)
    r_d = rho(design[1], design[2])
    v = math.sqrt(THRUST_MARGIN*W*g/(RHO0*A))
    # fan-out capability: 6+ fans in 3 lengthwise pairs, middle pair at CG -> worst fans need 1.5x nominal.
    # Assumes loading rules keep the CG at the middle pair (E8).
    k = 1.5*1.05/THRUST_MARGIN if nf >= 6 else 1.0
    m_shaft = P_inst/1000/8*1.3
    m_drive = 0.22*P_shaft/1000*(0.5+0.5*k**1.5) + 0.015*W*(nf/4)**0.5
    m_fans  = 20.0*A*(nf/4)**0.25*(k**0.5)         # ducted fan + duct ~20 kg per m2 of disk
    W_sto = W*(1+sto_gain)
    m_struct = 0.04*W_sto + (struct_frac-0.04)*W*(max(2.5*W, 2.0*W_sto)/(2.5*W))**0.6
    m_sys = 0.07*W + 3000
    m_hold = hold_t*1000                           # extra floor + corridor walls for a maximised hold (notes §14)
    m_rails = rail_mass(W, nf, rails)
    m_gear = gear_extra_t*1000
    m_jets, Tjet = 0, 0
    if jets:
        Tjet = 0.9*W*g/LD/jets['lapse']*1.3
        m_jets = Tjet/(4.5*g)
    hover_fuel = hover_power(W, r_d, A)/1000*0.27*HOVER_MIN/60   # hover at the design point
    W0 = W - hover_fuel
    K = cruise*LD/(0.6/3600) if jets else 0.75*LD/(g*0.28/3.6e6)
    burn = 1-math.exp(-range_km*1000/K)
    fuel = (hover_fuel + W0*burn)*(1+RESERVE)
    fuel_sto = W_sto*burn*(1+RESERVE)
    empty = m_shaft+m_drive+m_fans+m_struct+m_sys+m_jets+m_hold+m_rails+m_gear
    pay = W-empty-fuel; pay_sto = W_sto-empty-fuel_sto
    res = {'empty': empty/1000, 'pay': pay/1000, 'pay_sto': pay_sto/1000, 'P': P_inst/1e6, 'hot': {},
           'W_sto': W_sto, 'W_land_sto': W_sto*(1-burn), 'A': A, 'P_inst': P_inst, 'P_shaft': P_shaft,
           'rails': m_rails/1000}
    for lab, h, t in CONDITIONS:
        Wmax = max_vtol_weight(A, P_inst, P_shaft, rho(h, t))
        res['hot'][lab] = (min(Wmax, W)-empty-fuel)/1000
    res['max_vtol_sl'] = max_vtol_weight(A, P_inst, P_shaft, rho(0, 15))/1000
    if not quiet:
        print(f"\n== {name} ({desc}): {W_t} t VTOL, {nf} fans x {fans[0]} m ({A:.0f} m2), power sized for {design[0]}")
        print(f"  installed {P_inst/1e6:.0f} MW (SL) | downwash {v:.0f} m/s | L/D {LD} | fan-out capable: {'yes' if nf>=6 else 'NO'}")
        print(f"  shafts {m_shaft/1e3:.1f} | drive {m_drive/1e3:.1f} | fans {m_fans/1e3:.1f} | struct {m_struct/1e3:.1f} | sys {m_sys/1e3:.1f}"
              f" | jets {m_jets/1e3:.1f} | hold {m_hold/1e3:.1f} | rails {m_rails/1e3:.1f} | gear+ {m_gear/1e3:.1f}  -> EMPTY {empty/1e3:.1f} t")
        print(f"  fuel {fuel/1e3:.1f} t | PAYLOAD VTOL {pay/1e3:.1f} t | STO {W_sto/1e3:.0f} t: {pay_sto/1e3:.1f} t | cruise {cruise*1.944:.0f} kn"
              f" | max VTOL weight at SL {res['max_vtol_sl']:.0f} t")
        for lab, p in res['hot'].items():
            print(f"    VTOL payload at {lab:32s} {p:6.1f} t")
    return res

if __name__ == "__main__":
    for rng in MISSIONS_KM:
        print(f"\n############ mission {rng} km + {HOVER_MIN} min hover + {RESERVE:.0%} reserve ############")
        for name, v in VARIANTS.items():
            run(name, range_km=rng, **v)

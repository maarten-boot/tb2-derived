# Thunderbird 2 redesign - rough first-order sizing model (see th-2-re-design-ideas.md section 8)
# Run: python3 th-2-sizing.py   - edit the run(...) lines at the bottom to try variants.
import math
g, rho = 9.81, 1.225
RANGE_KM, HOVER_MIN, RESERVE = 1500, 4, 0.10

def run(name, W_t, fans, struct_frac, jets, LD, cruise, sto_gain):
    W = W_t*1000
    A = sum(math.pi*(d/2)**2 for d in fans)
    T = 1.15*W*g                                  # control/hover margin
    v = math.sqrt(T/(rho*A))                      # ducted fan, fully expanded wake
    P_hover = T*v/2/0.80                          # W, duct+fan efficiency 0.8
    P_inst = 1.2*P_hover                          # OEI contingency / hot-day margin
    m_shaft = P_inst/1000/8*1.3                   # 8 kW/kg bare, x1.3 installed
    m_drive = 0.22*P_inst/1000 + 0.015*W          # gearboxes, cross-shafts, tilt mech
    m_fans  = 0.045*W                             # fans + ducts
    # Structure: landing gear (4 %) sized for STO weight; bending structure sized by the
    # worse of 2.5 g at VTOL weight or 2.0 g at STO overload weight (transport practice).
    W_sto = W*(1+sto_gain)
    m_gear = 0.04*W_sto
    m_struct = m_gear + (struct_frac-0.04)*W*(max(2.5*W, 2.0*W_sto)/(2.5*W))**0.6
    m_sys   = 0.07*W + 3000
    m_jets, Tjet = 0, 0
    if jets:
        D = 0.9*W*g/LD
        Tjet = D/jets['lapse']*1.3                # SL static, climb margin
        m_jets = Tjet/(4.5*g)
    hover_fuel = P_hover/1000*0.27*HOVER_MIN/60
    W0 = W - hover_fuel
    R = RANGE_KM*1000
    if jets:
        V = cruise; c = 0.6/3600
        K = V*LD/c                       # TSFC c in 1/s (weight basis)
    else:
        cp = 0.28/(1000*3600); K = 0.75*LD/(g*cp)
    cruise_fuel = W0*(1-math.exp(-R/K))
    fuel = (hover_fuel + cruise_fuel)*(1+RESERVE)
    fuel_sto = W_sto*(1-math.exp(-R/K))*(1+RESERVE)   # STO: no hover, heavier cruise
    empty = m_shaft+m_drive+m_fans+m_struct+m_sys+m_jets
    pay = W - empty - fuel
    print(f"\n== {name}: VTOL gross {W_t} t, fans {fans} m, area {A:.0f} m2")
    print(f"  downwash {v:.0f} m/s | hover power {P_hover/1e6:.0f} MW | installed {P_inst/1e6:.0f} MW")
    for k,m in [("turboshafts",m_shaft),("drivetrain+tilt",m_drive),("fans+ducts",m_fans),("structure",m_struct),("systems",m_sys),(f"cruise jets ({Tjet/1e3/2:.0f} kN x2)",m_jets)]:
        print(f"  {k:28s} {m/1000:6.1f} t")
    print(f"  EMPTY {empty/1000:.1f} t ({empty/W:.0%}) | fuel {fuel/1000:.1f} t (hover {hover_fuel/1000:.1f})")
    pay_sto = W_sto - empty - fuel_sto
    print(f"  PAYLOAD VTOL {pay/1000:.1f} t ({pay/W:.0%}) | STO {W_sto/1000:.0f} t gross: {pay_sto/1000:.1f} t (fuel {fuel_sto/1000:.1f} t)")
    print(f"  cruise {cruise*1.944:.0f} kn, L/D {LD}, range {RANGE_KM} km + {HOVER_MIN} min hover + {RESERVE:.0%}")

run("Baseline v3 (compound)", 150, [9,9,10,10], 0.25, {'lapse':0.35}, 11, 221, 0.15)
run("TB2-H Heavy (B+D, fans only)", 200, [12,12,12,12], 0.29, None, 10, 170, 0.35)
run("TB2-F Fast (A+C, separate turboshafts + jets)", 100, [8,8,8,8], 0.27, {'lapse':0.30}, 12, 239, 0.25)

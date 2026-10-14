# Thunderbird 2 redesign - first-order STO / STOL strip-length estimate (see th-2-re-design-ideas.md section 11)
# Point-mass simulation: fans tilted forward by a fixed angle (best angle searched), wing+body lift,
# ground roll to lift-off, then airborne to 15 m (50 ft). Landing: steep approach + braked roll.
# Run: python3 th-2-strip.py
import math
g = 9.81
def rho(h, t_c):
    p = 101325*(1-2.25577e-5*h)**5.25588
    return p/(287.05*(t_c+273.15))
def hover_power(W, r, A): return (1.15*W*g)**1.5/(2*math.sqrt(r*A))/0.80

VARIANTS = {   # VTOL gross, fans, design point, CL*S (wing+body, flaps), flat-plate drag f, span
    "TB2-H Heavy": dict(W=200e3, fans=[14]*6, design=(2500, 40), CLS=2560, f=45, b=64),
    "TB2-F Fast":  dict(W=100e3, fans=[10]*6, design=(2500, 40), CLS=1205, f=18, b=62),
}
def powerplant(v):
    A = sum(math.pi*d*d/4 for d in v['fans'])
    r_d = rho(*v['design'])
    P_shaft = 1.2*hover_power(v['W'], r_d, A)          # gearbox limit
    P_inst = P_shaft/(r_d/1.225)                       # flat-rated turbines (SL rating)
    return A, P_inst, P_shaft
def static_thrust(v, r):
    A, P_inst, P_shaft = powerplant(v)
    P = min(P_inst*r/1.225, P_shaft)
    return (P*0.80*2*math.sqrt(r*A))**(2/3)

def takeoff(v, W, h, t, mu=0.03, dt=0.02):
    r = rho(h, t); T0 = static_thrust(v, r); m = W; Wn = W*g
    if T0 >= 1.05*Wn: return 0.0, 0.0, None            # can lift off vertically
    best = None
    for th_deg in range(10, 80, 5):
        th = math.radians(th_deg); x = z = vx = vz = 0.0; air = False
        for _ in range(40000):
            V = math.hypot(vx, vz); q = 0.5*r*V*V
            T = T0*max(0.6, 1-V/150)                    # thrust falls off with speed
            L = q*v['CLS']*(1 if V < 90 else 0.6)       # flaps retracted at speed (unused in practice)
            Di = (L*L/(q*math.pi*v['b']**2*0.8)) if q > 1 else 0
            D = q*v['f'] + Di
            Fz = L + T*math.cos(th) - Wn
            if not air:
                N = max(0.0, -Fz)
                ax = (T*math.sin(th) - D - mu*N)/m
                vx += ax*dt; x += vx*dt
                if Fz >= 0.05*Wn: air = True; x_lo = x
                if x > 6000: break
            else:
                ax = (T*math.sin(th) - D)/m; az = Fz/m
                vx += ax*dt; vz += az*dt; x += vx*dt; z += vz*dt
                if z >= 15: break
        if air and z >= 15 and (best is None or x < best[0]): best = (x, x_lo, th_deg)
    return best if best else (float('inf'), float('inf'), None)

def landing(v, W, h, t, mu_b=0.35, approach_deg=6):
    r = rho(h, t); T0 = static_thrust(v, r); Wn = W*g
    # touchdown: fans at 70 % thrust, tilted 30 deg, wing carries the rest; V_TD = 1.1 x balance speed
    Tv = 0.7*T0*math.cos(math.radians(30))
    if Tv >= Wn: V_td = 0.0
    else: V_td = 1.1*math.sqrt(2*(Wn-Tv)/(r*v['CLS']))
    air = 15/math.tan(math.radians(approach_deg))
    roll = V_td**2/(2*g*mu_b)
    return air+roll, roll, V_td

def max_weight_for(v, dist, h, t, mu):
    lo, hi = 50e3, 400e3
    for _ in range(30):
        mid = (lo+hi)/2
        if takeoff(v, mid, h, t, mu)[0] <= dist: lo = mid
        else: hi = mid
    return lo

if __name__ == "__main__":
    CONDS = [("Sea level 15 C, paved", 0, 15, 0.03, 0.40),
             ("Sahel SL 50 C, unpaved", 0, 50, 0.08, 0.25),
             ("E-Africa 2,500 m 40 C, unpaved", 2500, 40, 0.08, 0.25),
             ("Andes El Alto 4,000 m 25 C, paved", 4000, 25, 0.03, 0.40)]
    cases = {"TB2-H Heavy": (270e3, 230e3), "TB2-F Fast": (125e3, 113e3)}
    for name, v in VARIANTS.items():
        A, P_inst, P_shaft = powerplant(v)
        Wto, Wl = cases[name]
        print(f"\n=== {name}: fans {A:.0f} m2, installed {P_inst/1e6:.0f} MW (SL), gearbox {P_shaft/1e6:.0f} MW")
        print(f"  take-off at {Wto/1e3:.0f} t (STO max), landing at {Wl/1e3:.0f} t (after 1,500 km)")
        for lab, h, t, mu, mub in CONDS:
            r = rho(h, t); hov = static_thrust(v, r)/1.05/g/1e3
            to = takeoff(v, Wto, h, t, mu); ld = landing(v, Wl, h, t, mub)
            w800 = max_weight_for(v, 800, h, t, mu)/1e3
            tos = "vertical" if to[0] == 0 else (f"{to[0]:5.0f} m (roll {to[1]:4.0f} m, fans {to[2]} deg)" if to[0] < 1e9 else "not possible")
            lds = "vertical" if ld[2] == 0 else f"{ld[0]:4.0f} m (roll {ld[1]:4.0f} m, touchdown {ld[2]*1.944:3.0f} kn)"
            print(f"  {lab:34s} max hover {hov:4.0f} t | TO to 15 m: {tos} | LDG over 15 m: {lds} | max TOW for 800 m: {w800:4.0f} t")

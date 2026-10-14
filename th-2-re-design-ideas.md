# Thunderbird 2 — "Flyable" Redesign Ideas

Working notes on turning the original *Thunderbirds* (1965) Thunderbird 2 into a
physically plausible heavy-lift VTOL transport, while keeping the bulky green hull
(the pod was later replaced by an internal hold + rear ramp, see §5).

Concept drawing (current, v3 — compound, ramp, no pod): `th-2-re-design.svg` / `.png`.
Earlier versions: `th-2-re-design-v2.*` (ramp, fans only).
Wing / lift-area options sheet: `th-2-wing-options.svg` / `.png`.
Variants sheet (TB2-H Heavy + TB2-F Fast, top + side views, same scale): `th-2-variants.svg` / `.png`.
Original pod version: `th-2-re-design-v1.svg` / `th-2-re-design-v1.png`.

> Canon figures used below are approximate (sources disagree): length ≈ 76 m,
> span ≈ 55 m, empty mass ≈ 400 t, plus pod.

---

## 1. What's wrong with the original

### 1.1 Lift vs. CG placement (the fatal flaw)
- Wings sit at the extreme rear; the long, heavy nose and the pod sit well forward.
- With the CG far ahead of the main lifting surface there is a large nose-down
  moment and nothing up front to counter it. A conventional tail can't help — it
  is also at the back.
- The pod is swappable, so the CG moves a lot depending on what is carried.

### 1.2 Wing area — surprisingly not crazy
- Rough estimate: ~450 m² wing, ~500 t gross → wing loading ≈ 1,100 kg/m².
- Boeing 747 ≈ 750 kg/m². High, but not absurd for a fast transport
  (needs long runways / big flaps).

### 1.3 Forward-swept wings — buildable today
- Problem: aeroelastic divergence (tips twist up under load until failure).
- Solved by the Grumman X-29: aeroelastically tailored composite skins
  plus fly-by-wire for an unstable airframe. Can be kept.

### 1.4 VTOL — the real physics problem
- Hovering ~500 t needs ~5–6 MN vertical thrust (~4× the total thrust of an An-225).
- Momentum theory, induced velocity: `v = sqrt(T / (2·ρ·A))`
  (T = thrust, ρ = air density ≈ 1.225 kg/m³, A = total fan/jet area).
  - **Jet lift** (Harrier style, small A): hot, jet-velocity exhaust; erodes the
    ground and blows away debris, people and the thing being rescued.
  - **Fans, A ≈ 1,000 m²** (e.g. 8 × ~12.6 m Ø): ~45 m/s at the fan, ~90 m/s in
    the fully developed wake — hurricane-force air at the landing site.
- Hover power: `P ≈ T^1.5 / sqrt(2·ρ·A) / FM` (FM = figure of merit, ~0.75)
  → ~290 MW shaft power for 500 t on 1,000 m². Largest helicopter turboshaft
  ≈ 10 MW → ~30 engines. The canon nuclear power plant is the one ingredient
  that makes this half-plausible.
- Hover fuel (if turbofan lift): roughly 3 t/min → only minutes of hover.

### 1.5 Pod-bay structure
- Fuselage straddles the pod → open U-section → very weak in torsion.
- Needs deep continuous keel beams along both sides and a stiff closed "roof"
  box over the bay.

### 1.6 Speed
- Canon top speed ~5,000 mph (hypersonic) is impossible for this blunt,
  pod-carrying shape. Realistic: subsonic, Mach 0.6–0.75.

---

## 2. Redesign (keeping the bulky look)

### A. Lifting-body / blended-wing-body hull
- Widen and flatten the hull, give it a cambered airfoil side profile.
- Broad body carries ~30–40 % of the lift; the bulk becomes an asset.
- Pod bay in the centre of the "wing" body — also a stiffer box structurally.

### B. Pitch balance — **chosen: canard foreplanes** ✅
- Large lifting canard near the nose; forward-swept main wing moved forward to
  mid-body so canard lift line and wing lift line **bracket the CG**.
- Both surfaces carry positive lift (unlike a conventional tail which pushes down)
  → more efficient, and the canard stalls first, giving natural stall protection.
- Fly-by-wire with relaxed stability; active fuel transfer for trim (Concorde-style).

### C. Pod CG control
- Standardised pods with a defined CG envelope and ballast points.
- Every pod CG must land in a narrow band under the combined lift centre **and**
  the centroid of the hover thrust.

### D. VTOL — low-disk-loading tilting ducted fans
- Chosen layout in drawing: **4 tilting ducted fans** — 2 on the canard tips
  (Ø ≈ 9 m), 2 on the main-wing tips (Ø ≈ 10 m). Fans rotate 90° forward for
  cruise (V-22 principle, ducted).
- The canard gives a natural forward mounting point for the front fan pair, so the
  hover thrust centroid can sit on the CG — the canard choice solves hover
  balance as well as cruise balance.
- Alternatives considered: lift fans buried in the hull behind louvred doors
  (cleaner TB2 look, but worse downwash and power); jet lift (rejected).
- Aim for as much fan area as practical (≥ 1,500 m² ideal at canon weight).

### E. Bring the weight down (the honest fix)
- At 500 t any VTOL is brutal. At ~120–150 t gross it becomes "a very large but
  conceivable tiltrotor transport" (~6–7× a Mi-26).

### F. Optional: partial buoyancy (hybrid airship)
- Helium lifts ~1 kg/m³ → 500 t fully buoyant needs ~500,000 m³ (~2.5 Hindenburgs).
- Partial (20–30 % of weight, Airlander 10 style) reduces hover power, but the
  hull would swell and stop looking like TB2.

---

## 3. Summary spec of the concept

| Item              | Original (canon)        | Redesign                                  |
|-------------------|-------------------------|-------------------------------------------|
| Hull              | Bulky fuselage          | Wider, flatter cambered lifting body      |
| Main wing         | Fwd-swept, at tail      | Fwd-swept, moved to mid-body              |
| Pitch control     | Tail fin only           | Lifting canard + FBW + fuel-transfer trim |
| Tail              | Single fin              | Twin canted fins                          |
| VTOL              | Unexplained thrusters   | 4 tilting ducted fans (canard + wing tips)|
| Pod bay           | Open U-section          | Keel beams + closed roof box              |
| Cruise speed      | ~5,000 mph (canon)      | ~Mach 0.55 with tilt-fans (see §6)        |
| Gross mass        | ~400 t + pod            | Target 120–150 t                          |
| Hover downwash    | n/a                     | ~45–90 m/s (still a site hazard)          |

---

## 4. Open questions / future notes

- [ ] Size canard vs. wing area split so the CG margin covers empty-pod to full-pod.
- [ ] Choose fan diameters so front/rear fan pairs share hover load in proportion
      to their distance from the CG.
- [ ] Power plant: turboshaft cluster vs. hybrid-electric distributed drive vs.
      (fictional) compact nuclear.
- [ ] One-engine-out / one-fan-out hover safety (cross-shafting like the V-22?).
- [ ] Downwash mitigation at rescue sites: hover height, deploy pod from altitude
      on winches instead of landing?
- [ ] ~~Front view drawing~~ (deferred 2026-10-14 by user: not needed for now).

<!-- Append further notes below -->

---

## 5. Iteration 2 (2026-10-14): drop the pod, add a rear ramp, composite structure

### 5.1 Pod → internal hold + rear loading ramp ✅ (adopted)
**Gains**
- Closed fuselage box instead of open U-section: much stiffer in torsion and
  lighter. Probably the single biggest structural weight saving available.
- Cargo sits *inside* the lifting body: better aerodynamics (no blunt pod
  hanging in the airflow), so less drag and better range.
- Tall pod-straddling legs no longer needed: short "kneeling" gear lowers the
  floor so the ramp angle is shallow enough for vehicles.
- Ramp can open in hover: winch, rappel, low-level drop, or vehicles driving out
  (keeps the TB2 "rescue vehicle rolls out" moment).

**Costs / design consequences**
- Lose the "drop the pod and leave" quick-swap capability.
  Middle ground: **standardised palletised mission modules** loaded through the
  ramp on a roller floor, so the pod idea lives on inside the hold.
- Aft body must sweep upward (C-130 / A400M / C-17 style). This is natural for a
  lifting body, but the twin fins have to move outboard or onto the upswept tail.
- CG control changes from "pod under CG" to loadmaster discipline: hold centred
  on the CG, marked load zones, fuel-transfer trim, and FBW limits.

### 5.2 Payload with ducted tilt-fans: realistically modest
Reference payload / useful-load fractions:

| Aircraft        | Max gross | Empty   | Payload | Payload / gross |
|-----------------|-----------|---------|---------|-----------------|
| V-22 (VTOL)     | 23.9 t    | ~15 t   | ~9 t    | ~0.25–0.35      |
| CH-47F          | 22.7 t    | ~11 t   | ~10.9 t | ~0.45 (useful)  |
| Mi-26           | 56 t      | ~28 t   | 20 t    | ~0.36           |
| C-17 (CTOL)     | 265 t     | ~128 t  | 77 t    | ~0.29           |

Estimate for the 150 t gross concept:
- Metal baseline: empty ≈ 95 t, fuel ≈ 25 t, **payload ≈ 30 t** (C-130J / A400M class).
- Ducts give more thrust per unit of power than an open rotor of the same
  diameter, but the ducts, tilt mechanisms, cross-shafting and gearboxes are
  heavy. Net effect: payload fraction is lower than a helicopter's.
- **STOL overload mode**: fans tilted ~45–60°, short rolling take-off, wing and
  body lift help. The V-22 gets about +15 % gross weight this way. Plan two
  ratings: "VTOL weight" and "STO weight".

### 5.3 Composite structure (Rutan / Scaled Composites lineage): yes, worth it
- Structure is ~30–35 % of gross for transports, so ~50 t at 150 t gross.
- Realistic composite saving: 15–25 % of *structure* (787 / A350 class),
  about 8–12 t.
- Because payload is a small fraction of gross, the leverage is large:
  **+8–12 t payload is about +30–40 %**.
- Weight-spiral bonus: lighter empty weight → smaller fans → less power → less
  fuel → lighter structure again. VTOL designs have high growth factors
  (2–3×), so savings compound.
- The forward-swept wing *needs* composites anyway (aeroelastic tailoring, X-29).
- Caveats:
  - Rutan's moldless foam-core sandwich (VariEze, Voyager) doesn't scale to large
    primary structure. At this size, use autoclave or out-of-autoclave carbon
    like the 787, or Stratolaunch (Scaled Composites, 117 m span, all-composite).
  - Voyager-level lightness relied on a fragile, low-g airframe. That isn't
    acceptable for a rescue workhorse (rough landings, debris, ramp loads,
    crashworthiness).
  - Impact and damage tolerance, lightning protection, fire resistance and
    field repair need design attention. Use hybrid metal at ramp hinges, landing
    gear and the cargo floor.
  - Engines, drivetrain and systems (a large share of empty weight) don't
    benefit from composites.

### 5.4 Revised estimate (150 t VTOL gross)
| Configuration                         | Empty   | Fuel  | Payload    |
|---------------------------------------|---------|-------|------------|
| Metal, pod version                    | ~100 t  | 25 t  | ~25 t      |
| Metal, closed hull + ramp             | ~95 t   | 25 t  | ~30 t      |
| Composite, closed hull + ramp         | ~83 t   | 25 t  | **~40 t**  |
| Same, STO overload (+15 % gross)      | ~83 t   | 25 t  | **~60 t**  |

### 5.5 New open questions
- [x] Update drawing: upswept aft body with ramp, outboard fins, kneeling gear, no pod (done 2026-10-14: `th-2-re-design.svg/.png`; v1 with pod kept as `th-2-re-design-v1.*`).
- [ ] Mission-module standard (size like an ISO container? 463L pallets?).
- [ ] Hold dimensions vs. target cargo (largest rescue vehicle to carry).
- [ ] Downwash effect on the open ramp area and on people near it during hover.

---

## 6. Iteration 3 (2026-10-14): replace the fans with jets?

**Short answer: the technology has existed since the 1960s, but jets are the wrong
choice for a rescue heavy-lifter.**

### 6.1 Jet VTOL exists
- Harrier / AV-8B (Pegasus vectored thrust), Yak-38 / Yak-141, F-35B.
- **Dornier Do 31 (1967)**: a jet VTOL *transport*, ~27 t, 2 vectored Pegasus +
  8 lift jets in wingtip pods. It flew well, but was cancelled because of noise,
  fuel burn, and lift engines that were dead weight in cruise.

### 6.2 The physics: fan ↔ jet is one spectrum
rotor → ducted fan → high-bypass turbofan → low-bypass jet → turbojet.
Moving right: smaller, lighter per unit of thrust, but higher exhaust velocity.
Ideal hover power is `P = T·v/2`, so a faster exhaust costs more power for the same
thrust. (A turbofan *is* a ducted fan with a gas-turbine core in the middle.)

Hover at 150 t (T ≈ 1.7 MN incl. margin), rough numbers:

| Lift system                          | Exit area | Exit velocity | Hover power | Hover fuel  |
|--------------------------------------|-----------|---------------|-------------|-------------|
| 4 ducted fans Ø 9–10 m (current)     | ~285 m²   | ~70 m/s       | ~75 MW      | ~0.35 t/min |
| 6 high-bypass turbofans, fan Ø ~3 m  | ~42 m²    | ~180 m/s      | ~155 MW     | ~0.85 t/min |
| Lift jets / low-bypass (Harrier-ish) | small     | 400–600 m/s, 500°C+ | ~400 MW+ | ~2.5 t/min  |

### 6.3 Why jets are bad for this mission
- 2–3 minutes of hover per landing burns 5–8 t of fuel, which comes straight out
  of payload.
- Hot, high-speed exhaust: melts asphalt, sets dry vegetation on fire, throws
  debris, and kills people near the aircraft. The F-35B needs heat-resistant pads.
  A rescue site has none.
- Hot exhaust gets sucked back into the intakes (loss of thrust); extreme noise.
- Lift-only jets are dead weight in cruise (the Do 31 lesson).
- Lilium (small electric ducted-fan "jet", insolvent 2024/25) is a modern
  reminder: small, high-disk-loading fans need lots of power.

### 6.4 Where jets *do* make sense: cruise speed
- Correction to earlier notes: tilting ducted fans are limited to roughly
  300–380 kn (the V-22 does ~275 kn), so realistic cruise is **≈ Mach 0.5–0.55**,
  not Mach 0.7.
- Options if more speed is wanted:
  1. Accept ~350 kn (simplest, lightest). **Current baseline.**
  2. **Compound**: keep the hover fans (stopped and stowed or feathered in
     cruise) and add 2 cruise turbofans in the upswept tail, where TB2 had its
     jets. This gives ~Mach 0.7, but costs extra weight and maybe −5 to −10 t
     payload.
  3. Tilting large-fan turbofans (middle of the spectrum): faster cruise, but
     harsher downwash and about double the hover fuel.

---

## 7. Iteration 4 (2026-10-14): compound adopted + more lifting area + two variants

### 7.1 Compound layout ✅ (adopted, drawing v3)
- 2 dorsal cruise turbofans (~130 kN class each, CFM56/LEAP size) on top of the
  upswept aft body, between the outboard fins.
  - High mounting keeps hot exhaust away from the ramp, people and the ground;
    the fins shield noise and infrared.
  - Debris ingestion is less likely than with low-mounted engines.
- Flight phases: fans for hover → fans tilt forward for transition → jets take over
  above ~120–150 kn → fans feathered, ducts aligned with the airflow.
- Cost: jets + nacelles + pylons ≈ 6–8 t → payload ~32 t VTOL / ~52 t short take-off
  (was 40 / 60). Cruise ≈ Mach 0.7.
- Engines sit aft of the CG, so balance them with the forward fan pair and fuel
  placement.
- Advanced option: **convertible engines** (turbofan that can also deliver
  shaft power, as NASA/GE tested on a TF34 in the 1980s). These would drive the
  lift fans in hover and give jet thrust in cruise, so no separate turboshafts.
  Saves weight, but is research-level.

### 7.2 Options for more lifting area (see `th-2-wing-options.png`)
| Option | Idea | Pros | Cons | Fits |
|---|---|---|---|---|
| A | Bigger-span main wing (+folding tips) | best cruise efficiency, STO lift | forward-sweep twist grows with span, larger footprint | both |
| B | Tandem wing (canard grown to ~main-wing size; Rutan Quickie / Proteus) | ~1.6× area at same span, both wings lift, huge CG range, fans on all 4 tips; tips can be joined by a boom (box frame, also a cross-shaft route) | front-wing downwash on rear wing, heavier, draggier at speed | SLOW / HEAVY |
| C | Three-surface: add H-tail bridging the fins (Piaggio P.180) | widest trim range, shields jet exhaust, small change | extra wetted area/weight | both |
| D | Wide blended body + air guides | body gives 40–50 % of lift, much bigger hold | thick body draggy above ~Mach 0.6, harder to pressurise | SLOW / HEAVY |

**"Air guides" that keep the lift working:**
- **Wing fences** (MiG-15): stop air flowing sideways along a swept wing.
- **Vortex generators**: keep airflow attached at high angles of attack.
- **Chines / leading-edge extensions** (SR-71, F/A-18): create strong vortices
  that add lift at high angles of attack. A natural fit for a wide lifting body.
- **Endplates / winglets / side fences**: stop high-pressure air under a wide body
  or wing spilling over the edges (less induced drag, more effective lift).
- **Upper-surface blowing / Coandă effect** (Boeing YC-14, An-72): blow engine
  exhaust over the wing/flaps for extra low-speed lift. Possible later with
  partly-tilted fans blowing over the wing during short take-offs.

### 7.3 Two variants (first guess, superseded by §8)
Very rough targets:

| | **TB2-H "Heavy" (slow)** | **TB2-F "Fast" (light)** |
|---|---|---|
| Mission | bulk relief, heavy vehicles, bridging gear | rapid response, crews, medical, light vehicles |
| Body | wide blended body (D) + chines/endplates | slim lifting body |
| Lifting surfaces | tandem wing (B) or A with folding tips | high-aspect forward-swept wing + small canard + H-tail (C) |
| Propulsion | 4 large ducted fans only. No cruise jets, which saves ~6–8 t | 4 smaller fans + 2 cruise turbofans |
| Cruise | ~300–350 kn (Mach ~0.5) | Mach 0.75–0.8 |
| VTOL gross | ~200 t | ~100 t |
| Payload VTOL / STO | ~55 t / ~85 t | ~15–20 t / ~30 t |
| Tech risk | low–medium (scale is the challenge) | higher: fans must stop and fold their blades for Mach 0.8 (research-level) |

### 7.4 New open questions
- [x] Lifting-area options per variant: **H = B+D, F = A+C** (decided 2026-10-14, see §8).
- [ ] Stop/fold fan mechanism for TB2-F, or accept ~Mach 0.7 with feathered fans?
- [ ] Shared parts between H and F (cockpit, fans, avionics, mission modules)?
- [x] Drawings for both variants (see `th-2-variants.*`).

---

## 8. Recomputed sizing (2026-10-14): H = B+D, F = A+C

Model: `th-2-sizing.py` (first-order; rerun after changing assumptions).

### 8.1 Common assumptions
- Design mission: **1,500 km + 4 min hover (2 landings) + 10 % reserve**, full VTOL payload.
- Hover thrust = 1.15 × weight; ducted fans with fully expanded wake, 80 % efficient;
  installed power = 1.2 × hover power (one-engine-out / hot-day margin). ISA sea level.
  Hot-and-high sites will reduce payload.
- Turboshafts 8 kW/kg bare (×1.3 installed), 0.27–0.28 kg/kWh.
  Drivetrain 0.22 kg/kW + tilt mechanism 1.5 % of gross. Fans + ducts 4.5 % of gross.
- Composite structure: 25 % of gross baseline. H +4 % (tandem wing + wide body + air
  guides). F +2 % (folding tips + higher loads at high speed).
- Systems 7 % of gross + 3 t.
- Cruise jets: thrust/weight 4.5, cruise TSFC 0.6 /h, sized to cruise drag with
  altitude lapse and a 1.3 climb margin. Fans-only cruise: propulsive efficiency 0.75.
- Short take-off (STO) gain over VTOL gross: baseline +15 %, F +25 %, H +35 % (big
  lifting area). This assumes structure and gear are sized for the STO weight.

### 8.2 Results (superseded by §9.2)
| | Baseline v3 | **TB2-H Heavy** (B+D) | **TB2-F Fast** (A+C) |
|---|---|---|---|
| VTOL gross | 150 t | 200 t | 100 t |
| Fans | 2×Ø9 + 2×Ø10 m (284 m²) | 4×Ø12 m (452 m²) | 4×Ø8 m (201 m²) |
| Downwash (fan exit) | ~70 m/s | ~64 m/s | ~68 m/s |
| Hover / installed power | 74 / 88 MW | 90 / 108 MW | 48 / 57 MW |
| Turboshafts | 14.4 t | 17.5 t | 9.3 t |
| Drivetrain + tilt | 21.7 t | 26.8 t | 14.1 t |
| Fans + ducts | 6.8 t | 9.0 t | 4.5 t |
| Structure | 37.5 t | 58.0 t | 27.0 t |
| Systems | 13.5 t | 17.0 t | 10.0 t |
| Cruise jets | 10.1 t (2×224 kN) | — | 7.2 t (2×159 kN) |
| **Empty** | 104 t (69 %) | 128 t (64 %) | 72 t (72 %) |
| Fuel (1,500 km) | 17.4 t | 32.7 t | 10.0 t |
| Cruise | ~430 kn (M0.7), L/D 11 | ~330 kn, L/D 10 | ~465 kn (M0.77), L/D 12 |
| **Payload VTOL** | **~29 t** | **~39 t** | **~18 t** |
| **Payload STO** | ~51 t | ~100 t (if built for 270 t) | ~43 t |

Comparisons: H VTOL ≈ an A400M load (~2× Mi-26); H STO approaches C-17 class.
F VTOL ≈ 2× a V-22 internal load, at ~1.7× V-22 speed.

### 8.3 What the numbers say
1. **VTOL payload is ~18–20 % of gross in every version.** That is the price of
   hovering. Empty weight is 64–72 % of gross.
2. **Engines + drivetrain ≈ ¼ of gross.** This is the biggest lever, bigger than
   structure.
3. **H's real strength is short take-off.** The big tandem wing + wide body
   (B+D) more than doubles payload from a short strip (~300–500 m, estimate).
   Mission doctrine: VTOL into the disaster site, STO for bulk delivery to a
   nearby strip or road.
4. **H burns more fuel**: slower, lower L/D, and fans are less efficient propulsors
   than jets at these speeds. It is lighter only because it has no jets.
   Good for short-to-medium range bulk work.
5. **For F, the turboshafts are dead weight in cruise (~9 t) and the jets are dead
   weight in hover (~7 t).** This is the strongest case for **convertible engines**:
   a quick estimate (convertible engines 30 % heavier than turboshafts, no
   separate jets) gives **~+4–5 t payload (≈ +25 %)**.
6. For F, option A means **more span, not more area**: the fans handle take-off,
   so the wing is sized for cruise. A high aspect ratio gives low induced drag
   without the drag of extra area.

### 8.4 New open questions
- [x] H: structure designed for 270 t STO (decided 2026-10-14, see §9).
- [x] F: proven separate turboshafts + cruise jets (decided 2026-10-14, see §9).
- [ ] F: stop/fold fans (true Mach 0.77) vs. feathered fans (~Mach 0.7, simpler)?
- [ ] Hot-and-high performance check (e.g. 35 °C / 1,500 m site).
- [x] Drawings for TB2-H and TB2-F: `th-2-variants.svg/.png` (2026-10-14).

---

## 9. Decisions + final first-order numbers (2026-10-14)

### 9.1 Decisions
- **TB2-F Fast: proven separate engines.** Turboshafts drive the lift fans, and 2
  turbofans provide cruise thrust. Convertible engines are dropped (lower risk,
  gives up ~4–5 t payload).
- **TB2-H Heavy: structure and gear designed for the full 270 t short take-off weight.**

### 9.2 Model refinements (`th-2-sizing.py`)
- Landing gear (4 % of weight) is sized for the STO weight.
- Bending structure is sized by the worse of **2.5 g at VTOL weight** or **2.0 g at
  STO overload weight**. Lower g-limits at overload weight are normal transport
  practice (C-130 style). This keeps the 270 t penalty to ~5 t instead of ~11 t if
  the full 2.5 g were kept at 270 t.
- STO fuel is now computed at the heavier STO weight (no hover).

| | Baseline v3 | **TB2-H Heavy** | **TB2-F Fast** |
|---|---|---|---|
| VTOL / STO gross | 150 / 172 t | 200 / **270 t** | 100 / 125 t |
| Structure | 38.4 t | 63.2 t (+5.2 t for 270 t) | 28.0 t |
| Empty | 105 t (70 %) | 134 t (67 %) | 73 t (73 %) |
| Fuel VTOL / STO mission | 17 / 19 t | 33 / 42 t | 10 / 12 t |
| Cruise | ~430 kn | ~330 kn | ~465 kn |
| **Payload VTOL** | **~28 t** | **~34 t** | **~17 t** |
| **Payload STO** | **~49 t** | **~95 t** | **~40 t** |
(Mission: 1,500 km + 4 min hover + 10 % reserve.)

### 9.3 Consequences of the Heavy's 270 t short take-off
- VTOL payload drops ~39 → ~34 t. That is the price of the 270 t rating.
- After a 1,500 km trip the aircraft still weighs ~230 t, above its 200 t hover
  limit. So **STO missions are strip-to-strip**: short rolling landing on a
  strip or road at the destination, or offload first, then hover.
  A short mission (less fuel) or burning fuel down can bring it under 200 t to
  hover in.
- Doctrine: Heavy = bulk to a forward strip (STO, ~95 t), then shuttle loads
  into the disaster site by VTOL (~34 t), or the Fast handles the last leg.

### 9.4 Open questions (carried forward)
- [ ] F: stop/fold fans (true Mach 0.77) vs. feathered fans (~Mach 0.7, simpler)?
- [ ] H: STO strip length and rough-field capability (gear flotation for 270 t on
      unpaved strips).
- [ ] Hot-and-high performance check (e.g. 35 °C / 1,500 m site).
- [x] Drawings for TB2-H and TB2-F: `th-2-variants.svg/.png` (2026-10-14).

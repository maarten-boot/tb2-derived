# TB2 — "Flyable" Redesign Ideas

Working notes on turning the original *Thunderbirds* (1965) Thunderbird 2 into a
physically plausible heavy-lift VTOL transport, while keeping the spirit of the bulky
green hull.

**How this file is organised**
- **§0 Current status**: the design as it stands now, all decisions, and the *only*
  live open-questions list. Start here.
- **§1 onwards: history**: each iteration in the order it happened. Numbers in early
  sections are superseded by later ones (marked *superseded*). Old checkboxes there
  point to §0.
- Conversation flow: `th-2-conversation-log.md`.

**Files**
| File | What |
|---|---|
| `th-2-heavy.svg/.png` | **Current** drawing (v5): TB2-H Heavy only, top + side + front views with dimension arrows, ladder-frame fans, maximised corridor hold |
| `th-2-variants-v4.*`, `-v3.*`, `-v2.*`, `-v1.*` | Previous two-variant drawings (v4: Heavy + Fast with maximised hold, v3: small hold, v2: 6 fans on wings, v1: 4 fans) |
| `th-2-wing-options.svg/.png` | Lift-area options A–D compared |
| `th-2-fan-tilt.svg/.png` | How the fans tilt: sequence, structural issues, mounting options, Heavy ladder-frame proposal |
| `th-2-re-design.svg/.png` | Single-aircraft concept v3 (compound, ramp), before the H/F split |
| `th-2-re-design-v2.*` | v2 (ramp, fans only). The original pod-on-legs v1 was dropped as impractical (still in git history) |
| `th-2-sizing.py` | Weight/payload sizing model (6 fans, hot-and-high, STO) |
| `th-2-strip.py` | Take-off / landing strip-length simulation |

> Canon figures used in §1 are approximate (sources disagree): length ≈ 76 m,
> span ≈ 55 m, empty mass ≈ 400 t, plus pod.

---

## 0. Current status (2026-10-14)

### 0.1 The design: TB2-H Heavy (the Fast was dropped, §19)
| | **TB2-H Heavy** |
|---|---|
| Layout | Tandem wing (B) + wide blended body with chines/edge guides (D) |
| Size | ~82 m long, ~66 m span, body ~26 m wide, fins ~25 m high |
| Lift fans | 6 × Ø14 m tilting ducted in ladder bays (pivots on inner + outer rails, z ≈ 9 m); also cruise propulsors |
| Cruise | fans only, ~330 kn, L/D ~9 |
| Gross | VTOL 200 t at the 2,500 m / 40 °C design point (≈ 228 t at sea level); STO 270 t structural limit (2.0 g) |
| Empty | ~182 t (incl. ~15 t rails, ~9 t hold, ~2 t soft-field gear) |
| Hold | 50 × 20 m, 3 corridors (centre 7 × 5 m high, sides 6 × 4.2 m), ≈ 4,300 m³, 3 rear ramps |
| VTOL payload (up to 2,500 m / 40 °C) | **~9 t** (300 km shuttle) / none (1,500 km) |
| STO payload (300 / 1,500 km) | ~78 t / ~42 t |
| Strip (planning) | ≤ 700 m at 270 t; VTOL up to ~228 t at sea level |
| Downwash | ~45 m/s |
| Gear | ~22 main wheels (soft strips) |
| Role | Bulk to forward strip, VTOL shuttle into site |

**Doctrine:** fly long-range to a strip (big STO payload), then short VTOL shuttles
(~300 km). At 4,000–5,000 m (Andes / Himalaya): STO from strips only.

**Numbers above are from the corrected model (§18, 2026-10-14):** consistent
margins, rails, soft-field gear and ladder-frame L/D. Rail mass is the least
certain item (±50 % → VTOL shuttle ~2–17 t).

### 0.2 Decisions so far
| Topic | Decision | § |
|---|---|---|
| Pitch balance | Lifting canard / forward surface, FBW | 2 |
| Cargo access | No pod: internal hold + rear ramp, kneeling gear | 5 |
| Structure | Carbon composite (787 / Stratolaunch style, not Rutan foam) | 5 |
| Jets | Not for lift (hot exhaust, fuel); no cruise jets (fans only) | 6, 7 |
| Variants | Heavy (B+D) only; the Fast (A+C) was dropped as covered by existing aircraft | 8, 19 |
| Heavy STO | Structure and gear built for 270 t | 9 |
| Cargo standard | ISO 20 ft containers, plus vehicles etc. in the maximised hold | 10, 14 |
| Fan count | 6 fans (fan-out survivable in hover) | 10 |
| Climate | Design point 2,500 m / 40 °C (Africa incl. highlands + warming) | 10 |
| Rescue hoist | Not from the rear ramp; hoist/hook at CG or land and drive out | 10 |
| Pod designs | Original pod-on-high-legs dropped entirely (impractical) | 13 |
| Fan mounting | Ladder frame (provisional, D6) | 12, 13 |
| Hold | Maximised: vehicles, small helicopters, livestock, people; corridor walls with doors (D7) | 14 |

### 0.3 Open questions (the only live list)
**Decisions for the user**
- [ ] **D1** Lowland VTOL above 200 t: with full margins the limit is ~228 t at sea level. Allow up to that at lowland sites? (§18)
- [ ] **D2** Balance from empty to full hold: adopt all of hold-centred loading, fore/aft trim tanks, surfaces sized for ±4 % CG, FBW? (§10.5 Q8)
- [ ] **D3** Fan load split: 6 equal fans balanced by blade pitch? (§10.5 Q9)
- [ ] **D4** Heavy middle fans: tilting, or fixed (hover only, dead weight in cruise)? (§10.7)
- [ ] **D5** A future light high-altitude variant for Andes / Himalaya? (§10.4, §10.7)
- [ ] **D8** Water capability: design the Heavy to land/float/take off vertically on water (watertight lower hull, spray-proof engines, ramp as boat slipway)? (§15)
- [ ] **D10** **Payload vs. VTOL weight.** With rails and gear counted, the Heavy carries only ~9 t vertically at 2,500 m / 40 °C. Bigger fans or a bigger aircraft barely help (§20). Remaining options: lower the design point (SL 35 °C: ~22 t; 1,500 m 35 °C: ~15 t), or lighter / fewer rails (fans on wing roots + body sides). (§18)
- [ ] **D11** **The Heavy's niche.** Same test as for the Fast: a C-17 (~77 t, ~1,000 m strips, longer range, faster) plus a CH-53K (~12 t vertical, hot-and-high) cover most of the Heavy's numbers. What stays unique: ~4,300 m³ hold, ≤ 700 m soft strips at 270 t, vertical + STO in one airframe, water landing (D8). Is that enough, or does D10 have to raise VTOL payload first? (§19, comparison in §21: existing C-17 / A400M + Mi-26 / CH-53K cover both roles; the Heavy's only edge is no transshipment, ~78 t from ≤ 700 m soft strips, volume and water.)
- [ ] **D9** Second level: no fixed deck; use removable mezzanine / multi-deck modules only when a mission needs them? (§16)
- [x] **D7** Maximise the hold (user decision, §14).
- [x] **D6** *(provisionally adopted in drawing v3, §13)* Fan mounting: adopt the Heavy "ladder frame" (fans alternate with wings, pivots on inner + outer rails) and, for the Fast, tip spindles at canard / H-tail + a fork bay for the wing fans? (§12)

**Engineering checks**
- [ ] **E1** Fan-wake interaction front → middle → rear during transition. (§10.7)
- [ ] **E2** Cross-shaft routing to 6 fans; drivetrain failure modes. (§10.7)
- [ ] **E3** Fan/engine failure during the take-off roll or first 15 m: reject or continue distances. (§11.5)
- [x] **E4** Rail and soft-field gear weight added to `th-2-sizing.py` (rough; §18). Refine with a real rail structure → **E9**.
- [ ] **E9** Size the rails properly (load cases: hover fan-out, cruise thrust, landing, gusts); current estimate ~15 t ±50 %. (§18)
- [ ] **E5** Heavy footprint (~64 m span) at rescue sites; booms and sponsons structure. (§10.7)
- [x] ~~**E6** Fast canard / H-tail drag~~: Fast dropped (§19).
- [ ] **E8** Heavy hold centre (x ≈ 37 m) lies ahead of the CG (x ≈ 46 m): loading rules / trim range, or shift the hold aft. (§14)
- [ ] **E7** Downwash: people at rescue sites, open ramp area in hover, brown-out and debris on unpaved strips. (§4, §5.5, §11.5)

**Deferred**
- [x] Front-view drawing: done in `th-2-variants` v3 (§13).

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

### C. Pod CG control *(superseded: pod dropped in §5)*
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

## 3. Summary spec of the concept *(superseded: see §0)*

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

## 4. Open questions / future notes *(historical: live list in §0.3)*

- [→] Size canard vs. wing area split for the CG range: now **D2** in §0.3.
- [→] Choose fan diameters so front/rear fan pairs share hover load (now **D3** in §0.3)
      to their distance from the CG.
- [x] Power plant: settled on turboshafts (+ turbofans on the Fast), §9. Was: turboshaft cluster vs. hybrid-electric distributed drive vs.
      (fictional) compact nuclear.
- [x] One-engine-out / one-fan-out hover safety: solved with 6 fans, §10.3.
- [→] Downwash mitigation at rescue sites (now **E7** in §0.3): hover height, deploy pod from altitude
      on winches instead of landing?
- [→] ~~Front view drawing~~ (deferred; listed in §0.3).


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

### 5.4 Revised estimate (150 t VTOL gross) *(superseded: see §8–§10)*
| Configuration                         | Empty   | Fuel  | Payload    |
|---------------------------------------|---------|-------|------------|
| Metal, pod version                    | ~100 t  | 25 t  | ~25 t      |
| Metal, closed hull + ramp             | ~95 t   | 25 t  | ~30 t      |
| Composite, closed hull + ramp         | ~83 t   | 25 t  | **~40 t**  |
| Same, STO overload (+15 % gross)      | ~83 t   | 25 t  | **~60 t**  |

### 5.5 New open questions *(historical: live list in §0.3)*
- [x] Update drawing: upswept aft body with ramp, outboard fins, kneeling gear, no pod (done 2026-10-14: `th-2-re-design.svg/.png`; v1 with pod kept as `th-2-re-design-v1.*`).
- [x] Cargo standard: ISO 20 ft containers (decided 2026-10-14, §10).
- [x] Hold sized for 2×2 20 ft containers (Heavy), see §10.
- [→] Downwash effect on the open ramp area and on people near it during hover (now **E7**).

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

### 7.4 New open questions *(historical: live list in §0.3)*
- [x] Lifting-area options per variant: **H = B+D, F = A+C** (decided 2026-10-14, see §8).
- [x] Stop/fold fans vs. feathered: feathered, ~Mach 0.7 (§10.1).
- [x] Shared parts: no, optimise each aircraft (decided 2026-10-14).
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

### 8.4 New open questions *(historical: live list in §0.3)*
- [x] H: structure designed for 270 t STO (decided 2026-10-14, see §9).
- [x] F: proven separate turboshafts + cruise jets (decided 2026-10-14, see §9).
- [x] F: feathered fans, ~Mach 0.7, no experimental tech (decided 2026-10-14, §10).
- [x] Hot-and-high check: done, see §10.
- [x] Drawings for TB2-H and TB2-F: `th-2-variants.svg/.png` (2026-10-14).

---

## 9. Decisions + final first-order numbers (2026-10-14)

### 9.1 Decisions
- **TB2-F Fast: proven separate engines.** Turboshafts drive the lift fans, and 2
  turbofans provide cruise thrust. Convertible engines are dropped (lower risk,
  gives up ~4–5 t payload).
- **TB2-H Heavy: structure and gear designed for the full 270 t short take-off weight.**

### 9.2 Model refinements (`th-2-sizing.py`) *(numbers superseded by §10.4: 6 fans, hot-and-high)*
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

### 9.4 Open questions (carried forward) *(historical: live list in §0.3)*
- [x] F: feathered fans, ~Mach 0.7, no experimental tech (decided 2026-10-14, §10).
- [x] H: STO strip length and rough-field capability (see §11) (gear flotation for 270 t on
      unpaved strips).
- [x] Hot-and-high check: done, see §10.
- [x] Drawings for TB2-H and TB2-F: `th-2-variants.svg/.png` (2026-10-14).

---

## 10. Iteration 5 (2026-10-14): containers, 6 fans, hot-and-high

### 10.1 Decisions
- **Cargo = standard ISO 20 ft containers** (6.06 × 2.44 × 2.59 m; high-cube 2.90 m;
  max gross ~30 t).
- **Fast: feathered fans, ~Mach 0.7.** No experimental technology.
- **No shared parts:** each aircraft is fully optimised for its role.
- **Hot-and-high included up front:** Africa (desert + highlands), Andes, Himalaya,
  with a global-warming temperature margin.
- **6 fans** for fan-out safety (see 10.3).

### 10.2 Container hold
- **Heavy, 2 × 2 on one level: yes, realistic.** Hold ≈ 13.5 m long × 6.0 m wide ×
  3.3 m high (3.6 m for high-cube), roller floor + winch, loaded via the rear ramp.
  Comparison: C-17 hold 5.5 m wide, An-124 6.4 m wide. The Heavy's ~26 m wide body
  has room to spare.
  - Option: hold length ~20 m (3 × 2 = 6 containers) for light/bulky STO cargo.
- **Weight, not volume, is the limit:** 4 full containers (up to ~120 t) exceed
  every payload. VTOL: 1–2 loaded containers or 4 light ones (relief goods).
  STO: 4 containers at ~18–26 t average.
- **Fast:** 1 wide × 2 long; hold ≈ 13.5 × 3.2 × 3.3 m. VTOL: 1 lightly loaded
  container; STO: 1–2.

### 10.3 Six fans: why it works
- **4 fans, one fails:** the diagonally opposite fan must drop to ~0 to keep the
  aircraft level, leaving only 2 fans at 2× thrust each. Not survivable in a hover.
- **6 fans as 3 lengthwise pairs, middle pair at the CG, one fails:** solving the
  roll/pitch balance gives the 4 remaining "good" fans at **1.5×** nominal
  thrust, with the fan opposite the failure throttled to ~0.
  Total power is only ~+7 % (fine on a 2.5-min emergency rating). But each fan +
  gearbox must handle ~1.37× thrust ≈ 1.6× power for a short time, which makes
  the drivetrain heavier.
  (8 fans → 1.33×, but more units; 6 is the sweet spot.)
- **Cost:** about −10 t VTOL payload on the Heavy at sea level (heavier
  drivetrain + more fan units). This is the price of a survivable hover
  ("Category A" style).
- **Layout:**
  - Heavy: front tandem-wing tips / middle pair at CG on short sponsons beside the
    hold / rear wing tips.
  - Fast: canard tips / main-wing tips (wing moved so its fans sit at the CG) /
    H-tail tips.

### 10.4 Hot-and-high results (`th-2-sizing.py`, flat-rated engines)
Design conditions (with warming margin): SL 15 °C, Sahel SL 50 °C, E-Africa highlands
2,500 m 40 °C, Andes altiplano 4,000 m 25 °C, Himalaya 5,000 m 15 °C.

**The physics:** thin, hot air means the fans need more power, *and* the engines
make less. At 2,500 m / 40 °C the engines need ~1.8× sea-level rating. Bigger fans
(lower disk loading) are the main lever, up to a point (duct weight grows with area).

VTOL payload, 6 fans, **design point 2,500 m / 40 °C (recommended)**:

| | Heavy 6 × Ø14 m | Fast 6 × Ø10 m |
|---|---|---|
| Disk loading / downwash | ~217 kg/m² / ~45 m/s | ~212 kg/m² / ~44 m/s |
| Installed power (SL rating) | ~135 MW | ~67 MW |
| Empty | ~156 t | ~83 t |
| VTOL payload, 1,500 km mission, up to 2,500 m/40 °C | ~12 t | ~5 t |
| **VTOL payload, 300 km shuttle, up to 2,500 m/40 °C** | **~36 t** | **~14 t** |
| VTOL 300 km shuttle, Andes 4,000 m | ~10 t | ~0 |
| VTOL Himalaya 5,000 m | not possible | not possible |
| STO payload (sea level, 1,500 / 300 km) | ~72 / ~105 t | ~28 / ~39 t |

For comparison, designing for sea level 50 °C only (Heavy 6 × 12 m, Fast 6 × 10 m)
gives more payload at low altitude (H ~22 / 47 t, F ~10 / 19 t for 1,500 / 300 km),
but **no VTOL at all in the highlands**.

**Conclusions**
1. 2,500 m / 40 °C as the design point covers all of Africa incl. the highlands,
   with warming margin. Bonus: the bigger fans cut downwash from ~65 to ~45 m/s.
2. **Operating doctrine becomes essential**: fly long distance to a strip (STO or
   conventional landing, big payload), then **VTOL shuttle** from there
   (~300 km legs, light fuel).
3. **4,000–5,000 m heavy VTOL is beyond physics for this class**, and for real
   aircraft too: the Mi-26 can only hover out of ground effect up to ~1,800 m
   at max weight. Himalaya rescues are done by light helicopters. Andes /
   Himalaya = STO onto high-altitude strips (El Alto 4,060 m has a 4 km runway),
   or a future light high-altitude variant.
4. The Fast at 1,500 km + VTOL is now a medevac/crew aircraft (~5 t). Its value is
   speed to a strip, then short VTOL hops.

### 10.5 Discussion: options for Q8 (balance) and Q9 (fan load split)
**Q8: keep the aircraft balanced from empty to full hold**
- a. Hold centred on the CG (done), containers loaded symmetrically around it.
- b. Fore/aft fuel trim tanks (Concorde-style).
- c. Lifting surfaces sized for a CG range of ±~4 % of length. Rough lift split:
  Heavy tandem ~45 % front / 55 % rear; Fast canard ~15 %, wing ~75 %, H-tail ~10 %.
- d. Fly-by-wire with relaxed stability.
- Recommendation: all four. None of them is exotic.

**Q9: fan load split (6 fans, middle pair at the CG)**
- a. **Equal fans everywhere**: one fan type, loads balanced by blade pitch.
  Simplest; fan-out case is symmetric. (Recommended.)
- b. Larger middle pair: carries more in normal hover, but the fan-out case loads
  the outer fans, so little is gained.
- c. Unequal front/rear fans matched to lever arms: needed only if the middle pair
  can't sit at the CG.

### 10.6 Q10: downwash and rescue hoisting
- Agreed: **winching from the rear ramp is unrealistic.** The load hangs behind the
  CG, sits in the rear fans' wake, and can swing into the tail.
- Options:
  - **Rescue hoist + cargo hook at the CG** through a floor hatch between the
    middle fans (CH-47 "hell-hole" style), with a long line (40–60 m) to get people
    below the worst downwash.
  - Primary Thunderbird doctrine: **land 100–200 m away and deploy vehicles down
    the ramp.**
  - Downwash ~45 m/s (bigger fans) is still well above a heavy helicopter's, so
    keep people clear.

### 10.7 New open questions (from 6 fans + hot-and-high) *(historical: live list in §0.3)*
- [→] Heavy middle fans on sponsons: width impact (now **E5**).
- [→] Middle fans: tilting or fixed? (now **D4**)
- [→] Fan-wake interaction during transition (now **E1**).
- [→] Cross-shaft routing to 6 fans (now **E2**).
- [→] Fast canard / H-tail ~34 m: still "slim"? (now **E6**)
- [→] Future light high-altitude variant? (now **D5**)
- [x] Q7 strip length + rough field: first estimate done, see §11.
      compared with existing aircraft (C-130J, A400M, C-17, An-72/74 USB).
- [x] `th-2-variants` redrawn: 6 fans on side booms (H) / canard-wing-H-tail (F), container hold, more wheels (2026-10-14). Old version: `th-2-variants-v1.*`.

---

## 11. Strip length vs. existing aircraft (2026-10-14)

Model: `th-2-strip.py`. Point-mass simulation: fans tilted forward at the best fixed
angle, wing + body lift, thrust falling with speed, rolling friction (paved 0.03 /
unpaved 0.08), airborne to 15 m. Landing: 6° steep approach from 15 m, touchdown with
fans at 70 % thrust, braked roll (paved μ 0.40 / unpaved 0.25). Uses the 6-fan,
2,500 m / 40 °C design (H 6 × Ø14 m, F 6 × Ø10 m).

### 11.1 Results (unfactored, first-order)
| Condition | **Heavy TO @ 270 t** | **Heavy LDG @ 230 t** | **Fast TO @ 125 t** | **Fast LDG @ 113 t** |
|---|---|---|---|---|
| Sea level 15 °C, paved | vertical | ~190 m | vertical | ~190 m |
| Sahel SL 50 °C, unpaved | vertical | ~240 m | vertical | ~240 m |
| E-Africa 2,500 m 40 °C, unpaved | ~320 m | ~310 m | ~250 m | ~310 m |
| Andes El Alto 4,000 m 25 °C, paved | ~470 m | ~300 m | ~380 m | ~300 m |

**Planning values (×1.5 for engine/fan-out margins, pilot technique, model
optimism): Heavy ≲ 700 m, Fast ≲ 600 m, at every condition up to 4,000 m.**

### 11.2 Existing aircraft for comparison (published / press figures)
| Aircraft | Weight | Field performance |
|---|---|---|
| C-130J-30 | MTOW ~74 t | landing ~915 m (3,000 ft) at 61 t |
| A400M | ~120–140 t | landing on unprepared strips < 800 m (2025 grass trials, 123 t) |
| C-17 | MTOW 265 t | operates from 1,067 m (3,500 ft) strips; take-off with 72.6 t payload needs ~2,300 m (7,600 ft) |
| An-72 (USB, Coandă) | ~33 t | take-off roll 620 m, landing roll 420 m |

**Takeaway:** both TB2 variants beat everything in service by a wide margin. The
Heavy at C-17 weight needs a strip about the length an A400M needs (or less),
and the An-72's rolls are longer than TB2's estimated distances.
Reason: the fans carry most of the weight, so wing lift only has to make up the rest.

### 11.3 Surprise: hot-and-high power gives lowland VTOL at STO weight
> **Superseded by §18:** with consistent margins the sea-level hover limit is ~228 t
> (Heavy) / ~114 t (Fast), not 280 / 140 t, so VTOL at 270 t is not available.

The engines are flat-rated for 2,500 m / 40 °C, so at sea level there is lots of
spare thrust. Max hover (5 % margin): Heavy ~280 t, Fast ~140 t at sea level.
At lowland sites the Heavy could **take off vertically at up to the 270 t structural
limit**, so the "STO payload" (~72–105 t) becomes VTOL payload there.
Caveats: control margin is reduced (1.05 instead of 1.15) and fan-out safety is not
covered at that weight. Needs a rule like "VTOL above 200 t only below X m / Y °C,
fan-out risk accepted" or a lower cap (~230–250 t). → open question.

### 11.4 Rough-field gear (flotation)
- Main-wheel load reference: A400M ~11 t/wheel, C-17 ~17 t/wheel.
- Heavy 270 t on 12 wheels = 22.5 t/wheel. Too much for soft strips →
  **~22 main wheels (11 per side)** for A400M-class soft-field capability.
- Fast 125 t on 4 wheels = 31 t/wheel. Far too much → **~10 main wheels (5 per side)**.
- Drawing `th-2-variants` updated accordingly.

### 11.5 New open questions *(historical: live list in §0.3)*
- [→] Lowland VTOL above 200 t (now **D1**).
- [→] Downwash on unpaved strips (now **E7**).
- [→] Fan-out during take-off roll (now **E3**).
- [→] Gear weight for 22 / 10 main wheels (now **E4**).

---

## 12. How the fans tilt without hurting the wing (2026-10-14)

Sheet: `th-2-fan-tilt.svg/.png`.

**The problem:** in the `th-2-variants` v2 drawing the Heavy's fans sit *on top of*
the wings and booms. They could not rotate there without hitting structure, and in
hover they would blow straight down onto the wing ("download", ~10 % thrust loss on
the V-22).

### 12.1 How a pod tilts
- Each duct rotates about a **spanwise spindle**: 0° (hover, thrust up) → ~45°
  (transition) → 90° (cruise, thrust forward).
- **The drive shaft runs along the tilt axis**, into a gearbox at the pivot, so
  tilting never disconnects the drive (the V-22 principle).
- Conversion takes ~15–30 s while accelerating; tilt actuators are synchronised
  by fly-by-wire.
- Left and right fans counter-rotate, so the gyroscopic moments from tilting
  cancel out.
- In cruise the duct is aligned with the flow and acts as a ring wing (a little lift).

### 12.2 Structural / aero issues and standard fixes
| Issue | Fix |
|---|---|
| Download onto a wing below the fan | No wing under any fan in plan view |
| Cantilevered heavy spinning pod: whirl flutter | Short, stiff supports, preferably on both sides of the duct |
| Pivot carries full thrust (1.5× in fan-out) + tilt torque | Pivot is a frame node in the torsion box |
| Gyroscopic loads | Counter-rotating pairs, slow tilt |
| Cruise drag of the duct | Tilt 90°, duct works as ring wing |

### 12.3 Three ways to mount a tilting fan
- **A. Tip spindle** (Bell X-22A ducts, V-22 nacelles):
  - Proven. The wing ends where the duct starts, so there is no download.
  - Cantilever, so flutter risk. Only works at a tip.
  - → Fast canard tips and H-tail tips.
- **B. Fork / ladder bay:**
  - The duct sits between an inner and an outer rail and pivots on both, so
    there is no cantilever. Rails + wings form a stiff ladder frame.
  - Costs some extra rail weight and drag.
  - → all 6 Heavy fans; the Fast's wing fans (fork bay at the wing-fold joint).
- **C. Fan-in-body + exit louvres** (Ryan XV-5 Vertifan):
  - No tilt mechanism, but needs deep structure. A Ø14 m fan doesn't fit
    beside a 6 m hold (~10 m available).
  - Limited vectoring; dead weight in cruise.
  - → possibly smaller fixed middle fans (ties to D4).

### 12.4 Proposed Heavy layout: ladder frame
- Along each side: **front fan · front wing · middle fan · rear wing · rear fan**.
  No wing sits under any fan.
- Two longitudinal rails per side (inner ~14.5 m, outer ~29.5 m from the
  centreline). Each fan pivots on both rails. The wings are the "rungs" that tie
  the rails to the body.
- Fan stations at ~20 / 46 / 74 m from the nose. The middle pair stays at the CG
  above the hold.
- Span ≈ 66 m. In cruise the front fans blow over the front wing (blown-wing bonus).
- Front fans' wake hitting the middle/rear fans in transition remains open (E1).

---

## 13. Variants v3: ladder frame + front views; pod designs dropped (2026-10-14)

- **User:** add front views; drop any design with the original pod on high legs
  (too impractical). → `th-2-re-design-v1.*` removed (still in git history).
- `th-2-variants.svg/.png` v3: top, side and **front** views of both variants,
  redrawn with the ladder-frame fan mounting (D6, adopted provisionally).
  The previous sheet is kept as `th-2-variants-v2.*`.

### 13.1 Layout changes the front view forced
- **Tilt clearance:** an upright fan reaches one radius below its pivot. Pivots
  must be ≥ radius + ~2 m above the ground, or the fans hit the ground when
  tilting (or during a rolling take-off at large tilt angles).
  → **Heavy rails at z ≈ 9 m** (Ø14 m fans: 2 m clearance upright),
  **Fast rails at z ≈ 7 m** (Ø10 m: 2 m clearance).
- **Heavy:** the low front wing now rises to the rails (*dihedral*); the high rear
  wing drops to the rails (*anhedral*). Seen from the front, the two wings and the
  rails form a closed box: stiff, and it keeps the rails level.
- **Fast:** reordered along each rail as front fan · canard · middle fan
  (at CG, x ≈ 32 m) · main wing · rear fan · H-tail + twin fins on the outer rails.
  This keeps the wing out from under every fan. The hold moved forward to the
  new CG.
  The wing now folds just outboard of the outer rail: **folded span ≈ 37 m**
  (was ≈ 42 m).
- Rail weight (4 rails per aircraft, ~70 m long each) is not yet in the sizing
  model → E4.

---

## 14. Maximised hold with corridors (2026-10-14, decision D7)

**Why:** the drawing showed the old hold used ~1 % of the Heavy's body (270 m³ in a
~25,000 m³ envelope); a C-17 hold is twice that in a smaller aircraft.
**User:** maximise the hold to practical measures for normal vehicles, small
helicopters, livestock and people. A central wall, or two walls with doors giving
3 corridors, is fine for structure.

**Why walls work:** a wide, flat body can't use a round pressure hull, so it
needs internal walls/ties anyway. This is the blended-wing-body "multi-bay"
layout (e.g. Boeing BWB studies). The walls carry body bending and tie the flat
skins; door openings every ~12 m keep the corridors connected.

### 14.1 Heavy (drawing v4)
| | |
|---|---|
| Hold floor | x ≈ 12–62 m (50 m) behind the cockpit, + ramp area to ~76 m |
| Corridors | **centre 7 m wide × 5.0 m high**; **2 sides 6 m wide × 4.2 m high**; two walls with doors |
| Volume | ≈ 4,300 m³ (16× the old hold, ~8× a C-17) |
| Ramps | 3 rear ramps, one per corridor (smaller, lighter than one 20 m ramp; redundant) |
| Structure change | front wing moved from low to **mid (z ≈ 8.5 m), above the hold ceiling**, so its carry-through no longer cuts the hold; rear wing stays high |
| Engines | turboshafts in the rails / fan stations, not in the body |
| Gear | sponsons along the lower sides, outside the corridors |

What fits (centre corridor): 2 trucks abreast (2.55 m wide, up to 4.0 m high), small
helicopters (e.g. H125 class, ~3.3 m high, rotor folded), fire engines.
Side corridors: 2 × 20 ft containers abreast, livestock pens, seats or stretchers.

### 14.2 Fast
- Hold x ≈ 11–55 m (44 m), 9.5 m wide, **one central wall → 2 corridors 4.6 m ×
  4.0 m**, ≈ 830 m³, 2 rear ramps.
- The canard and wing carry-throughs (z ≈ 7 m) pass above the 4 m ceiling.
- The Fast cruises at FL250, so the hold must be pressurised; the central wall
  also ties the flat sides.

### 14.3 Cost (in `th-2-sizing.py`, `hold_t`)
> Payloads below are before the §18 model fixes; current values are in §0.1.

- Heavy-duty floor in the vehicle lanes, light-duty floor elsewhere, plus corridor
  walls: **≈ +9 t Heavy, ≈ +4 t Fast** (rough estimate; partly offset by
  wall-tied skins).

| Payload | Heavy before → now | Fast before → now |
|---|---|---|
| VTOL, 300 km shuttle | 36 → **27 t** | 14 → **10 t** |
| VTOL, 1,500 km | 12 → **3 t** | 5 → **1 t** |
| STO, 300 / 1,500 km | 105 / 72 → **96 / 63 t** | 39 / 28 → **35 / 24 t** |

**Volume is now never the limit; weight is.** Rough capacities in a VTOL shuttle
(Heavy ~27 t): ~250 people with kit, ~50 cattle, 2–3 trucks, a small helicopter
plus vehicles. On STO (~96 t): ~900 people, ~190 cattle, 8–10 trucks.
The 1,500 km VTOL mission is now marginal: the doctrine "STO to a strip, VTOL
shuttle from there" matters even more.

### 14.4 Notes
- The Heavy's hold centre (x ≈ 37 m) is ahead of the CG / middle fans (x ≈ 46 m),
  so heavy items go aft and light items forward; loading rules and trim → **E8**.
- The Heavy can cruise unpressurised at ≤ 3,000 m (fans, ~330 kn), which suits
  livestock and the huge flat hold.

---

## 15. Could it land on water? (2026-10-14)

**Short answer: yes, surprisingly well, because it lands vertically.** The hard
part of seaplanes is the high-speed touch-down and take-off run (planing hull, step,
slamming loads). A VTOL aircraft hovers down to near-zero speed and simply floats.
(TB2 in the series set down on water to launch Thunderbird 4 from its pod.)

| | Heavy | Fast |
|---|---|---|
| Water displaced at VTOL weight | ~195 m³ | ~98 m³ |
| Draft on its flat bottom (if watertight) | **~0.13 m** | **~0.18 m** |
| Fan ducts above water (hover position) | ~7.6 m | ~5.8 m |
| Roll stability (metacentric radius) | ~370 m (barge-like) | ~57 m |

**What it needs**
- **Watertight lower hull** and ramp seals, bilge pumps, sea anchor, mooring points.
- **A chined / shallow-V bottom** instead of dead flat, against wave slamming
  while floating (the chines are already there).
- **Spray-tolerant fans and engines.** ~45 m/s downwash onto water makes heavy
  spray: salt erosion and engine ingestion. Needs marinised engines (as on naval
  helicopters), inlet spray shields, fresh-water wash. The composite airframe
  itself doesn't corrode.
- **Ramp as a boat slipway:** with the ramp lowered into the water, launch and
  recover rescue boats or amphibious vehicles. Ideal for floods.

**Limits**
- **VTOL only on water.** No STO from water without a planing hull and step
  (not worth the weight).
- **Sea state ~4–5** max to keep waves off the ramp sill and rails (rails ~7–9 m up).
- A floating Heavy at 0.13 m draft drifts like a barge in wind: needs a sea anchor.
- Cost: sealing, pumps, marinisation, maybe ~1–3 t. → **D8**.

**Bonus idea:** firefighting. Hover over water and refill an internal tank with a
snorkel pump (like helicopter "Bambi" snorkels); the hold volume allows a very
large tank.

---

## 16. Would a second level help? (2026-10-14)

**Short answer: a fixed second deck mostly adds weight, not capacity.** The hold is
already limited by payload *weight*, not floor area or volume.

| | Value |
|---|---|
| Heavy main deck | ~950 m² (50 × 19 m), ~4,300 m³ |
| Average load density at full payload | VTOL shuttle 27 t → ~28 kg per m² of floor; STO 96 t → ~100 kg/m² |
| Floor area needed for a full 96 t STO load | people ~580 m², cattle ~350 m², sheep ~670 m²: **all fit on the main deck** |
| Fixed 2nd deck, side corridors only (600 m²) | ≈ +6 t |
| Fixed 2nd deck, full width (950 m²) | ≈ +9 t |
| Effect on Heavy VTOL shuttle payload | 27 → ~21 t (side) / ~18 t (full) |

**Where a second level *does* help**
- **Mixed loads:** vehicles or livestock below, people above, kept separate
  (hygiene, safety).
- Low-density cargo that can't be stacked (small animals, fragile goods).
- Stretcher racks for medevac (standard 3-high racks, no deck needed).

**Height check (Heavy):** lower deck 4.2 m + floor 0.5 m + upper deck ~2.5 m
needs ~7.2 m (z 2.3 → 9.5). That fits under the body top, but it clashes with the
front-wing carry-through at z ≈ 8–9 m. Either the front wing moves up to ~10 m
(only ~2.5 m below the rear wing), or the upper deck is interrupted there.
**Fast:** 8 m body, 4 m hold, so no room for a real second deck (racks only).

**Recommendation → D9:** no fixed deck. Use **removable mezzanine / multi-deck
modules** (palletised passenger decks, double-deck livestock stalls, stretcher
racks) that roll in on the floor rails and lock to the corridor walls. Their
weight counts only when carried, as payload. The corridor walls make good
attachment points.

---

## 17. Use case: prefab housing (2026-10-14)
> VTOL counts below assume ~27 t / ~10 t; after §18 the Heavy carries ~9 t (≈ 50
> shelters or 1 container home per VTOL shuttle). STO counts drop ~20 %.


User idea: transport prefab houses. Rough industry figures, not a specific product:

| Prefab type | Typical size / weight | Heavy (VTOL ~27 t / STO ~96 t) | Fast (VTOL ~10 t / STO ~35 t) |
|---|---|---|---|
| Modular house module (wood frame) | ~3–4.3 m wide, 3–3.9 m high, 10–15 m long, ~10–20 t | centre corridor 7 × 5 m fits any; sides take ≤ ~4 m wide. VTOL 1–2, STO ~5–6 | ≤ 4.3 m wide fits a corridor; ~1 on STO |
| Container home (20 ft) | 6 × 2.4 × 2.6 m, ~3–6 t fitted | VTOL ~5, STO ~16–20 | VTOL 2, STO ~6 |
| Flat-pack emergency shelter (Better-Shelter type, ~17 m²) | ~150–200 kg, ~1–2 m³ packed | VTOL ~150 (homes for ~750 people), STO ~500 (~2,500 people) | VTOL ~50, STO ~180 |

- **Flat-pack shelters are the ideal cargo:** light and bulky, so they fill the
  4,300 m³ hold at about the same point as the weight limit.
- House modules fit easily by size; weight limits them to 1–2 per VTOL trip.
  The 7 m centre corridor takes even "double-wide" units that need road escorts.
- Loading: modules on skids over the floor rails or on a low trailer through the
  corridor's own ramp.
- Relief chain: Heavy STO load of ~500 shelters / ~16 container homes to the
  nearest strip, then VTOL shuttles of modules or shelter batches into the
  cut-off area.

---

## 18. Model cross-check and fixes (2026-10-14)

Cross-check of `th-2-sizing.py` and `th-2-strip.py` against the current design
(log entry 22), then fixed:

| Fix | Before | After |
|---|---|---|
| Shared data and physics | two copies of variants, rho, hover power | `VARIANTS`, margins and `max_vtol_weight()` in `th-2-sizing.py`; `th-2-strip.py` imports them |
| Margins in the strip sim | 1.05 thrust, full contingency power | same as sizing: 1.15 thrust, 20 % power reserve |
| Ladder-frame rails | not in model | 4 rails (72 m / 66 m), per-metre mass from fan-out pivot load + pivot fittings: **~14.9 t / ~8.5 t** |
| Soft-field gear | not in model | Heavy +2 t (22 main wheels); Fast none |
| Cruise L/D | 10 / 11 | **9 / 9.5** (rails + ducts add ~30 % wetted area); Fast cruise jets grow 7.4 → 8.6 t |
| Hover fuel | at sea-level density | at the design point |
| Strip sim | span 64 m, drag before rails, landing weight typed in, max TOW uncapped | span 66 m, drag +15–20 % for rails, landing weight from sizing fuel, max TOW capped at STO limit |
| Mission range | global changed in `__main__` | `range_km` argument |

### 18.1 Results
| | Heavy before → now | Fast before → now |
|---|---|---|
| Empty | 165 → **182 t** | 87 → **97 t** |
| Max VTOL weight, sea level | "282 t" → **228 t** | "141 t" → **114 t** |
| VTOL payload 300 km (2,500 m / 40 °C) | 27 → **9 t** | 10 → **none (−0.3 t)** |
| VTOL payload 1,500 km | 3 → none | 1 → none |
| STO payload 300 / 1,500 km | 96 / 63 → **78 / 42 t** | 35 / 24 → **25 / 12 t** |
| STO take-off to 15 m (270 / 125 t) | vertical at SL; 316 m at 2,500 m | **265 m** at SL; **478 m** at 2,500 m unpaved; **679 m** El Alto (Fast 222–522 m) |

All STO cases still meet the ≤ 700 m / ≤ 600 m planning strips.

### 18.2 Sensitivity to rail mass (300 km mission)
| Rails | Heavy VTOL / STO | Fast VTOL / STO |
|---|---|---|
| × 0.5 | 17 t / 86 t | 4 t / 29 t |
| × 1.0 | 9 t / 78 t | −0.3 t / 25 t |
| × 1.5 | 2 t / 71 t | −5 t / 20 t |

Design point (rails × 1.0, 300 km VTOL payload): Heavy at SL 35 °C ~22 t, at
1,500 m 35 °C ~15 t; Fast at SL 35 °C ~6 t, at 1,500 m 35 °C ~3 t.

### 18.3 What it means
- The ladder frame costs about as much as the useful VTOL payload. **VTOL is now
  marginal for the Heavy and not viable for the Fast at the 2,500 m / 40 °C point.**
- STO is still strong: the aircraft are good STOL freighters with VTOL as a
  light-load capability. → **D10**.
- Volume is huge relative to payload (§14); a 9 t VTOL load is ~50 flat-pack
  shelters or one container home.
- Remaining assumptions: CG kept at the middle fan pair by loading rules (E8);
  CLS (wing+body lift) not re-derived for the ladder layout.

---

## 19. Fast variant dropped (2026-10-14)

**User:** with the §18 results, the Fast is probably already covered by current
aircraft; if so, drop it.

**Check (rough public figures):**

| | Fast (after §18) | A400M | C-130J-30 | C-390 |
|---|---|---|---|---|
| Payload | 25 t (300 km) / 12 t (1,500 km) | up to ~37 t; ~20 t over ~6,000 km | ~19 t | ~26 t |
| Cruise | ~420 kn | ~420 kn | ~340 kn | ~470 kn |
| Strip | ≤ 600 m | ~750–1,000 m, soft strips | ~900–1,100 m | unpaved capable |
| Vertical | none at the design point | — | — | — |

Vertical light lift is covered by CH-47F (~10 t sling) and CH-53K (~12 t hot-and-high).
Without real VTOL the Fast is roughly an A400M with a ~300 m shorter strip and far less
range. **Decision: drop the Fast.**

**What changed**
- `th-2-sizing.py` / `th-2-strip.py`: Fast removed from `VARIANTS` (last entry kept
  as a comment for comparison runs).
- Drawing: new Heavy-only sheet `th-2-heavy.svg/.png` (v5); the two-variant sheet
  is kept as `th-2-variants-v4.*`.
- Fast-only items closed: E6, the Fast engine and cruise-fan decisions. History
  sections (8–18) keep their Fast content as record.

**Same test for the Heavy → D11.** A C-17 (~77 t, ~1,000 m strips, more range,
faster) plus a CH-53K (~12 t vertical) cover most of its numbers. What the Heavy
still has alone: the ~4,300 m³ corridor hold, 270 t from ≤ 700 m soft strips,
vertical + STO in one airframe, and water landing (§15). With only ~9 t VTOL
(§18), D10 (more VTOL payload) decides whether that niche is worth an aircraft.

---

## 20. Do bigger fans and engines exist? (2026-10-14)

**What the Heavy needs per fan:** ~22.5 MW installed (SL rating), ~15 MW through
the gearbox, Ø14 m duct.

| Part | Largest that exists (rough public figures) | vs. the Heavy |
|---|---|---|
| Open rotors | Mi-26: 32 m rotor; Mi-12 (V-12): 2 × 35 m; CH-53K: 24 m | Bigger diameters are common; but open, not ducted or tilting |
| Ducted fans on aircraft | A few metres (fan lifts, ducted-fan VTOL prototypes, turbofan fans ~3.4 m) | **Nothing near 14 m has flown** |
| Large ducted fans on the ground | NASA Ames 40×80 / 80×120 ft wind tunnel: 6 fans Ø ~12 m, ~100 MW total | Similar size and power, but heavy and fixed |
| Turboshafts | ~8–10 MW each (Mi-26 D-136 ~8.5 MW; A400M TP400 ~8 MW turboprop) | ~2–3 engines per fan; marine/industrial units (LM2500 ~25–30 MW) are much heavier per MW |
| Gearboxes | Mi-26 main gearbox ~17 MW, the largest flying | Each fan needs ~15 MW: **one Mi-26 gearbox per fan, and it must tilt** |

**Conclusion:** the engines exist in number (≈ 15 units), the gearboxes are at the
edge of what has flown, and 14 m tilting ducted fans would be new. Bigger than
that is beyond current hardware.

**Would bigger help anyway?** No, the model says (300 km mission):

| Case | Per-fan gearbox | Empty | VTOL payload | STO payload |
|---|---|---|---|---|
| Current: 200 t, 6 × Ø14 m | 15.3 MW | 182 t | **9.3 t** | 78 t |
| 6 × Ø16 m (rails 80 m) | 13.4 MW | 185 t | 6.7 t | 75 t |
| 6 × Ø18 m (rails 88 m) | 11.9 MW | 190 t | 1.8 t | 70 t |
| 8 × Ø14 m (rails 96 m) | 9.9 MW | 188 t | 3.9 t | 73 t |
| 240 t VTOL, 6 × Ø16 m | 17.6 MW (> Mi-26) | 217 t | 12.9 t | 96 t |

Bigger fans need less power, but the longer rails and heavier ducts cost more
than the power saved. Scaling the whole aircraft to 240 t gains only ~3.6 t of
VTOL payload and needs gearboxes beyond anything flying. So D10 now rests on
lower design point, lighter rails / other fan mounting, or accepting VTOL as a
light-load capability.

---

## 21. Do existing aircraft already do this? (2026-10-14)

Two roles: **(1) heavy transport over long distance**, **(2) final delivery** (STOL
strip or VTOL). Rough public figures from memory; approximate.

**Heavy (current / 240 t version):** STO 78 t (300 km) / 42 t (1,500 km) from
≤ 700 m soft strips at 270 t, ~330 kn; VTOL 9 t (13 t at 240 t) at 2,500 m / 40 °C.

### 21.1 Role 1: long-distance heavy transport
| Aircraft | Payload | Range with that load | Strip | vs. Heavy |
|---|---|---|---|---|
| **C-17** | ~77 t | ~4,400 km | lands in ~1,000 m semi-prepared; needs ~2,000+ m to take off at max weight | Same payload, ~3× the range, ~450 kn |
| A400M | ~37 t | ~3,300 km (20 t: ~6,000 km) | ~750–1,000 m soft at tactical weights | Less payload, much more range |
| An-124 | ~120–150 t | ~3,000–4,500 km | ~3,000 m paved | Far more payload, runways only |
| Il-76MD-90A | ~60 t | ~4,000 km | ~1,500–2,000 m | Less payload, more range |

Over long distance the **Heavy loses clearly** (42 t over 1,500 km at ~330 kn).

### 21.2 Role 2: final delivery
**STOL** (delivering only needs a heavy *landing*; the aircraft leaves light):
| Aircraft | Payload | Strip | vs. Heavy |
|---|---|---|---|
| C-17 | ~70 t | ~1,000 m (landing) | Close to the Heavy's 78 t; needs a longer, firmer strip |
| A400M | ~25 t | ~750 m soft | |
| C-130J | ~15–19 t | ~900 m soft | |
| C-27J / C-295 | ~9–11 t | ~600 m soft | Same strip class as the Heavy, ~1/8 the load |

**VTOL / helicopter:**
| Aircraft | Payload | Notes | vs. Heavy |
|---|---|---|---|
| **Mi-26** | ~20 t internal or sling (sea level) | Largest flying helicopter; less when hot-and-high (no reliable figure from me) | ≥ the Heavy's 9 t |
| **CH-53K** | ~12 t sling over ~200 km radius at 900 m / 33 °C | Spec'd for hot-and-high | ≈ the 240 t Heavy (13 t) |
| CH-47F | ~10 t sling | Widely available | ≈ the Heavy |

In development, not yet existing: hybrid airships (e.g. Flying Whales LCA60T, ~60 t
with VTOL-style hover loading; Airlander ~10 t).

### 21.3 Conclusion
- The combination **C-17 / A400M to a strip + Mi-26 / CH-53K / CH-47 for the last
  leg** already covers both roles, with more range in role 1 and equal or better
  VTOL payload in role 2.
- What only the Heavy does:
  - delivers **~78 t into a ≤ 700 m soft strip with no transshipment** (C-17
    needs ~1,000 m firmer ground; the next aircraft that lands in 700 m soft
    carries ~10 t);
  - a **~4,300 m³** hold (C-17 ~550 m³) for bulky relief cargo;
  - VTOL and STO in one airframe, and water landing.
- The 240 t version doesn't change this: VTOL ~13 t ≈ a CH-53K.
- So the Heavy is best seen as a **short-strip bulk lifter for the last few
  hundred km**, not as a long-haul transport or a heavy helicopter. That is
  the honest frame for D11.

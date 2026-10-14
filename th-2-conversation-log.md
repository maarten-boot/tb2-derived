# Thunderbird 2 redesign: conversation log

Condensed log of each exchange (user request → what was answered/done).
Technical detail lives in `th-2-re-design-ideas.md`; this file records the flow of the
discussion. Started 2026-10-14 (earlier exchanges reconstructed from the session).

---

### 1. Is the original TB2 flyable? What changes would make it fly?
**User:** TB2 flight capability is unscientific. Keep the bulky body (maybe as a lifting
body) and make it a real heavy VTOL transport.
**Answer:** The fatal flaw is wings at the tail with the CG far forward. Wing loading is
actually plausible (~1,100 kg/m²). VTOL is the real problem (~6 MN thrust,
hurricane downwash, ~290 MW). Redesign: lifting-body hull, canard or mid-body wing,
FBW, pod CG control, tilting ducted fans, weight down to ~150 t, optional partial
buoyancy.

### 2. Canard chosen; render an image; write notes to a file
**User:** Likes the canard (had thought of it too). Asked for an image (SVG/PNG)
and a notes file.
**Done:** `th-2-re-design.svg/.png` (plan + side), `th-2-re-design-ideas.md`.
Canard + mid-body forward-swept wing bracket the CG; 4 tilting ducted fans.

### 3. Drop the pod → rear ramp; fans limit payload; Rutan-style composites?
**Answer:** Adopt the ramp: closed hull is stiffer and lighter, less drag, kneeling
gear. Payload fraction for VTOL is low (~30 t at 150 t). Composites save 15–25 % of
structure (+30–40 % payload); Rutan foam-sandwich doesn't scale, so use
787/Stratolaunch-style carbon.

### 4. Update drawings (ramp, upswept tail, outboard fins, kneeling gear)
**Done:** drawing v2; v1 kept as `th-2-re-design-v1.*`.

### 5. No front view for now
**Done:** front view deferred in notes.

### 6. Could the fans be jets?
**Answer:** Possible (Harrier, Do 31), but bad for rescue: hot, fast exhaust, ~2.5
t/min hover fuel. Correction: tilt-fans cruise ~Mach 0.55. Options: accept, compound
(cruise jets), or tilting turbofans.

### 7. Go compound; more wing/lift area; two variants later
**Done:** drawing v3 with dorsal cruise jets; `th-2-wing-options.*` (A bigger span,
B tandem, C three-surface H-tail, D wide body + air guides). Variant idea: Heavy/slow
vs Fast/light.

### 8. Recompute with H = B+D, F = A+C
**Done:** `th-2-sizing.py`, same mission (1,500 km + 4 min hover). H ~39 t VTOL, F ~18 t.
Suggested convertible engines for F.

### 9. F uses proven separate engines; H structure for max STO weight (270 t)
**Done:** +5 t structure (2.0 g at overload weight). H ~34 / 95 t, F ~17 / 40 t.
STO missions are strip-to-strip.

### 10. Side views of the variants
**Done:** `th-2-variants.svg/.png` (top + side, same scale, spec boxes).

### 11. What questions are open?
**Answer:** Listed 12 open items, grouped as decisions / engineering checks / stale.

### 12. Answers on open questions; is the conversation being logged?
**User decisions:** ISO 20 ft containers, 2×2 on one level for Heavy? F feathered fans
(no experimental tech). No shared parts (optimise each). Explore 6 fans. Include
Africa / Andes / Himalaya hot-and-high (with global warming) up front. Q7 strip
length later (compare with existing planes). Rear-ramp winching unrealistic. Discuss
options for Q8/Q9.
**Done/answered:**
- 2×2 containers fit (hold ~13.5 × 6.0 × 3.3 m), but weight limits VTOL to 1–2
  loaded containers.
- 6 fans make a fan failure in hover survivable (remaining fans at 1.5×), costing
  ~10 t payload.
- Hot-and-high: recommended design point 2,500 m / 40 °C with bigger fans
  (H 6 × 14 m, F 6 × 10 m). VTOL is realistic up to the African highlands. At
  4,000–5,000 m heavy VTOL isn't physically viable, so STO onto high strips there.
- Doctrine: long-range to a strip, then 300 km VTOL shuttles (H ~36 t, F ~14 t).
- Model fix: flat-rated engines.
- Q8/Q9 options listed; winch replaced by a hoist/hook at the CG.
- This log file was created (previously only design notes were recorded, not the
  conversation).

### 13. Redraw with 6 fans + container hold, then strip length
**User:** Redraw the variants, then do the strip-length comparison.
**Done:**
- `th-2-variants.svg/.png` v2 (old one kept as `-v1`):
  - Heavy: 6 × Ø14 m fans on two side booms (box frame with the tandem wings),
    middle pair at the CG on sponsons, 2 × 2 orange containers, 11 wheels/side.
  - Fast: 6 × Ø10 m fans on canard / wing / H-tail tips, 2 containers in line,
    5 wheels/side.
- `th-2-strip.py` take-off/landing sim:
  - Heavy 270 t: vertical at lowland sites, ~320 m at 2,500 m/40 °C, ~470 m at El
    Alto 4,000 m. Landing ~190–310 m.
  - Fast: similar or shorter.
  - Planning values ≤ 700 / 600 m. Beats C-130J, A400M, C-17, An-72.
- Surprise: the hot-and-high power allows lowland VTOL up to ~270 t (open
  question on margins).
- Gear flotation: Heavy needs ~22 main wheels, Fast ~10.

### 14. Project moved to git repo `tb2-derived`; housekeeping
**User:** Moved the files into the git repo; asked for a status, then housekeeping.
**Done:**
- `th-2-re-design-ideas.md`:
  - New **§0 Current status**: variant summary, decisions table, and the single
    live open-questions list (D1–D5 decisions, E1–E7 engineering checks, 1 deferred).
  - Superseded sections marked; old checkboxes in §1–§11 now point to §0 or are
    closed (power plant, fan-out, stop/fold fans).
  - File index added.
- `README.md` expanded: summary table, drawing, file index, how to run the models.
- `th-2-sizing.py` default run now shows the current design (6 fans, 2,500 m / 40 °C,
  1,500 km and 300 km missions) instead of old comparisons.

### 15. How do the fans tilt without compromising wing strength and aerodynamics?
**User:** Can't visualise how the 6 fans move from horizontal to vertical without
compromising wing strength and aerodynamics.
**Answer / done:** `th-2-fan-tilt.svg/.png`, notes §12:
- The v2 drawing had fans on top of the wings, so they couldn't tilt and would
  cause download.
- Pod tilt: spanwise spindle with the drive shaft along the tilt axis.
- Issues listed: download, whirl flutter, hard points, gyroscopic loads.
- Mounting options: A tip spindle, B fork/ladder bay, C fan-in-body.
- Proposed Heavy "ladder frame": fans alternate with wings, each pivots on inner +
  outer rails.
- New decision D6 added.

### 16. Front views; drop the pod-on-legs designs
**User:** Add front views; drop any design with the original TB2 lowering pods on
high legs (too impractical).
**Done:**
- `th-2-re-design-v1.*` removed (git rm; still in history).
- `th-2-variants` v3: top/side/front views with the ladder frame (D6 provisionally
  adopted). The old sheet is kept as `-v2`.
- Front view drove changes:
  - Pivot height ≥ fan radius + 2 m (Heavy rails z ≈ 9 m, Fast z ≈ 7 m).
  - Heavy front wing dihedral / rear wing anhedral into the rails (box seen from
    the front).
  - Fast fans/wing reordered so no wing is under a fan; folded span ≈ 37 m.
- Notes §13.
- PNG re-render was briefly blocked by a full root disk; the user freed space and
  it was completed.

### 17. Are the containers to scale? → maximise the hold
**User:** Containers look small. Then: maximise the hold for vehicles, small
helicopters, livestock and people; a central wall, or 2 walls with doors (3
corridors), is fine.
**Answer / done:**
- The containers were to scale; the hold was only ~1 % of the body.
- New hold:
  - Heavy: 50 × 20 m, 3 corridors (centre 7 × 5 m, sides 6 × 4.2 m),
    ~4,300 m³, 3 ramps. Front wing moved to mid height, above the hold.
  - Fast: 44 × 9.5 m, 2 corridors, ~830 m³.
- Floor + walls cost ~9 t / ~4 t:
  - Heavy VTOL shuttle 36 → 27 t, STO 105 → 96 t.
  - Fast 14 → 10 t.
- `th-2-sizing.py` gains `hold_t`. Drawing v4 (v3 kept). Notes §14, D7 decided,
  E8 added (hold centre ahead of the CG).

### 18. Could this design land on water?
**Answer:** Yes. VTOL avoids the seaplane problem (high-speed planing).
- Floating draft is only ~0.13 m (Heavy) / ~0.18 m (Fast) if watertight; very
  stable.
- Needs: sealed lower hull and ramps, chined bottom, spray-proof marinised
  engines.
- The ramp can work as a boat slipway (floods; nod to TB4).
- VTOL only on water, sea state ≤ ~4–5, ~1–3 t cost.
- Bonus: snorkel-refilled firefighting tank.
- Notes §15, open decision D8.

### 19. Would a second level help, or be too heavy?
**Answer:** A fixed second deck adds ~6–9 t (Heavy VTOL shuttle 27 → ~18–21 t)
but little useful capacity: payload weight, not floor area, is the limit. A full
96 t STO load of people, cattle or sheep already fits on the 950 m² main deck. The
deck also clashes with the front-wing carry-through. Useful only for mixed loads
(people above vehicles/animals). Recommendation: removable mezzanine /
multi-deck modules on the floor rails, attached to the corridor walls, carried
only when needed. Notes §16, decision D9.

### 20. Add length / height / width arrows on the 3 views
**Done:** `th-2-variants` v4 now has dimension arrows:
- Top: length, span, body width.
- Side: overall height to the fin tops, body height, hold length.
- Front: span, height, body width, hold width, fan-pivot height.
- Values: Heavy 82 × 66 m, 25 m high, body 26 × 14 m, hold 50 × 20 m, pivots 9 m.
  Fast 70 × 62 m (folded 37 m), 15 m high, body 12 × 10 m, hold 44 m, pivots 7 m.

### 21. "We could even transport prefab houses"
**Answer:** Yes.
- Modular house modules (10–20 t) fit by size (the 7 × 5 m centre corridor takes
  even double-wide units); weight limits them to 1–2 per VTOL trip, ~5–6 per STO.
- Container homes: ~5 VTOL / ~16–20 STO.
- Flat-pack emergency shelters are the ideal match (light + bulky): ~150 per VTOL
  shuttle, ~500 per STO flight (homes for ~2,500 people).
- Notes §17.

### 22. Cross-check the Python models against the current design
**Findings (no code changed yet):**
- Fan sizes/counts, weights, design point, hold weights, cruise speeds and the
  printed results all match notes, README and drawing.
- Main issue: inconsistent margins.
  - `th-2-strip.py` uses a 1.05 thrust margin and full contingency power;
    `th-2-sizing.py` keeps 1.15 and a 20 % power reserve.
  - Effect: lowland max hover is overstated: Heavy 282 → 228 t, Fast 141 → 114 t
    with consistent margins. So §11.3 "VTOL up to 270 t" and D1 are overstated,
    and the strip distances are optimistic.
- Ladder-frame rails are not in the weight model (E4). Rough order 8–15 t
  Heavy / 4–7 t Fast, possibly most of the VTOL shuttle payload.
- L/D (10 / 11) predates the ladder frame + 6 large ducts in cruise; likely
  optimistic, especially for the Fast.
- Other issues:
  - The fan-out model assumes the CG sits at the middle pair (E8 shows the
    Heavy's hold centre is 9 m forward of it).
  - Strip-sim span (64 m) and CL·S are pre-ladder.
  - "Max TOW for 800 m" isn't capped at the 270 t structure limit.
  - Physics code is duplicated across the two scripts.
  - Landing weights are hard-coded.
  - Hover fuel is at sea-level density.

### 23. Fix the model issues
**Done:**
- `th-2-sizing.py` now holds `VARIANTS`, the margins and `max_vtol_weight()`;
  `th-2-strip.py` imports them (one source of truth).
- Model changes:
  - consistent margins in the strip sim,
  - rails ~14.9 / ~8.5 t, Heavy soft-field gear +2 t,
  - L/D 10/11 → 9/9.5,
  - hover fuel at the design point,
  - strip span 66 m, drag including rails, landing weight computed,
    800 m max TOW capped at the STO limit,
  - `range_km` argument.

**Result:**
- Heavy: empty 182 t, VTOL shuttle 27 → 9 t, STO 78 / 42 t, max VTOL at SL
  228 t.
- Fast: empty 97 t, VTOL shuttle 10 → none, STO 25 / 12 t, max VTOL at SL
  114 t.
- STO strips still ≤ 700 / 600 m.
- Rails ±50 % moves the Heavy VTOL shuttle payload over ~2–17 t.
- New decision D10 (payload vs. VTOL weight), engineering check E9 (size the
  rails), D1 reframed, E4 done.
- Notes §0 and §18 updated, superseded notes in §11.3/§14.3/§17, README and
  drawing spec boxes updated.

### 24. Drop the Fast?
**User:** With these results the Fast is probably covered by existing aircraft; if
so, drop it.
**Answer / done:**
- Confirmed. A400M: ~37 t, ~420 kn, ~750–1,000 m soft strips, far more range.
  C-130J and C-390 are similar; CH-47F / CH-53K cover light vertical lift. The Fast
  (25 / 12 t, no VTOL) adds only a ~300 m shorter strip.
- Fast removed from `VARIANTS` (kept as a comment).
- New Heavy-only drawing `th-2-heavy.*` (v5); two-variant sheet kept as
  `th-2-variants-v4.*`.
- Notes §0 rewritten for one design, §19 added, E6 closed, README updated.
- Flagged: the same test applied to the Heavy (C-17 + CH-53K) → new decision D11.

### 25. Do bigger fans and engines currently exist?
**Answer:**
- Per fan the Heavy needs ~22.5 MW installed / ~15 MW gearbox in a Ø14 m duct.
- Turboshafts: ~8–10 MW is the largest flying (D-136), so ~2–3 per fan.
- Gearboxes: the Mi-26's ~17 MW is the largest flying, so the Heavy is already
  at that edge.
- Ducted fans: nothing near 14 m has flown; only ground wind-tunnel fans
  (NASA Ames, ~12 m).
- Open rotors do go to 32–35 m (Mi-26, Mi-12).
- Model: bigger fans lower payload (rails/ducts grow faster than the power
  saving); 240 t gains only ~3.6 t VTOL.
- Notes §20; D10 narrowed to design point, rail weight / mounting, or accepting
  light VTOL.

### 26. Do existing aircraft already cover long-haul transport + final delivery?
**Answer:**
- Long haul: C-17 (~77 t, ~4,400 km) beats the Heavy (42 t over 1,500 km).
  A400M, Il-76 and An-124 cover the rest.
- Final delivery:
  - Mi-26 (~20 t at sea level) and CH-53K (~12 t hot-and-high) ≥ the Heavy's
    9 t / 13 t VTOL.
  - STOL: C-17 lands ~70 t in ~1,000 m; C-27J / C-295 do ~10 t in ~600 m.
- Unique to the Heavy: ~78 t into ≤ 700 m soft strips without transshipment,
  ~4,300 m³ hold, VTOL + STO in one airframe, water.
- Reframed as a short-strip bulk lifter for the last few hundred km. Notes §21,
  D11 updated.

### 27. Is "Gross 200 t / 270 t" still correct?
**Answer:** Yes. 200 t is the VTOL limit at the 2,500 m / 40 °C design point
(≈ 228 t at sea level); 270 t is the structural STO limit (strip sim: ≤ 700 m in
all conditions). What changed is the empty weight (182 t), leaving ~18 t for
fuel + payload in VTOL. Labels in README and notes §0.1 made explicit.

### 28. Is "Thunderbird" still protected? Reduce it to TB2?
**Answer (not legal advice):**
- The episodes and the craft design are copyrighted (UK film copyright: 70 years
  after the last key author's death; Gerry Anderson d. 2012) and held by
  ITV Studios.
- The name is protected by trademark (use in trade), not copyright.
- "TB2" is still a clear reference; what lowers risk is framing: a non-commercial
  study, credited, not affiliated.
**Done:**
- Current titles → "TB2" (notes, scripts, fan-tilt and wing-options sheets,
  re-rendered).
- README keeps one credited reference and adds a disclaimer.
- Archived drawings and history sections left unchanged as record.

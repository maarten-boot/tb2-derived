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

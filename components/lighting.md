# Components — Lighting

Cards for LEDs, LED drivers, MOSFET, COB strip, and diffuser. See the [template & field guide](README.md).
Build context: [Lighting](../docs/08-lighting.md).

---

### 3W High-Power LED — Pure White 6500K — strobes (+ landing-light fallback)
- **Category:** LED (bare high-power emitter)
- **Status:** ✅ reordered (29 Jul 2026) — replaces the earlier listing (ordered 24 Jun 2026, ⚠️ never
  arrived — AliExpress bug); switched to a different listing/seller (SZRZGT) for the reorder
- **Used for:** white wingtip **strobes**; fallback **landing light** if the 10W LED is too
  big/hot/power-hungry or fails — [Lighting](../docs/08-lighting.md)
- **Source / price:** AliExpress · "Pure White 6500K" / "3W 10pcs" variant · €3.16 / 10 pcs (checkout
  price; **the ≥2-piece bulk discount doesn't apply here** — that tier needs ≥2 packs of the *same*
  colour variant, and each colour is priced individually at qty 1: white €3.16, red €3.57, green
  €3.41)
- **Link:** https://www.aliexpress.com/item/1005003810952677.html

| Spec | Value |
|------|-------|
| Power | 3 W |
| Forward voltage (Vf) | 3.2–3.6 V |
| Forward current | 700 mA |
| Luminous flux | 260–280 lm |
| Colour / CT | Pure White 6500K |
| Chip | 42 mil |
| Rated life | >50,000 h |
| Package | bare emitter — **no 20 mm star PCB** included |
| Weight | ~0.3 g *(est. from bulk-carton data; not on datasheet)* |
| Dimensions | Ø8.0 mm lens, 5.5 mm tall (dome to base), 14.4 mm overall incl. leads |
| Base / slug | 7.26 mm across; Ø6.0 mm copper slug (bottom) |
| Pinout | **2-pin** single-die (anode/cathode), thermal slug |

- **Notes:** drive on a 700mA CC driver (PWM-dimmable) from the 12V rail; needs a heatsink. 10 pcs
  → spares. As a landing-light substitute, run on the 3A driver dialled down, or its own 700mA driver.

---

### 3W High-Power LED — Red 625nm — port nav light
- **Category:** LED (bare high-power emitter)
- **Status:** ✅ reordered (29 Jul 2026) — replaces the earlier listing (ordered 24 Jun 2026, ⚠️ never
  arrived — AliExpress bug); switched to a different listing/seller (SZRZGT) for the reorder
- **Used for:** **port (left) wingtip** navigation light — [Lighting](../docs/08-lighting.md)
- **Source / price:** AliExpress · "Red 625nm" / "3W 10pcs" variant · €3.57 / 10 pcs (checkout price
  at qty 1 — see the white-LED card above for why the ≥2-piece bulk tier doesn't apply across colours)
- **Link:** https://www.aliexpress.com/item/1005003810952677.html

| Spec | Value |
|------|-------|
| Power | 3 W |
| Forward voltage (Vf) | 2.4–2.6 V |
| Forward current | 700 mA |
| Luminous flux | 60–70 lm |
| Colour / wavelength | Red 625 nm |
| Chip | 42 mil |
| Rated life | >50,000 h |
| Package | bare emitter — no star PCB |
| Weight | ~0.3 g *(est. from bulk-carton data; not on datasheet)* |
| Dimensions | Ø8.0 mm lens, 5.5 mm tall (dome to base), 14.4 mm overall incl. leads |
| Base / slug | 7.26 mm across; Ø6.0 mm copper slug (bottom) |
| Pinout | **2-pin** single-die (anode/cathode), thermal slug |

- **Notes:** **lower Vf (2.4–2.6 V)** than the white/green — the 700mA CC driver handles this
  automatically (it's a current source), so no separate resistor needed. Dim to ~40% for scale.

---

### 3W High-Power LED — Green 520nm — starboard nav light
- **Category:** LED (bare high-power emitter)
- **Status:** ✅ reordered (29 Jul 2026) — replaces the earlier listing (ordered 24 Jun 2026, ⚠️ never
  arrived — AliExpress bug); switched to a different listing/seller (SZRZGT) for the reorder
- **Used for:** **starboard (right) wingtip** navigation light — [Lighting](../docs/08-lighting.md)
- **Source / price:** AliExpress · "Green 520nm" / "3W 10pcs" variant · €3.57 / 10 pcs (€3.39 ea ≥2
  packs — buying 3 packs, one per colour, together qualifies)
- **Link:** https://www.aliexpress.com/item/1005003810952677.html

| Spec | Value |
|------|-------|
| Power | 3 W |
| Forward voltage (Vf) | 3.2–3.6 V |
| Forward current | 700 mA |
| Luminous flux | 140–160 lm |
| Colour / wavelength | Green 520 nm |
| Chip | 42 mil |
| Rated life | >50,000 h |
| Package | bare emitter — no star PCB |
| Weight | ~0.3 g *(est. from bulk-carton data; not on datasheet)* |
| Dimensions | Ø8.0 mm lens, 5.5 mm tall (dome to base), 14.4 mm overall incl. leads |
| Base / slug | 7.26 mm across; Ø6.0 mm copper slug (bottom) |
| Pinout | **2-pin** single-die (anode/cathode), thermal slug |

- **Notes:** same 700mA CC driver + heatsink as the others. Dim to ~40% for scale brightness.

> **Shared notes (all three 3W LEDs):** ⚠️ **reordering from a new listing** (brand **SZRZGT**, CE
> cert, spec box lists "Voltage 3.0–3.6V" for the family; AI summary quotes **2.2–2.4V / 3.0–3.6V /
> 3.2–3.6V / 6–7V** forward-voltage bins and **300–350mA / 600–700mA** current bins across the whole
> colour/wattage range) — broadly consistent with the per-colour Vf/current figures already recorded
> below (red lower-Vf, white/green ~3.2–3.6V, 700mA at 3W), but this listing gives far less per-colour
> detail than the original. **Dimensions confirmed identical** via a datasheet drawing pasted from
> this listing: Ø8.0mm lens, 5.5mm tall, 14.4mm overall incl. leads, 7.26mm body width, Ø6.0mm copper
> slug, 2-pin anode/cathode+slug — matches the figures below exactly, so this is almost certainly the
> **same physical emitter**, just a different reseller. The **42 mil chip size and luminous-flux
> figures** are still carried over from the earlier (never-arrived) listing and aren't independently
> re-confirmed, but given the dimensional match there's no reason to expect them to differ. Bare
> **2-pin single-die** emitters, on a copper slug — no heatsink/PCB included, so plan a small heatsink
> + mount per LED. The listing also sells **4-pin / 6-pin RGB**
> versions (three dies in one package) and many other colours/wavelengths (grow-light IR/UV, etc.) —
> **not** what we're using here; only the Red 625nm / Green 520nm / Pure White 6500K, 3W variants
> apply.

---

### 10W LED 5050 XML-T6 — landing light
- **Category:** LED (high-power emitter on star PCB)
- **Status:** ✅ reordered (29 Jul 2026) — original order (24 Jun 2026) ⚠️ never arrived (AliExpress bug)
- **Used for:** **landing light** — [Lighting](../docs/08-lighting.md). (3W white is the fallback.)
- **Variant / qty:** 12 mm / Cold White 6500K · 1 pc
- **Price:** €5.85 (€4.50 ea ≥2)
- **Link:** https://www.aliexpress.com/item/1005009615663192.html

| Spec | Value |
|------|-------|
| Weight | ~0.6 g *(est. from 12 mm aluminium MCPCB geometry + emitter)* |
| PCB diameter | 12 mm (round aluminium MCPCB; listing also 14/16/20 mm) |
| Emitter | 5050 (XM-L2 / XML-T6 class) |
| Power | 10 W |
| Forward voltage (Vf) | 2.9–4.0 V |
| Forward current (If) | 3.0 A |
| Colour / CT | Cold White 6500K (also 3000K / 4500K) |
| Viewing angle | 110–125° |
| Thermal resistance | 2.5 °C/W |
| Max junction temp | 150 °C |
| Brand / model | SFNCHGOT, 10W 5050 |

- **Notes:** ~10.5 W at full 3 A → significant heat. Drive on the **3A adjustable CC driver** from
  the 12V rail; **thermal-glue to metal, not LW-PLA**; use ≥20×20 mm or two stacked 14×14×6 mm
  heatsinks (adequate for intermittent landing-light bursts — see
  [Lighting heatsinks](../docs/08-lighting.md)). PWM-dim to ~1–1.5 A for continuous use.

---

### 3mm 400-LED 12V COB flexible strip — formation lights
- **Category:** LED strip (COB on flexible FPC)
- **Status:** ✅ reordered (29 Jul 2026) — replaces the earlier listing (ordered 24 Jun 2026), which
  **shipped the wrong product**; switched to a different listing/seller for the reorder
- **Used for:** **formation lights** on the F-35B — [Lighting](../docs/08-lighting.md)
- **Variant / qty:** Green / 3 mm, 400 LEDs per m / 1 m · 1 pc
- **Price:** €3.06 (current price; list €6.37)
- **Link:** https://www.aliexpress.com/item/1005009818813644.html

| Spec | Value |
|------|-------|
| Weight | ~7 g/m *(est., carried over from the earlier strip — same 3mm/400-LED class; weigh to confirm)* |
| Model | — *(not stated on this listing)* |
| Input voltage | DC 12 V (per marketing image and listing spec box) — **⚠️ see mismatch below** |
| Power per metre | ⚠️ **MISSING** — not clearly stated (listing gives only an odd "Luminous Flux 2000-82000" range, not a per-metre power/current figure). Previous listing's ~5.76–7 W/m / ~0.35–0.48 A/m is **not** carried over — different product. Measure on arrival before relying on it for the power budget. |
| LED density | 400 LEDs/m, COB (per variant title) |
| Efficacy | — *(not stated on this listing)* |
| CRI (Ra) | ≥98 ("full spectrum," per marketing image — AliExpress CRI claims run optimistic, treat as best-case) |
| Luminous angle | 180° (per marketing image) |
| Width × thickness | 3 mm width (caliper-verified in a marketing image; thickness not given numerically, described as "Ultra Thin") |
| Cut interval | 20 mm (per marketing image) |
| Cascade length | — *(not stated on this listing)* |
| Leads | — *(not stated on this listing)* |
| Backing | adhesive-backed (per marketing image) |
| Waterproof | — *(not stated on this listing)* |
| Life / cert | — *(not stated on this listing)* |

- **⚠️ Spec mismatch:** the cutting-guide marketing image prints **"24V+"** silkscreen labels at the
  pads either side of each cut mark, but every other source (title, spec box, the "DC 12V" marketing
  graphic) says **12 V**. Likely a reused PCB artwork shared across a 12V/24V product family (same
  pattern of listing sloppiness as the earlier strip) rather than an actual 24V part — but **confirm
  with a multimeter/bench test before powering it from the 12V rail**, since driving a 24V-rated
  strip at 12V would just under-drive it (safe) but the reverse would not be.
- **Notes:** dimmable per the listing. Several specs still aren't stated (per-metre power/current,
  cascade length, lead length, waterproofing) — **treat current draw as unverified until measured on
  arrival**, since carrying over the old listing's figures isn't safe for a different product that
  arrived wrong once already. Cut to length and solder ~0.3 mm² wire to the pads (don't bridge the two
  rails). For the
  [12V VTX rail budget](../docs/08-lighting.md#current-budget-12v-vtxcam-rail-2a), size by the
  **actual measured current** at the cut length used for formation lighting once it arrives.

---

### Frosted translucent PP sheet — LED diffuser
- **Category:** Material (diffuser sheet)
- **Status:** 🛒 to reorder — original order (24 Jun 2026) ⚠️ never arrived (AliExpress bug); **not yet
  re-ordered** (held back on 29 Jul 2026 due to card safety limits) — plan to order ~30 Jul 2026
- **Used for:** diffusing the wingtip nav / formation LEDs (and other point sources) for an even
  glow — [Lighting](../docs/08-lighting.md)
- **Variant / qty:** 100 × 200 mm × 0.5 mm · 10 sheets
- **Price:** €3.83 + €1.58 shipping = €5.41 total
- **Link:** https://www.aliexpress.com/item/1005008661393360.html

| Spec | Value |
|------|-------|
| Material | Polypropylene (PP), frosted translucent |
| Sheet size | 100 × 200 mm |
| Thickness | 0.5 mm |
| Qty | 10 sheets |
| Weight | ~9 g/sheet *(calc: 100×200×0.5 mm × 0.905 g/cm³; negligible per cut piece)* |
| Heat resistance | up to 105 °C |
| Model | TP0316V |

- **Notes:** cuts/drills easily; 0.5 mm is flexible. Frosts point LEDs into an even glow / scale
  lens look. ⚠️ PP softens near 105 °C — keep it off the **10W landing-light** hot metal/heatsink;
  fine over the cool 3W nav LEDs. Listing offers 0.3–2 mm thicknesses and larger sheets.

---

### ASLENT 1156 BA15S P21W LED bulb — afterburner
- **Category:** LED bulb (automotive turn-signal type)
- **Status:** ✅ reordered (29 Jul 2026) — replaces the earlier YiRui-listing order (ordered 24 Jun
  2026, ⚠️ never arrived — AliExpress bug); switched to a different listing/seller (ASLENT) for the
  reorder
- **Used for:** **afterburner glow** — [Lighting](../docs/08-lighting.md#afterburner-power--the-canbus-resistor-mod)
- **Variant / qty:** Socket Type: **1156 ba15s P21W** / Emitting Color: **Amber Yellow** · 2 pcs
- **Price:** €6.57 / 2 pcs
- **Link:** https://www.aliexpress.com/item/1005007026242769.html

| Spec | Value |
|------|-------|
| Weight | ~15–20 g *(est.; carried over from the earlier bulb — same bulb class; weigh to confirm)* |
| Dimensions | Ø20 mm × 57 mm bulb body (per marketing image); 15 mm socket base pin spacing |
| Base / socket | BA15S (1156), single-contact **180° straight pins** — confirmed via marketing image socket-comparison chart (distinct from the 150°-offset BAU15S) |
| Voltage | 12 V (per spec box and marketing image) |
| Current | ~1.86–1.95 A stock (CANBUS, carried over est.); **~0.7 A after resistor removal** — not re-confirmed for this listing, verify after the CANBUS-resistor mod |
| Power | 21 W (per marketing image: "12V 21W 2100LM/Bulb") |
| Luminous flux | 2100 lm (per spec box and marketing image) |
| Emitter | 144 × 3014 SMD, "2 Sides LED Chipsets," 360° shine (per marketing image) — matches the earlier bulb's emitter spec exactly |
| Body / cooling | metal base + frosted dome cap (per marketing images); no explicit material/rating given |
| Waterproof | — *(not stated on this listing)* |
| Driver | **built-in load resistor + "Intelligent IC Drive"** — marketing image explicitly shows it converting unstable input current to stable output current, i.e. a built-in CANBUS load resistor + constant-current IC, same mechanism as the earlier bulb |
| Life | — *(not stated on this listing)* |
| Colour | Amber Yellow |

- **Notes (afterburner):** **remove the CANBUS load resistor** → stock current should drop
  substantially, same as the earlier bulb — **re-verify the before/after current** on this specific
  bulb once it arrives rather than assuming the old ~1.5→0.7A figures carry over exactly (the
  underlying built-in-resistor + IC-driver mechanism is now confirmed the same, so the mod should
  still apply, just re-measure the actual current). **Power from the 12V VTX/CAM rail** — sharing it
  with the landing light only works because of the **hover/cruise flight-mode interlock** (afterburner
  off in hover, landing light off in cruise/transition) that keeps the two from ever loading the rail
  together — see
  [Lighting](../docs/08-lighting.md#landing-light--afterburner-flight-mode-interlock-firmware-required).
  **BA15S = straight 180° pins** → easy to print a holder for (this listing's own **BAU15S** variant
  is the 150°-offset one — not the one selected; confirmed via the listing's own socket-comparison
  chart). 2 pcs = spare.
- **Listing is cleaner than the earlier one:** the spec box here says *Interface Type: BA15S (1156)*,
  which **matches** the Socket Type variant selected — no mismatch to flag this time (the earlier
  YiRui listing's spec box wrongly said BA15D/1157 and had to be overridden by the variant selector).
  Dimensions, emitter type, and driver mechanism are now confirmed via marketing images rather than
  carried over as estimates.

---

### eletechsup LD2740SC 3A — constant-current LED driver (landing light)
- **Category:** LED driver (switch-mode buck, constant-current)
- **Status:** ✅ reordered (29 Jul 2026) — original order (24 Jun 2026) ⚠️ never arrived (AliExpress bug)
- **Used for:** drives the **10W landing light** — [Lighting](../docs/08-lighting.md)
- **Variant / qty:** 3A, No Terminal · 1 pc
- **Price:** €7.42
- **Link:** https://www.aliexpress.com/item/1005005776802021.html

| Spec | Value |
|------|-------|
| Weight | 10 g (no-terminal; 13 g with terminal) |
| Dimensions | 42 × 22 × 16 mm |
| Type | switch-mode step-down (buck) constant-current |
| Input voltage | 6–27 V (3A/4A); 4–27 V for 1–1.5A |
| Output current | 3 A (range 0–4A, set by R4: Iout = 0.16/R4 → 3A = 0.055 Ω) |
| Output (LED string) | 3–24 V |
| Max power | 80 W (20 V × 4 A) — realistically less |
| Efficiency | up to 92% (~90% measured) |
| Current accuracy | 5% |
| PWM dimming | 3.3 V/5 V logic-level on PWM pin (RP2040-compatible) |
| Switching freq | up to 1 MHz |
| Protection | open-circuit LED |
| Pins | VIN, GND (power) · LED+, LED− · PWM+, GND (dimming) |
| Brand / model | eletechsup LD2740SC |

- **Notes:** drives the 10W LED from the 12V VTX rail; PWM from an RP2040 GPIO for brightness/strobe.
  At the LED's ~3.5 V/3 A (~10.5 W out) the buck loss is ~1 W → runs cool; a reviewer saw ~70 °C only
  when driving a 12 V/36 W load. The "3A No Terminal" variant ships set for 3 A (R4 fitted). ⚠️ One
  buyer asked whether the output stays on with **no PWM signal** while still wired to a controller —
  **verify this for strobe use** (you want LED off at 0% duty).
- **Note:** this is a **buck (switching)** CC driver (~92% eff.), *not* linear. Confirmed: the
  700 mA nav driver is **also** buck (~96%) — so the old "drivers are linear, run off 12 V to cut
  heat" claim was wrong and has been corrected in [Lighting → driver heat](../docs/08-lighting.md).

---

### ICGOICIC 3W/2W 700mA LED driver — nav-light / strobe driver
- **Category:** LED driver (switch-mode buck, constant-current)
- **Status:** ✅ reordered (29 Jul 2026) — replaces the ACELEX listing (ordered 24 Jun 2026, ⚠️ never
  arrived — AliExpress bug); same 36×20mm form factor and specs, different listing/seller
- **Used for:** drives the **3W nav LEDs + white strobes** (one driver per channel) — [Lighting](../docs/08-lighting.md)
- **Variant / qty:** "5PCS" pack (4 needed + 1 spare)
- **Price:** €6.37 / 5 pcs (€1.27 ea)
- **Link:** https://www.aliexpress.com/item/1005007486363935.html

| Spec | Value |
|------|-------|
| Weight | ~4 g *(est., carried over from the ACELEX board — same dimensions; weigh to confirm)* |
| Dimensions | 36 × 20 mm |
| Type | switch-mode step-down (buck) constant-current |
| Input voltage | DC 5–35 V |
| Output current | 700 mA ±20 mA (fixed) |
| LED load | 1–10× 3W (or 2W) LEDs in series (string Vf must be ~2–3 V below Vin) |
| Efficiency | — *(not stated on this listing; ~96% on the equivalent ACELEX board, not re-confirmed for this seller)* |
| Ripple + noise | — *(not stated on this listing)* |
| PWM dimming | logic-level (frequency/min-on-time not stated on this listing) |
| Protection | overload / short-circuit / overcurrent |
| Pins | VIN+, VIN−, PWM (implied), LED+, LED− |
| Brand | ICGOICIC (item no. LED-3w) |

- **Notes:** one driver per nav LED / strobe channel, from the 12V rail. Same dimensions and core
  specs (5–35V in, 700mA±20mA out, 1–10× 3W LEDs) as the ACELEX board it replaces — likely the same
  generic board relisted by a different seller. Efficiency/ripple/PWM-frequency figures from the old
  ACELEX listing are **not re-confirmed** for this one; treat as estimates until checked on arrival.
- **⚠️ Verify PWM polarity:** this listing's text says *"PWM dimming high level off output, low
  level on output"* (**inverted** — logic-high = LED off) — same polarity quirk flagged on the
  ACELEX board. Confirm on arrival so the RP2040 strobe/dim logic is the right way round (it changes
  whether 0% duty = off or on).

---

### IRLZ44N — logic-level N-channel MOSFET (LED-strip / load switch)
- **Category:** MOSFET (low-side switch)
- **Status:** ✅ reordered (29 Jul 2026) — replaces the earlier listing (ordered 24 Jun 2026, ⚠️ never
  arrived — AliExpress bug); switched to a different listing/seller (GUXINWAY) for the reorder
- **Used for:** switching the **12V COB strip** on/off from an RP2040 GPIO (also usable as a
  landing-light on/off switch) — [Lighting](../docs/08-lighting.md)
- **Variant / qty:** Color: **IRLZ44N** · 10 pcs
- **Price:** €3.23 / 10 pcs (€0.32/pc)
- **Link:** https://www.aliexpress.com/item/1005009242758699.html

| Spec | Value |
|------|-------|
| Weight | ~2 g each (TO-220) |
| Package | TO-220AB, 3-pin (Gate / Drain / Source) |
| Type | N-channel, **logic-level** enhancement MOSFET |
| V_DS (max) | 55 V |
| I_D (continuous) | 47 A @ 25 °C (~36 A @ 100 °C) |
| R_DS(on) | ~22 mΩ @ V_GS = 5 V; ~28 mΩ @ 4 V |
| V_GS(th) | 1.0–2.0 V (logic-level) |
| Gate drive | fully on from 3.3–5 V → **RP2040-compatible** |
| P_D (max) | ~83 W (heatsinked) |

- **Notes:** specs from the **standard IRLZ44N datasheet** (this listing itself gives no electrical
  spec table beyond brand/package/condition — the generic AliExpress "Type: Voltage Regulator" tag is
  a mislabelled category, not a real spec). Wire as a low-side switch: Source→GND, Drain→COB strip −,
  strip +→12 V; Gate→RP2040 GPIO via a ~100–220 Ω series resistor + a 10 kΩ gate→GND pulldown. At the
  COB strip's ~0.4 A the R_DS(on) loss is negligible and no heatsink is needed, even with a 3.3 V
  gate. Being **logic-level**, it's fully enhanced by 3.3–5 V (unlike a standard IRFZ44N that needs ~10 V).
- **Listing:** unlike the earlier reorder-source (a generic multi-MOSFET page with no part-specific
  data), **this listing has a "Color" variant selector that names the exact part** (IRLZ24N / IRLZ34N
  / **IRLZ44N**) — a cleaner pick, less ambiguity about what actually ships. Reviews reference this
  specific listing working fine for small projects. Still worth confirming the parts are stamped
  "IRLZ44N" on arrival, as with any AliExpress MOSFET buy.

---

### Aluminium heatsink 14×14×6 mm (black) — LED cooling
- **Category:** Heatsink (thermal hardware)
- **Status:** ✅ owned (10-pack · ordered 24 Jun 2026)
- **Used for:** cooling the **10W landing-light LED** (stack two); spares for any warm LED driver — [Lighting → driver heat](../docs/08-lighting.md#led-driver-heat--efficient-buck-drivers-no-big-heatsinks-needed)
- **Variant / qty:** black, 14×14×6 mm · 10 pcs
- **Price:** €2.68 / 10 pcs
- **Link:** https://www.aliexpress.com/item/1005006066873634.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D

| Spec | Value |
|------|-------|
| Dimensions | 14 × 14 × 6 mm |
| Material | aluminium 6063, **black anodised** |
| Mounting | pre-applied thermal double-sided adhesive tape |
| Finish | slotted/finned |

- **Notes:** **black anodised → better radiative cooling** than bare silver (matches the lighting-doc
  pick). Stack two on the 10W LED for intermittent landing-light use (≈400 mm² needed). ⚠️ For the
  **10W LED, don't rely on the adhesive tape alone onto LW-PLA** — bond the LED to the metal and keep
  the plastic out of the heat path. 10 pcs → ~2 used + spares.

---

*Lighting category complete — all parts carded.*

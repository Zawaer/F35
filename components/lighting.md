# Components — Lighting

Cards for LEDs, LED drivers, MOSFET, COB strip, and diffuser. See the [template & field guide](README.md).
Build context: [Lighting](../docs/08-lighting.md).

---

### 3W High-Power LED — Pure White 6500K — strobes (+ landing-light fallback)
- **Category:** LED (bare high-power emitter)
- **Status:** 🛒 in cart (1 set)
- **Used for:** white wingtip **strobes**; fallback **landing light** if the 10W LED is too
  big/hot/power-hungry or fails — [Lighting](../docs/08-lighting.md)
- **Source / price:** AliExpress · €1.48 / 10 pcs

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
- **Status:** 🛒 in cart (1 set)
- **Used for:** **port (left) wingtip** navigation light — [Lighting](../docs/08-lighting.md)
- **Source / price:** AliExpress · €1.82 / 10 pcs

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
- **Status:** 🛒 in cart (1 set)
- **Used for:** **starboard (right) wingtip** navigation light — [Lighting](../docs/08-lighting.md)
- **Source / price:** AliExpress · €1.82 / 10 pcs

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

> **Shared notes (all three 3W LEDs):** same listing/family (CE/RoHS, 42 mil chip, >50,000 h).
> Bare **2-pin single-die** emitters on a Ø6 mm copper slug — no heatsink/PCB included, so plan a
> small heatsink + mount per LED (slug is the thermal path). Dimensions from the datasheet drawing;
> only **weight** remains unknown. The same listing also sells **4-pin / 6-pin RGB** versions (three
> dies in one package) — **not** what we're using here. Full 3W-row reference from the listing:
> Warm/Nature/Cold White & 6500K all ≈ 3.2–3.6 V / 700 mA / 260–280 lm; Yellow 2000K ≈ 180–200 lm;
> Blue 460 / Royal Blue 445 ≈ 30–40 lm.

---

### 10W LED 5050 XML-T6 — landing light
- **Category:** LED (high-power emitter on star PCB)
- **Status:** 🛒 in cart
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
- **Status:** 🛒 in cart
- **Used for:** **formation lights** on the F-35B — [Lighting](../docs/08-lighting.md)
- **Variant / qty:** Green / 3 mm / 1 m · 1 pc
- **Price:** €2.68
- **Link:** https://www.aliexpress.com/item/1005009514688713.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D

| Spec | Value |
|------|-------|
| Weight | ~7 g/m *(est. from FPC cross-section; +1–2 g for lead wires; weigh to confirm)* |
| Model | COB-3mm-400D-12V/24V (2025 Ed.1) |
| Input voltage | DC 12 V (chosen; listing also 24 V) |
| Power per metre | **see mismatch below** (~5.76–7 W/m) |
| Current draw | ~0.35–0.48 A/m at 12 V (≈4.2–5.8 W/m) |
| LED density | 400 LEDs/m, COB (Epistar) |
| Efficacy | 90 lm/W ±10% (@4000K) |
| CRI (Ra) | >90 |
| Width × thickness | ~2.7–3 mm × 1.5 mm (see mismatch) |
| Cut interval | every ~10–20 mm (see mismatch) |
| Cascade length | >5 m |
| Leads | both ends 15 cm, 20AWG; free DC head + 2-pin wire |
| Waterproof | none (IP20/IP21) |
| Life / cert | 50,000 h · CE/RoHS/UL |

- **⚠️ Spec mismatches in the listing** (flagged per KB convention — verify on arrival):
  - **Power/m:** PDF says **7 W/m**; product-page spec says **5.76 W/m**; description says
    **6–8 W/m**; a reviewer measured **~0.35 A/m (≈4.2 W/m)** at 12 V. Use **~0.4–0.5 A/m** for the
    power budget and confirm by measuring.
  - **Width:** title/“COB width” say **3 mm**, but the dimensions line says **2.7 mm**.
  - **Cut interval:** PDF “minimum 10 mm” vs description “20 mm”.
  - **Waterproof:** PDF IP20 vs description IP21 (both effectively non-waterproof).
- **Notes:** dimmable; cut to length and solder ~0.3 mm² wire to the pads (don't bridge the two
  rails). For the [12V VTX rail budget](../docs/08-lighting.md#current-budget-12v-vtxcam-rail-2a),
  size by the **actual cut length** used for formation lighting — a full metre at ~0.4–0.5 A is
  more than the ~0.13 A assumed for a short accent segment.

---

### Frosted translucent PP sheet — LED diffuser
- **Category:** Material (diffuser sheet)
- **Status:** 🛒 in cart
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

### YiRui 1156 BA15S P21W LED bulb — afterburner
- **Category:** LED bulb (automotive turn-signal type)
- **Status:** 🛒 in cart
- **Used for:** **afterburner glow** — [Lighting](../docs/08-lighting.md#afterburner-power--the-canbus-resistor-mod)
- **Variant / qty:** 1156 BA15S P21W / Yellow (amber) · 2 pcs
- **Price:** €4.11 / 2 pcs
- **Link:** https://www.aliexpress.com/item/1005007112305568.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D

| Spec | Value |
|------|-------|
| Weight | ~15–20 g *(est.; weigh to confirm)* |
| Dimensions | Ø20 × 55 mm |
| Base / socket | BA15S (1156), single contact, **180° straight pins** |
| Voltage | 12–48 V |
| Current | ~1.86–1.95 A stock (CANBUS); **~0.7 A after resistor removal** |
| Power | ~20–25 W (P21W class) |
| Luminous flux | 2200 lm |
| Emitter | 144 × 3014 SMD, 360° beam |
| Body / cooling | aviation aluminium 6063 + clear glass cover |
| Waterproof | IP68 |
| Driver | built-in constant-current + intelligent temp control |
| Life | 50,000 h |
| Colour | Yellow / amber |

- **Notes (afterburner):** **remove the CANBUS load resistor** → stock ~1.5 A drops to ~0.7 A and
  runs cooler. **Power from the servo BEC or a dedicated 12V tap, not the VTX rail** (too close to
  the 2A limit). Very bright (2200 lm) — dim/diffuse for a scale glow. **BA15S = straight 180° pins**
  → easy to print a holder for (BAU15S is the 150° offset version — not this). 2 pcs = spare.
- **⚠️ Listing spec mismatch:** the generic spec box says *Interface Type: BA15D (1157)* / model
  C-0023, but the **ordered variant is 1156 BA15S P21W** — the variant selector governs what ships,
  so ignore the box. (Confirm it's the single-contact 180° base on arrival.)

---

### eletechsup LD2740SC 3A — constant-current LED driver (landing light)
- **Category:** LED driver (switch-mode buck, constant-current)
- **Status:** 🛒 in cart
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

### ACELEX 3W 700mA LED driver — nav-light / strobe driver
- **Category:** LED driver (switch-mode buck, constant-current)
- **Status:** 🛒 in cart
- **Used for:** drives the **3W nav LEDs + white strobes** (one driver per channel) — [Lighting](../docs/08-lighting.md)
- **Variant / qty:** "3W LED Driver" (700 mA) · 4 pcs
- **Price:** €0.70 ea · 4 × €0.70 = €2.80 + €2.36 shipping = €5.16 total
- **Link:** https://www.aliexpress.com/item/32826230105.html

| Spec | Value |
|------|-------|
| Weight | ~4 g *(est.; weigh to confirm)* |
| Dimensions | 36 × 20 mm |
| Type | switch-mode step-down (buck) constant-current |
| Input voltage | DC 5–35 V |
| Output current | 700 mA ±20 mA (fixed) |
| LED load | 1–10× 3W LEDs in series (string Vf must be ~2–3 V below Vin) |
| Efficiency | ~96% (full load) |
| Output accuracy | ±2–3% |
| Ripple + noise | 120 mV |
| PWM dimming | 20 Hz–20 kHz, logic-level; **min on-time 0.7 ms** |
| Protection | overload / short-circuit / overcurrent |
| Pins | VIN+, GND, PWM, LED+, LED− |
| Brand | ACELEX (1W sibling = 350 mA) |

- **Notes:** one driver per nav LED / strobe channel, from the 12V rail. Efficient buck → internal
  loss <1 W at a single-3W-LED load, so it **runs cool and a heatsink is optional** at these loads.
  Min PWM on-time 0.7 ms → keep dimming frequency modest (≈≤1 kHz).
- **⚠️ Verify PWM polarity:** the listing text for this 3W board says *"high level closes the output,
  low level opens"* (**inverted** — logic-high = LED off), but the waveform diagrams look
  non-inverted. Confirm on arrival so the RP2040 strobe/dim logic is the right way round (it changes
  whether 0% duty = off or on).

---

### IRLZ44N — logic-level N-channel MOSFET (LED-strip / load switch)
- **Category:** MOSFET (low-side switch)
- **Status:** 🛒 in cart
- **Used for:** switching the **12V COB strip** on/off from an RP2040 GPIO (also usable as a
  landing-light on/off switch) — [Lighting](../docs/08-lighting.md)
- **Variant / qty:** IRLZ44N · 10 pcs
- **Price:** €3.93 / 10 pcs (€0.39/pc)
- **Link:** https://www.aliexpress.com/item/1005012176934991.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D

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

- **Notes:** specs from the **standard IRLZ44N datasheet** (the AliExpress listing is a generic
  multi-MOSFET page with no IRLZ44N data). Wire as a low-side switch: Source→GND, Drain→COB strip −,
  strip +→12 V; Gate→RP2040 GPIO via a ~100–220 Ω series resistor + a 10 kΩ gate→GND pulldown. At the
  COB strip's ~0.4 A the R_DS(on) loss is negligible and no heatsink is needed, even with a 3.3 V
  gate. Being **logic-level**, it's fully enhanced by 3.3–5 V (unlike a standard IRFZ44N that needs ~10 V).
- **Listing:** generic multi-MOSFET page (IRFZ/IRLZ family); the **IRLZ44N variant** is the one
  ordered, and reviews confirm IRLZ44N units (one notes it "works perfectly with Arduino"). Confirm
  the parts are stamped "IRLZ44N" on arrival.

---

### Aluminium heatsink 14×14×6 mm (black) — LED cooling
- **Category:** Heatsink (thermal hardware)
- **Status:** 🛒 in cart (10-pack)
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

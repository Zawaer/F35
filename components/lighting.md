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
- **Link:** https://www.aliexpress.com/item/1005008661393360.html?mp=1

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

## Still to card (paste product pages)

700mA CC LED driver · 3A adjustable CC LED driver · BA15S P21W afterburner bulb · IRLZ44N MOSFET.

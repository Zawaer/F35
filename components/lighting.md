# Components — Lighting

Cards for LEDs, LED drivers, MOSFET, COB strip, and diffuser. See the [template & field guide](README.md).
Build context: [Lighting](../docs/08-lighting.md).

---

### 3W High-Power LED — Pure White 6500K — strobes (+ landing-light fallback)
- **Category:** LED (bare high-power emitter)
- **Status:** 🛒 in cart (1 set)
- **Used for:** white wingtip **strobes**; fallback **landing light** if the 10W LED is too
  big/hot/power-hungry or fails — [Lighting](../docs/08-lighting.md)
- **Source / price:** AliExpress (NewStarRiver / QINGYING), €1.48 / 10 pcs

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
| Weight | ⚠️ MISSING *(not on datasheet; ~0.5–1 g typical for this class — weigh to confirm)* |
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
- **Source / price:** AliExpress (NewStarRiver / QINGYING), €1.82 / 10 pcs

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
| Weight | ⚠️ MISSING *(not on datasheet; ~0.5–1 g typical for this class — weigh to confirm)* |
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
- **Source / price:** AliExpress (NewStarRiver / QINGYING), €1.82 / 10 pcs

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
| Weight | ⚠️ MISSING *(not on datasheet; ~0.5–1 g typical for this class — weigh to confirm)* |
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

## Still to card (paste product pages)

10W LED 5050 XML-T6 6500K · 700mA CC LED driver · 3A adjustable CC LED driver · BA15S P21W
afterburner bulb · 12V COB strip (green) · IRLZ44N MOSFET · frosted PP diffuser sheet.

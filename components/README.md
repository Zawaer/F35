# Component Knowledge Base

A datasheet-style reference for every physical component in the build. Each part gets a **spec
card** capturing weight, size, and the specs that matter for *this* project (current draw, thrust,
cell count, etc.) — so the [BOM](../docs/11-bill-of-materials.md) stays a buy-list while the real
numbers (for CG/AUW, the power budget, and the Fusion model) live here.

## How to add a component

Paste the **full product page** (or datasheet) into chat — ideally one part per message, including
the section that shows **weight, dimensions, and electrical specs**. State the **chosen variant**
(colour, wattage, size, pack qty) and **how it's used** in the build.

When processing a paste, the assistant must:

- **Strip the clutter.** The page is usually grabbed with select-all (⌘A), so it includes
  "Recommended", "More to love", "People also searched", store/footer links, the cart sidebar, etc.
  **Ignore all of that** — extract specs only for the named product/variant. Never card a
  recommended/related product by mistake.
- **Accept images as context.** Some specs (weight, dimensions, wiring) live only in product
  images, so the user may paste screenshots/photos instead of (or alongside) text. Read specs from
  images too.
- Keep only useful build data — drop marketing copy, reviews, and SEO keywords.
- **Source:** default to **AliExpress** — do *not* record the specific AliExpress store name. Only
  note a source when it isn't AliExpress: **batteries are from ChinaHobbyLine**, and some parts come
  from Finnish local shops (**Biltema**, **Motonet**). The product **link** is what identifies the
  exact item.
- Where a real spec corrects the BOM or a subsystem doc (true weight, current, etc.), update those too.

### Marking missing data

- **Minor/unknown field** → leave as `—`.
- **Critical field missing** → mark it **`⚠️ MISSING`** in the card *and* ask the user for it in the
  reply (paste an image, check the listing, or measure it). Don't silently leave a critical gap as
  `—`, and never guess/fabricate a value — a wrong spec is worse than a flagged blank.
- A field is **critical** when the build depends on it:
  - **Weight** — feeds AUW and CG (every component).
  - **Key dimensions / mounting** — feeds the Fusion model and fit.
  - The part's **defining electrical spec** — e.g. servo torque & voltage; EDF/motor max current,
    cell count & thrust; battery cells/capacity/C; LED Vf & current; ESC current rating & cell count.
- When asking, list exactly which critical fields are missing and the easiest way to get each.

### Quick-add from a spreadsheet row

Pasting the order-spreadsheet row is enough to identify a part. Column order (Finnish headers):

`Tuote | Määrä | Variantti | Hinta per kpl | Extratoimituskulut | Hinta yhteensä | Linkki`
→ **product | qty | variant | price/unit | extra shipping | total price | link**

Example:

```
suuuuper bright white LED  1  12mm / Cold White 6500K  5,85€    5,85€  https://www.aliexpress.com/item/1005009615663192.html
```

From a row I take the name, qty, variant, unit/total price, any extra shipping, and the **product
link** (stored in the card). Combine it with the pasted product page / images for the full specs.

## Files by category

| File | Holds |
|------|-------|
| [flight-control.md](flight-control.md) | FC stack, Raspberry Pi Pico, multiplexer, cockpit display |
| [propulsion.md](propulsion.md) | EDFs, motors, ESCs |
| [power.md](power.md) | Batteries, BEC/regulators, connectors, wire |
| [servos.md](servos.md) | All servos (flight surface, VTOL, smart, micro) |
| [sensors.md](sensors.md) | Current sensors, thermistors, etc. |
| [lighting.md](lighting.md) | LEDs, LED drivers, MOSFET, COB strip, diffuser |
| [structural.md](structural.md) | Carbon tube/rod, bearings, balls, fasteners, wheels, glue |

## Spec-card template

```markdown
### <Model / name> — <short role>
- **Category:** <servo / EDF / battery / …>
- **Status:** ✅ owned · 🛒 in cart · ordered
- **Used for:** <subsystem + link, e.g. [Flaperons](../docs/05-servos.md)>
- **Variant / qty:** <chosen variant, pack qty>
- **Price:** <€/unit · total · + extra shipping if any>
- **Link:** <product URL>

| Spec | Value |
|------|-------|
| Weight | — |
| Dimensions | — |
| …category-specific (see below)… | — |

- **Notes:** <quirks, mods, compatibility, what to verify>
```

### Category-specific fields to capture

- **Servo:** torque (@V), speed (s/60°), voltage range, current (idle / stall), gear material,
  spline/teeth, bearing type, signal (PWM / serial), wire length, weight, dimensions.
- **EDF / motor:** fan diameter, KV, cell count, max current (A), max power (W), thrust (g),
  blade count, shaft/bore, weight, included ESC?, dimensions.
- **ESC:** continuous / burst current (A), cell count, BEC (V/A) or opto, firmware/protocol
  (DSHOT/BLHeli_S), weight, dimensions.
- **Battery:** chemistry, cells (S) / nominal V, capacity (mAh), C-rating (cont/burst),
  connector, balance lead, measured IR, weight, dimensions.
- **BEC / regulator / buck:** input V range, output V and/or current, adjustable?, dimming,
  switching vs linear, efficiency, weight, dimensions.
- **LED:** power (W), forward voltage (Vf), forward current (A/mA), colour / wavelength / CT,
  luminous flux (lm), package / emitter size, viewing angle.
- **Sensor:** measured quantity + range, interface (analog / I2C / 1-Wire), accuracy/resolution,
  supply voltage, current draw, package, weight.
- **Display:** diagonal size, resolution, driver IC, interface (SPI/…), pin count + pitch,
  logic/backlight voltage, dimensions, weight.
- **Connector / wire:** type, current rating, gauge (AWG), conductor diameter, jacket.
- **Structural (tube/rod/bearing/fastener/wheel):** material, OD / ID / wall, length, thread,
  bore, load rating, weight.

## Cross-references

Build context for how each part is used lives in the subsystem docs under [`../docs/`](../docs/).
Buy status and prices live in the [Bill of Materials](../docs/11-bill-of-materials.md).

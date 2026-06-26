# Components — Sensors

Cards for current sensors, thermistors, etc. See the [template & field guide](README.md).
Build context: [Sensors & Monitoring](../docs/07-sensors-monitoring.md).

---

### NTC thermistor MF52B 100K B3950 — temperature sensing
- **Category:** Sensor (NTC thermistor, analog)
- **Status:** ✅ owned (2× 10-pack = 20 pcs · ordered 24 Jun 2026)
- **Used for:** ESC / battery / exhaust temperature → CD74HC4067 mux → Pico ADC — [Sensors & Monitoring](../docs/07-sensors-monitoring.md)
- **Variant / qty:** B3950 100K · 2 packs (20 pcs)
- **Price:** €1.78 / 10 pcs (€3.56 for 2 packs)
- **Link:** https://www.aliexpress.com/item/1005006889194503.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D

| Spec | Value |
|------|-------|
| Type | NTC thermistor, MF52B epoxy-bead (model MF52B-104F3950) |
| Resistance @25 °C | **100 kΩ** |
| B value | **B3950** (3950 K) |
| Tolerance | ±1% |
| Bead size | ≤1.3 mm × ≤7 mm (teardrop) |
| Leads | enamelled wire, 80 mm, ~3 mm stripped ends |
| Operating temp | −40 to +110 °C |
| Response time | ~3 s |
| Encapsulation | epoxy resin |

- **Notes:** each NTC goes mux channel → GND; a **single shared 47 kΩ** resistor on the mux SIG line
  (3.3 V → 47 kΩ → SIG) forms the divider with whichever channel is selected — one resistor for all 16
  channels (full recipe: [Sensors & Monitoring](../docs/07-sensors-monitoring.md#temperature-sensing-ntc-100k--multiplexer)).
  Convert via the beta equation (NTC_R25 = 100 k, B = 3950). ⚠️ **Divider resistor:** **47 kΩ** (not the
  naive 10 kΩ) centres the room-to-100 °C range for a 100 kΩ NTC — 10 kΩ cramps the hot end.
  **Enamelled leads must be scraped/tinned** before soldering. 20 pcs → ~16 used + spares.

---

### ACS712 20A — Hall current sensor ×3
- **Category:** Sensor (Hall-effect current, analog)
- **Status:** ✅ owned (3 pcs · ordered 24 Jun 2026)
- **Used for:** FC/servo/LED rail current (×1) + roll-post EDF L/R (×2) — [Sensors & Monitoring](../docs/07-sensors-monitoring.md)
- **Variant / qty:** 3 pcs ACS712-20A
- **Price:** €3.40 (3 pcs, ~€1.13/pc)
- **Link:** https://www.aliexpress.com/item/1005008666499396.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D

| Spec | Value |
|------|-------|
| Range | ±20 A (bidirectional, AC/DC) |
| Accuracy | ±2% |
| Sensitivity | ~100 mV/A @ 5 V (20A variant) |
| Zero-current output | VCC/2 ≈ 2.5 V @ 5 V |
| Output | analog, 0 V–VCC (OUT pin) |
| Supply | **5 V DC** (chip needs 4.5–5.5 V) |
| Operating temp | −40 to +85 °C |
| Size | ~31 × 13 mm |
| Pins | VCC, GND, OUT (+ 2-screw terminal in series with the measured wire) |

- **Wiring:** the measured current passes through the screw terminals (in series); OUT → ADC.
- **⚠️ ADC level mismatch (must fix):** at 5 V the output is 2.5 V @0 A + ~100 mV/A → swings **0.5–4.5 V**
  across ±20 A. The **Pico ADC maxes at 3.3 V**, so above ~8 A the output exceeds 3.3 V — it
  **overranges and can stress the Pico pin**. Both the roll-post EDFs (~11 A) and the FC rail (~11.5 A)
  exceed 8 A, so a **resistor divider (~×0.66) on OUT→ADC is required** (or read via a 5 V-tolerant
  ADC). Note the chip needs ≥4.5 V, so you *can't* just run it at 3.3 V to dodge this.
- **Notes:** calibrate the zero-current offset in firmware (±2% + offset drift). Main/lift EDF
  currents (89 A / 40 A) are out of range — not monitored (see [Sensors doc](../docs/07-sensors-monitoring.md#current-sensing)).

---

### Load cell 10 kg + HX711 ADC — bench thrust-test rig
- **Category:** Sensor (strain-gauge load cell + 24-bit ADC) — **bench test tool, not on-aircraft**
- **Status:** ✅ owned (1 set · ordered 2 Apr 2026) — **bought for testing**
- **Used for:** **bench-measuring EDF/motor thrust** (verify the ~220 g roll-post / ~3300 g main-EDF
  figures) on a test stand — not flown
- **Variant / qty:** 10 kg load cell + HX711 module · 1 set
- **Price:** **€3.29**
- **Source:** AliExpress — GUXINWAY 10 kg load cell + HX711

| Spec | Value |
|------|-------|
| Load cell | aluminium-alloy bar, **10 kg** rated, 4-wire strain gauge |
| ADC | **HX711** 24-bit, 2-channel, PGA gain 32/64/128 |
| Data rate | 10 or 80 SPS |
| Supply | 2.6–5.5 V (<1.5 mA; <1 µA power-down) |
| Interface | 2-wire serial (CLK/DAT), pin-driven |
| Op temp | −20 to +85 °C |
| Wiring | load cell **red E+ · black E− · green A+ · white A−** → HX711 |

- **Notes:** **bench tool** for a thrust stand — read by the Pico/Arduino over the HX711 2-wire
  interface; tare + calibrate against a known weight. 10 kg range covers the **main/lift 70 mm EDFs
  (~3.3 kg)** and roll-post EDFs (~0.2 kg); mount the cell as a cantilever on a rigid stand. Not a
  flight component — for validating the thrust numbers in [Propulsion](../docs/06-propulsion.md).
  HX711 is slow (≤80 SPS) — fine for steady thrust, not fast transients.

---

*Sensors carded: NTC thermistor + ACS712 (on-aircraft) · load cell + HX711 (bench thrust test).*

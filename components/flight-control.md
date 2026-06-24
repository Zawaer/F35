# Components — Flight Control & Electronics

Cards for the FC stack, the Pico, and the cockpit/IO electronics. See the
[template & field guide](README.md). Build context: [Flight Controller](../docs/03-flight-controller.md),
[Raspberry Pi Pico](../docs/04-raspberry-pi-pico.md).

---

### CoreWing F405 WING V2 — flight controller
- **Category:** Flight controller stack (FC + PDB PLUS + wireless board)
- **Status:** ✅ owned
- **Used for:** main flight control — [Flight Controller](../docs/03-flight-controller.md)
- **Variant:** ICM-42688-P IMU, pre-soldered needle + pre-soldered XT60 plug
- **Price:** €66.88 (list €93.60) + €2.84 shipping
- **Source:** Banggood
- **Link:** Banggood — COREWING F405 Wing APP V2 (ICM42688, pre-soldered needle + XT60)

| Spec | Value |
|------|-------|
| Weight | **40 g** (stack) |
| Dimensions | **52 × 32 mm**, ~17–18 mm stack height |
| MCU | STM32F405, 168 MHz, 1 MB flash |
| IMU | ICM-42688-P (BMI270 optional) |
| Barometer | SPA06-003 |
| OSD | AT7456E |
| Blackbox | microSD, SDSC/SDHC (not SDXC), ≤32 GB, FAT16/32 (INAV ≤4 GB) |
| UARTs | 6 (USART1 wireless, USART2, 3, UART4, 5, USART6) |
| I2C / ADC / PWM | 1 / 4 / 12 (11 motor+servo, 1 LED) |
| RX | ELRS/CRSF on USART6; reverse-SBUS on USART2-RX |
| Input voltage (PDB) | 10–28 V (3–6S) |
| PDB current sense | 90 A cont, 125 A peak |
| Flight BEC | 5.2 V ±0.1, 4 A (5 A peak) |
| VTX/CAM BEC | 9 V ±0.1, 2 A (3 A peak); switchable 5/9/12 V |
| Servo BEC | 5/6/7.2 V adjustable, **14 A peak** — sustained ⚠️ see below |
| Firmware | INAV (factory) / ArduPilot (used here) |

- **⚠️ Servo BEC sustained rating mismatch:** the spec text says **4 A sustained**, but the V2
  product images ("61% super enhanced") label the Servo BEC **"Duration 8 A, peak 14 A"**. If it's
  truly **8 A sustained**, the servo-rail "marginal at ~4 A cruise" worry in
  [Power](../docs/02-power-system.md#servo-rail-headroom--the-marginal-case) and
  [Servos](../docs/05-servos.md) **goes away**. Until confirmed, docs keep the conservative 4 A.
  **How to verify (ranked):**
  1. **Read the servo-BEC regulator IC** (chip near "SERVO BEC" on the PDB) — zoom a photo, read the
     part number, check its datasheet continuous-current rating. The silicon is the hard limit; settles
     it for free. (A ~5–6 A buck IC → 8 A is marketing; a 10 A+ part → 8 A plausible.)
  2. **Bench load test** the 6 V rail: hold **5 A → 6 A → 8 A** for ~5–10 min each via an electronic
     DC load / power resistors / ganged servos; watch rail voltage stays ~6 V and the regulator temp
     (IR/thermistor). Holds 8 A near 6 V w/o cutoff → real 8 A; sags/cuts early → ~4 A. (The rail's
     ACS712 reads the current.)
  3. **Official V2 manual / ask CoreWing** — the V1 spec text may be stale; the "61% enhanced" wording
     implies a V2 BEC upgrade.
- **Notes:** "formerly SpeedyBee F405 WING APP". Three boards in a stack (FC + PDB PLUS + wireless);
  PDB does all power, FC only signals. Wireless board: BLE / WiFi-AP / WiFi-STA. Current scale
  158 (INAV) / 64 A/V (ArduPilot). Ships with mounting hardware (M2×12 brass standoffs, M2×4 screws),
  cables (VTX/GPS/DJI/CAM/DuPont), and a capacitor.

---

### Raspberry Pi Pico (RP2040) — secondary I/O controller
- **Category:** Microcontroller board
- **Status:** ✅ owned
- **Used for:** PWM expansion, NTC temp mux, LEDs, cockpit display — [Pico](../docs/04-raspberry-pi-pico.md)
- **Source / price:** —

| Spec | Value |
|------|-------|
| Weight | — |
| Dimensions | — *(≈51 × 21 mm — confirm)* |
| MCU | RP2040 (dual Cortex-M0+) |
| GPIO / ADC | 26 GPIO / 3× 12-bit ADC |
| Logic voltage | 3.3 V |
| Input power | via VSYS from PDB 5.2 V rail |

- **Notes:** programmed in MicroPython. Pin map in [Pico doc](../docs/04-raspberry-pi-pico.md#pin-map).

---

### CD74HC4067 — 16-channel analog multiplexer (breakout)
- **Category:** IC / breakout
- **Status:** ✅ owned
- **Used for:** expand Pico ADC for NTC thermistors (16 sensors on 1 ADC pin) — [Sensors](../docs/07-sensors-monitoring.md)
- **Variant / qty:** module (HW-178 style) · 1
- **Price:** €1.74
- **Link:** https://www.aliexpress.com/item/1005008558127708.html?mp=1

| Spec | Value |
|------|-------|
| Channels | 16 (C0–C15), common SIG |
| Control | S0–S3 (channel select) + EN (active-low enable) |
| Supply voltage | 2–6 V |
| On-resistance | ~70 Ω |
| Signal | analog or digital, bidirectional; **input ≤ VCC** |
| Working temp | −55 to +125 °C |
| Dimensions | 40.6 × 17.9 mm |
| Weight | — *(minor)* |

- **Notes:** 5 Pico pins (S0–S3 + SIG→ADC) read all 16 NTC channels. Tie **EN low** to enable. Run
  VCC = 3.3 V so signals stay ≤ VCC (matches the Pico ADC range). The ~70 Ω on-resistance is in
  series with the NTC divider — negligible vs the shared 47 kΩ divider, but let it settle a few µs
  after switching channels before sampling (~50 µs is plenty).

---

### 1.47" ST7789 TFT — cockpit display
- **Category:** Display
- **Status:** ✅ owned
- **Used for:** cockpit screen — [Pico](../docs/04-raspberry-pi-pico.md#4-cockpit-tft-display)
- **Variant / qty:** 1.47" 12-pin · 1
- **Price:** €3.40
- **Link:** https://www.aliexpress.com/item/1005011816140812.html?mp=1

| Spec | Value |
|------|-------|
| Diagonal | 1.47" |
| Resolution | 172 × 320 (RGB) |
| Driver IC | ST7789 |
| Interface | 4-wire SPI |
| Pins / pitch | 12-pin, 0.5 mm FFC (permanent ribbon → ZIF adapter) |
| Logic voltage | 2.8–3.3 V |
| Module size | 19.39 × 36.28 × 1.51 mm (+ ~20 mm FPC tail) |
| Active area | 17.39 × 34.15 mm |
| Weight | — *(minor)* |

- **Notes:** 12-pin chosen over 8-pin for thinner bezels; unused touch pins left floating.
  Needs a 12P 0.5 mm ZIF FFC→2.54 mm adapter board (carded below). Tiny module (~19×36 mm) — fits the
  cockpit footprint easily. ⚠️ The cheap listings vary (€3.40 working one vs a €16.58 8-pin that's
  sold out / won't ship here) — the owned unit is the €3.40 12-pin.

---

### FFC/FPC adapter board 12P 0.5 mm → 2.54 mm (ZIF) — display breakout
- **Category:** Adapter board
- **Status:** ✅ owned (5-pack)
- **Used for:** the [cockpit TFT](#147-st7789-tft--cockpit-display)'s 0.5 mm FFC ribbon → 2.54 mm
  pins → Pico SPI
- **Variant / qty:** 12P · 5 pcs
- **Price:** €2.95 / 5 pcs
- **Link:** https://www.aliexpress.com/item/1005012257691410.html

| Spec | Value |
|------|-------|
| Pins | 12P |
| FFC pitch | 0.5 mm, **ZIF flip-latch** socket |
| Output pitch | 2.54 mm through-hole pins |
| Board | FR-4, 1.6 mm thick, 1 mm holes |
| Dimensions (12P) | 24 × 26 mm |

- **Notes:** the screen's permanent FFC ribbon slides into the **ZIF socket** (flip latch — no
  soldering to the screen); then solder wire (28 AWG / school stock) from the 2.54 mm pins to the
  Pico SPI lines. 5 pcs → 4 spares.

---

### Jumper T14 CNC Hall ELRS — RC transmitter (ground side)
- **Category:** RC transmitter (radio) — ground equipment, not on-aircraft
- **Status:** ✅ owned
- **Used for:** piloting; its built-in **ELRS 2.4 GHz** pairs with the on-aircraft ELRS receiver →
  FC **USART6/CRSF** ([Flight Controller](../docs/03-flight-controller.md))
- **Variant / qty:** CNC Hall gimbals · 1
- **Price:** €123.09 (+ 2× 21700 cells €8.18, +€14.49 ship → €145.76 order)
- **Source:** Rotorama (rotorama.com)
- **Link:** Rotorama — Jumper T14 CNC Hall ELRS

| Spec | Value |
|------|-------|
| Weight | 471 g (without cells) |
| Dimensions | 185 × 175 × 79 mm |
| Firmware | EdgeTX |
| RF module | built-in ELRS 2.4 GHz, **up to 1000 mW**, refresh up to 1 kHz, active-cooled |
| Gimbals | Hall-effect CNC metal |
| Controls | 4 switches, 2 buttons, 2 pots, trims |
| Display | 2.42" OLED |
| Power | 2× 21700 Li-ion (not included); USB-C charging, 10 W |
| Storage | integrated memory (no SD card) |
| Expansion | JR-bay external module shaft |
| Includes | TX, USB-C cable, case |

- **Notes:** the airframe needs a matching **ELRS 2.4 GHz receiver** (on the buy list) to bind to
  this TX → CRSF into the FC's USART6. EdgeTX = full mixes/telemetry for the VTOL modes. Comparable
  in size to a RadioMaster Boxer / TBS Mambo.

---

### Jumper T14/T15 modified rocker (switch mod) — extra TX switches
- **Category:** Transmitter accessory (ground side)
- **Status:** ✅ owned
- **Used for:** add **switch controls** to the T14 for the F-35B's many modes (VTOL transition,
  gear, lights, afterburner, etc.) — pairs with the [Jumper T14](#jumper-t14-cnc-hall-elrs--rc-transmitter-ground-side)
- **Variant / qty:** 1 set (2 switches)
- **Price:** €6.51 (+€1.32 ship)
- **Source:** Banggood

| Spec | Value |
|------|-------|
| Type | 2× 2-position toggle switches (replace the top momentary button + 2-pos button) |
| Fits | Jumper T14 / T15 |
| Weight / dims | — *(minor; not specified)* |

- **Notes:** swaps the two top push-buttons for proper 2-position toggles → more latching switch
  channels in EdgeTX, useful for assigning the F-35B's flight-mode/gear/lighting toggles. Cosmetic/
  ergonomic mod; no effect on the airframe.

---

### RadioMaster RP3 — ELRS 2.4 GHz diversity receiver (on-aircraft)
- **Category:** RC receiver (ExpressLRS, diversity)
- **Status:** ✅ owned
- **Used for:** binds to the [Jumper T14](#jumper-t14-cnc-hall-elrs--rc-transmitter-ground-side); **CRSF
  → FC USART6** ([Flight Controller](../docs/03-flight-controller.md))
- **Variant / qty:** RP3 diversity · 1
- **Price:** €22.03 (+€1.38 ship)
- **Source:** Banggood

| Spec | Value |
|------|-------|
| Weight | 4.6 g (incl. both antennas) |
| Dimensions | 22 × 13 × 4 mm |
| MCU / RF | ESP8285 / SX1280 (Skyworks SE2431L LNA+PA) |
| Band | 2.4 GHz (2400–2480 MHz) |
| Diversity | dual antenna (2× 65 mm UFL T antenna) + switching |
| Telemetry power | up to 100 mW |
| Refresh rate | 25 Hz … 500 Hz / 1000 Hz (F1000) |
| Working voltage | 5 V |
| Bus interface | **CRSF** |
| Firmware | ExpressLRS v3.0 preinstalled (target "RadioMaster RP3 Diversity 2400 RX") |
| Includes | RX, 2× 65 mm UFL T antenna, manual |

- **Notes:** this is the receiver the original project plan named ("RP3 → F405 UART6"). Wire **CRSF
  to USART6** (TX6/RX6 pads), power from the FC 5 V pad (PDB Flight BEC 5.2 V is fine). Bind via
  **bind phrase**; WiFi firmware updates (no bind plug). Diversity + LNA/PA = good link reliability
  for the VTOL. Must match the TX's ELRS band/version (both 2.4 GHz). The "ELRS receiver" is now
  owned (no longer a buy-list item).

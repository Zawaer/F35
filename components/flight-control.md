# Components — Flight Control & Electronics

Cards for the FC stack, the Pico, and the cockpit/IO electronics. See the
[template & field guide](README.md). Build context: [Flight Controller](../docs/03-flight-controller.md),
[Raspberry Pi Pico](../docs/04-raspberry-pi-pico.md).

---

### CoreWing F405 WING V2 — flight controller
- **Category:** Flight controller stack (FC + PDB PLUS + wireless board)
- **Status:** ✅ owned (ordered 9 Apr 2026)
- **Used for:** main flight control — [Flight Controller](../docs/03-flight-controller.md)
- **Variant:** ICM-42688-P IMU, pre-soldered needle + pre-soldered XT60 plug
- **Price:** €66.88 (list €93.60) + €2.84 shipping
- **Source:** Banggood
- **Link:** Banggood — COREWING F405 Wing APP V2 (ICM42688, pre-soldered needle + XT60)

| Spec | Value |
|------|-------|
| Weight | **40 g** (full stack, **incl. the wireless/USB expansion board**) |
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
| Servo BEC | 5/6/7.2 V adjustable, **8 A sustained, 14 A peak** |
| Firmware | INAV (factory) / ArduPilot (used here) |

- **✅ Servo BEC = 8 A continuous (confirmed).** The product-page *text* said 4 A but its images said
  8 A; the **official manual + RaceDayQuads listing** confirm **5 V (adj 5/6/7.2 V) @ 8 A continuous,
  14 A peak**. So the servo rail is **not marginal** — no UBEC split, and **no external UBEC will be
  ordered** (see [Power → servo rail](../docs/02-power-system.md#servo-rail-headroom)). Still worth
  confirming first-hand: read the PDB servo-BEC regulator chip's part number (IC by the SERVO BEC
  inductor) and/or bench-load the 6 V rail to ~8 A.
- **Notes:** "formerly SpeedyBee F405 WING APP". Three boards in a stack (FC + PDB PLUS + wireless);
  PDB does all power, FC only signals. Wireless board: BLE / WiFi-AP / WiFi-STA. Current scale
  158 (INAV) / 64 A/V (ArduPilot). Ships with mounting hardware (M2×12 brass standoffs, M2×4 screws),
  cables (VTX/GPS/DJI/CAM/DuPont), and a capacitor.

---

### RP2040 secondary I/O controller — WeAct RP2040 (primary) + Pi Pico (spare)
- **Category:** Microcontroller board
- **Status:** ✅ owned (both: WeAct RP2040 ×1 + Raspberry Pi Pico ×1 — both had on hand, neither ordered for this build)
- **Used for:** PWM expansion (doors/nozzle servos), NTC temp mux, LEDs, cockpit ST7789 display, UART
  to the FC — [Pico/RP2040 doc](../docs/04-raspberry-pi-pico.md)
- **Source / price:** —

| Spec | WeAct RP2040 (primary) | Raspberry Pi Pico (spare) |
|------|------------------------|---------------------------|
| MCU | RP2040 (dual Cortex-M0+ @133 MHz) | RP2040 (same) |
| Flash | 2 MB QSPI | 2 MB QSPI |
| RAM | 264 KB | 264 KB |
| GPIO / ADC | ~28 GPIO / 3× 12-bit | 26 GPIO / 3× 12-bit |
| USB | **USB-C** | micro-USB |
| Reset button | **yes** | no |
| Size | 53 × 21.5 mm | 51 × 21 mm |
| Logic / power | 3.3 V · VSYS from PDB 5.2 V rail | same |

- **Notes:** **WeAct is the primary** secondary-I/O board (USB-C + hardware reset button = nicer for
  flashing/field resets); the bare **Pi Pico is the flash-and-swap spare** — same RP2040, pin/firmware
  compatible, so a crash-fried board is a 2-minute swap. Programmed in MicroPython; pin map in the
  [RP2040 doc](../docs/04-raspberry-pi-pico.md#pin-map).
- **Why RP2040 over the ESP32-S3 stash:** the secondary controller's analog sensing (NTC mux + ACS712)
  wants the RP2040's cleaner 3.3 V ADC, PIO gives jitter-free multi-servo/LED timing, and there's **no
  2.4 GHz conflict** with the ELRS RX (the ESP32's WiFi/BT shares the control band). The cockpit screen
  (172×320 ST7789, mostly-static dashboard) is well within RP2040 headroom. ESP32-S3 is ~4–5× the CPU
  but that power isn't needed here — those boards are better used for bench/ground tooling.

---

### CD74HC4067 — 16-channel analog multiplexer (breakout)
- **Category:** IC / breakout
- **Status:** ✅ owned (ordered 24 Jun 2026)
- **Used for:** expand Pico ADC for NTC thermistors (16 sensors on 1 ADC pin) — [Sensors](../docs/07-sensors-monitoring.md)
- **Variant / qty:** module (HW-178 style) · 1
- **Price:** €1.74
- **Link:** https://www.aliexpress.com/item/1005008558127708.html

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
- **Status:** ✅ owned (ordered 24 Jun 2026)
- **Used for:** cockpit screen — [Pico](../docs/04-raspberry-pi-pico.md#4-cockpit-tft-display)
- **Variant / qty:** 1.47" 12-pin · 1
- **Price:** €3.40
- **Link:** https://www.aliexpress.com/item/1005011816140812.html

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
- **Status:** ✅ owned (5-pack · ordered 24 Jun 2026)
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
- **Status:** ✅ owned (ordered 10 Nov 2025)
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
- **Status:** ✅ owned (ordered 9 Apr 2026)
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
- **Status:** ✅ owned (ordered 1 Apr 2026)
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

---

### Electronics starter kit (200+ pcs) — prototyping / passives stock
- **Category:** Component kit (passives, semiconductors, headers)
- **Status:** ✅ owned (1 set · ordered 1 Apr 2026)
- **Used for:** **divider/pull-up resistors, header pins, bench prototyping** across the build (e.g.
  the STS3032 10 kΩ UART resistor, ADC dividers, breadboarding) — general
- **Variant / qty:** "Set" · 1 kit (~230 pcs)
- **Price:** **€2.88** (pack 53 g)
- **Source:** AliExpress — JYJD basic electronics starter kit

**Contents:**

| Item | Qty |
|------|-----|
| 5 mm LEDs — white / yellow / blue / green / red | 10 each (50) |
| RGB LED | 1 |
| Photoresistor (LDR) | 2 |
| Thermistor (NTC) | 1 |
| Diode 1N4007 | 5 |
| NPN transistor PN2222 | 5 |
| Optocoupler 4N35 · shift register 74HC595 | 1 · 1 |
| Tactile button | 10 |
| Active / passive buzzer | 1 / 1 |
| Precision potentiometer | 1 |
| Ceramic cap 22 pF / 104 (0.1 µF) | 10 / 10 |
| Electrolytic 10 µF / 100 µF (50 V) | 5 / 5 |
| Resistors 10R·100R·220R·330R·1K·2K·5K1·10K·100K·1M | 10 each (100) |
| 40-pin header strips | 2 |

- **Notes:** general bench/prototyping stock — provides the **10 kΩ** for the STS3032 half-duplex UART
  trick, assorted divider resistors, and **header pins** for the Pico/FC. ⚠️ **No 47 kΩ** in the kit
  (values jump 10K → 100K), so the **shared 47 kΩ NTC divider resistor** comes from school stock / a
  separate buy (see [Sensors](../docs/07-sensors-monitoring.md#temperature-sensing-ntc-100k--multiplexer));
  likewise the ACS712 10 k/20 k pairs. The bundled single NTC + LEDs are hobby-grade — the build's
  real sensors/lights are the dedicated cards, not these.

---

### 40-pin breakable male header strips 2.54 mm (×30) — Pico / FC / adapter pins
- **Category:** Connector (pin header)
- **Status:** ✅ owned (30 strips · ordered 1 Apr 2026)
- **Used for:** **header pins for the Pico, FC pads, the FFC adapter board, proto wiring** — snap to
  length
- **Variant / qty:** 1×40P single-row male, breakable · 30 strips (multi-colour)
- **Price:** **€2.23**
- **Source:** AliExpress — 30× 1×40P 2.54 mm breakable male headers

| Spec | Value |
|------|-------|
| Type | single-row **male** pin header, **breakable / snappable** |
| Pitch | 2.54 mm |
| Pins | 40 per strip (snap to any length) |
| Qty | 30 strips |
| Colours | black / blue / green / yellow / red / white |

- **Notes:** snap to length for the Pico, FC breakouts, the
  [FFC adapter board](#ffcfpc-adapter-board-12p-05-mm--254-mm-zif--display-breakout), and
  prototyping. 30 × 40 = 1200 pins — bulk/spares (the starter kit also includes 2 strips). Colours are
  cosmetic; pins are standard tin-plated 2.54 mm.

---

### Dupont jumper wires 15 cm (M-M / M-F / F-F) ×240 — prototyping / signal wiring
- **Category:** Cable (Dupont jumper wires)
- **Status:** ✅ owned (2× 120 = 240 pcs · ordered 2 Apr 2026)
- **Used for:** **general prototyping & low-current signal hookups** — Pico/FC/sensor breadboarding,
  temporary links — general
- **Variant / qty:** 15 cm · 3 kinds (M-M, M-F, F-F) · 120 ×2 = 240
- **Price:** **€7.87** (€3.94 × 2 packs)
- **Source:** AliExpress — ENLINCA Dupont jumper wire kit (15 cm, 3 kinds)

| Spec | Value |
|------|-------|
| Pitch | 2.54 mm, 1-pin Dupont |
| Length | 15 cm |
| Types | M-M, M-F, F-F (40 each per 120-pack) |
| Qty | 240 (2× 120) |
| Wire | thin ribbon, multicolour |

- **Notes:** general bench/prototyping jumpers — breadboard the Pico/FC/sensors and make temporary
  signal links. ⚠️ **Thin, low-current, crimped Dupont ends** — fine for signal/logic, **not** for
  power or vibration-critical flight connections (solder + strain-relieve those). Pairs with the
  [40-pin headers](#40-pin-breakable-male-header-strips-254-mm-30--pico--fc--adapter-pins) and the
  starter kit.

---

### Breadboards MB-102 (830-pt) + 400-pt — solderless prototyping
- **Category:** Tool (solderless breadboard) — **bench, not on-aircraft**
- **Status:** ✅ owned (1 of each · ordered 1 Apr 2026)
- **Used for:** **solderless bench prototyping** — test Pico/FC/sensor circuits before soldering —
  general
- **Variant / qty:** "Kit" = **1× 830-point (MB-102) + 1× 400-point (mini)**
- **Price:** **€3.77**
- **Source:** AliExpress — MB-102 breadboard kit (400 + 830 points)

| Spec | Value |
|------|-------|
| Boards | 830-point (MB-102) + 400-point (mini) |
| Pitch | 2.54 mm |
| 830-pt size | 163 × 54 mm |
| Rails | ± power buses both sides |
| Type | solderless, reusable |

- **Notes:** bench tool for breadboarding the Pico + sensors/dividers before committing to solder —
  e.g. prototype the NTC/mux + ACS712 divider circuits and the LED-driver/MOSFET wiring. Pairs with
  the [Dupont jumpers](#dupont-jumper-wires-15-cm-m-m--m-f--f-f-240--prototyping--signal-wiring) and
  the starter kit. Not flown.

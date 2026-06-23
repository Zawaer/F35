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

### CD74HC4067 — 16-channel analog multiplexer
- **Category:** IC / breakout
- **Status:** 🛒 in cart (€1.74)
- **Used for:** expand Pico ADC for NTC thermistors — [Sensors](../docs/07-sensors-monitoring.md)
- **Source / price:** AliExpress, €1.74

| Spec | Value |
|------|-------|
| Channels | 16 (S0–S3 select + SIG) |
| Supply voltage | 2–6 V |
| Weight / dims | — |

- **Notes:** —

---

### 1.47" ST7789 TFT — cockpit display
- **Category:** Display
- **Status:** 🛒 in cart (€3.40)
- **Used for:** cockpit screen — [Pico](../docs/04-raspberry-pi-pico.md#4-cockpit-tft-display)
- **Source / price:** AliExpress, €3.40

| Spec | Value |
|------|-------|
| Diagonal | 1.47" |
| Resolution | 172 × 320 |
| Driver IC | ST7789 |
| Interface | 4-wire SPI |
| Pins / pitch | 12-pin, 0.5 mm FFC (permanent ribbon → ZIF adapter) |
| Logic voltage | 2.8–3.3 V |
| Weight / dims | — |

- **Notes:** 12-pin chosen over 8-pin for thinner bezels; unused touch pins left floating.
  Needs a 12P 0.5 mm ZIF FFC→2.54 mm adapter board.

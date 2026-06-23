# Components — Flight Control & Electronics

Cards for the FC stack, the Pico, and the cockpit/IO electronics. See the
[template & field guide](README.md). Build context: [Flight Controller](../docs/03-flight-controller.md),
[Raspberry Pi Pico](../docs/04-raspberry-pi-pico.md).

---

### CoreWing F405 WING V2 — flight controller (worked example)
- **Category:** Flight controller stack (FC + PDB PLUS + wireless board)
- **Status:** ✅ owned
- **Used for:** main flight control — [Flight Controller](../docs/03-flight-controller.md)
- **Source / price:** —

| Spec | Value |
|------|-------|
| Weight | — *(add from product page)* |
| Dimensions / mounting | — *(add; mounting hole pattern needed for the Fusion model)* |
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
| Servo BEC | 5 V ±0.1, 4 A (14 A peak); adjustable 5/6/7.2 V |
| Firmware | INAV (factory) / ArduPilot (used here) |

- **Notes:** three boards in a stack; PDB does all power, FC only signals. Wireless board:
  BLE / WiFi-AP / WiFi-STA. Current scale 158 (INAV) / 64 A/V (ArduPilot).

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

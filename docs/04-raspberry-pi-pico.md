# Raspberry Pi Pico (RP2040)

> **Role:** the secondary I/O alongside the F405 FC, split across **two RP2040 boards** (see the pin
> budget below — one board can't fit it all). Between them they handle: (1) up to ~16 PWM outputs
> for secondary/cosmetic servos, (2) **temperature sensing** via NTC thermistors through a
> CD74HC4067 multiplexer, (3) the **LED system** (nav/strobe/landing/COB), and (4) the **cockpit TFT
> display**. Each board talks to the FC over its own **UART** and is powered from the PDB **5.2V
> Flight BEC**. Programmed in **MicroPython**. ("RP2040" in notes = these boards.)

> **Boards:** **two RP2040s.** The **WeAct Studio RP2040 (2 MB)** (USB-C + hardware reset) runs the
> **avionics board** (sensors + screen + lights); a **Raspberry Pi Pico** runs the **servo-bank
> board**. Both are RP2040, so firmware/pinouts are interchangeable. Because the bare Pico is now an
> *active* board (no longer the spare), a fresh RP2040 is on the buy-later list as the flash-and-swap
> hot-spare. **RP2040 chosen over the owned ESP32-S3 boards** for cleaner ADC (NTC/ACS712 sensing),
> jitter-free PIO servo/LED timing, and no 2.4 GHz clash with the ELRS RX; the mostly-static 172×320
> cockpit dashboard is well within its headroom.

The boards exist because the F405 runs out of PWM outputs and ADC ports. Offloading temp sensing,
secondary actuation, lighting, and the cockpit screen keeps the FC free for flight.

## Why two boards (pin budget)

An RP2040 board exposes **26 usable GPIO** (GP0–22, GP26–28), only **3 of them ADC** (GP26/27/28) —
budgeted to 26/3 so the bare-Pico spare stays swap-compatible. One board doing *everything* doesn't
fit on two counts:

- **ADC:** 13 NTC + 2 ACS712 + 2 battery dividers = **17 analog signals** vs **3 ADC pins**. Resolved
  by muxing: **GP26 = mux SIG** (13 NTC + 2 current = 15 of the mux's 16 channels, 1 free), **GP27 =
  main-pack V**, **GP28 = roll-post V**.
- **GPIO:** even with that fix, one board's overhead is UART (2) + mux SIG+select (5) + 2× battery-V
  (2) + LEDs (~5) + cockpit TFT (~5) = **~19 pins**, leaving only **7** for servos — but the
  secondary/cosmetic actuators number **~13–16** (gear retracts, gear/lift-fan doors, vane box, nose
  steer, nozzle, canopy). Short by 6–9 outputs.

**Split:**

| Board | Carries | ~GPIO used |
|-------|---------|-----------|
| **WeAct — avionics** | UART↔FC, NTC mux (SIG + S0–S3), 2× battery-voltage ADC, LEDs, cockpit TFT | ~19 / 26 |
| **Pico — servo bank** | UART↔FC, 13–16 secondary-servo PWM | ~15–18 / 26 |

Each board uses one of the F405's spare UARTs (UART tally: USART1 wireless, USART6 ELRS, 1 for the
STS3032 serial bus, 2 for the two RP2040s → 1 still free).

> **Alternative considered — single board + PCA9685:** one WeAct plus a **PCA9685** (16-ch PWM over
> I²C, ~€2) collapses the 16 servo pins to 2 I²C pins, so one RP2040 does everything and the bare
> Pico stays a true hot-spare. 50 Hz servo PWM is exactly the PCA9685's job; the FC→UART→WeAct→I²C
> hop is fine for slow door/gear actuators. Cheaper and preserves the spare, at the cost of an extra
> I²C chip. **Current plan uses two RP2040s** (hardware already owned); switch to this if board count
> or the lost spare becomes the bigger concern.

## Pin map — avionics board (WeAct)

| Pin | Function | Connected to |
|----------|----------|--------------|
| GPIO 26 (ADC0) | Multiplexer analog in | CD74HC4067 SIG — 13 NTC + 2 ACS712 (15 of 16, 1 free) |
| 4× GPIO (e.g. 18–21) | Mux channel select | CD74HC4067 S0–S3 |
| GPIO 27 (ADC1) | Main-pack voltage | 100 k/10 k divider |
| GPIO 28 (ADC2) | Roll-post-pack voltage | 10 k/2 k divider |
| GPIO 10 / 11 / 12 | LED PWM | driver PWM inputs (red / green / strobe) |
| GPIO 15 | Strobe enable / MOSFET gate | LED enable / IRLZ44N (COB strip) |
| SPI (SCK/MOSI/CS/DC/RST/BLK) | Cockpit TFT | 1.47" ST7789 via FFC adapter |
| UART (TX/RX) | FC link | F405 spare UART (MAVLink telemetry + LED/screen cmds) |
| 3.3V | Sensor / mux / pull-up supply | NTC dividers, mux, screen logic |
| VSYS/5V in | Power | PDB 5.2V Flight BEC |
| GND | Common ground | FC / PDB / sensors |

> Pin numbers for LEDs (10/11/12/15) and the ADCs (26/27/28) are design values; SPI pins are
> allocated as the screen is finalised. **All ADC inputs live on this board** (3 ADC pins; the
> current sensors ride the mux's spare channels — see [Sensors](07-sensors-monitoring.md)).

## Pin map — servo-bank board (Pico)

| Pin | Function | Connected to |
|----------|----------|--------------|
| 13–16× PWM GPIO | Secondary servos | gear retracts, gear/lift-fan doors, vane box, nose steer, nozzle, canopy |
| UART (TX/RX) | FC link | F405 spare UART (MAVLink PWM commands) |
| VSYS/5V in | Power | PDB 5.2V Flight BEC |
| GND | Common ground | FC / PDB |

> Each secondary servo's specific GPIO is assigned as the airframe layout firms up. Door servos on
> the **4.0 V LM2596 rail** (M005/S002), others on the 6 V servo rail — see [Servos](05-servos.md).

## Roles in detail

### 1. Extra PWM outputs
The F405 has only 11 usable PWM channels; the F-35B needs more. The Pico adds **up to 16** PWM
outputs over UART. Primary flight surfaces + ESCs stay on the FC; **secondary/cosmetic actuators**
(gear doors, lift-fan doors, canopy, nozzle) live on the Pico. See [Servos](05-servos.md).

### 2. Temperature sensing (NTC + CD74HC4067)
NTC 100K thermistors form a voltage divider — **one shared 47 kΩ** on the mux SIG line — feeding a
**CD74HC4067 16-channel analog multiplexer**; the Pico selects channels via S0–S3 and reads the SIG
line on one ADC pin (cheap, 16 channels from one ADC). Full detail and
the current-sensing (ACS712) story are in [Sensors & Monitoring](07-sensors-monitoring.md).

### 3. LED control
The Pico PWM-dims the CC LED drivers (nav/strobe/landing) and switches the 12V COB strip via an
IRLZ44N MOSFET. Budget and the afterburner caveat are in [Lighting](08-lighting.md).

### 4. Cockpit TFT display
A **1.47" ST7789 SPI TFT** (172×320, 12-pin) shows a cockpit image or live flight data. Its
permanently-attached **0.5 mm-pitch FFC ribbon** slides into a **ZIF FFC→2.54 mm adapter board**
(12P); the Pico then connects to the adapter's through-hole pins with 28AWG wire — **no soldering
to the screen itself**. The 12-pin variant was chosen over 8-pin for thinner bezels (unused touch
pins left floating). Driven over SPI by the Pico.

## MicroPython

Firmware will be written once the actual components are in hand. The wiring/divider recipes it will
implement are recorded in
[Sensors & Monitoring](07-sensors-monitoring.md#temperature-sensing-ntc-100k--multiplexer) (NTC + mux)
and [Lighting](08-lighting.md) (strobe/dimming). Planned modules:

- temperature — NTC-via-CD74HC4067-mux reading (beta-equation conversion).
- LED control — nav-light dimming + strobe pattern.

## Communication with the FC (and onward to the T14)

The RP2040↔F405 link is **MAVLink over UART**. For the Pico's own sensor values (temps, currents,
voltages), MAVLink's **`NAMED_VALUE_FLOAT`** (string name + float) carries arbitrary readings —
ArduPilot logs them to the blackbox and shows them in any MAVLink GCS (Mission Planner / QGC / phone
via the wireless board). So getting Pico data *into* the FC is a solved problem; bandwidth is trivial
(~18 values at a few Hz).

Getting custom values onward to the **Jumper T14** is the limited hop: the T14 (EdgeTX) only sees
ArduPilot's **fixed CRSF telemetry schema** (attitude, GPS, battery V/I/mAh, vario, mode, RPM, a few
temps). A custom `NAMED_VALUE_FLOAT` does **not** auto-appear on the radio. Therefore:

- **Temperatures live on the cockpit TFT** (this board already drives it and holds the NTC data) — no
  protocol gymnastics, and the right place for a 13-channel dashboard.
- **Full picture on a MAVLink GCS** during bench/tuning.
- **Only 1–2 critical temps on the T14** (e.g. main + lift ESC), if wanted, via an ArduPilot **Lua
  script → CRSF custom sensor** + a matching EdgeTX sensor — the payoff is EdgeTX audio alerts. Don't
  try to push all 13. (The Skywalker V2 ESCs are PWM-only, so no ESC temp/RPM comes back natively.)

## Open questions / TODO

- ✅ **Resolved: two RP2040 boards** (WeAct avionics + Pico servo bank) — one board can't fit the
  pin/ADC budget (see [above](#why-two-boards-pin-budget)). PCA9685 single-board alternative noted.
- Lock down the MAVLink dialect/rate on each RP2040↔F405 UART.
- Allocate specific GPIOs for each secondary PWM servo (servo-bank board) and the mux select lines.
- Rewrite the temperature code for NTC + CD74HC4067.
- Confirm SPI pin mapping for the ST7789 display.

## Related

[Flight Controller](03-flight-controller.md) · [Servos](05-servos.md) ·
[Sensors & Monitoring](07-sensors-monitoring.md) · [Lighting](08-lighting.md)

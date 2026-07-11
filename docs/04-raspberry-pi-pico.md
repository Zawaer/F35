# Raspberry Pi Pico (RP2040)

> **Role:** the secondary I/O alongside the F405 FC, split across **two RP2040 boards** (see the pin
> budget below — one board can't fit it all). Between them they handle: (1) up to ~16 PWM outputs
> for secondary/cosmetic servos, (2) **temperature sensing** via NTC thermistors through a
> CD74HC4067 multiplexer, (3) the **LED system** (nav/strobe/landing/COB), and (4) the **cockpit TFT
> display**. Each board talks to the FC over its own **UART** and is powered from the PDB **5.2V
> Flight BEC**. Programmed in **MicroPython**. ("RP2040" in notes = these boards.)

> **Boards:** **two RP2040s.** The **WeAct Studio RP2040 (2 MB)** (USB-C + hardware reset) runs the
> **avionics board** (sensors + screen + lights); a **Raspberry Pi Pico** runs the **servo-bank
> board**. Both are RP2040, so firmware/pinouts are interchangeable. **RP2040 chosen over the owned
> ESP32-S3 boards** for cleaner ADC (NTC/ACS712 sensing),
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
| **Pico — servo bank** | UART↔FC, ~8–10 secondary-servo PWM channels (~14 servos, symmetric pairs share a channel) | ~10–12 / 26 |

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
| GPIO 0 (TX) / GPIO 1 (RX) | UART0 FC link | F405 spare UART (MAVLink telemetry + LED/screen cmds) |
| GPIO 2 (SCK) / GPIO 3 (MOSI) | SPI0 data | ST7789 SCK / SDA |
| GPIO 4 (CS) | SPI0 chip select | ST7789 CS |
| GPIO 5 (DC) | SPI0 data/command | ST7789 DC |
| GPIO 6 (RST) | Display reset | ST7789 RST |
| GPIO 7 (BLK) | Backlight enable | ST7789 BLK |
| GPIO 10 / 11 / 12 | LED PWM | driver PWM inputs (red / green / strobe) |
| GPIO 15 | Strobe enable / MOSFET gate | LED enable / IRLZ44N (COB strip) |
| GPIO 8 (SDA) / GPIO 9 (SCL) | I2C0 | 2× MPU6050 vibration sensors (main + lift EDF), shared bus — AD0 pin sets 0x68/0x69 |
| GPIO 18 / 19 / 20 / 21 | Mux channel select | CD74HC4067 S0–S3 |
| GPIO 26 (ADC0) | Multiplexer analog in | CD74HC4067 SIG — 13 NTC + 2 ACS712 (15 of 16, 1 free) |
| GPIO 27 (ADC1) | Main-pack voltage | 100 k/10 k divider |
| GPIO 28 (ADC2) | Roll-post-pack voltage | 10 k/2 k divider |
| 3.3V | Sensor / mux / pull-up supply | NTC dividers, mux, screen logic |
| VSYS/5V in | Power | PDB 5.2V Flight BEC |
| GND | Common ground | FC / PDB / sensors |

> **21 of 26 GPIO used.** SPI1 is unavailable (GP10/11 taken by LEDs), so SPI0 is used for the
> display. GP23/24/25/29 are internal board functions (SMPS, VBUS sense, user LED, VSYS ADC) —
> leave floating/unused. **All ADC inputs live on this board** (3 ADC pins; current sensors ride
> the mux's spare channels — see [Sensors](07-sensors-monitoring.md)).

## Pin map — servo-bank board (Pico)

| Pin | Function | Connected to |
|----------|----------|--------------|
| 8–10× PWM GPIO | Secondary servos | gear retracts, gear/lift-fan doors, vane box, nose steer, nozzle (canopy skipped v1) — symmetric pairs share a channel |
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

**Contrast / anti-glare filter (optional, V1 trial):** the ST7789 is a transmissive TFT — washed-out
blacks, backlight bleed, and outdoor glare. A thin **neutral smoke filter (~30–50% transmission)**
behind the canopy with a **black bezel** around the screen makes it read like a real avionics MFD.
The mechanism is ambient-rejection, *not* "darkening blacks more than whites" (a neutral tint is
linear — it attenuates all emitted light equally): reflected sunlight passes through the filter
**twice** (in and out, ∝ T²) while the display's own light passes **once** (∝ T), so the image-to-glare
ratio improves by 1/T. This matters because the plane is viewed outdoors. Note the **tinted canopy
already does some of this** — build with just a black bezel first, look through the actual canopy, and
add a dedicated smoke disc (a smoked-acrylic offcut, *not* uneven packaging plastic) only if still
washed out. Burn-in is a non-issue: this is a TFT, not OLED. See [Canopy](09-materials-airframe.md#canopy-transparency).

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
- ✅ **Resolved: mux select lines (GP18–21) and SPI0 display pins (GP2–7) locked** — avionics board pin map complete.
- Allocate specific GPIOs for each secondary PWM servo (servo-bank board).
- Rewrite the temperature code for NTC + CD74HC4067.

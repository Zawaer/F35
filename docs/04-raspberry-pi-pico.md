# Raspberry Pi Pico (RP2040)

> **Role:** the secondary I/O controller alongside the F405 FC. It handles: (1) up to **16 extra
> PWM outputs** for secondary/cosmetic servos, (2) **temperature sensing** via NTC thermistors
> through a CD74HC4067 multiplexer, (3) the **LED system** (nav/strobe/landing/COB), and (4) the
> **cockpit TFT display**. It talks to the FC over **UART** and is powered from the PDB **5.2V
> Flight BEC**. Programmed in **MicroPython**. ("RP2040" in notes = this Pico.)

The Pico exists because the F405 runs out of PWM outputs and ADC ports. Offloading temp sensing,
secondary actuation, lighting, and the cockpit screen to the Pico keeps the FC free for flight.

## Pin map

| Pico pin | Function | Connected to |
|----------|----------|--------------|
| GPIO 26 (ADC0) | Multiplexer analog in | CD74HC4067 SIG (16 NTC channels) |
| 4× GPIO (e.g. 18–21) | Mux channel select | CD74HC4067 S0–S3 |
| GPIO 27 / 28 (ADC1/2) | Spare analog in | reserved |
| GPIO 10 / 11 / 12 | LED PWM | driver PWM inputs (red / green / strobe) |
| GPIO 15 | Strobe enable / MOSFET gate | LED enable / IRLZ44N (COB strip) |
| SPI (SCK/MOSI/CS/DC/RST/BLK) | Cockpit TFT | 1.47" ST7789 via FFC adapter |
| UART (TX/RX) | FC link | F405 spare UART (PWM cmds + telemetry) |
| PWM GPIOs (allocated) | Secondary servos | gear/lift-fan doors, canopy, nozzle |
| 3.3V | Sensor / mux / pull-up supply | NTC dividers, mux, screen logic |
| VSYS/5V in | Power | PDB 5.2V Flight BEC |
| GND | Common ground | FC / PDB / sensors |

> Pin numbers for LEDs (10/11/12/15) and the mux ADC (26) are design values; SPI and
> secondary-servo PWM GPIOs are allocated as those subsystems are finalised.

## Roles in detail

### 1. Extra PWM outputs
The F405 has only 11 usable PWM channels; the F-35B needs more. The Pico adds **up to 16** PWM
outputs over UART. Primary flight surfaces + ESCs stay on the FC; **secondary/cosmetic actuators**
(gear doors, lift-fan doors, canopy, nozzle) live on the Pico. See [Servos](05-servos.md).

### 2. Temperature sensing (NTC + CD74HC4067)
NTC 100K thermistors form 10kΩ voltage dividers feeding a **CD74HC4067 16-channel analog
multiplexer**; the Pico selects channels via S0–S3 and reads the SIG line on one ADC pin. This
replaced the earlier DS18B20 1-Wire plan (cheaper NTCs, 16 channels from one ADC). Full detail and
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

## Open questions / TODO

- Lock down the UART protocol/framing between Pico and F405.
- Allocate specific GPIOs for each secondary PWM servo and the mux select lines; add to the map.
- Rewrite the temperature code for NTC + CD74HC4067.
- Confirm SPI pin mapping for the ST7789 display.
- Decide whether one Pico handles everything (servos + temp + LEDs + screen) or a second RP2040 is needed.

## Related

[Flight Controller](03-flight-controller.md) · [Servos](05-servos.md) ·
[Sensors & Monitoring](07-sensors-monitoring.md) · [Lighting](08-lighting.md)

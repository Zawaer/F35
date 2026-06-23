# Raspberry Pi Pico

> **Role:** a secondary I/O controller alongside the F405 FC. It (1) provides up to **16 extra PWM
> outputs** for secondary/cosmetic servos, (2) reads **DS18B20 temperature sensors** on a 1-Wire
> bus, and (3) drives the **LED system** (nav lights + strobes) via PWM dimming. It talks to the FC
> over **UART** and is powered from the PDB **5.2V Flight BEC**. Programmed in **MicroPython**.

The Pico exists because the F405 runs out of both PWM outputs and ADC ports (all 4 ADCs go to
battery monitoring — see [Flight Controller](03-flight-controller.md)). Offloading temp sensing and
secondary actuation to the Pico solves both.

## Pin map

| Pico pin | Function | Connected to |
|----------|----------|--------------|
| GPIO 26 | 1-Wire bus (DS18B20) | All DS18B20 sensors' DQ, with 4.7kΩ pull-up to 3.3V |
| GPIO 27 (ADC1) | Spare analog in | (reserved — e.g. NTC if ever used) |
| GPIO 28 (ADC2) | Spare analog in | (reserved) |
| GPIO 10 | PWM — red nav light | LED driver PWM input (port wingtip) |
| GPIO 11 | PWM — green nav light | LED driver PWM input (starboard wingtip) |
| GPIO 12 | PWM — white strobe | LED driver PWM input (wingtips) |
| GPIO 15 | Digital out — strobe pattern | LED driver enable (alt strobe method) |
| UART (TX/RX) | Telemetry + PWM command link | F405 spare UART |
| 3.3V | Sensor/​pull-up supply | DS18B20 VDD + pull-up |
| VSYS/5V in | Power | PDB 5.2V Flight BEC |
| GND | Common ground | FC / PDB / sensors |

> The GPIO assignments for LEDs (10/11/12/15) and the 1-Wire pin (26) are the values used in the
> design code below. The PWM-servo expansion pins are allocated as the secondary servo list is
> finalised — see [Servos](05-servos.md).

## Roles in detail

### 1. Extra PWM outputs

The F405 has only 11 usable PWM channels; the F-35B needs more once VTOL servos, doors, gear, and
cosmetics are counted. The Pico provides **up to 16 additional PWM outputs**, commanded by the FC
over UART. Primary flight-surface servos and ESCs stay on the FC; **secondary/cosmetic actuators**
(gear doors, lift-fan doors, canopy, exhaust nozzle, etc.) live on the Pico.

### 2. Temperature sensing (DS18B20, 1-Wire)

All DS18B20 sensors share **one** GPIO (26) on a single 1-Wire bus with a 4.7kΩ pull-up:

```
Pico 3.3V ──── 4.7kΩ ──┬──── DQ (pin 2) — all sensors
                        │
Pico GPIO 26 ───────────┘
Pico GND  ───────────────── GND (pin 1) — all sensors
Pico 3.3V ───────────────── VDD (pin 3) — all sensors
```

Each DS18B20 has a unique factory 64-bit address, so all sensors live on one wire and are addressed
individually. Sensors planned: ESC 1, ESC 2, Battery 1 (and optionally Battery 2 / EDF exhaust).
The Pico reads temps and sends them to the FC over UART for ArduPilot blackbox logging. Full wiring,
labelling workflow, and reasoning are in [Sensors & Monitoring](07-sensors-monitoring.md). A 5kΩ
(or 5.1kΩ) pull-up is acceptable in place of 4.7kΩ (1-Wire tolerates ±20%).

### 3. LED control

The Pico PWM-dims the constant-current LED drivers: nav lights held at a constant ~40% brightness,
white strobes flashed in software. Details and current budget in [Lighting](08-lighting.md).

## MicroPython

Working/reference snippets live in [`code/pico/`](../code/pico/):

- `temp_logger.py` — scan + read all DS18B20 sensors by hardcoded address.
- `led_control.py` — nav-light dimming + strobe pattern.

Minimal DS18B20 read:

```python
import machine, onewire, ds18x20, time
ow = onewire.OneWire(machine.Pin(26))
ds = ds18x20.DS18X20(ow)
sensors = ds.scan()          # auto-discovers all sensor addresses
while True:
    ds.convert_temp()
    time.sleep_ms(750)       # conversion time
    for s in sensors:
        print(ds.read_temp(s))
    time.sleep(1)
```

## Open questions / TODO

- Lock down the UART protocol/framing between Pico and F405 (PWM commands out, telemetry in).
- Allocate and document the specific GPIOs used for each secondary PWM servo.
- Confirm whether strobes use PWM dimming (GPIO 12) or hard on/off enable (GPIO 15).

## Related

[Flight Controller](03-flight-controller.md) · [Servos](05-servos.md) ·
[Sensors & Monitoring](07-sensors-monitoring.md) · [Lighting](08-lighting.md)

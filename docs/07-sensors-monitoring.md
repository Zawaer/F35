# Sensors & Monitoring

> **Current setup:** 2× Matek 150A Hall current sensors on the battery leads (→ F405 ADC),
> DS18B20 digital temperature sensors on a 1-Wire bus to the **Pico** (because all 4 F405 ADCs are
> used by battery monitoring), and ArduPilot blackbox logging to the FC's microSD. An INA219 is an
> optional add-on for precise servo-rail current data.

## Current sensing

| Sensor | On | To | Purpose |
|--------|----|----|---------|
| Matek 150A #1 | 5000 mAh main lead | F405 **ADC 2** | Total current from main battery (main EDF + BEC tap) |
| Matek 150A #2 | 2700 mAh lift lead | F405 **ADC 4** | Lift EDF current only (nothing else taps lift) |

Because only the lift EDF draws from the lift battery, sensor #2 reads pure lift-EDF current.
Subtracting known EDF datasheet current from sensor #1 yields a rough servo+FC+LED figure.
Current scale matches FC config **158 (INAV) / 64 A/V (ArduPilot)** — see [Flight Controller](03-flight-controller.md).

## Temperature sensing

### What to monitor (and what not to)

| Component | Method | Why |
|-----------|--------|-----|
| EDF motor | **Don't** — rely on ESC thermal protection | Spins ~50,000 RPM mid-airflow; any sensor is destroyed or unreliable |
| ESC 1 / ESC 2 | DS18B20 on case → Pico | Static, accessible; overheating → throttle cut → crash |
| Battery 1 | DS18B20 on surface → Pico | In-flight pack temp; warn >50 °C |
| Battery 2 | IR thermometer post-flight (or 4th DS18B20) | Easy enough without in-flight sensor |
| EDF exhaust air | Optional DS18B20 in duct exit | Rough proxy for motor temp |

The ESC's built-in thermal protection is the real safety net; the DS18B20s are for **logging and
trend data**, not protection.

### Why DS18B20 over NTC thermistors

| | DS18B20 | NTC thermistor |
|--|---------|----------------|
| Output | Digital (1-Wire) | Analog voltage (needs ADC) |
| Accuracy | ±0.5 °C | ±1–2 °C |
| Multiple on one wire | ✅ daisy-chain, unique 64-bit ID | ❌ |
| Range | −55 to +125 °C | varies |
| Cost | ~€0.22 ea | ~€0.03 ea |

DS18B20 wins because it needs **no ADC** (the F405 has none free) and all sensors share **one** Pico
GPIO. Confirmed compatible at the Pico's 3.3 V (DS18B20 runs 3.0–5.5 V).

### Wiring (1-Wire to Pico GPIO 26)

```
Pico 3.3V ──── 4.7kΩ ──┬──── DQ (pin 2) — all sensors
                        │
Pico GPIO 26 ───────────┘
Pico GND  ───────────────── GND (pin 1) — all sensors
Pico 3.3V ───────────────── VDD (pin 3) — all sensors
```

DS18B20 pinout (TO-92, flat face toward you): pin 1 = GND, pin 2 = DQ, pin 3 = VDD. Pull-up: 4.7kΩ
ideal; **5kΩ/5.1kΩ is fine** (1-Wire tolerates ±20%); a 10kΩ works in parasite mode but slower.

### Labelling the sensors

Each DS18B20 has a unique 64-bit address. Workflow before installing in the airframe:

1. Connect **one** sensor → scan → record its address → physically mark it (heat-shrink colour /
   paint dot).
2. Repeat for each sensor.
3. Connect all together and hardcode the addresses in the Pico script.
4. Install in the plane.

```python
import machine, onewire, ds18x20
ow = onewire.OneWire(machine.Pin(26))
ds = ds18x20.DS18X20(ow)
for s in ds.scan():
    print(s)   # e.g. b'\x28\xff\x64\x1e\x16\x05\x00\x1c'

# then hardcode:
ESC1 = b'\x28\xff\x64\x1e\x16\x05\x00\x1c'
ESC2 = b'\x28\xff\x64\x2a\x16\x05\x00\x1c'
BAT1 = b'\x28\xff\x64\x3b\x16\x05\x00\x1c'
```

See [`code/pico/temp_logger.py`](../code/pico/temp_logger.py).

## Optional — servo-rail current (INA219)

For precise per-flight servo current data, add an **INA219** I2C power monitor inline on the 6V
servo rail (~€2): logs voltage, current, and power. Wire it to the Pico (or FC) I2C bus. Useful for
confirming the marginal-servo-rail analysis (see [Power](02-power-system.md#servo-rail-headroom--the-marginal-case))
and deciding whether the 3A UBEC split is needed. Cheaper alternatives: ACS712 Hall module, or a
shunt + ADC.

## Blackbox logging (ArduPilot)

ArduPilot auto-logs to the FC microSD: per-servo PWM positions, battery V/A (from the Matek
sensors), throttle, flight-mode transitions, RC inputs vs outputs. Combined with Pico temperature
telemetry over UART, this gives a **complete per-flight picture** at zero extra hardware cost — e.g.
correlating a flaperon deflection with a battery voltage sag at a given timestamp.

### Other monitoring ideas (parked)

- RPM sensor on EDFs (~€2) — detect imbalance / health.
- Vibration sensor (MPU6050 over I2C, ~€2) — early EDF imbalance detection.

## Open questions / TODO

- Decide final DS18B20 count (3 vs 4) and whether to add the exhaust-air sensor.
- Decide whether to fit the INA219 in v1 or wait for a brownout signal.
- Confirm Pico→FC telemetry framing for temperatures.

## Related

[Power System](02-power-system.md) · [Flight Controller](03-flight-controller.md) ·
[Raspberry Pi Pico](04-raspberry-pi-pico.md) · [Wiring Diagrams](10-wiring-diagrams.md)

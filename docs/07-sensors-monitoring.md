# Sensors & Monitoring

> **Current setup:** **NTC 100K thermistors** read through a **CD74HC4067 16-channel analog
> multiplexer** into the Pico/RP2040 ADC (replaces the earlier DS18B20 plan). **3× ACS712 20A**
> Hall current sensors monitor the FC/servo rail and both roll-post EDFs. Main and lift EDF current
> are **not** monitored in v1 (89A/40A exceed the 20A sensors). ArduPilot blackbox logs to microSD.

## Current sensing (ACS712 20A ×3)

| Sensor | On | Current | Fits 20A? |
|--------|----|---------|-----------|
| #1 | FC + servo + LED rail (tap) | ~11.5A max | ✅ |
| #2 | Roll-post EDF L | ~11.2A | ✅ |
| #3 | Roll-post EDF R | ~11.2A | ✅ |

The 3-pack (€3.40) was chosen over a single (€2.32) — only €1.08 more for two extra channels.

> ⚠️ **ACS712 output needs scaling for the Pico ADC.** At 5 V the module outputs 2.5 V @0 A + ~100 mV/A,
> i.e. **0.5–4.5 V** across ±20 A — but the Pico ADC tops out at **3.3 V**, so above ~8 A it overranges
> and can stress the pin. Both the FC rail (~11.5 A) and roll-post EDFs (~11 A) exceed 8 A, so add a
> **resistor divider (~×0.66) on each OUT→ADC** (the chip needs ≥4.5 V, so you can't just run it at
> 3.3 V). See the [ACS712 card](../components/sensors.md). Calibrate the zero-offset in firmware.

**ACS712 divider recipe (×3, one per sensor):**

```
ACS712 OUT ── 10 kΩ ──┬── Pico ADC (GPIO 26/27/28)
                      │
                    20 kΩ
                      │
                     GND
```

Ratio = 20 / (10 + 20) = **0.667**, so the 4.5 V full-scale output maps to **3.0 V** — safely under
the 3.3 V ADC cap, with a little headroom. 0 A (2.5 V) reads as 1.67 V. Multiply the ADC reading by
**1.5** (= 1/0.667) in firmware to recover the true OUT voltage, then apply the 100 mV/A scale and the
calibrated zero-offset. Any 1:2 resistor pair works (10 k/20 k keeps current draw low); use 1% parts so
the ratio is predictable.

**Not monitored in v1:** main EDF (~89A) and lift EDF (~40A) both exceed the ACS712 20A range.
Monitoring those would need a higher-range Hall sensor (e.g. the Matek 150A sensors from the
earlier plan, or the PDB's own 90A/125A current detection). Decision: skip dedicated main/lift
current logging for v1; the PDB still reports pack voltage/current to the FC.

> ⚠️ This supersedes the earlier "Matek 150A on each battery lead → ADC2/ADC4" plan in
> [Flight Controller](03-flight-controller.md). If precise main/lift EDF current logging is wanted
> later, add a 150A-class sensor — the ACS712 cannot do it.

## Temperature sensing (NTC 100K + multiplexer)

### Approach

NTC 100K thermistors (MF52, B3950) form a voltage divider read through a **CD74HC4067 16-channel
multiplexer**, which the Pico/RP2040 reads on a single ADC pin by selecting channels. This replaces
the DS18B20 1-Wire approach — NTCs are cheaper, and the mux gives up to 16 channels from one ADC,
leaving room for many sensors plus other analog inputs.

**NTC divider recipe — single shared 47 kΩ (the "mux trick"):**

```
3.3V ── 47 kΩ ──┬── SIG → Pico ADC (GPIO 26/27/28)     ← ONE resistor, shared
                │
           CD74HC4067 (SIG pin)
                │
   selected channel ── NTC ── GND        (×16, one NTC per channel, no per-channel resistor)

S0..S3 ← Pico GPIO (channel select)
```

The top half of the divider (one **47 kΩ** resistor from 3.3 V) sits on the mux's common **SIG** line,
so it is shared by all 16 channels — whichever NTC is selected forms the bottom leg. That's one resistor
instead of sixteen. **47 kΩ** (vs the naive 10 kΩ) centres the divider's sensitive range over the
room-temp→100 °C span for a 100 kΩ NTC; 10 kΩ cramps the low (hot) end. Convert to °C via the beta
equation (NTC_R25 = 100 k, B = 3950). The mux's ~70 Ω on-resistance is in series with the selected NTC —
negligible vs 47 kΩ, but settle ~50 µs after switching channels before sampling.

- Buy ~30 NTCs (3× 10-pack) — ~16 used + spares. **Prefer the wired version** (10 cm leads
  pre-soldered, e.g. "MF52 NTC 100K with wire") over bare-bead parts to avoid soldering 16 tiny legs.
- 100K B3950 variant selected.

### What to monitor

| Component | Monitor? | Why |
|-----------|----------|-----|
| EDF motor | ❌ | ~50,000 RPM mid-airflow; rely on ESC thermal protection |
| ESC 1 / ESC 2 | ✅ NTC on case | Overheat → throttle cut → crash |
| Battery 1 (+2) | ✅ NTC on surface | In-flight pack temp; warn >50 °C |
| EDF exhaust air | optional NTC in duct | Rough motor-temp proxy |
| LED drivers / misc | optional | Spare mux channels available |

The ESC's built-in thermal protection remains the real safety net; NTC logging is for trend data.

### Why the switch from DS18B20

The DS18B20 (digital 1-Wire, ±0.5 °C, daisy-chainable) was the earlier plan. The build moved to
**NTC + CD74HC4067** because: NTCs are far cheaper in bulk, the multiplexer scales to 16 analog
channels (useful beyond temperature), and it keeps everything on the RP2040's ADC. DS18B20 remains
a valid fallback if analog noise on the mux proves troublesome.

## Blackbox logging (ArduPilot)

ArduPilot auto-logs to the FC **microSD** (card owned, fitting later): per-servo PWM, pack V/A,
throttle, flight-mode transitions, RC in vs out. Combined with the Pico's temperature + ACS712
telemetry over UART, this gives a complete per-flight picture.

### Other monitoring ideas (parked)

- RPM sensor on EDFs (~€2) — imbalance / health.
- Vibration sensor (MPU6050 over I2C, ~€2) — early EDF imbalance detection.

## Open questions / TODO

- MicroSD card: owned, fitting **later**. Divider resistors (one 47 kΩ for the shared NTC divider,
  10 kΩ for STS3032 half-duplex, 10 k/20 k ×3 for the ACS712 dividers): covered by the electronics
  kit / school stock — no purchase needed.
- Decide final NTC count and whether to add the exhaust-air sensor.
- Decide whether to add a 150A-class sensor for main/lift EDF current, or accept no logging there.
- Confirm CD74HC4067 wiring (S0–S3 select pins + SIG) and the Pico ADC pin used.

## Related

[Power System](02-power-system.md) · [Flight Controller](03-flight-controller.md) ·
[Raspberry Pi Pico](04-raspberry-pi-pico.md) · [Wiring Diagrams](10-wiring-diagrams.md) ·
[Bill of Materials](11-bill-of-materials.md)

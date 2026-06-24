# Sensors & Monitoring

> **Current setup:** **NTC 100K thermistors** read through a **CD74HC4067 16-channel analog
> multiplexer** into the Pico/RP2040 ADC. **3× ACS712 20A**
> Hall current sensors monitor **both roll-post EDFs** (the avionics-tap current is read by the PDB's
> own sensor). Main and lift EDF current
> are **not** monitored in v1 (89A/40A exceed the 20A sensors). ArduPilot blackbox logs to microSD.

## Current sensing (ACS712 20A ×3)

| Sensor | On | Current | Fits 20A? |
|--------|----|---------|-----------|
| #1 | Roll-post EDF L | ~11–15A | ✅ (÷0.66 divider) |
| #2 | Roll-post EDF R | ~11–15A | ✅ (÷0.66 divider) |
| #3 | spare | — | — |

The **avionics-tap current** (FC/BEC/servo/LED) is read by the **PDB's own current sensor**, so no
ACS712 is needed there — both used sensors go on the roll-post EDFs, one spare. (3-pack was €3.40.)

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

## Battery voltage monitoring

Voltage matters more than current here — you must land before a pack is over-discharged. Plan:

| Pack | How its voltage is sensed |
|------|---------------------------|
| **Lift** 5000 mAh | **via the PDB** — the avionics tap comes off this pack, so the FC reads its voltage directly |
| **Main** 5000 mAh | **resistor divider → Pico ADC** (isolated from the FC; **100 kΩ / 10 kΩ** from the kit → 25.2 V ≈ 2.3 V; or 100 k/15 k for fuller range) |
| **Roll-post** 850 mAh | **resistor divider → Pico ADC** (3S; **10 kΩ / 2 kΩ** from the kit → 12.6 V ≈ 2.1 V) |

**Wiring:** `Batt+ → R_top → [ADC pin] → R_bottom → GND`.

- **Where to tap `Batt+`:** the **exposed power-connector solder joint**, same as the 18 AWG avionics
  tap — the **main ESC's EC5 joint** for the main pack, a **LittleBee XT60H power-input pad** for the
  850 mAh. **Never tap the balance leads** — they're thin (~22 AWG) and reserved for charging/balancing;
  leave them alone. (The lift pack needs no divider — its voltage already comes through the PDB.)
- **Ground** is already common (each ESC's signal-ground lead ties its pack − to the FC/Pico ground),
  so `R_bottom` goes to any nearby system-ground point — no extra wire run back to the battery.
- Optional **0.1 µF (kit "104") from ADC→GND** to filter noise.
- **Firmware scale:** V_batt = V_adc × (R_top+R_bottom)/R_bottom → **×11** for 100 k/10 k, **×6** for
  10 k/2 k; calibrate against a multimeter (kit resistors are 5 %, so a one-time cal gets you accurate).
- The 100 k top draws only ~0.2 mA — fine in flight, just unplug for long storage.

ACS712 reads **current only** (no voltage). Main/lift EDF *current* stays unmonitored until a Matek
150A-class sensor is added.

## Temperature sensing (NTC 100K + multiplexer)

### Approach

NTC 100K thermistors (MF52, B3950) form a voltage divider read through a **CD74HC4067 16-channel
multiplexer**, which the Pico/RP2040 reads on a single ADC pin by selecting channels. NTCs are cheap,
and the mux gives up to 16 channels from one ADC, leaving room for many sensors plus other analog
inputs.

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

**Finalised plan: 13 NTC channels** (of the mux's 16 — 3 spare):

| # | Channel | Why |
|---|---------|-----|
| 1 | Main EDF ESC | safety-critical — overheat → throttle cut |
| 2 | Lift EDF ESC | safety-critical |
| 3 | Roll-post ESC L | |
| 4 | Roll-post ESC R | |
| 5 | Main LiPo pack (5000 mAh) | surface temp; warn >50–60 °C |
| 6 | Lift LiPo pack (5000 mAh) | |
| 7 | Roll-post LiPo (850 mAh) | |
| 8 | Main EDF housing (near motor) | motor-area heat-soak proxy |
| 9 | Lift EDF housing (near motor) | |
| 10 | Roll-post EDF housing L | enclosed in wingtip — limited airflow |
| 11 | Roll-post EDF housing R | |
| 12 | Servo-rail BEC | warms under flaperon load |
| 13 | 10W landing-light LED heatsink | |

Plus the **WeAct/Pico RP2040 self-monitors** via its **built-in on-chip temperature sensor** (read in
firmware — no NTC channel needed).

**Not monitored (deliberately):** EDF motors directly (spinning outrunners — the ESC thermal cutoff is
the real net); 3BSM nozzle (the main-EDF housing covers that zone); **the FC stack** (the F405 + IMU
already self-report temp); cockpit ST7789 screen + LED driver boards (run cool — the 10W LED *heatsink*
is the only hot LED part); nav lights; and — **skipped for now** — a dedicated **PDB-board**,
**bay-ambient**, or **EDF exhaust-air** sensor. **3 mux channels left spare.**

⚠️ ESC / heatsink beads must be **bonded to the case** (thermal paste + Kapton). **EDF housing:** the
main/lift **70 mm are outrunners** (the can spins) → bond the bead to the **static duct/mount**; the
roll-post **30 mm are inrunners** (static case) → the bead can sit on the **motor body** directly. NTC
range −40 to +110 °C suits all of these; all 13 ride one mux → one Pico ADC pin.

The ESC's built-in thermal protection remains the real safety net; NTC logging is for trend data.

## Blackbox logging (ArduPilot)

ArduPilot auto-logs to the FC **microSD** (card not owned yet — buy when needed): per-servo PWM, pack V/A,
throttle, flight-mode transitions, RC in vs out. Combined with the Pico's temperature + ACS712
telemetry over UART, this gives a complete per-flight picture.

### Other monitoring ideas (parked)

- RPM sensor on EDFs (~€2) — imbalance / health.
- Vibration sensor (MPU6050 over I2C, ~€2) — early EDF imbalance detection.

## Open questions / TODO

- MicroSD card: **not owned — buy when needed.** Divider resistors (one 47 kΩ for the shared NTC divider,
  10 kΩ for STS3032 half-duplex, 10 k/20 k ×3 for the ACS712 dividers): covered by the electronics
  kit / school stock — no purchase needed.
- Decide final NTC count and whether to add the exhaust-air sensor.
- Decide whether to add a 150A-class sensor for main/lift EDF current, or accept no logging there.
- Confirm CD74HC4067 wiring (S0–S3 select pins + SIG) and the Pico ADC pin used.

## Related

[Power System](02-power-system.md) · [Flight Controller](03-flight-controller.md) ·
[Raspberry Pi Pico](04-raspberry-pi-pico.md) · [Wiring Diagrams](10-wiring-diagrams.md) ·
[Bill of Materials](11-bill-of-materials.md)

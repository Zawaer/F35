# Wiring Diagrams

Consolidated power and signal wiring for the Phase 3 F-35B. Source detail lives in
[Power System](02-power-system.md), [Flight Controller](03-flight-controller.md),
[Raspberry Pi Pico](04-raspberry-pi-pico.md), and [Sensors & Monitoring](07-sensors-monitoring.md).

## Power distribution (dual battery)

```
[6S 5000mAh main]
   ├── 10AWG ──────────────► ESC 1 (Hobbywing 100A) ──► Main EDF (~89A)
   └── 18AWG tap (EC5 joint) ─► CoreWing PDB input
                                  ├── Flight BEC  5.2V/4A ─► F405 + ELRS + Pico
                                  ├── Servo BEC   6V/4A-14A ─► all servos + STS3032
                                  └── VTX/CAM BEC 12V/2A   ─► LED drivers

[6S 2700mAh lift]
   └── 10AWG ──────────────► ESC 2 (Hobbywing 100A) ──► Lift EDF (~89A)

Current sensors:
   Matek 150A #1 → on 5000mAh main lead → F405 ADC 2
   Matek 150A #2 → on 2700mAh lift lead → F405 ADC 4
```

No external buck converters or standalone BECs — the PDB supplies all three rails. If the servo
rail browns out, add a Hobbywing 3A UBEC fed from the battery tap and **split** the servo load
(never join two BEC outputs). See [Power — servo rail](02-power-system.md#servo-rail-headroom--the-marginal-case).

### Single-battery alternative (if ever consolidated)

```
[6S 5000mAh] ── AS150 ──┬── XT90 ── ESC 1 ── Main EDF
                        └── XT90 ── ESC 2 ── Lift EDF
```
AS150 on the battery side handles full ~180 A; each XT90 branch sees only ~90 A.

## Signal / control

```
ELRS RX ── CRSF ──► F405 USART6
F405 ◄── UART ──► Raspberry Pi Pico   (PWM commands out, temp telemetry in)

F405 PWM (11 ch): ESC1, ESC2, flaperons, stabilators, rudders, main flight surfaces, wingtip-motor ESCs
Pico PWM (≤16):   gear doors, lift-fan doors, canopy, exhaust nozzle, other secondary/cosmetic servos
STS3032 ×2 (3BSM): serial half-duplex bus (10kΩ resistor for UART half-duplex)
```

## Temperature + current sensing (→ Pico)

```
NTC 100K ──┬── CD74HC4067 channel (×16)        CD74HC4067 SIG → Pico ADC (GPIO 26)
10kΩ ──────┘   (divider: 3.3V─10kΩ─+─NTC─GND)  S0..S3        → Pico GPIO (channel select)

ACS712 20A #1 (FC/servo rail)  → Pico ADC
ACS712 20A #2/#3 (roll-post EDF L/R) → Pico ADC

NTC sensors: ESC1, ESC2, Battery1 (+ optional Battery2 / EDF exhaust)
```
(Earlier DS18B20 1-Wire plan superseded by NTC + multiplexer — see [Sensors](07-sensors-monitoring.md).)

## Cockpit display

```
1.47" ST7789 TFT ── permanent 0.5mm FFC ribbon ── ZIF FFC adapter (12P) ── 2.54mm pins ── Pico SPI
```

## LED system

```
PDB 12V ──► LED driver (700mA CC, PWM dim) ──► 3W LED
                ▲ PWM input
                └── Pico GPIO  (10=red nav, 11=green nav, 12=white strobe; 15=strobe enable alt)
```

## Pin / port reference (quick)

| F405 | Use |
|------|-----|
| USART6 | ELRS / CRSF |
| USART1 | Wireless board |
| One UART (e.g. UART4/5) | Pico link |
| ADC 1 / 2 | Battery 1 voltage / current (Matek #1) |
| ADC 3 / 4 | Battery 2 voltage / current (Matek #2) |
| PWM ×11 | ESCs + primary surfaces |

| Pico GPIO | Use |
|-----------|-----|
| 26 | DS18B20 1-Wire bus |
| 27 / 28 | spare ADC |
| 10 / 11 / 12 | LED PWM (red / green / strobe) |
| 15 | strobe enable (alt) |
| UART TX/RX | F405 link |

## Open questions / TODO

- Confirm exact F405 UART used for the Pico and the framing.
- Assign each secondary servo to a specific Pico GPIO and add it to this map.
- Add a proper schematic/drawing (e.g. exported from KiCad or a diagram tool) once finalised.

## Related

[Power System](02-power-system.md) · [Flight Controller](03-flight-controller.md) ·
[Raspberry Pi Pico](04-raspberry-pi-pico.md) · [Sensors & Monitoring](07-sensors-monitoring.md)

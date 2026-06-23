# Flight Controller — CoreWing F405 WING V2

> **Current setup:** CoreWing F405 WING V2 three-board stack (Wireless board + F405 FC + PDB PLUS),
> running **ArduPilot** (quadplane config for VTOL). ELRS receiver on **USART6 / CRSF**. Power and
> all BEC rails are handled by the PDB board, not the FC — see [Power System](02-power-system.md).

## The CoreWing stack

```
┌─────────────────────┐
│ Wireless board      │ ← WiFi / Bluetooth config (BLE / WiFi-AP / WiFi-STA)
├─────────────────────┤
│ F405 FC board       │ ← flight logic; receives clean 5.2V FROM the PDB
├─────────────────────┤
│ PDB PLUS board      │ ← power management; all three BECs live here
└─────────────────────┘
          ↑
     battery input
```

Clean separation: the **PDB does all power work** (battery input, current sense, three BEC rails);
the **FC just flies**. The FC does *not* handle motor power at all — that's the ESCs. It outputs
only signal (PWM/DSHOT) to the ESCs.

## F405 FC specifications

| Item | Spec |
|------|------|
| MCU | STM32F405, 168 MHz, 1 MB flash |
| IMU | ICM-42688-P (BMI270 optional) |
| Barometer | SPA06-003 |
| OSD | AT7456E |
| Blackbox | microSD (SDSC/SDHC, **not** SDXC), ≤32 GB, FAT16/FAT32. *INAV only reads ≤4 GB* |
| UARTs | 6 (USART1 wireless, USART2, USART3, UART4, UART5, USART6) |
| I2C | 1 port (compass / digital airspeed) |
| ADC | 4 ports (voltage, current, RSSI, analog airspeed) |
| PWM | 12 (11 motor/servo channels + 1 LED) |
| RX | ELRS/CRSF on **USART6**; reverse-SBUS circuit on **USART2-RX** |
| LEDs | Blue/Green/Red status (3.3V) |
| Firmware | INAV (factory) or **ArduPilot** (used here for VTOL) |

### Port assignments (planned)

| Port | Assigned to |
|------|-------------|
| USART1 | Wireless expansion board |
| USART6 | ELRS receiver (CRSF) |
| One UART (e.g. UART4/5) | **Raspberry Pi Pico** link — 16 extra PWM outputs + temp telemetry (see [Pico](04-raspberry-pi-pico.md)) |
| ADC 1 | Battery 1 voltage (from PDB divider) |
| ADC 2 | Battery 1 current (Matek 150A sensor #1, main lead) |
| ADC 3 | Battery 2 voltage |
| ADC 4 | Battery 2 current (Matek 150A sensor #2, lift lead) |

⚠️ All four ADC ports are consumed by battery monitoring — **no ADC is left on the F405 for
thermistors**. Temperature sensing is therefore offloaded to the Pico (see
[Sensors & Monitoring](07-sensors-monitoring.md)).

> **Current scale:** the PDB current sensor matches FC scale **158 in INAV** / **64 A/V in ArduPilot**.

## PDB PLUS board

| Item | Spec |
|------|------|
| Input voltage | 10–28 V (3–6S LiPo) |
| Voltage detection | to FC VBAT, divider 10K:100K |
| Current detection | 90 A continuous, 125 A peak |
| TVS surge suppression | included |
| Flight BEC | 5.2V ±0.1, 4A sustained, 5A peak → FC, ELRS, GPS, Pico |
| VTX/CAM BEC | 9V ±0.1, 2A sustained, 3A peak; switchable 5/9/12V → LED drivers |
| Servo BEC | 5V ±0.1, 4A sustained, **14A peak**; adjustable 5/6/7.2V → servos |

All three BECs run **simultaneously and independently** (like a PC PSU's 3.3/5/12V rails). See
[Power System — BEC rails](02-power-system.md#bec-rails-from-the-corewing-pdb) for the load budget
and the marginal servo-rail analysis.

## Wireless expansion board (PRO)

Long-press BOOT to cycle modes:

- **BLE** → CoreWing APP, SpeedyBee APP, INAV Configurator
- **WiFi-AP / WiFi-STA** → SpeedyBee, INAV Configurator, Mission Planner, QGroundControl
- Four RGB LEDs show real-time voltage ratio.

## PWM channel budget

The F405 provides 11 usable PWM outputs. The F-35B needs far more than that once VTOL servos,
flight surfaces, landing gear, and doors are counted — so the **Pico adds up to 16 extra PWM
outputs** over UART. Motor/ESC channels and primary flight surfaces stay on the FC; secondary and
cosmetic actuators move to the Pico. See [Servos](05-servos.md) and [Pico](04-raspberry-pi-pico.md).

## Open questions / TODO

- Finalise exact UART number for the Pico link and the CRSF/MAVLink-style framing used.
- Confirm ArduPilot quadplane motor/servo output mapping against the [Propulsion](06-propulsion.md)
  4-motor hover mix.

## Related

[Power System](02-power-system.md) · [Raspberry Pi Pico](04-raspberry-pi-pico.md) ·
[Servos](05-servos.md) · [Sensors & Monitoring](07-sensors-monitoring.md)

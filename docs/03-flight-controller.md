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

> **Barometer (SPA06-003) placement:** the onboard baro is enough — keep it where it is. A *buried*
> FC is actually good for a baro (away from EDF wash + ram air); the risks are **light** and
> **airflow**, not depth. Do: **cover the baro with a scrap of open-cell foam** (dish sponge / soft
> packing foam — *not* closed-cell styrofoam, which would trap a pressure pocket) to block light and
> damp downwash, and give the electronics bay **one small vent** to ambient (don't pressurize it or
> place it in the EDF intake/exhaust stream). A second external baro won't help. For better hover
> altitude hold the real upgrades are a **GPS** (EKF fusion — **planned for later**, after the
> airframe is validated; deferred for budget) and/or a **downward rangefinder/lidar** (e.g. TF-Luna /
> VL53L1X) — **both deferred for budget**, likely added after airframe validation — not another baro.

### Port assignments (planned)

| Port | Assigned to |
|------|-------------|
| USART1 | Wireless expansion board |
| USART6 | ELRS receiver (CRSF) |
| One UART | **RP2040 avionics board** (WeAct) — MAVLink: temp/current/voltage telemetry + LED/screen cmds |
| One UART | **RP2040 servo-bank board** (Pico) — MAVLink: secondary-servo PWM commands |
| One UART | **Feetech STS3032** serial half-duplex bus (3BSM nozzle) |
| ADC 1 | Battery 1 (main) voltage — from PDB divider |
| ADC 2 | Battery 2 (lift) voltage |
| ADC 3/4 | Spare / RSSI / airspeed |

> Six UARTs, four now spoken for (wireless, ELRS, two RP2040s) plus the STS3032 bus = five; one
> free. The **two RP2040 boards** (one couldn't fit the pin/ADC budget) each run **MAVLink** to the
> FC — see [Pico — why two boards](04-raspberry-pi-pico.md#why-two-boards-pin-budget). Note: their
> custom sensor values reach a MAVLink GCS and the blackbox easily, but **only ArduPilot's fixed CRSF
> schema reaches the Jumper T14** — custom temps go on the cockpit TFT, not the radio (see
> [Pico — communication](04-raspberry-pi-pico.md#communication-with-the-fc-and-onward-to-the-t14)).

> **Current sensing changed:** the earlier plan put Matek 150A sensors on each battery lead into
> ADC2/ADC4. The current plan uses **3× ACS712 20A** on the FC/servo rail + both roll-post EDFs
> (read via the Pico), and **does not log main/lift EDF current** in v1 (89A/40A exceed 20A). The
> PDB's own current detection still reports pack current to the FC. See
> [Sensors & Monitoring](07-sensors-monitoring.md).

Temperature sensing is offloaded to the Pico regardless — the F405 has no spare ADC for an array of
thermistors (NTC + multiplexer lives on the Pico).

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
| Servo BEC | 5V ±0.1, **7.5A sustained, 14A peak** (SCT2481, IC-verified); adjustable 5/6/7.2V → servos |

All three BECs run **simultaneously and independently** (like a PC PSU's 3.3/5/12V rails). See
[Power System — BEC rails](02-power-system.md#bec-rails-from-the-corewing-pdb) for the load budget
and the servo-rail analysis (servo BEC **verified at 7.5 A continuous** (SCT2481 IC, 2026-06-26)).

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
- **GPS + downward rangefinder/lidar:** both planned for **later** (after the airframe is validated) —
  GPS strongly benefits ArduPilot VTOL altitude/position hold, lidar gives precise low-altitude hover
  hold; both deferred now for budget.

## Related

[Power System](02-power-system.md) · [Raspberry Pi Pico](04-raspberry-pi-pico.md) ·
[Servos](05-servos.md) · [Sensors & Monitoring](07-sensors-monitoring.md)

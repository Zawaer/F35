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

### Port assignments

| Port | ArduPilot SERIAL | Assigned to | Key params |
|------|-----------------|-------------|------------|
| USART1 | SERIAL1 | Wireless expansion board | — |
| USART2 | SERIAL2 | **Feetech STS3032** half-duplex bus (3BSM nozzle) | `PROTOCOL=23, BAUD=1000, OPTIONS=4` |
| USART3 | SERIAL3 | **RP2040 avionics board** (WeAct) — MAVLink telemetry | `PROTOCOL=2, BAUD=57` |
| UART4  | SERIAL4 | **RP2040 servo-bank board** (Pico) — MAVLink PWM cmds | `PROTOCOL=2, BAUD=57` |
| UART5  | SERIAL5 | **HGLRC M100-5883 GPS** — GPS+Galileo+BDS, no GLONASS (settled pick, not purchased — deferred post-airframe) | `PROTOCOL=5 (GPS), BAUD=115, GPS_TYPE=2 (u-blox)` |
| USART6 | SERIAL6 | ELRS receiver (CRSF) | — |
| ADC 1 | — | Battery 1 (main) voltage — from PDB divider | — |
| ADC 2 | — | Battery 2 (lift) voltage | — |
| ADC 3/4 | — | Spare / RSSI / airspeed | — |

> USART2 has a hardware-inverted RX pad (reverse-SBUS circuit on the board). That's fine for the
> STS3032: half-duplex uses TX only (`OPTIONS=4` ties TX/RX internally), so the inverted RX pad is
> left unconnected and plays no role. All six UARTs now spoken for; UART5 is the GPS's home.
>
> ⚠️ **UART3 is already taken (WeAct avionics MAVLink) — don't wire GPS there.** Some generic online
> advice for this FC assumed 2 free UARTs ("UART3 free, UART4 free as backup") — that's wrong for
> this specific build; only UART5 is actually free, and putting GPS on UART3 would silently break
> the avionics telemetry link instead. Always check this table, not generic advice, before wiring a
> new UART peripheral.
>
> GPS compass wiring: the FC's single **I2C port** was already earmarked for "compass / digital
> airspeed" ([F405 FC specifications](#f405-fc-specifications)) — the HGLRC module's SDA/SCL go
> there directly, no conflict. If a digital airspeed sensor is added later, it shares the same I2C
> bus (different address, not a hardware conflict).

> The **two RP2040 boards** each run **MAVLink v2** to the FC — see
> [Pico — why two boards](04-raspberry-pi-pico.md#why-two-boards-pin-budget). Custom sensor values
> reach a MAVLink GCS and the blackbox easily, but **only ArduPilot's fixed CRSF schema reaches the
> Jumper T14** — custom temps go on the cockpit TFT, not the radio (see
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

## ArduPilot output mapping

The F405 provides 11 usable PWM outputs: 4 VTOL motor ESCs + 6 flight surfaces + 1 spare. Secondary
actuators (gear doors, lift-fan doors, vane box, nozzle, etc.) are on the Pico servo-bank board —
see [Servos](05-servos.md) and [Pico](04-raspberry-pi-pico.md).

All four VTOL motors use standard **50 Hz PWM** — the Hobbywing 100A V2 ESCs don't support DSHOT,
and mixing DSHOT (LittleBee 20A roll posts) with PWM on the same motor group complicates setup.

**Q_FRAME_TYPE = 0 (plus):** Motor 1 = front, Motor 2 = right, Motor 3 = rear, Motor 4 = left.

| Output | Connected to | ArduPilot `SERVOn_FUNCTION` | Notes |
|--------|-------------|-----------------------------|-------|
| SERVO1 | Lift fan ESC (Hobbywing 100A V2) | **33** (Motor 1 — front) | VTOL front lift |
| SERVO2 | Right roll-post ESC (FVT LittleBee 20A) | **34** (Motor 2 — right) | VTOL roll |
| SERVO3 | Main EDF ESC (Hobbywing 100A V2) | **35** (Motor 3 — rear) | VTOL rear lift + forward thrust via 3BSM |
| SERVO4 | Left roll-post ESC (FVT LittleBee 20A) | **36** (Motor 4 — left) | VTOL roll |
| SERVO5 | Flaperon L (NEEBRC 28g) | **24** (Flaperon) | Aileron + flap mixing |
| SERVO6 | Flaperon R (NEEBRC 28g) | **24** (Flaperon), reversed | |
| SERVO7 | Stabilator L (NEEBRC 21g) | **19** (Elevator) | |
| SERVO8 | Stabilator R (NEEBRC 21g) | **19** (Elevator), reversed | |
| SERVO9 | Rudder L (MG90S) | **21** (Rudder) | |
| SERVO10 | Rudder R (MG90S) | **21** (Rudder), reversed | |
| SERVO11 | — | spare | Reserved |

> **Servo reversal:** set `SERVOn_REVERSED = 1` on the reversed outputs (SERVO6, 8, 10) after bench
> rigging — direction depends on physical linkage.

> **Main EDF dual-use (SERVO3):** in VTOL, the 3BSM points down and Motor 3 provides rear lift. In
> cruise, the 3BSM rotates back and the same ESC becomes the forward thruster. ArduPilot tiltrotor
> params (`Q_TILT_MASK`, `Q_TILT_TYPE`) handle the throttle blend during transition, but since the
> 3BSM is STS3032-driven (Lua script) rather than a standard PWM tilt servo, the nozzle rotation is
> custom. **Bench-test this transition before any hover attempt.**

> **Roll-post mixing:** Motor 2 (right) and Motor 4 (left) provide roll via differential thrust in
> the wing plane. ArduPilot's quad mixer treats them as lift motors — tune `Q_MOT_THST_HOVER` and
> PID gains carefully; the roll posts contribute ~5% of total hover thrust, so their mixing weight
> will need manual adjustment.

## Open questions / TODO

- ✅ **Resolved: UART assignments locked** — USART2=STS3032, USART3=WeAct, UART4=Pico, UART5=GPS
  (HGLRC M100-5883, settled pick, not purchased).
- ✅ **Resolved: ArduPilot output mapping table complete** — SERVO1–10 assigned; see above.
- Bench-validate the SERVO3 (main EDF) tiltrotor transition and roll-post mixer weights before first hover.
- **GPS + downward rangefinder/lidar:** both planned for **later** (after the airframe is validated) —
  GPS strongly benefits ArduPilot VTOL altitude/position hold, lidar gives precise low-altitude hover
  hold; both deferred now for budget.

# Servos

> **Current assignment (Phase 2 F-35B):** flaperons on NEEBRC 12kg, stabilators on NEEBRC 9kg,
> rudders on MG90S, VTOL/cosmetic actuators on MG90S/SG90, 3BSM sections on Feetech **STS3032**
> smart servos. Landing gear uses **custom 3D-printed retracts** (no COTS retract units, no MG996R).
> All servos run off the PDB 6V rail (**7.5 A continuous**, IC-verified — ample, no UBEC split — see [Power](02-power-system.md)).

## Inventory on hand

| Servo | Qty | Torque | Weight | Gears |
|-------|-----|--------|--------|-------|
| SG90 | 12 | 1.8 kg·cm | 9 g | Plastic |
| MG90S | 7 | 2.2 kg·cm | 13 g | Metal |
| NEEBRC 21g | 2 | 9 kg·cm | 21 g | Metal |
| NEEBRC 28g | 2 | 12 kg·cm | 28 g | Metal |
| MG996R | 4 | ~15 kg·cm | 55 g | Metal |
| Feetech STS3032 | 1 used | 4.5 kg·cm | 20 g | Metal (built-in magnetic encoder) |
| NEEBRC M005 "2g" (plastic gear) | 4 | ~0.5 kg·cm | 2 g | Plastic — **max 4.2 V** |

MG996R are deliberately **avoided** in the final build — too heavy (55 g each).

> ⚠️ **Small servo voltage:** the 2g mini servos (**max 4.2 V**) will **burn out on the 6 V servo
> rail**. Power them through an **LM2596 buck set to 4.0 V** (safely below the 4.2 V max). One
> LM2596 (max 3 A; ~85–92% efficient) easily covers all 4 small servos (~1.4 A stall, ~0.2 A
> average). See [Power System](02-power-system.md). (The listing's "4.8–6 V" text is a mislabel —
> the 3.7–4.2 V spec is correct for a 2 g micro servo.)

## Final servo assignment

| Function | Servo | Torque | Weight | Status |
|----------|-------|--------|--------|--------|
| Flaperon L / R | NEEBRC 28g | 12 kg | 28 g | ✅ own |
| Stabilator L / R | NEEBRC 21g | 9 kg | 21 g | ✅ own |
| Rudder L / R | MG90S | 2.2 kg | 13 g | ✅ own |
| Gear retract ×2 (main) | custom 3D-printed retract (servo-driven) | — | — | 🛒 design |
| Nose retract | custom 3D-printed retract | — | — | 🛒 design |
| Gear doors ×2–3 | SG90 | 1.8 kg | 9 g | ✅ own |
| Nose steering | MG90S | 2.2 kg | 13 g | ✅ own |
| 3BSM nozzle rotate (all sections) | STS3032 ×1 | 4.5 kg | 20 g | ✅ — sections gear-linked |
| 3BSM yaw tilt (±15°) | MG90S (or SG90) | 2.2 kg | 13 g | ✅ own |
| Lift-fan doors ×2–4 | SG90 | 1.8 kg | 9 g | ✅ own |
| Lift-fan vane box | MG90S | 2.2 kg | 13 g | ✅ own |
| Roll post L / R* | MG90S | 2.2 kg | 13 g | ✅ own |
| Exhaust nozzle (opt) | SG90 | 1.8 kg | 9 g | ✅ own |
| Canopy | SG90 | 1.8 kg | 9 g | 🛒 v1 |

\* Roll-post *servos* only apply if vanes/doors are actuated; roll **thrust** now comes from small
wingtip motors, not bleed-air vanes — see [Propulsion — roll control](06-propulsion.md#roll-control).

**Door servos:** the 4 owned **NEEBRC M005 2g micro servos** cover the lightweight door actuators
instead of SG90 to save weight — but they run on the **4.0 V LM2596 rail**, not the 6 V servo rail
(see voltage warning above). SG90 remain the fallback for any doors not covered by the 4 units.

### MG90S count check

Rudder ×2 + nose steer ×1 + 3BSM yaw ×1 + vane box ×1 + roll posts ×2 = **7 MG90S**. Exactly the
7 on hand. ✅

## Torque sizing (why the choices are right)

Computed at ~100 km/h cruise (dynamic pressure q ≈ 473 Pa), with a 3× safety factor for gusts/snap:

| Surface | Required torque | Servo torque | Margin |
|---------|-----------------|--------------|--------|
| Flaperon | 2.6 kg·cm | 12 kg·cm | 4.6× ✅ |
| Stabilator | 1.26 kg·cm | 9 kg·cm | 7.1× ✅ |
| Rudder | 0.43 kg·cm | 2.2 kg·cm (MG90S) | 5× ✅ |

The flight surfaces look "oversized" on aerodynamic load alone, but that margin is correct: it
covers **landing impact loads**, high-speed maneuvers, and rapid VTOL-transition movements, and
servo failure on a VTOL is catastrophic. Rudder aerodynamic load is genuinely tiny, so MG90S
(rather than a heavier 9kg servo) is the right call and saves weight.

> **Internal actuation, scale appearance:** the real F-35B has no external pushrods. Use **internal
> pushrods** (Option B) — servo mounted in the wing/tail close to the surface, short 50–80 mm carbon
> pushrod hidden in the skin, exiting through a 2–3 mm slot at the hinge line. The NEEBRC 21g
> (13.2 × 29.6 mm) fits inside the F-35B wing-root thickness at 70mm EDF scale. Design servo bays
> and pushrod channels directly into the LW-PLA print in Fusion 360.

## 3BSM actuation — single STS3032 + gear-linked sections

The 3-bearing swivel module needs **continuous rotation with position feedback** (sections turn
well past 180°), which standard PWM servos can't do. **Decision: ONE Feetech STS3032** (serial-bus
smart servo, built-in magnetic encoder) drives the nozzle, with the **three 3BSM sections coupled
mechanically by gears running along each section's circumference** — so one motor rotates the whole
nozzle assembly down for hover. (A YouTube build demonstrated this works well.)

Yaw is separate: a **single MG90S (or SG90)** tilts the *whole* 3BSM ±~15° for yaw control — a
small range, so an ordinary 90°/180° servo is plenty (no continuous rotation needed there).

- STS3032 uses a **serial half-duplex bus** driven directly from the F405 over one UART.
- STS3032 current (datasheet): **6 mA idle · 150 mA no-load · 1200 mA stall** @ 6 V — stall is non-trivial; factor into servo-rail budget for worst-case transitions.
- This replaces the earlier "2× STS3032 for the sections" plan — gear-coupling means **one** smart
  servo suffices, saving ~€35 and a servo. The earlier rejected alternatives (continuous-360 SG90 +
  external AS5600 encoder) are moot.

### Wiring (half-duplex, software option)

Connect the STS3032 signal wire to the **TX pad** of a free F405 UART only (no RX connection needed
for a single servo). A **10 kΩ resistor** between TX and the bus line provides the required
pull-up. ArduPilot handles half-duplex internally — no hardware transceiver needed.

### ArduPilot parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| `SERIALx_PROTOCOL` | `23` | Smart Servo (native Feetech/Dynamixel driver) |
| `SERIALx_BAUD` | `1000` | 1 Mbps — STS3032 default |
| `SERIALx_OPTIONS` | `4` | Half-duplex mode (ties TX/RX internally) |

Replace `x` with the actual UART number once assigned (see [Flight Controller](03-flight-controller.md)).

### Lua script required for 3BSM mixing

The 3BSM nozzle must transition 0° (forward flight) → 90° down (hover) while also handling yaw
vectoring. This cannot be done with standard fixed-wing mixing. An ArduPilot **Lua script**
(`SCR_ENABLE = 1`) reads internal pitch/yaw output channels and translates them into Feetech
position packets (servo ID + target angle + checksum) sent over the UART.

> ⚠️ **Servo rail voltage: set to 6.0 V — not 7.2 V.** The STS3032 operating range is 4.8–6.0 V;
> 7.2 V will burn it out. The PDB servo BEC is adjustable — confirm the solder bridge is at 6 V
> before powering the bus. All other servos (MG90S, SG90, NEEBRC) are also rated to 6 V — no
> conflict.

## Landing gear actuation

**Decision: custom 3D-printed retracts**, servo-driven — *not* COTS electric retract units.
Reasons: COTS units are bulky/expensive and don't reproduce the F-35B's **90° wheel twist** during
retraction. The print-it-yourself route gives full control of the kinematics.

- **Over-centre lock:** at both end positions the linkage/drag-brace passes slightly past straight,
  so it self-locks and the servo is unloaded at the ends — no separate unlock servo needed. The
  servo only works during travel. Geometry is designed in Fusion 360.
- Retraction load is small (~0.18 kg·cm; wheel+strut ~45 g on a ~40 mm arm), so torque isn't the
  challenge — **reliable over-centre geometry under landing loads is.** ⚠️ This is a known-hard part.
- Main gear also needs the multi-axis **90° wheel twist** so the wheel lies flat in the bay.

## PWM routing

Primary flight surfaces + ESCs are on the **F405** (10 of 11 channels used, 1 spare). Secondary
actuators move to the **Raspberry Pi Pico**. The servo count (~14) is higher than the PWM channel
count because symmetric pairs share one channel:

| PWM channel | Drives | Servos |
|-------------|--------|--------|
| FC 1–2 | Flaperon L/R | NEEBRC 28g ×2 |
| FC 3–4 | Stabilator L/R | NEEBRC 21g ×2 |
| FC 5–6 | Rudder L/R | MG90S ×2 |
| FC 7 | Main EDF ESC | — |
| FC 8 | Lift EDF ESC | — |
| FC 9–10 | Roll-post EDF ESCs L/R | — |
| FC 11 | Spare | — |
| Pico 1 | Main gear retracts | custom retract ×2 (shared) |
| Pico 2 | Nose retract | custom retract ×1 |
| Pico 3 | Gear doors | SG90/M005 ×2–3 (shared) |
| Pico 4 | Nose steering | MG90S ×1 |
| Pico 5 | Lift-fan doors | SG90 ×2–4 (shared) |
| Pico 6 | Lift-fan vane box | MG90S ×1 |
| Pico 7 | 3BSM yaw | MG90S ×1 |
| Pico 8 | Exhaust nozzle (opt) | SG90 ×1 |
| Pico 9+ | Roll-post servos (if needed) | MG90S ×2 |

**Pico v1 channel count: 9 (canopy now included; optional nozzle + possible roll-post servos adds 1–3 more).** STS3032 nozzle rotate is on its own serial bus — not a PWM channel.

See [Flight Controller](03-flight-controller.md) and [Pico](04-raspberry-pi-pico.md).

## Open questions / TODO

- Finalise the custom retract linkage geometry and validate the over-centre lock under load. ⚠️
- Map each servo to a specific FC or Pico PWM output.
- ✅ **Resolved: STS3032 wiring and ArduPilot config** — TX-only + 10 kΩ, PROTOCOL=23, BAUD=1000, OPTIONS=4; Lua script for 3BSM mixing.
- Write the Lua script for 3BSM nozzle mixing (pitch/yaw → STS position packets).

## Related

[Power System](02-power-system.md) · [Flight Controller](03-flight-controller.md) ·
[Raspberry Pi Pico](04-raspberry-pi-pico.md) · [Propulsion](06-propulsion.md) ·
[Materials & Airframe](09-materials-airframe.md)

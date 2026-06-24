# Servos

> **Current assignment (Phase 3 F-35B):** flaperons on NEEBRC 12kg, stabilators on NEEBRC 9kg,
> rudders on MG90S, VTOL/cosmetic actuators on MG90S/SG90, 3BSM sections on Feetech **STS3032**
> smart servos. Landing gear uses **custom 3D-printed retracts** (no COTS retract units, no MG996R).
> All servos run off the PDB 6V rail (with a possible UBEC split — see [Power](02-power-system.md)).

## Inventory on hand

| Servo | Qty | Torque | Weight | Gears |
|-------|-----|--------|--------|-------|
| SG90 | 12 | 1.8 kg·cm | 9 g | Plastic |
| MG90S | 7 | 2.2 kg·cm | 13 g | Metal |
| NEEBRC 21g | 2 | 9 kg·cm | 21 g | Metal |
| NEEBRC 28g | 2 | 12 kg·cm | 28 g | Metal |
| MG996R | 4 | ~15 kg·cm | 55 g | Metal |
| Feetech STS3032 | 1 used | 4.5 kg·cm | 20 g | Metal (built-in magnetic encoder) |
| NEEBRC M005 (2g) | 4 | ~0.5 kg·cm | 2 g | Plastic — **max 4.2 V** |
| NEEBRC S002 (4.3g) | 2 | ~0.8 kg·cm | 4.3 g | Plastic — **max 5.0 V** |

MG996R are deliberately **avoided** in the final build — too heavy (55 g each).

> ⚠️ **Small servo voltage:** the M005 (2g, **max 4.2 V**) and S002 (4.3g, max 5.0 V) door servos
> will **burn out on the 6 V servo rail**. Power them through an **LM2596 buck set to 4.0 V** (safely
> below the M005's 4.2 V max). One LM2596 (max 3 A; ~85–92% efficient) easily covers all 6 small
> servos (~1.8 A stall, ~0.3 A average). See [Power System](02-power-system.md). (The M005 listing's
> "4.8–6 V" text is a mislabel — the 3.7–4.2 V spec is correct for a 2 g micro servo.)

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
| Canopy (opt) | SG90 | 1.8 kg | 9 g | ✅ own |

\* Roll-post *servos* only apply if vanes/doors are actuated; roll **thrust** now comes from small
wingtip motors, not bleed-air vanes — see [Propulsion — roll control](06-propulsion.md#roll-control).

**Door servos:** the 6 lightweight door actuators (gear doors, lift-fan doors) can use the new
**M005 2g / S002 4.3g** micro servos instead of SG90 to save weight — but these run on the **4.0 V
LM2596 rail**, not the 6 V servo rail (see the voltage warning above). SG90 remain an option on the
6 V rail.

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

- STS3032 uses a **serial half-duplex bus** — hence the 10kΩ resistor (UART half-duplex). Resistors
  are covered by the on-hand electronics kit / school stock.
- STS3032 current: ~100 mA idle, ~300 mA active — trivial for the PDB servo rail.
- This replaces the earlier "2× STS3032 for the sections" plan — gear-coupling means **one** smart
  servo suffices, saving ~€35 and a servo. The earlier rejected alternatives (continuous-360 SG90 +
  external AS5600 encoder) are moot.

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

Primary flight surfaces + ESCs are on the **F405** (11 PWM channels). Secondary/cosmetic actuators
(doors, canopy, nozzle, etc.) move to the **Raspberry Pi Pico** (up to 16 extra PWM over UART). See
[Flight Controller](03-flight-controller.md) and [Pico](04-raspberry-pi-pico.md).

## Open questions / TODO

- Finalise the custom retract linkage geometry and validate the over-centre lock under load. ⚠️
- Map each servo to a specific FC or Pico PWM output.
- Confirm STS3032 half-duplex bus wiring and IDs.

## Related

[Power System](02-power-system.md) · [Flight Controller](03-flight-controller.md) ·
[Raspberry Pi Pico](04-raspberry-pi-pico.md) · [Propulsion](06-propulsion.md) ·
[Materials & Airframe](09-materials-airframe.md)

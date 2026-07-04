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

**Speed uncertainty is accepted as covered by the 3× margin.** There's no way to know the real
top speed before the airframe flies, but hinge moment scales with V², so even a 30% error on the
100 km/h estimate (i.e. ~130 km/h) is only ~1.7× the computed torque — well inside the 3× factor
already applied. Not chasing an exact failure torque or planning a bench pull-test as a separate
validation step; the analytical margin is enough.

> **Internal actuation, scale appearance:** the real F-35B has no external pushrods. Use **internal
> pushrods** (Option B) — servo mounted in the wing/tail close to the surface, short 50–80 mm carbon
> pushrod hidden in the skin, exiting through a 2–3 mm slot at the hinge line. The NEEBRC 21g
> (13.2 × 29.6 mm) fits inside the F-35B wing-root thickness at 70mm EDF scale. Design servo bays
> and pushrod channels directly into the LW-PLA print in Fusion 360.

**Real-aircraft reference:** full-scale fighter jets use the same basic principle as Option B — a
linear actuator (hydraulic on older jets like the F-15's cable/pushrod-controlled valve actuators;
electro-hydraulic/EHA on newer designs, avoiding hydraulic lines routed through the wing) drives a
pushrod into a control horn, converting linear motion into the surface's rotation. Also worth
noting: the horn/actuator junction on the real aircraft isn't perfectly flush with the skin either —
it's covered by a small streamlined fairing/blister (visible on e.g. the 787's ailerons), so a tiny
cosmetic bump at the hinge-line slot would be more scale-accurate than forcing it perfectly flush.
See [How do linear actuators for flight controls work in fighter jets?](https://aviation.stackexchange.com/questions/78967/how-do-linear-actuators-for-flight-controls-work-in-fighter-jets)
(Aviation Stack Exchange).

### Internal-horn leverage — resolved

Worry: does hiding the horn inside the skin (vs. an external horn) cost leverage or max deflection
angle, since an internal horn is boxed in by the surface's actual thickness near the hinge line,
unlike an external horn which has unlimited room in open air?

**No — not inherently.** Torque multiplication and achievable deflection angle are both set by the
*ratio* of servo-arm radius to horn-arm radius, not the horn's absolute length:

```
pushrod travel   ≈ r_servo · Δθ_servo ≈ r_horn · Δθ_surface
torque to surface = T_servo · (r_horn / r_servo)
```

Shrink the horn to fit inside a thin flaperon/stabilator, and shrink the servo arm to match — the
deflection range and torque ratio are both preserved (a horn arm longer than the servo arm, easily
done at this scale, actually multiplies torque above the servo's rated spec). What genuinely gets
worse as the horn shrinks: linkage slop turns into a bigger *angular* error at the surface
(error ≈ backlash / r_horn), pushrod force rises for the same torque, and below roughly 8–10 mm
horn radius the 2 mm CF rod / M2 clevis hardware already in the BOM stops mounting reliably. That
hardware floor — not the physics — is the real constraint.

**Action once the Fusion model exists:** take a cross-section at the hinge line of each flight
surface and confirm ≥8–10 mm of internal depth with clearance for the horn to sweep ±25° without
touching either skin. Re-run the torque-sizing table above with the actual surface area/chord —
the current numbers are pre-CAD estimates and need recalculating once exact geometry is known.

### Direct-drive wire linkage ("RDS") — considered, deferred

An alternative to horn + pushrod + clevis: skip the horn entirely and mount a precisely bent wire
directly on the servo spline, with the bend engaging a tight-fitting pocket printed into the
control surface. Some sources online call this a "Rotary Drive System (RDS)" — that name isn't
established RC terminology as far as I can tell (treat write-ups using it with some skepticism,
they read as SEO/marketing content), but the mechanism itself is real and used in some scale foamy
jets. [Demonstration video](https://www.youtube.com/watch?v=X5JoxLxJ3tM).

- **Benefit:** one fewer joint than horn+pushrod+clevis, so marginally less backlash. Real, but
  small — the internal-pushrod plan above already has little slop to begin with.
- **Cost:** no post-build trim adjustability (a clevis can move to a different hole or thread
  in/out; a bent wire sized to one pocket geometry can't), it's tolerance-critical before the exact
  surface geometry is known (wire bend angle must match the pocket angle or you get binding/slop
  with no fine-tuning), and a worn pocket in a printed LW-PLA surface is harder to fix than
  swapping a $0.50 clevis.
- **Decision: not adopted for v1.** Keep the internal pushrod + horn (Option B above) as the
  default for all surfaces — it stays adjustable while tuning trim on first flights, and the build
  has bigger open risks (3BSM fit, hover/cruise CG) than the small backlash this would shave off.
  Revisit a direct-drive wire for one specific surface only if flight testing shows it has annoying
  play with the pushrod — a targeted upgrade, not the starting design.

**Why it's genuinely hard, if this is revisited later** (filtered from marketing-flavored source
material — some of its claims were overstated or wrong, corrected below):

- **Zero-slop pocket fit is the crux, not the wire bend.** A pocket even ~0.2 mm oversized lets the
  wire rattle under aero load — the same backlash-driven flutter risk already flagged above, except
  here there's no clevis to snug up afterward; the fit has to be right in the print.
- **The wire's bend point must land on the hinge axis**, or the crank-in-slot geometry binds partway
  through the sweep — this shows up as the servo drawing high current / stalling, not a clean
  deflection. Worth simulating the full sweep in Fusion before committing to a bend angle.
- **L/R bend-angle mismatch is real but not the big deal one source made it out to be** — it shows
  up as asymmetric neutral/authority between wings, correctable with ordinary per-channel
  trim/endpoints in ArduPilot. That uses a negligible slice of the servo's PWM resolution (thousands
  of steps), not a meaningful loss of it as claimed — just something to trim out, not a blocker.
- **Spline-to-wire coupling wear** — a printed plastic coupler under cyclic torque from a steel wire
  can wallow out over time. Same "hardware floor" concern already flagged above for small horns,
  relocated to the servo end.

**Mitigations if ever adopted:** a machined aluminium set-screw coupler at the servo spline (cheap,
removes the plastic-wear failure mode) and a thin PTFE or brass wear strip lining the printed
pocket, so the steel wire rides on a hard, low-friction surface instead of bare LW-PLA/PETG.

## 3BSM actuation — single STS3032 + gear-linked sections

The 3-bearing swivel module needs **continuous rotation with position feedback** (sections turn
well past 180°), which standard PWM servos can't do. **Decision: ONE Feetech STS3032** (serial-bus
smart servo, built-in magnetic encoder) drives the nozzle, with the **three 3BSM sections coupled
mechanically by gears running along each section's circumference** — so one motor rotates the whole
nozzle assembly down for hover. [LaLaRC built exactly this — a 3BSM driven by one servo with the
sections gear-linked together](https://www.youtube.com/watch?v=paESNOqIGYk) — direct evidence the
approach works.

![LaLaRC's single-servo, gear-linked 3BSM](img/3bsm/lalarc-single-servo-gear-linked.jpeg)
*One servo (top left) drives the whole nozzle via curved gear-toothed arcs running along each
section's edge — the same gear-coupling principle planned here, from the linked build.*

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

### Reference images — real F-35B gear geometry

![Nose gear left-front view](img/landing-gear-front/nose-gear-left-front.jpeg)
*Nose gear left-front: single small wheel, simple trailing-link strut, doors flush with fuselage underside.*

![Nose gear right-front view](img/landing-gear-front/nose-gear-right-front.jpeg)
*Nose gear right-front: shows the shimmy damper and pivot point geometry for the steering linkage.*

![Nose gear front view](img/landing-gear-front/nose-gear-front.jpeg)
*F-35B nose gear front view.*

![Main gear front view](img/landing-gear-rear/main-gear-front-01.jpeg)
*Main gear front view: single large wheel, compact vertical strut retracting inward into the fuselage.*

![Main gear side view](img/landing-gear-rear/main-gear-side.jpeg)
*Main gear side-on view — shows the full strut height, drag-brace geometry, and how the strut retracts inward into the fuselage bay.*

![Main gear shock strut close-up](img/landing-gear-rear/main-gear-strut-closeup.jpeg)
*Main gear oleo strut detail — shows the retraction pivot and drag-brace attachment points that the custom retract linkage needs to reproduce.*

## Door reference images

### Landing gear doors

![Nose gear doors open](img/doors/nose-gear-doors-open.jpeg)
*Nose gear doors open during retraction — two thin flat panels fold back flush with the fuselage belly. Shows the door geometry and hinge line relative to the strut.*

![Main gear doors on RC model](img/doors/main-gear-doors-rc-model.jpeg)
*RC model with main gear doors open — useful for understanding how the doors split and the bay geometry at scale.*

### Lift fan and VTOL doors

![Lift fan inlet door open](img/doors/lift-fan-inlet-door-open.jpeg)
*Lift fan inlet door fully open — single large clamshell panel hinged at the forward edge, revealing the full circular rotor face. The aft auxiliary inlet is also visible below.*

![Lift fan exhaust doors open](img/doors/lift-fan-exhaust-doors-open.jpeg)
*Lift fan exhaust doors open from below during hover — multiple small panels fold out around the exhaust aperture between the lift fan and the main gear bay.*

![3BSM nozzle in hover position](img/doors/3bsm-nozzle-hover-deployed.jpeg)
*3BSM nozzle deployed for hover — three-section bearing structure rotated ~90° down, serrated nozzle pointing directly downward. The surrounding door petals and the roll-post openings are visible.*

![Roll post exhaust opening](img/doors/roll-post-exhaust-opening.jpeg)
*Roll post exhaust opening from below — small rectangular aperture in the wing-fuselage junction with the door open, showing the internal actuator linkage.*

### Other doors

![Canopy open](img/doors/canopy-open.jpeg)
*Canopy open — single-piece clamshell hinged at the rear, tilting forward and up. Note the hinge mechanism and the lack of a centre frame across the whole transparency.*

![Aux air intake door open](img/doors/aux-air-intake-door-open.jpeg)
*Auxiliary air intake door open on the fuselage spine — rectangular panel that pops up to supply additional intake airflow at low speed and during VTOL.*

![Aerial refueling door open](img/doors/aerial-refueling-door-open.jpeg)
*Aerial refueling receptacle door open on the left spine forward of the cockpit, with the probe engaged on a tanker drogue. Shows the door size and location relative to the canopy.*

![Weapons bay doors open](img/doors/weapons-bay-doors-open.jpeg)
*Weapons bay doors open in flight from below-rear — both bays open simultaneously, missiles on launchers visible inside. Illustrates the door span and hinge geometry.*

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

**Why FC surfaces get separate channels even though they're symmetric pairs:** the FC needs independent control over each side for differential mixing (elevon, flaperon), surface reversal, and trim. Pico actuators (doors, retracts) that always move identically share one channel via Y-splitter cable.

See [Flight Controller](03-flight-controller.md) and [Pico](04-raspberry-pi-pico.md).

## Open questions / TODO

- Finalise the custom retract linkage geometry and validate the over-centre lock under load. ⚠️
- Map each servo to a specific FC or Pico PWM output.
- ✅ **Resolved: STS3032 wiring and ArduPilot config** — TX-only + 10 kΩ, PROTOCOL=23, BAUD=1000, OPTIONS=4; Lua script for 3BSM mixing.
- Write the Lua script for 3BSM nozzle mixing (pitch/yaw → STS position packets).

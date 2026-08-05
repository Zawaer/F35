# 3BSM — swivel kinematics, geometry & the V1/V2 roadmap

> **Locked plan:** **V1** = one motor, standard circular gears, **23.75° wedge cuts**, 80 mm joint
> diameter, full mechanical rotation lands on a **95° max downward vector** with perfect
> left-right symmetry at that end-stop. Braking margin beyond ~90° comes from **pitching the whole
> airframe nose-up in software**, not from over-rotating the nozzle. **V2** (funds permitting) =
> **3 independent servos**, one per bearing, fully software-controlled trajectory — removes every
> compromise below at the cost of 2 extra motors, wiring, and control complexity.

This doc captures the CAD/kinematics reasoning behind the 3BSM (three-bearing swivel module) worked
out in Fusion 360 — why the joints are built the way they are, the geometric traps that don't show
up until you actually animate the mechanism, and why V1 settles for a single-motor, gear-linked
design instead of the real F-35B's fully independent bearings. For servo/electrical specifics see
[Servos — 3BSM actuation](05-servos.md#3bsm-actuation--single-sts3032--gear-linked-sections) and
[Propulsion — 3BSM](06-propulsion.md#3bsm--three-bearing-swivel-module); for bearing/ball-race
hardware see [Materials — Bearings & 3BSM rotation](09-materials-airframe.md#bearings--3bsm-rotation).

⚠️ **Provenance note:** most of the reasoning below came out of an AI-assisted research/design
chat (Google AI Mode), cross-checked against the user's own live Fusion 360 testing wherever a
concrete number is claimed. Where the AI's citations turned out to be fabricated on inspection,
that's flagged explicitly below — treat the *geometry and mechanism* conclusions (independently
reproduced by the user's own Motion Study testing) as solid, and any specific "the real F-35B
document/paper says X" quote as unverified unless it's linked to an actual source.

## 1. Why joints alone aren't enough — the grounding problem

A naive build grounds the bottom segment and lets the motion cascade upward through two revolute
joints. That fails for two independent reasons:

1. **Cross-talk when driving from the top.** With a plain joint chain (Base → Joint1 → Middle →
   Joint2 → Top), grabbing the *top* segment back-drives Joint1 too, because Fusion's solver
   resolves force through the whole chain — dragging the top segment visibly (and wrongly) spins
   the middle one too. (Fixes exist — ground the middle temporarily, use *Drive Joint*, or lock a
   joint — but none of them matter once the mechanism is motor-driven rather than hand-dragged in
   the CAD viewport.)
2. **The bottom segment must itself rotate relative to the airframe** (real F-35B nozzles yaw the
   whole assembly), so it can't be the fixed reference either.

**Fix: add a 4th, hidden "Engine Frame" component and ground *that*, not any of the three visible
nozzle sections.** Joint chain becomes:

```
Grounded Engine Frame → Joint 1 → Section 1 (lowest) → Joint 2 → Section 2 (middle) → Joint 3 → Section 3 (top)
```

All three visible sections are now free to rotate relative to the airframe — none of them is
directly locked in place.

## 2. Motion Link math — why 1:1 and 1:2 both fail

Fusion's **Motion Link** tool forces one joint's rotation to follow another's, at a ratio set by
two "degree" fields (e.g. `360°` : `-360°` = 1:1 reversed).

**The naive guess (1 : -1, i.e. `360 / -360`) does not work.** Because Section 2 (the middle) is
riding on top of a platform (Section 1) that is *already spinning* relative to the grounded frame,
linking Joint 2 to Joint 1 at a flat 1:1 reversed ratio leaves a leftover rotation — the top
section ends up twisting off to the side instead of staying parallel to the bottom.

**Confirmed-working ratio (found by iterative testing in Fusion, not derived from a formula
first):**

| Motion Link | Joints tied | Degree fields | Effective ratio |
|---|---|---|---|
| A | Joint 1 ↔ Joint 2 | `360°` : `-720°` | Joint 2 = **−2× Joint 1** |
| B | Joint 2 ↔ Joint 3 | `360°` : `-360°` | Joint 3 = **−1× Joint 2** (= +2× Joint 1) |

Net effect of driving Joint 1 by angle *X*: Section 1 and Section 3 both rotate **+X** (same
direction, same magnitude — they stay parallel), while Section 2 (middle) rotates **−2X** — double
speed, opposite direction. This 1 : −2 : 2 ratio is what a single-motor gear train has to
physically reproduce (see [Servos — gear-linked
sections](05-servos.md#3bsm-actuation--single-sts3032--gear-linked-sections); LaLaRC's build uses
the same one-motor, gear-coupled-sections principle).

**Why the 2:1 middle ratio, intuitively:** the middle segment sits on a moving platform (Section 1
is already turning), so its rotation has to "cancel out" that platform motion *and then* add its
own opposite twist — which is exactly a 2× overdrive in the opposite direction.

## 3. Wedge cut angle — the "4× angle" rule, and how it moved

Each joint face is cut at an angle relative to the flat horizontal cross-section of the tube (not
the vertical wall — that's a common measurement mix-up that silently doubles/complements the real
angle if you dimension from the wrong reference; always double-check this in the sketch before
trusting any of the numbers below).

**The rule:** for a symmetric 3-bearing swivel with the 1 : −2 : 2 motion-link ratio above, a full
**180° relative rotation** at each bearing gives a total downward deflection of **4× the wedge cut
angle**, and — critically — **that 180°-rotation point is the only position where the assembly is
perfectly left-right symmetric** (front-to-back too). Any partial rotation is geometrically
asymmetric to some degree; see §5.

| Wedge angle | Deflection at full 180° rotation | Status |
|---|---|---|
| 30° | 120° | ❌ first guess — overshoots, had to stop rotation early → broke symmetry (this is what led to discovering the symmetry problem in §5) |
| 26.25° | 105° | Superseded — matched the real F-35B's ~95–105° braking-margin target, but re-opened the 90°-hover asymmetry problem below |
| 22.5° | 90° | Superseded — perfectly symmetric at a flat 90° hover, but zero margin for braking |
| **23.75°** | **95°** | **✅ locked for V1** — see §5 |

Outer diameter for all three joint circles: **80 mm** (constant across the wedge-angle changes
above — diameter doesn't affect the 4× rule, only how visually aggressive the ellipse/loft
transition looks).

## 4. The "banana path" — an unavoidable transition artifact, not a bug

Watching the Motion Study play through the transition (not sitting at either end-stop), the nozzle
tip does **not** travel in a straight line (`|`) from cruise to hover — it sweeps out to one side
in a shallow crescent (`(`) before snapping back to center at the end position.

This is inherent 3D geometry, not a Fusion glitch: because the joint axes are tilted (not
perpendicular to the rotation direction), the vector math only cancels the lateral component at
the two end-stops (0° and full rotation); partway through, the lateral terms haven't summed to
zero yet, so the whole assembly's exit vector is dragged sideways mid-transition.

**Real-world handling:** the real F-35B counters the resulting yaw/roll disturbance during
transition with **roll posts** (bleed-air ducts in the wings) plus non-uniform bearing speeds. This
project already rejected bleed-air roll posts in favor of **dedicated small wingtip motors** for a
different reason (RC-scale bleed air is far too weak — see [Propulsion — roll
control](06-propulsion.md#roll-control)); those same wingtip motors are what will absorb any
transition-induced roll/yaw disturbance here too, exactly as ArduPilot's quadplane mixing already
plans for.

⚠️ **Unverified citation, flagged during the original chat:** a specific "Kinematic Modeling and
Testing of 3-Bearing Swivel Duct Nozzle" journal quote and a Lockheed Martin document quote were
given as sources for the banana-path phenomenon. The *geometric behavior itself* is consistent with
what was independently observed in the live Motion Study (so trust that part), but those specific
quoted sentences were not verified against a real source and should not be repeated as confirmed
fact without checking the paper/PDF directly.

## 5. The 90°-hover asymmetry problem (why 95°, not 90° or 105°)

Perfect left-right symmetry only happens at **0°** (straight, cruise) and at the **full 180°
relative rotation** (the mechanical end-stop). A static hover sitting at exactly 90° down is,
depending on the wedge angle chosen, *not* at that end-stop — so the nozzle tip points slightly off
to one side even when "centered."

This was discovered directly: with 26.25° cuts (105° at full rotation), reaching a 90° vector
requires stopping the bearings at ~154° instead of the full 180°, and the resulting geometry is
visibly asymmetric front-to-back.

**Two resolution paths were evaluated:**

- **Independent per-joint drive (real F-35B approach):** with 3 separate motors you're not bound
  to a fixed gear ratio at all — the flight computer can command whatever non-uniform combination
  of bearing angles produces a perfectly straight, symmetric vector at *any* deflection angle, not
  just the two end-stops. This is only viable once each bearing has its own motor — see V2 (§7).
- **Design the end-stop to *be* the hover position (V1's approach):** if the wedge angle is chosen
  so the full 180°-rotation end-stop lands exactly where the nozzle should sit for a static hover,
  the perfectly-symmetric point and the hover point are the same point — no compromise needed, at
  the cost of losing any extra margin past that angle.

**Why 95°, specifically, and not a flat 90°:** a flat 90° end-stop gives perfect symmetry exactly
at hover, but during flight the flight controller is constantly making small, rapid corrective
nozzle movements around that hover point (never sitting dead-still) — and it also loses any margin
to nose the exhaust slightly forward for braking during transition from forward flight to hover.
Landing on **95°** as the end-stop (instead of the real jet's ~105°) means:

- The mechanical end-stop (perfectly symmetric point) sits just 5° past the nominal 90° hover
  target, so the flight controller's normal small corrective movements around 90° only ever pick up
  a tiny, easily-gyro-correctable asymmetry — not the large one that a 105°-designed end-stop would
  produce at the 90° mark.
- There's still a small amount of forward-pointing margin available for braking without needing a
  separate high-deflection mode.
- Wedge angle for a 95° end-stop: **23.75°** (95° ÷ 4, per the rule in §3).

**Braking beyond that:** rather than engineering extra nozzle-angle margin (which reopens the
symmetry trade-off), V1 brakes by having the flight controller **pitch the whole airframe nose-up
in software** — a 90°-locked hover nozzle plus a 10–15° nose-up aircraft pitch achieves the same
net rearward-pointing thrust component a 105° nozzle would, without any extra mechanical
complexity. This was the deciding factor that let V1 stay at a single motor (§7) instead of forcing
a 3-motor upgrade just to solve the braking-margin problem.

⚠️ This whole section (89°/90°/95°/105° tradeoff) is geometric reasoning worked through
interactively during CAD testing, not sourced from a published F-35B spec — the real jet's exact
production wedge angles and control logic are not public. Treat "95°" as this project's own
considered design point, not a claimed match to the real aircraft's internals.

## 6. The ellipse/hourglass wall problem

A straight cylindrical tube cut at a bevel angle produces an **elliptical** face at the cut (a
measured example: a 70 mm circle cut at 30° gives an ellipse with an ~80.8 mm major axis and
~237 mm perimeter, vs. the original circle's 219.9 mm — confirmed by direct measurement, not just
formula).

Two ways to connect two of these elliptical joint faces into a smooth tube wall were evaluated:

- **Plain loft between the circles (no guide rails) → hourglass shape.** Fusion's loft takes the
  shortest mathematical path between the stretched-ellipse cut faces, which pulls the tube wall
  inward at the middle section — a visible waist/pinch when the nozzle is straight (cruise). The
  pinch relaxes back to round when the nozzle is fully deflected.
- **Loft with straight vertical guide rails → straight tube when cruising, bulge when hovering.**
  Projecting the true outer diameter as straight guide rails into the loft forces a uniform
  cylinder wall in the straight (cruise) position; the trade-off shows up only when the nozzle
  bends — the "extra" material that was stretched straight for cruise has nowhere to go but
  outward, so the middle section bulges slightly on the sides at full deflection. No gaps or holes
  form either way — this only changes where the wall bulges, not whether it stays sealed.

**Aerodynamic reasoning behind each option:** a pinch (hourglass) acts as a flow bottleneck —
compression through a restriction always costs more (turbulence, pressure drop, heat) than the
mild expansion a bulge causes. Real turbofan installations generally protect cruise/high-speed
efficiency over the ~1% of flight time spent transitioning or hovering, which argues for the
guide-rail option if the two states must trade off at all.

**Decision for V1: no guide rails — accept the hourglass pinch, matching the reference build.**
Eric Maglio's F-35B 3BSM (referenced build for this project — [YouTube build
guide](https://www.youtube.com/watch?v=paESNOqIGYk), also see [Servos → 3BSM
actuation](05-servos.md#3bsm-actuation--single-sts3032--gear-linked-sections)) uses the plain
hourglass approach successfully at RC scale, where duct velocities/pressures are nowhere near
real-jet severity, so the theoretical cruise-efficiency cost of a mild pinch is expected to be
negligible in practice. **Guide rails are kept as a documented fallback** — if ground/bench testing
shows the hourglass pinch meaningfully chokes the main EDF's airflow (see [Propulsion — main EDF
intake sizing](06-propulsion.md#main-edf-intake-sizing--fan-swept-area-fsa) for how airflow
restriction shows up as current draw / heat, the same failure mode), switch that specific loft
feature to guide rails without needing to touch the rest of the model.

## 7. V1 vs V2 — the motor-count decision

**Constraint:** budget and weight rule out 3 independent servo motors for the initial build — V1 is
a **single-motor** design (see [Servos — 3BSM
actuation](05-servos.md#3bsm-actuation--single-sts3032--gear-linked-sections) for the STS3032 +
gear-linked-sections implementation already locked in for this reason, independent of the angle
math above).

A single motor forces the three sections through the **fixed** 1 : −2 : 2 gear ratio derived in
§2 — there is no way to independently command one bearing without the others, which is the root
cause of the 90°-hover asymmetry problem in §5.

**Two alternatives were evaluated for removing that constraint later:**

| Option | Removes the asymmetry at any angle? | Practical for 3D-printed R/C? |
|---|---|---|
| **3 independent motors** (V2) | ✅ yes — software can command any per-bearing combination, at any deflection angle, not just the two end-stops | ✅ standard approach — this is what the real F-35B does, and what the reference builder (Eric Maglio / Lofted Aero) actually uses in the real (not fabricated) build history |
| **Non-circular (elliptical/oval) gears on one motor** | Partially — could be profiled to force symmetry at one specific angle | ❌ rejected — see below |

**Why non-circular gears were rejected**, despite being an appealing "just reshape the gears, no
extra wiring" idea:

- **Center-to-center distance problem.** Standard circular gears keep their shaft centers at a
  fixed distance while meshing. Non-circular (oval) gears change effective radius continuously as
  they spin, which means the gear shafts would need to physically move closer/further apart during
  rotation to stay meshed — but the 3BSM's bearing shafts are rigidly fixed by the joint geometry,
  so an oval gear pair would bind/jam rather than smoothly mesh.
- **Friction/stall risk.** Non-uniform tooth pitch concentrates friction at the tightest point in
  the profile; a single hobby servo is far more likely to stall there under EDF thrust load than a
  uniform circular gear train would be.
- **Manufacturing tolerance.** Standard hobby FDM printing tolerances are not tight enough to hold
  a custom variable-pitch tooth profile without slipping — this is a precision-manufacturing
  problem, not just a modeling one.
- It would also only be tuned for **one specific deflection angle** (e.g. exactly 90°) — the
  general independent-control benefit of 3 real motors (any angle, any time, changeable in
  software) isn't something a fixed mechanical gear profile can reproduce.

**Locked plan:**

- **V1 (now):** single Feetech STS3032, 3 sections gear-linked circumferentially (1 : −2 : 2 ratio
  baked into the gear teeth), 23.75° wedge cuts, 95° max deflection at the fully-symmetric end-stop,
  hourglass (no guide-rail) loft walls, braking handled by airframe pitch in software. Accepts a
  small, gyro-correctable lateral offset during partial-deflection transitions and during the
  flight controller's normal small corrective movements around the 90° hover point.
- **V2 (future, funds permitting):** upgrade to **3 independent servos**, one per bearing, each
  addressed separately over the same type of serial bus already used for the V1 STS3032. Removes
  the fixed-ratio constraint entirely — the flight controller can compute whatever per-bearing
  angle combination keeps the exhaust vector perfectly on-axis at *any* commanded deflection angle,
  including all the in-between positions (e.g. a 45° short-takeoff vector) that V1 can only pass
  through briefly and imprecisely. No mechanical redesign of the sections themselves is implied —
  just replacing the gear-linkage with 3 independent drives and updating the mixing logic.

## Open questions / TODO

- ⚠️ Confirm on the bench whether the V1 hourglass pinch actually restricts main-EDF airflow
  enough to matter (see [Propulsion — main EDF intake
  sizing](06-propulsion.md#main-edf-intake-sizing--fan-swept-area-fsa)) before deciding whether the
  guide-rail fallback (§6) is worth implementing.
- Model and validate the 1 : −2 : 2 gear-tooth ratio physically (tooth counts / arc coverage) once
  the outer gear-ring flanges are drawn — see [Propulsion — 3BSM cable/gear
  notes](06-propulsion.md#3bsm--three-bearing-swivel-module).
- Confirm in Fusion, on the actual current sketch, that the 23.75° wedge dimension is measured from
  the flat horizontal cross-section, not the vertical centerline (see §3 — this is an easy
  measurement mistake that silently breaks all of the above).
- If/when V2 is funded: revisit whether the 80 mm joint diameter and section proportions still make
  sense once 3 independent servos replace the gear-linked drivetrain (removing the gears may free
  up space for a different diameter).

## Related

[Servos — 3BSM actuation](05-servos.md#3bsm-actuation--single-sts3032--gear-linked-sections) ·
[Propulsion — 3BSM](06-propulsion.md#3bsm--three-bearing-swivel-module) ·
[Materials — Bearings & 3BSM rotation](09-materials-airframe.md#bearings--3bsm-rotation) ·
[Decision log](../journal/decisions.md)

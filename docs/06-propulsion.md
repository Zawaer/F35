# Propulsion

> **Phase 3 F-35B:** 2× QX-Motor **70mm EDF** (6S) — one **main** (rear, thrust-vectored by the
> 3BSM) and one **lift** (front), each on its own Hobbywing 100A V2 ESC. Hover is flown as an
> **ArduPilot 4-motor quadcopter**: main EDF + lift fan + **2× small wingtip motors** for roll.
> **Phase 1 trainer:** A2212 2200KV + 3S + 30–40A ESC + 5×4–6×4 prop. The two systems are entirely
> separate.

## Phase 1 — trainer prop plane

| Item | Spec |
|------|------|
| Motor | A2212 2200KV |
| Battery | 3S LiPo, 1500–2200 mAh |
| ESC | 30–40 A |
| Props | 5×4 to 6×4 |
| Airframe | Foamboard |

Purpose: learn to fly and validate the basic FC + receiver setup before EDF/VTOL complexity.

## Phase 3 — EDF propulsion

| Item | Spec |
|------|------|
| Fans | 2× QX-Motor 70mm EDF |
| Motor RPM | ~50,000 RPM |
| Thrust | ~3300 g each |
| Current draw | ~72–89 A normal (peaks ~100 A) |
| Battery | 6S (main 5000 mAh, lift 2700 mAh) |
| ESC | 2× Hobbywing 100A V2, individual (not 4-in-1) |

The EDFs already produce a convincing jet sound across the throttle range (rising whine on spool-up,
turbine hum at idle, jet scream at full throttle, descending whine on spool-down). See
[Power System](02-power-system.md) for battery/ESC/connector detail.

## VTOL / hover control architecture

Hover is controlled as a **4-motor quadcopter** in ArduPilot — chosen after evaluating bleed-air
roll posts and finding them unworkable at RC scale (below):

| Hover "motor" | Hardware | Function |
|---------------|----------|----------|
| 1 | Main rear EDF | Lift + pitch, **thrust-vectored via the 3BSM** |
| 2 | Front lift fan | Lift (front) |
| 3 | Left wingtip micro motor | Roll |
| 4 | Right wingtip micro motor | Roll |

ESC throttle response is instant, vs slow servo-actuated vanes — which is why direct motors win for
roll. Yaw in hover comes from the 3BSM yaw element; pitch from the lift-fan/main-EDF balance.

### 3BSM — three-bearing swivel module

The main EDF exhausts through a **3-bearing swivel module** that vectors thrust from
horizontal (cruise) to downward (hover), mimicking the real F-35B nozzle.

- Driven by **2× Feetech STS3032** smart servos (continuous rotation + built-in encoder) for the
  rotating sections, plus an **MG90S** for ±20° yaw. See [Servos](05-servos.md#3bsm-smart-servos-sts3032).
- Needs **bearings at each section junction** — thin-section ball bearings sized to fit inside the
  70mm duct. **6805ZZ (37×25×7 mm)** is the sweet spot; buy ~10 (need 6 for two per junction + spares).
  **Buy bearings before modeling** the 3BSM in Fusion — design the seats around real bearing dims.
- ⚠️ Reliability of the 3BSM under exhaust pressure is a key open risk — test thoroughly on the
  ground before any hover attempt. See [Materials & Airframe](09-materials-airframe.md) for bearings.

### Lift fan

Front-mounted EDF providing ~3300 g lift at peak, with actuated **lift-fan doors** (SG90) and a
**variable-area vane box** (MG90S) to modulate/redirect thrust. Balances against the rear 3BSM for
pitch in hover — driving the CG constraint (see [Project Overview](01-project-overview.md#cg-the-central-challenge)).

### Roll control

**Decision: small dedicated wingtip motors, NOT bleed air.**

Bleed-air roll posts were researched (Eric Maglio's pioneering RC F-35B took several iterations and
ultimately abandoned them; the Resourcium build uses motors+props). At RC scale an EDF produces
near-0 PSI compression, ducting loses energy over its length, servo valves respond too slowly, and
bleeding air **reduces main lift**. Required roll moment ≈ 3400 g × 0.35 m arm → ~100 g+ thrust per
side; bleed air would deliver maybe 50–150 g with large losses — marginal at best.

Final plan:

- **2× 30mm micro EDF** in the wingtips (~150 g thrust, ~25 g each) — scale-accurate, hidden inside
  the wing behind small inlet/outlet doors. (Alternatives: 2204+2" or 2812+3" prop, but props are
  visible.)
- **2× small ESCs** (10–15 A each).
- Cosmetic roll-post inlet/outlet doors on SG90.
- ArduPilot mixes them as quadcopter roll motors.

Cost ~€23–28, weight ~50–60 g — cheap insurance against development crashes.

#### Micro-motor power

Small wingtip motors can be powered from a **2S tap off the main 6S battery's balance lead** (7.4 V),
e.g. 14000KV 2S motor variants — minimal current, no extra battery, lightweight.

## Open questions / TODO

- ⚠️ Validate 3BSM thrust-vectoring reliability and bearing wear under exhaust on the ground.
- Confirm wingtip motor/ESC selection (30mm micro EDF vs prop) and final thrust per side.
- Finalise ArduPilot quadplane motor mixing for the 4-motor hover layout.
- Tune lift-fan vane-box authority vs main-EDF balance for hover pitch.

## Related

[Power System](02-power-system.md) · [Servos](05-servos.md) ·
[Project Overview](01-project-overview.md) · [Materials & Airframe](09-materials-airframe.md) ·
[Bill of Materials](11-bill-of-materials.md)

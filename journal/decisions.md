# Decision log

A terse, **append-only** record of decisions that *changed* — what we were going to do, what we
do now, and why. The `docs/` KB only shows the *current* answer; this file remembers the path
there, so future-me doesn't re-litigate a settled question or forget why something is the way it is.

**How to use:** add a row when you reverse or settle a decision. Keep it one line. Exact dates live
in git history (`git log`); the *Ref* column points to the doc that holds the full reasoning.

## Reversals & settled trade-offs

| Decision | Was / considered | Now | Why | Ref |
|----------|------------------|-----|-----|-----|
| **Temp sensing** | DS18B20 digital (1-Wire) | NTC 100K + CD74HC4067 mux (shared 47 kΩ) | NTC is faster-responding and finer-grained, cheaper, and 16 ch ride one ADC pin; DS18B20 conversion latency/cost wasn't worth it | [07](../docs/07-sensors-monitoring.md) |
| **Project phases** | 3 phases (Trainer → single-EDF jet → VTOL F-35B) | 2 phases (Trainer → F-35B) | The single-EDF jet was a redundant stepping-stone; dropped to focus budget/effort on the F-35B | [01](../docs/01-project-overview.md) |
| **Lift battery** | 2700 mAh 6S (lighter nose) | 2nd 5000 mAh 6S (matched pair) | Current margin + longer hover + matched charging/spares; accepts +260 g forward CG (shift main pack rearward). Lighter fallbacks kept | [02](../docs/02-power-system.md) |
| **Servo BEC rating** | Feared 4 A → considered a UBEC split | IC-confirmed **7.5 A cont / 14 A peak** | Product *text* said 4 A (wrong); manual says 8 A (slightly rounded up); IC read on board: SCT2481 (Silicon Content Technology) → 7.5 A cont. CSD18511Q5A MOSFET (30 A) corroborates. Rail isn't marginal → no UBEC ordered | [02](../docs/02-power-system.md#servo-rail-headroom) |
| **Roll-post battery** | Per-side: one 850 mAh per roll post | Single 3S 850 mAh feeds **both** | A dead pack in a split = uncommanded asymmetric roll; one shared pack fails *symmetric* (both posts die together) — safer, and one 70C pack has ample current | [06](../docs/06-propulsion.md#roll-control) |
| **Roll-post ESCs** | Various options considered | 2× FVT LittleBee 20A (BLHeli_S/DSHOT) — bought separately | Better firmware/DShot, known-good. No BEC → cut the red wire, signal+GND to FC | [06](../docs/06-propulsion.md) |
| **Wingtip roll control** | Bleed-air roll posts (and a 40 mm EDF option) | Dedicated **30 mm EDFs** (inrunner) | Bleed air rejected as impractical; 30 mm over 40 mm (40 mm = more thrust/weight/cost than the roll task needs) | [06](../docs/06-propulsion.md) |
| **Main/lift EDF current sensing** | Matek 150A sensor on each battery lead → FC ADC | None in v1 (ACS712 20A only on roll posts; PDB reports pack A) | 89 A / 40 A exceed the ACS712 20A range; defer a 150A-class sensor; the PDB already logs pack current/voltage | [07](../docs/07-sensors-monitoring.md) |
| **3BSM actuation** | continuous-360 SG90 + external AS5600 encoder → then 2× STS3032 (one per section) | **One** STS3032, sections **gear-coupled** | Serial-bus smart servo with a built-in encoder does the >180° a PWM servo can't; gear-linking the sections lets one motor turn the whole nozzle → saves ~€35, a servo, *and* the external AS5600 encoder | [05](../docs/05-servos.md) |
| **3BSM bearing** | Caged 6805ZZ thin-section bearings | 4 mm loose ball race | Smoother rotation, cheaper, not purchased; the loose race works at the junctions | [06](../docs/06-propulsion.md) |
| **Secondary MCU** | Owned ESP32-S3 boards | WeAct RP2040 (+ Pico spare) | Cleaner ADC for NTC/ACS712, jitter-free PIO servo/LED timing, no 2.4 GHz clash with the ELRS RX; static cockpit dashboard is within headroom | [04](../docs/04-raspberry-pi-pico.md) |
| **Door micro-servos** | SG90 on the 6 V servo rail | **4× NEEBRC M005 "2g" (plastic gear)** for lightweight door actuators on a dedicated **4.0 V LM2596 rail** (SG90 fallback for remaining doors) | 2g servos max 4.2 V → can't share the 6 V rail; one LM2596 buck at 4.0 V powers all 4 | [05](../docs/05-servos.md) |
| **Battery voltage tap** | Solder to the balance lead | Tap the exposed **ESC-side power joint** (never balance leads) | Balance leads are thin and needed for charging — don't disturb them | [07](../docs/07-sensors-monitoring.md#battery-voltage-monitoring) |
| **Smoke stopper** | Planned for F-35B first power-up | Dropped for the F-35B (kept as bench gear) | Avionics are simple; the tool is XT30/XT60, doesn't fit the EC5 packs | [02](../docs/02-power-system.md) |
| **Airframe build** | Foam board (as on the trainer) | 3D-printed | The F-35B is printed, not foam | [09](../docs/09-materials-airframe.md) |
| **Retracts** | COTS electric retract units | Custom 3D-printed, servo-driven | Better fit/cost/control for a scratch airframe | [06](../docs/06-propulsion.md) |
| **CF spar** | 10×6.1 mm tube / local-aluminium; one-piece | **8 mm OD / 6 mm ID tubes joined by 6 mm sleeves** (press-fit), ~900 mm run | Joined tubes ship/store easier; a tight press-fit needs no glue gap | [09](../docs/09-materials-airframe.md#joining-method-press-fit-sleeve--epoxy) |
| **Spar-joint adhesive** | CA glue only (initial constraint) | **2-part epoxy** for spar joints (CA only for fast tacking) | CA is too brittle in tension; epoxy works in shear, carbon-on-carbon — so a 2-part epoxy was bought locally | [09](../docs/09-materials-airframe.md#joining-method-press-fit-sleeve--epoxy) |
| **Afterburner LED** | Addressable WS2812B RGB ring | Single **amber BA15S/1156** automotive bulb (throttle-PWM-dimmed; CANBUS resistor removed) | A plain incandescent-look amber bulb reads more realistic and needs no addressable-LED code; BA15S straight pins chosen over BAU15S offset for a simpler printed socket | [08](../docs/08-lighting.md) |
| **Roll-post exhaust doors** | Servo-actuated wingtip inlet/outlet doors (2× 2 g) | **v1: permanent open slots**; doors deferred to v2 | Skip the actuation complexity until the airframe flies; just cut openings for now | [06](../docs/06-propulsion.md#roll-control) |
| **Roll-post nozzle shape** | Simple radius bend (no deflectors) | **Simple radius + 2 deflectors** (turning vanes) | Paolo Raddri's thrust bench: no-deflector = 510 g / 55 A (9.3 g/A); 1 deflector = 620 g / 61 A; **2 deflectors = 630 g / 60 A (10.5 g/A best)**; elliptical no-deflector was worst (460 g). Deflectors prevent flow separation at the 90° bend — absolute numbers don't transfer to the 30 mm scale but the ranking does. See [devlog 2026-06-28](devlog.md) | [06](../docs/06-propulsion.md#roll-control) |
| **Canopy material** | Considered acrylic (PMMA) / polycarbonate mid-research | **Clear PETG, 0.5–0.75 mm** | Acrylic shatters cold-bent + needs vacuum/oven control; PC must be dried + ~50% failure rate. PETG is forgiving for a hobby heat/vacuum setup. Thin beats scale-thick (lighter nose, easier form, less distortion; RC wind load trivial) | [09](../docs/09-materials-airframe.md#canopy-transparency) |
| **Doc prices** | USD + EUR conversions | EUR only | Single currency, less clutter | — |

## Notable picks (settled, not reversals)

- **Hover control = 4-motor quadcopter mix** (ArduPilot quadplane) over bleed-air schemes.
- **Afterburner = amber BA15S bulb, throttle-reactive** (PWM brightness scales with throttle).
- **COB strip = exterior formation lights** (green, diffused through frosted PP 0.5 mm); cockpit
  glow was considered and dropped (not a priority, not scale-realistic).
- **Strobe = hard on/off, both wingtips synced** — full brightness, 0.2 s on / 0.8 s off (~1 Hz).
  Both strobe LEDs wired **in series on one 700 mA driver + one GPIO** (they always flash together) —
  saves a driver and a GPIO.
- **10 W landing light driven at ~1 A (~3–4 W), not its full 3 A** — far less heat / longer LED life;
  it's only on during approach/landing. Heatsink = **2× 14×14×6 mm stacked** (switched from 20×20×6 mm
  when that size's price jumped).
- **Cockpit screen = ST7789, 12-pin FFC** over 8-pin (thinner bezel).
- **Canopy = single piece** (real F-35 is a frameless bubble; splitting would add a seam, harder to
  form, more join lines). Clear / very-light-smoke tint — iridescent coating not replicable and a
  heavy tint would hide the cockpit screen.
- **Canopy V1 = servo-actuated opening** (SG90, hinged) — not deferred; adds minimal weight and the
  hinge mechanism is straightforward. Magnet-only approach dropped.
- **Canopy interior = realistic cockpit** — when the canopy opens it should look like a real cockpit
  (seat, instrument panel, pilot figure), not expose electronics or a battery. Hide any avionics
  below the instrument panel sightline.
- **Battery placement = TBD** — location depends on what fits and what keeps CG acceptable once the
  airframe geometry is known. "Weapons-bay hot-swap" was a placeholder idea, not a decision.
- **Vacuum-box material = undecided** (tub vs 3D-print vs MDF) — 3D-print not locked in on filament-cost
  grounds.
- **Final paint colour = pending** — decided after the first airframe flies.

## Related
[Project overview](../docs/01-project-overview.md) · [devlog](devlog.md)

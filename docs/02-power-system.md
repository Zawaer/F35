# Power System

> **Current setup (Phase 2 F-35B):** **two 6S 5000 mAh LiPos** — one per fan (main EDF + lift EDF),
> each feeding its own Hobbywing 100A ESC over 10AWG. The FC/servo/LED system runs off an 18AWG
> **tap** from the **lift** battery (it's dead weight in cruise, so this balances the two packs) into
the CoreWing PDB, which provides three regulated BEC rails. **Both EDFs are wired battery→ESC→motor
directly — no high current through the FC.** No
> external buck converters.

The dual-battery choice is driven by **CG/weight distribution** and **clean per-EDF current
measurement**, not by a current shortfall — electrically a single good 6S pack could feed both EDFs.

## Batteries

| Pack | Model | Capacity | C | Weight | Role | Connector |
|------|-------|----------|---|--------|------|-----------|
| Main | CNHL G+Plus 6S | 5000 mAh | 70C | ~714 g | Main (rear) EDF (direct) | EC5 |
| Lift | CNHL G+Plus 6S | 5000 mAh | 70C | ~714 g | Lift (front) EDF + 18AWG avionics tap | EC5 |

Both packs are **borrowed from the school drone club** (an availability/return constraint). Full
specs in the [battery component cards](../components/power.md).

Characteristics of the 5000 mAh main pack:

- Rated 70C → 5000 mAh × 70 = 350 A theoretical; ~150–250 A realistic continuous.
- Builder's measured pack IR ≈ **11.4 mΩ**, implying a real C-rating of **~105C** (~300 A+ real capability).
- The cells are never the bottleneck — **connectors and wiring are**.
- Both fans now run the **same 70C 5000 mAh** pack — matched current headroom, charging, and spares.
- **Battery mass dominates AUW/CG:** 714 g + 714 g ≈ **1428 g (~41% of ~3445 g AUW)** — placement is
  the main CG lever (below). ⚠️ The lift pack going 454 → 714 g (**+260 g, forward**) shifts CG
  forward — plan to move the main pack rearward to compensate, and re-verify CG.

### Battery placement & CG

To balance the nose-heavy lift fan and keep CG between the lift fan (front) and 3BSM (rear):

- **Main 5000 mAh** → central (e.g. weapons-bay area).
- **Lift 5000 mAh** → forward, near the lift fan — but it's **+260 g heavier** than the old 2700 mAh,
  so its forward moment is larger; expect to shift the main pack rearward to compensate.

⚠️ Verify CG carefully before first flight; CG must work for **both** hover and cruise (see
[Project Overview — CG](01-project-overview.md#cg-the-central-challenge)). A long power-wire run to
the main ESC should use 10AWG and be kept as short as possible.

## ESCs

- **2× Hobbywing 100A V2** (Skywalker-class), one per EDF. **Individual ESCs**, not a 4-in-1 —
  chosen for better cooling, high sustained current per channel, and easy replacement.
- Built-in **thermal protection** auto-reduces power on overheat, so no external ESC temp sensor
  is strictly required (one is added anyway for logging — see [Sensors](07-sensors-monitoring.md)).
- Each EDF draws ~72–89 A in normal use (peaks toward ~100 A). Total system peak ~160–200 A across
  both EDFs — this is why connector choice matters.

## Connectors

| Connector | Rating | Use |
|-----------|--------|-----|
| AS150 | ~180 A | Recommended for a single-battery main feed handling full dual-EDF current |
| XT90 | ~90 A | Per-ESC branch (each branch only sees ~90 A) |
| EC5 | ~120 A | 5000 mAh main pack lead / tap joint |
| XT60 | — | Charger side (via XT60→XT90 adapters) |

**Rule of thumb:** XT90 caps around 90 A, so for a single battery splitting to two ~90 A EDFs use
**AS150 on the battery side** and XT90 per branch. With the dual-battery layout actually chosen,
each ESC sits on its own lead and never exceeds its connector's rating.

## BEC rails (from the CoreWing PDB)

One battery tap → PDB → three independent, simultaneous regulated rails:

```
Rail 1: Flight BEC   5.2V  4A (peak 5A)  → FC + ELRS + Pico        (~1A)
Rail 2: Servo BEC    6V    7.5A (peak 14A) → all servos + STS3032
Rail 3: VTX/CAM BEC  9-12V 2A (peak 3A)  → LED drivers
```

Total realistic BEC load ≈ **25 W**, i.e. only **~1.1 A** drawn from the 22.2 V battery —
negligible against the pack's ~300 A capability. Voltage sag from the tap is ~0.057 V — immeasurable.

### Servo rail headroom

> ✅ **Verified: 7.5 A continuous / 14 A peak** (IC-confirmed 2026-06-26). The servo-BEC controller
> is a **SCT2481** (Silicon Content Technology synchronous step-down). The adjacent **CSD18511Q5A MOSFET
> (30 A rated)** corroborates a high-current design. Official manual says 8 A (slightly rounded up);
> product-page text said 4 A (wrong). Real value: **7.5 A continuous**. Rail is not marginal; no UBEC split needed.

The 6V servo rail at **7.5A sustained / 14A peak** comfortably covers the servo count:

| Phase | Servo current | vs 7.5A sustained | vs 14A peak |
|-------|--------------|-------------------|-------------|
| Hover | ~2.1 A | ✅ | ✅ |
| Cruise | ~3.8–4.1 A | ✅ | ✅ |
| Transition (2–3 s) | ~8–10 A | ✅ brief | ✅ |
| All servos stalled | ~11 A | brief | ✅ |

**Decision:** run all servos off the PDB 6V rail directly — 7.5 A sustained covers cruise with margin,
14 A peak covers transition/stall transients, and the FC sits on a *separate* 5.2 V rail so a servo
sag can't reboot it. **No UBEC split — no external UBEC will be ordered.** (Only a future servo
upgrade pushing sustained load past ~7.5 A would call for one — never join two BEC outputs onto one wire.)


## System tap wiring

The tap comes off the **lift-fan battery** (not the main) — the lift fan is dead weight in cruise, so
drawing the avionics from it balances the two packs. It carries only BEC *input* current, not EDF
current: the BEC steps 22.2 V → 6 V, so input current is far lower than servo output (~3.4 A input
for ~10.8 A of 6 V servo output). **Total tap current peaks ~4–5 A.**

- **18AWG silicone wire** (in cart) is plenty — rated ~24.5 A vs the ~5 A tap load. (The cart's
  **10AWG** is for *extending the main/lift EDF power* runs if needed — those carry the ~89 A.)
- **Tap point:** solder the 18AWG to the **exposed solder joint between the lift ESC and its EC5
  connector** (the battery-side EC5 joint is already heat-shrunk, so use the ESC side). Re-protect the
  new joint with heat shrink / Kapton, then run red/black to the PDB input pads.
- **The PDB's own current sensor reads this whole avionics load** — no separate ACS712 needed on the tap.

## Build caveats (power)

Verified-sound architecture; the must-gets:

- **Common ground is mandatory.** Every ESC's **signal-ground** lead must run to the FC (alongside its
  throttle signal) — this commons all three battery grounds at the FC through *thin signal wires*, not
  the fat power leads. Without it the throttle signals have no reference. It falls out naturally from
  wiring each ESC's 3-pin lead to the FC — just don't forget the ground pin.
- **The lift pack is a single point of failure for the avionics.** It powers the lift fan **and** the
  whole avionics tap, so **always fly with it connected** and watch its voltage (the PDB reads it). It
  does double duty (hover thrust + avionics), so it may sag before the main pack.
- **Plug-in spark:** EC5 is *not* anti-spark — a 6S pack sparks on connection (caps charging).
  Functionally harmless, but repeated sparks can **slowly corrode/pit the EC5 contacts**. If they
  degrade too much, just swap to **XT90-S** (anti-spark) — the wear is localized to the connectors, so
  it's a cheap, contained fix. (No smoke stopper used here — the avionics are simple, and the one on
  hand is XT30/XT60, not EC5.)
- **EDFs wire battery→ESC→motor directly** — no high current through the FC.
- **Roll-post split:** pack→split **trunk = the pack's 14AWG lead** (carries the combined ~22–29 A);
  the two per-ESC branches are 18AWG.

## Wire gauge plan (final)

| Gauge | Use | Note |
|-------|-----|------|
| **10AWG** | Main EDF power (89 A) | ✅ adequate — the silicone wire is rated **172 A** (RC silicone is rated well above NEC chassis figures; 10AWG for 80–100 A ESCs is standard RC practice). 8AWG is an optional upgrade, not needed. |
| **18AWG** | Battery tap → PDB; roll-post EDF power (~11–20 A) | ✅ rated **24.5 A** — covers the ~20 A BEC-tap peak and the ~11 A roll-post EDFs |
| **22AWG** | All servo cables | Rated ~9.8 A — ample for ~1 A servos; matches standard RC servo wire, durable under flexing |
| **~28–30AWG** | All signal/data/sensor wires | Using ~50 m red+black already available at school (no coloured set bought); fine for SPI, UART, I2C, PWM, ADC, NTC |

> Wire ampacities above are the manufacturer's ratings for this fine-strand silicone wire (see the
> [wire component card](../components/power.md)). They supersede the earlier conservative
> "10AWG ~55 A / marginal at 89 A" caution.

## Connectors

| Connector | Use |
|-----------|-----|
| AS150 | Single-battery main feed option (full ~180 A) |
| XT90 | Per-ESC branch (~90 A each) |
| EC5 | 5000 mAh main pack lead / system tap joint |
| XT60→XT90 adapters | Charger side |
| **XT60H** | Roll-post ESC power — 3S 850 mAh packs re-soldered from XT30U to XT60H |
| **2 mm bullet** | EDF motor leads (on the buy list) |

**Battery monitoring:** no standalone LiPo alarms — pack voltage is monitored via the FC/PDB
telemetry (PDB VBAT divider → FC).

## Charging

- **HOTA D6 Pro** charger (borrowed from the school drone club — see the
  [charger card](../components/power.md)) handles charging/balancing all packs, two channels at once.
- On **AC it's 200 W total**; for the full 650 W / 15 A×2 it needs an external **DC PSU >24 V**
  (~600–800 W). AC is fine for moderate charge rates.
- Charger output is **XT60**; **both 5000 mAh packs are EC5**, so each needs an **EC5→XT60 charge
  adapter** (4 owned). All packs use JST-XH balance leads.

## Open questions / TODO

- ⚠️ Confirm final CG once component placement is fixed; may need nose ballast or battery shuffle.
- Servo rail **verified: 7.5 A continuous (SCT2481 IC, 2026-06-26)** — no UBEC split, no external UBEC to order.
- **Lift battery decided: a 2nd 5000 mAh pack** (matched pair) for current margin + hover time, at a
  +260 g forward CG cost. Fallbacks if CG/weight don't work out: **2700 mAh lift + 5000 mAh main**
  (the old plan, lighter front), or **2× 2700 mAh** (lightest, shortest flight).

## Related

[Flight Controller](03-flight-controller.md) · [Propulsion](06-propulsion.md) ·
[Sensors & Monitoring](07-sensors-monitoring.md) · [Wiring Diagrams](10-wiring-diagrams.md) ·
[Bill of Materials](11-bill-of-materials.md)

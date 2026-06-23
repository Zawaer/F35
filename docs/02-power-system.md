# Power System

> **Current setup (Phase 3 F-35B):** two 6S LiPos — **5000 mAh** (main EDF) and **2700 mAh**
> (lift EDF) — each feeding its own Hobbywing 100A ESC over 10AWG. The FC/servo/LED system runs
> off an 18AWG **tap** from the main battery into the CoreWing PDB, which provides three regulated
> BEC rails. Two Matek 150A current sensors sit on the battery leads. No external buck converters.

The dual-battery choice is driven by **CG/weight distribution** and **clean per-EDF current
measurement**, not by a current shortfall — electrically a single good 6S pack could feed both EDFs.

## Batteries

| Pack | Cells | Capacity | Role | Connector |
|------|-------|----------|------|-----------|
| Main | 6S | 5000 mAh | Main (rear) EDF + system tap | EC5 |
| Lift | 6S | 2700 mAh | Lift (front) EDF only | (per ESC) |

Measured characteristics of the 5000 mAh pack (from the builder's IR measurements):

- Rated 70C → 5000 mAh × 70 = 350 A theoretical; ~150–250 A realistic continuous.
- Measured pack IR ≈ **11.4 mΩ**, implying a real C-rating of **~105C** (~300 A+ real capability).
- The cells are never the bottleneck — **connectors and wiring are**.

### Battery placement & CG

To balance the nose-heavy lift fan and keep CG between the lift fan (front) and 3BSM (rear):

- **5000 mAh main** → central (e.g. weapons-bay area), heavier and more central.
- **2700 mAh lift** → forward, near the lift fan, to shorten its moment arm.

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
Rail 2: Servo BEC    6V    4A (peak 14A) → all servos + STS3032
Rail 3: VTX/CAM BEC  9-12V 2A (peak 3A)  → LED drivers
```

Total realistic BEC load ≈ **25 W**, i.e. only **~1.1 A** drawn from the 22.2 V battery —
negligible against the pack's ~300 A capability. Voltage sag from the tap is ~0.057 V — immeasurable.

### Servo rail headroom — the marginal case

The 6V servo rail's **4A sustained** rating is marginal for the full servo count:

| Phase | Servo current | vs 4A sustained | vs 14A peak |
|-------|--------------|-----------------|-------------|
| Hover | ~2.1 A | ✅ fine | ✅ |
| Cruise | ~3.8–4.1 A | ⚠️ marginal | ✅ |
| Transition (2–3 s) | ~8–10 A | ❌ over | ✅ covered |
| All servos stalled | ~11 A | ❌ | ✅ briefly |

**Decision:** start on the PDB servo rail alone and fly conservatively — the 14A peak covers
transients and the FC sits on a *separate* 5.2V rail, so a servo-rail sag can't reboot the FC.
**Mitigation if brownout occurs** (FC reboot, servo twitch): add a **Hobbywing 3A UBEC** (~€1.68)
and *split the load* — PDB 6V rail drives the heavy flight-surface servos, UBEC drives the lighter
VTOL servos + Pico secondary servos. **Never join two BEC outputs onto one wire.** A 3A UBEC alone
is not enough (load ~3.8A); if going fully external instead, size a **10A UBEC**.

## System tap wiring

The tap only carries BEC *input* current, not EDF current. Because the BEC steps 22.2V down to
6V, input current is lower than servo output current even at servo stall (~3.4 A input for ~10.8 A
of 6V servo output). Total tap current peaks ~4–5 A.

- **Use 18AWG silicone wire** for the tap. At the servo-BEC peak the combined BEC input can
  approach ~20 A; 18AWG (~16 A continuous) is **marginal at peak** — keep the run **short
  (<150 mm)**, or step up to **16AWG** if the run is longer.
- Tap point: battery EC5 joint → 18AWG red/black → PDB input pads.

## Wire gauge plan (final)

| Gauge | Use | Note |
|-------|-----|------|
| **10AWG** | Main EDF power (89 A) | ⚠️ marginal (~55 A continuous rating); keep runs <200 mm. 8AWG is the textbook size — optional upgrade. |
| **18AWG** | Battery tap → PDB; roll-post EDF power (~11 A) | Fine for roll posts; marginal at BEC peak (above) |
| **22AWG** | All servo cables | Matches standard RC servo wire; durable under flexing |
| **~28–30AWG** | All signal/data/sensor wires | Using ~50 m red+black already available at school (no coloured set bought); fine for SPI, UART, I2C, PWM, ADC, NTC |

## Connectors

| Connector | Use |
|-----------|-----|
| AS150 | Single-battery main feed option (full ~180 A) |
| XT90 | Per-ESC branch (~90 A each) |
| EC5 | 5000 mAh main pack lead / system tap joint |
| XT60→XT90 adapters | Charger side |
| **XT60** | Roll-post ESC power — reusing the 3S 850 mAh packs' existing XT60s |
| **2 mm bullet** | EDF motor leads (on the buy list) |

**Battery monitoring:** no standalone LiPo alarms — pack voltage is monitored via the FC/PDB
telemetry (PDB VBAT divider → FC).

## Charging

- **HOTA D6 Pro** charger + an external **600–800 W DC PSU** is the recommended bench setup for
  charging the 6S packs (with appropriate XT60→XT90 adapters on the charge leads).

## Open questions / TODO

- ⚠️ Confirm final CG once component placement is fixed; may need nose ballast or battery shuffle.
- ⚠️ Validate servo-rail behaviour in a full ground test before deciding whether the 3A UBEC split
  is needed.
- Decide whether the lift battery stays 2700 mAh or grows for flight-time/balance reasons.

## Related

[Flight Controller](03-flight-controller.md) · [Propulsion](06-propulsion.md) ·
[Sensors & Monitoring](07-sensors-monitoring.md) · [Wiring Diagrams](10-wiring-diagrams.md) ·
[Bill of Materials](11-bill-of-materials.md)

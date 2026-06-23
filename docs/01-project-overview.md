# Project Overview

> **Goal:** build a 3D-printed, VTOL-capable RC **F-35B**. Originally a 3-phase plan; **Phase 2
> (single EDF jet) is now scrapped** — going straight from the trainer to the F-35B.

## Phases

| Phase | Build | Purpose | Status |
|-------|-------|---------|--------|
| 1 | Trainer prop plane (foamboard) | Learn to fly, validate basic FC/RX setup | **Built & repaired — awaiting re-flight** (see below) |
| 2 | ~~Single EDF jet~~ | — | ❌ **Scrapped** — skipping straight to Phase 3 |
| 3 | VTOL F-35B (LW-PLA print) | The real goal — VTOL + transition + scale | **Primary focus** / in design |

**Phase 1 status:** the foamboard trainer is fully built. First flight was a hand-launch with no
runway — it flew ~1 s, dropped, and broke (bad throw / not enough launch speed, not an airframe
fault). Already repaired and intact; will be re-flown from a proper runway when there's time. Main
effort is now on the **F-35B**.

The trainer and the F-35B VTOL systems are **electrically completely separate** — different
batteries, ESCs, and motors (see [Propulsion](06-propulsion.md) and [Power](02-power-system.md)).

## Phase 3 — F-35B target spec

| Parameter | Value |
|-----------|-------|
| Class | 70mm EDF scale |
| Wingspan | ~700–800 mm |
| Fuselage length | ~900–1100 mm |
| Wing chord | ~150–200 mm |
| Wing area | ~0.12 m² |
| All-up weight (AUW) | ~3185 g |
| Cruise speed (est.) | 80–120 km/h (22–33 m/s) |

### Subsystems

- **Propulsion:** 2× QX-Motor 70mm EDF (~50,000 RPM, ~3300 g thrust each) — one main (rear,
  thrust-vectored), one lift (front). Individual Hobbywing 100A V2 ESCs. See [Propulsion](06-propulsion.md).
- **Hover / VTOL control:** ArduPilot quadplane, controlled as a **4-motor quadcopter** in hover:
  main EDF (vectored by the 3BSM), front lift fan, and 2× wingtip micro motors for roll. Bleed-air
  roll posts were evaluated and **rejected** (see [Propulsion](06-propulsion.md#roll-control)).
- **Flight controller:** CoreWing F405 WING V2 stack, ArduPilot firmware. See [Flight Controller](03-flight-controller.md).
- **Secondary controller:** Raspberry Pi Pico for extra PWM outputs, temperature sensing, and LED
  control, talking to the FC over UART. See [Pico](04-raspberry-pi-pico.md).
- **Airframe:** LW-PLA printed shell + carbon/aluminium spars + plywood reinforcement. See
  [Materials & Airframe](09-materials-airframe.md).

## Hard open design questions

These are the genuinely unsolved / high-risk items flagged during design:

| Topic | Question | Where |
|-------|----------|-------|
| CG | Reconcile hover CG (above thrust centre) with cruise CG (~25–30% MAC) | [below](#cg-the-central-challenge) |
| 3BSM | Reliable 3-bearing swivel module that vectors main EDF and survives exhaust | [Propulsion](06-propulsion.md) |
| Roll control | Confirmed: small wingtip motors, **not** bleed air | [Propulsion](06-propulsion.md#roll-control) |
| Landing gear | Custom 3D-printed retracts with over-centre lock + 90° wheel twist (no COTS retracts) | [Servos](05-servos.md) |
| Servo power | PDB 6V rail marginal at sustained cruise; split load with a 3A UBEC as mitigation | [Power](02-power-system.md) |

### CG: the central challenge

VTOL hover requires CG **directly above the thrust centre** (between the front lift fan and the
rear 3BSM, weighted by their thrust ratio) — a precise requirement; any offset means constant
correction. Fixed-wing cruise wants CG at **~25–30% MAC**. The real F-35B manages a shifting CG
with fuel transfer and flight computers; the RC model has fixed component placement, so CG must be
chosen to satisfy both regimes. Battery placement is the main tuning lever (see
[Power — battery placement](02-power-system.md#battery-placement--cg)).

## Realism features

Now committed (parts in the cart — see [BOM](11-bill-of-materials.md)):

- **Cockpit screen:** 1.47" ST7789 SPI TFT, Pico-driven (see [Pico](04-raspberry-pi-pico.md#4-cockpit-tft-display)).
- **Afterburner glow:** BA15S P21W automotive LED bulb, CANBUS resistor removed (see [Lighting](08-lighting.md#afterburner-power--the-canbus-resistor-mod)).
- **Lighting:** nav lights, strobes, 10W landing light, COB accent strip (see [Lighting](08-lighting.md)).

Still parked (not committed):

- **Engine sound:** DFPlayer Mini (~€2) + 40mm 2W speaker, triggered by Pico from FC flight state.
  EDFs already sound convincingly jet-like.
- Weapons-bay battery hot-swap, canopy actuation, variable exhaust nozzle.

## Side project

A **GL823K-based SD card reader PCB** is referenced as a separate side project — tracked here only
as a pointer; it is not part of the aircraft build.

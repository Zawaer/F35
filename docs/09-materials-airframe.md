# Materials & Airframe

> **Current plan (Phase 3):** LW-PLA printed shell, PETG for structural parts, ASA/ABS for
> heat-critical parts near the EDF exhaust. Wing spars from **10×6.1 mm carbon tube** (or local
> aluminium tube to dodge CF shipping cost); existing 6mm CF tubes for secondary structure.
> Plywood reinforcement plates. **Phase 1 trainer is foamboard.**

## Filaments

| Filament | Use | Qty |
|----------|-----|-----|
| LW-PLA | Main airframe shell (light, printable internal channels) | 2–3 rolls |
| PETG | Structural parts, 3BSM sections | 1–2 rolls |
| ASA / ABS | Heat-critical parts near EDF exhaust, motor mounts | 1 roll |

A big advantage of a 3D-printed airframe: servo bays, internal pushrod channels, and horn slots can
be designed directly into the print (see [Servos — internal actuation](05-servos.md)).

## Carbon fibre / structural rods & tubes

**Rule:** tubes for spars (stiffer per gram — hollow = better strength-to-weight), solid rods for
pushrods (compression/tension).

### Already owned

- **10× CF tube, 6 mm OD / 4 mm ID, 400 mm** — too thin/short for primary F-35B structure, but good
  for: stabilator spars, tail reinforcement, 3BSM supports, landing-gear bay, ribs/formers — any
  piece under 400 mm.

### Needed for the F-35B (~3 kg airframe)

| Use | Spec | Notes |
|-----|------|-------|
| Main wing spar | 10 mm OD, **1.95 mm wall (10×6.1 mm)** | Thick wall is critical for stiffness at EDF speeds |
| Fuselage spine | 10 mm OD, 10×6.1 mm | Primary structural |
| Secondary spars | 8 mm OD / 10×8.1 mm (0.95 mm wall) | Lighter, non-critical only |
| Pushrods | 1.5–2 mm CF rod | Internal surface linkages |
| Spar sleeve / joiner | 4 mm CF rod | Inner sleeve to join two 500mm tubes → ~980 mm |

**10×6.1 mm vs 10×8.1 mm:** wall thickness dominates bending stiffness — use **10×6.1 mm for all
primary roles** (wing spar, fuselage spine); the 0.95 mm-wall 10×8.1 mm is too thin for main spars
on a 3 kg jet and only suits non-critical reinforcement.

### Joining short tubes

Two 400/500 mm tubes can be joined with a 4 mm CF rod inner sleeve (~150 mm, centred, epoxied both
sides) → ~780–980 mm effective spar. Fine for **secondary** spars; the joint is a weak point and
6mm OD is undersized for a **primary** wing spar at EDF speed.

### Avoiding CF shipping cost (~€25 for 1000 mm tubes)

| Alternative | Notes |
|-------------|-------|
| **Aluminium tube 10mm × 1000mm** | Local in Finland (Bauhaus/K-Rauta/Motonet), ~€3–5, free pickup. ~2× heavier than CF (~+45 g/spar, ~+90 g total — ~3% of AUW, acceptable) |
| Join existing 6mm tubes | Secondary spars only |
| Fibreglass tube 10mm × 1000mm | ~€3, cheaper shipping than CF, ~70% CF strength |
| Local hobby shops | Puuilo, Biltema, Verkkokauppa — pickup = no shipping |

**Recommendation:** join existing 6mm tubes for secondary spars; buy local aluminium tube for the
primary wing spars/fuselage spine.

## Bearings (3BSM)

- **6805ZZ thin-section ball bearings, 37 × 25 × 7 mm** — best fit inside the 70 mm EDF duct;
  ID large enough to pass airflow, OD leaves wall material. (~16 g.) Alternatives: 6806, 6904.
- ZZ = metal shields both sides (keeps exhaust debris out).
- Need **2 per junction** (one each side) to prevent wobble → **buy ~10** (6 used + spares).
- ⚠️ **Buy bearings before modeling** the 3BSM — design the seats around real bearing dimensions.

See [Propulsion — 3BSM](06-propulsion.md#3bsm--three-bearing-swivel-module).

## Fasteners

- **Stainless button-head kit, 600 pc**: M2/M3/M4/M5 in 8/12/16/20 mm + washers — covers 3BSM,
  servo/ESC/EDF mounting, carbon-tube clamps, landing gear, general airframe. Stainless chosen over
  zinc (no rust from exhaust condensation).
- ⚠️ Confirm **M2 nuts** are included (needed to secure 3BSM from both sides).
- Add **M2/M3 nyloc nuts** (~€2) for vibration-prone areas (EDF mounts, landing gear) so screws
  don't shake loose. **Threadlocker (Loctite blue)** for the rest.
- Linkage hardware: 2 mm linkage rods, clevises, M2 threaded rod for adjustable linkages.

## Adhesives & misc

- Thin CA (foam/CF fast bond) ×2, thick CA (gap fill) ×1, CA accelerator.
- 30-minute epoxy ×2 (structural bonds / spar joints).
- 3 mm plywood sheet (reinforcement plates).
- Silicone tubing 25–30 mm ID (was for bleed-air ducts — **likely obsolete** now roll posts use
  motors, see [Propulsion](06-propulsion.md#roll-control)).

## Magnets

- **Diametric rod magnet 4 × 10 mm N42** (magneettikauppa.fi) — only needed if a 3BSM position
  sensor is built from a bare encoder. The chosen **STS3032** smart servos already have a built-in
  magnetic encoder, so this is largely redundant. See [Servos](05-servos.md#3bsm-smart-servos-sts3032).

## Finishing

Grey primer + filler primer (hide layer lines), F-35B livery colours, sandpaper assortment, decals.

## Open questions / TODO

- Decide CF vs local aluminium for the primary spars (cost vs ~90 g weight).
- Confirm the 600 pc fastener kit includes M2 nuts; otherwise add separately.

## Related

[Propulsion](06-propulsion.md) · [Servos](05-servos.md) · [Bill of Materials](11-bill-of-materials.md)

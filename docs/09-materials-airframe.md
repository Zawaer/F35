# Materials & Airframe

> **Current plan (Phase 3):** LW-PLA printed shell, PETG for structural parts, ASA/ABS for
> heat-critical parts near the EDF exhaust. Spars from **16× 500×8×6 mm carbon tube** (8 mm OD /
> 6 mm ID), joined with the existing **6 mm OD / 3 mm ID** tubes as press-fit inner sleeves.
> Plywood reinforcement plates. **Phase 1 trainer is foamboard.**

## Filaments

| Filament | Use | Qty |
|----------|-----|-----|
| LW-PLA | Main airframe shell (light, printable internal channels) | 2–3 rolls |
| PETG | Structural parts, 3BSM sections | 1–2 rolls |
| ASA / ABS | Heat-critical parts near EDF exhaust, motor mounts | 1 roll |

**LW-PLA in hand:** 2 rolls of **eSUN LW-PLA, black, 1 kg** (foaming PLA, ~0.54 g/cm³ foamed at
260–270 °C) — for **test prints + the first airframe**. Full spec on the
[eSUN LW-PLA card](../components/structural.md). ⚠️ Needs an **all-metal hotend** to foam properly
(>250 °C); retraction is ineffective so expect stringing. A big advantage of a printed airframe:
servo bays, internal pushrod channels, and horn slots can be designed straight into the print (see
[Servos — internal actuation](05-servos.md)).

### Final airframe colour: gray vs paint

Black LW-PLA is **test/first-airframe only** (low HDT ~53 °C → can soften in strong sun; fine in
weak Finnish sun and for testing). Once the airframe is proven to fly well, pick the final finish:

- **Gray LW-PLA** — closest to the real F-35B colour out of the spool; no paint step, no added paint
  weight, but limited to that one grey.
- **White LW-PLA + paint** — full control of the scale livery (panel lines, markings, exact greys),
  but adds paint/primer weight and work, and LW-PLA's matte foamed surface needs care when painting.

**Decision: pending** — choose after the first airframe flies. Leaning gray for simplicity/weight if
the shade is close enough; white+paint if a faithful livery matters more. (To revisit.)

## Carbon fibre / structural rods & tubes

**Rule:** tubes for spars (stiffer per gram — hollow = better strength-to-weight), solid rods for
pushrods (compression/tension).

### Owned

- **10× CF tube, 6 mm OD / 3 mm ID, 400 mm** — used as **press-fit inner sleeves** to join the
  500 mm main tubes (the 6 mm OD slides into the 6 mm ID main tube with ~0 mm gap), plus secondary
  structure, 3BSM supports, ribs/formers.

### In cart (not yet ordered)

- **16× CF tube, 8 mm OD / 6 mm ID, 500 mm** (1 mm wall) — **main spars & fuselage spine**, joined
  in pairs into ~900 mm runs (see spar plan below).
- **10× CF rod, 2 mm × 250 mm** (solid) — pushrods / control linkages.

### Spar plan (final) — 16× 500×8×6 mm joined with 6 mm sleeves

The F-35B is ~1 m long, so a single 500 mm tube is only half a span/length — each full run is
**two 500 mm tubes joined**. Plan ~4 full runs (main spine, wing spar L+R, secondary spine, wing
secondary), so **8 tubes minimum**; the **16-pack (€33.71)** gives all runs plus spares and is far
better value than the 4× 10×6.1 mm option (€25.68, zero spares).

| Use | Spec |
|-----|------|
| Spars / spine (main tubes) | **8 mm OD / 6 mm ID, 500 mm** (1 mm wall), joined in pairs |
| Joining sleeve | existing **6 mm OD / 3 mm ID** tube, ~80–100 mm, ~50 mm into each side |
| Pushrods / linkages | 2 mm CF rod (have 2×250 mm 10-pack) |

**Wall thickness:** 8×6 mm is a **1 mm wall** — adequate for fuselage spines; for the most
wing-loaded spar, either run **two 8 mm tubes side-by-side** (≈ one 10 mm tube) or accept the 1 mm
wall given the joined-tube approach. (The earlier 10×6.1 mm / local-aluminium options are dropped.)

### Joining method (press-fit sleeve + epoxy)

```
[8mm tube A] ──[6mm OD sleeve, ~50mm each side]── [8mm tube B]
```

The 6 mm OD sleeve in the 6 mm ID tube is a **0 mm-gap interference fit** — ideal: maximum contact,
epoxy works in **shear** (strong) not tension, carbon-on-carbon. If too tight to slide, lightly sand
the sleeve or gently warm the outer tube. **Use 2-part epoxy** (5-min is fine) for spar joints —
*not* CA (brittle under vibration). Sand mating surfaces, glue, align straight, cure fully before
loading. Resulting run ≈ 900 mm. Budget ~35 ml epoxy total (~5 ml/joint).

## Bearings & 3BSM rotation

- **3BSM swivel — loose ball race:** the main 3BSM rotation runs on **4 mm loose steel balls
  (100 pc)** in a printed race, chosen deliberately for smoother rotation. Design the printed
  grooves around the 4 mm ball diameter.
- **MR62ZZ (2 × 6 × 2.5 mm)** bearings are kept as **backup / for small gears**, not the main swivel.
- **6805ZZ thin-section (37 × 25 × 7 mm)** was considered for full-section caged duct bearings but
  **dropped — not purchased**; the loose 4 mm ball race is used at the junctions instead.
- ⚠️ **Finalise the bearing/ball-race geometry before modeling** the 3BSM — design the seats and
  grooves around the real ball/bearing dimensions.

See [Propulsion — 3BSM](06-propulsion.md#3bsm--three-bearing-swivel-module).

## Landing gear hardware

- **Wheels:** standard RC-plane wheels (no O-ring tricks). **38 mm PU pair in cart** (front/nose gear,
  2.1 mm bore → 2 mm axle); remaining wheels (main gear) ordered later (budget).

## Fasteners

- **Stainless button-head kit, 600 pc**: M2/M3/M4/M5 in 8/12/16/20 mm + washers — covers 3BSM,
  servo/ESC/EDF mounting, carbon-tube clamps, landing gear, general airframe. Stainless chosen over
  zinc (no rust from exhaust condensation).
- ⚠️ Confirm **M2 nuts** are included (needed to secure 3BSM from both sides).
- Add **M2/M3 nyloc nuts** (~€2) for vibration-prone areas (EDF mounts, landing gear) so screws
  don't shake loose. **Threadlocker (Loctite blue)** for the rest.
- Linkage hardware: 2 mm linkage rods, clevises, M2 threaded rod for adjustable linkages.

## Adhesives & misc

- **CA glue: Deli 502** (15 g ×3) for foam/CF fast bonding and panels.
- **2-part epoxy** for structural bonds / spar joints (~35 ml — see joining method above). CA is
  too brittle for spar joints.
- 3 mm plywood sheet (reinforcement plates).
- **Frosted PP sheet 0.5 mm** (100×200 mm, 10 pc) — LED diffuser.
- Silicone tubing 25–30 mm ID (was for bleed-air ducts — **obsolete** now roll posts use motors,
  see [Propulsion](06-propulsion.md#roll-control)).

## Magnets

- **Diametric rod magnet 4 × 10 mm N42** (magneettikauppa.fi) — only needed if a 3BSM position
  sensor is built from a bare encoder. The chosen **STS3032** smart servos already have a built-in
  magnetic encoder, so this is largely redundant. See [Servos](05-servos.md#3bsm-smart-servos-sts3032).

## Finishing

Grey primer + filler primer (hide layer lines), F-35B livery colours, sandpaper assortment, decals.

## Open questions / TODO

- Confirm whether one 8 mm tube per wing spar suffices or two should be run side-by-side.
- Confirm rear wheel size (~50 mm) and add to cart.
- Confirm the fastener kit includes M2 nuts; otherwise add separately.

## Related

[Propulsion](06-propulsion.md) · [Servos](05-servos.md) · [Bill of Materials](11-bill-of-materials.md)

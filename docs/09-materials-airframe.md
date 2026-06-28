# Materials & Airframe

> **Current plan (Phase 2):** LW-PLA printed shell, PETG for structural parts, ASA/ABS for
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

![Structural load types — tension, compression, shear, bending, torsion](../journal/img/structural-load-types.jpg)

| Property | Pultruded tube | Roll-wrapped tube |
|----------|---------------|-------------------|
| Axial tension (pulling) | ★★★★★ Excellent | ★★★★☆ Very good |
| Axial compression (pushing) | ★★★★★ Excellent | ★★★★☆ Very good |
| Simple bending | ★★★★★ Very stiff | ★★★★☆ Good–excellent |
| Torsion (twisting) | ★★☆☆☆ Fair | ★★★★★ Excellent |
| Radial crushing (clamps, bolts) | ★★☆☆☆ Fair | ★★★★★ Excellent |
| Multi-directional loads | ★★☆☆☆ Fair | ★★★★★ Excellent |
| Impact resistance | ★★☆☆☆ Lower | ★★★★☆ Better |

> All CF tubes in this build are **pultruded** — excellent for the bending loads spars actually carry.
> Weak spots: radial crushing at mounting points → always use printed collars/saddles, never bare metal screws clamping directly onto the tube wall.

### Owned

- **10× CF tube, 6 mm OD / 3 mm ID, 400 mm** — used as **press-fit inner sleeves** to join the
  500 mm main tubes (the 6 mm OD slides into the 6 mm ID main tube with ~0 mm gap), plus secondary
  structure, 3BSM supports, ribs/formers.

### Ordered (24 Jun 2026)

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

- **Wheels:** standard RC-plane wheels (no O-ring tricks). **38 mm PU pair (ordered 24 Jun 2026)** = F35B **nose
  gear** (scale-matched, 2.1 mm bore → 2 mm axle). F35B **main gear** → order **~55/56 mm** later
  (cheap when in stock on AliExpress). The owned **45/50 mm pair is on the trainer** (45 mm nose,
  2× 50 mm main), not the F35B.

## Fasteners

- **Stainless button-head kit, 600 pc**: M2/M3/M4/M5 in 8/12/16/20 mm + washers — covers 3BSM,
  servo/ESC/EDF mounting, carbon-tube clamps, landing gear, general airframe. Stainless chosen over
  zinc (no rust from exhaust condensation).
- ⚠️ Confirm **M2 nuts** are included (needed to secure 3BSM from both sides).
- Linkage hardware: 2 mm linkage rods, clevises, M2 threaded rod for adjustable linkages.

## Adhesives & misc

- **CA glue: Deli 502** (15 g ×3) for foam/CF fast bonding and panels.
- **2-part epoxy: Biltema Pika Epoksi** (2×21 g, 20-min working time, transparent, gap-filling) —
  structural bonds / spar joints / tube sockets. CA is too brittle for spar joints. One pack
  (42 g) should cover all spar joints + sockets (~35 ml needed); buy a second as backup. Leave
  clamped 24 h before loading for full strength. 🛒 not yet ordered. €3.55 / pack.
  [Biltema](https://www.biltema.fi/rakentaminen/liimat/epoksiliimat/pika-epoksi-2-x-21-g-2000050118)
- **Frosted PP sheet 0.5 mm** (100×200 mm, 10 pc) — LED diffuser.
- Silicone tubing 25–30 mm ID (was for bleed-air ducts — **obsolete** now roll posts use motors,
  see [Propulsion](06-propulsion.md#roll-control)).

## Canopy (transparency)

> **Current plan:** single-piece clear **PETG, 0.5–0.75 mm**, heat-formed over a positive 3D-printed
> plug. **V1: removable, magnet-located** (no servo); **powered opening deferred to V2.** Forming
> method = DIY vacuum forming; the vacuum-box material is **still undecided** (see below).

### Material & thickness

- **PETG, clear, 0.5–0.75 mm.** PETG is chosen *because of the forming method*, not in the abstract:
  wide forming-temperature window, very forgiving, no pre-drying needed, clear enough at viewing
  distance. It is the RC community default for heat-/vacuum-formed canopies.
- **Acrylic (PMMA)** is what real canopies and the best RC bubbles are made of, but it shatters if
  cold-bent and needs an oven + tight temperature control — wrong tool for a hobby heat/vacuum setup.
  **Polycarbonate** must be dried before forming and has a narrow window (~50% failure rate even for
  experienced builders). Both rejected for this build.
- **Thickness:** 0.5 mm forms easiest and is structurally fine — wind load on a ~50 cm² canopy at RC
  cruise (~100–150 km/h) is trivial. 0.75 mm adds rigidity. *Scale thickness math is a red herring*
  (real F-22 canopy 19 mm ÷ ~15 ≈ 1.3 mm) — optical scale thickness is invisible at viewing distance,
  and thicker sheet is heavier on the nose, harder to form, and more optically distorting. Go thin.
- **Tint:** clear, or a *very* light smoke at most. The real F-35 canopy's blue/purple iridescence is
  a thin-film vapour-deposited coating — not replicable with hobby materials and not worth faking. A
  heavy tint would also hide the cockpit screen, which is the more impressive detail. See the
  [cockpit TFT filter note](04-raspberry-pi-pico.md#4-cockpit-tft-display).

### Single piece

Form the canopy as **one piece.** The real F-35 canopy is a frameless single bubble — splitting it
into a windscreen + canopy would *add* a seam the real aircraft doesn't have, and one bubble is also
easier (one plug, one pull) and optically cleaner (no join line to glue/align). The long, shallow
F-35 profile is forgiving to form; keep the plug's rear taper gradual so the sheet pulls in instead
of bridging.

### Opening vs fixed (V1 scope)

A powered opening canopy is a very cool scale detail, but its real cost is **one scarce Pico PWM
channel** plus a hinge mechanism — which is exactly why it was cut from V1 (servo budget short by
6–9 outputs, see [Pico](04-raspberry-pi-pico.md) / [Servos](05-servos.md)). **V1 plan: removable,
located by the owned N35 5×2 mm magnets** (see [Magnets](#magnets) below) — lift off by hand to show
the cockpit, self-aligns on replacement, zero servo/channel. **Powered opening = V2** once the pin
budget is resolved; it stays a single piece glued to a hinged printed sill either way.

### Forming method — DIY vacuum forming

The plan is **vacuum forming**, which gives far more even, crisp results than heat-gun draping (a
single nozzle pulls at one point and leaves the rest of the sheet loose/wrinkly). Principle: a sealed
air chamber (**plenum**) with a perforated top, the plug sitting on the perforated surface, and a
vacuum emptying the chamber so atmospheric pressure presses the heated sheet uniformly onto the plug.

Setup, all room-temperature except the sheet:

- **Plug:** solid 3D-printed canopy shape (LW-PLA or PLA), sanded smooth, slightly undersized, raised
  a few mm on standoffs / a small base so air reaches its edges, with release agent (wax/vaseline).
- **Box (plenum):** sealed chamber, hole grid (~1–1.5 mm, ~10–15 mm spacing) in the flat top over the
  plug footprint, one hose port in the **side or bottom** (never the top). Must be reasonably airtight
  *everywhere except the hole grid* — leaks steal suction. **Material undecided:**
  - *Plastic tub* — cheapest, already airtight, just drill a lid + side hole. Front-runner for cost.
  - *3D-printed box* — easiest clean hole grid + integral tapered hose port + plug standoffs, but
    **filament cost is significant** at canopy footprint (~220×80 mm, likely a 2-piece print on most
    beds) and FDM walls are porous (need 4+ perimeters + an inside epoxy wipe to seal). **Not locked
    in** pending the cost call.
  - *MDF/ply box* — classic, cheap, more woodwork.
- **Vacuum:** an ordinary household vacuum is plenty — the chamber spreads its suction evenly, so
  power matters less than seal quality. (Wet/dry shop vac slightly better.)
- **Heat:** the **kitchen oven** (~100–120 °C, sheet flat on a rack until it sags a few cm) gives the
  most even heat; a heat gun works for a part this small but heats less evenly. *(Air fryer too small
  for a ~220 mm canopy.)*

Process: heat **only the framed sheet** in the oven → the moment it droops, drape the frame over the
plug so it seals on the box rim → **switch the vacuum on immediately** (PETG stiffens in seconds) →
hold ~10–20 s → vacuum off, pop off plug, trim. Oven gloves: the frame is hot.

### Canopy sill / frame

Print the sill the PETG sits on as **part of the fuselage** in LW-PLA for an exact fit; CA-glue the
trimmed PETG to it. For the opening canopy (V1), the sill becomes a separate hinged printed part.

## Magnets

- **Diametric rod magnet 4 × 10 mm N42** (magneettikauppa.fi) — only needed if a 3BSM position
  sensor is built from a bare encoder. The chosen **STS3032** smart servos already have a built-in
  magnetic encoder, so this is largely redundant. See [Servos](05-servos.md#3bsm-actuation--single-sts3032--gear-linked-sections).
- **N35 neodymium discs, 5 × 2 mm (×100, owned)** — embedded in printed seats for **removable
  panels/hatches** (battery hatch, canopy, access covers). 80 °C max; keep clear of any
  compass/magnetometer. See the [magnet card](../components/structural.md).

## Cosmetic details — EOTS sapphire bump

The real F-35B has a distinctive **EOTS (Electro-Optical Targeting System) dome** on the nose underside — a small faceted sapphire window housing that reads as a raised bump, visible from below and slightly from the side.

![EOTS sapphire dome, side-below view](img/eots/eots-nose-side-below.jpeg)
*The amber-tinted faceted EOTS dome on the nose underside — one of the most recognisable detail features of the F-35 silhouette.*

![EOTS and nose wheel bay from below](img/eots/eots-nose-bay-below.jpeg)
*Nose wheel bay open, showing the EOTS housing in the context of the lower-forward fuselage geometry.*

![EOTS dome close-up from below](img/eots/eots-dome-closeup.jpeg)
*EOTS faceted sapphire dome close-up — multi-panel angled window set into a protruding housing, surrounded by hydraulic lines and actuators from the open nose bay.*

Model the EOTS as a **printed insert** in the nose-bottom panel — clear PETG or ASA, tinted amber from inside with translucent film if backlit.

## Finishing

Grey primer + filler primer (hide layer lines), F-35B livery colours, sandpaper assortment, decals.

## Open questions / TODO

- ⚠️ **Still open:** one 8 mm tube per wing spar, or two side-by-side? (Undecided — needs a load call.)
- Rear/main wheel (55–56 mm): **deferred to buy-later** (see [BOM](11-bill-of-materials.md)); 38 mm
  nose wheel already ordered.
- Confirm the fastener kit includes M2 nuts; otherwise add separately.

## Related

[Propulsion](06-propulsion.md) · [Servos](05-servos.md) · [Bill of Materials](11-bill-of-materials.md)

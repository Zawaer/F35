# Components — Structural & Hardware

Cards for filament, carbon tube/rod, bearings, balls, fasteners, wheels, and adhesives. See the
[template & field guide](README.md). Build context: [Materials & Airframe](../docs/09-materials-airframe.md).

---

### eSUN LW-PLA (ePLA-LW) — airframe filament
- **Category:** Filament (lightweight / foaming PLA)
- **Status:** ✅ owned (2 rolls, black · ordered 19 May 2026)
- **Used for:** F-35B airframe — **test prints + first airframe** ([Materials & Airframe](../docs/09-materials-airframe.md))
- **Variant / qty:** 1.75 mm, 1 kg spool, **black** · 2 rolls
- **Price:** €31.94 total (€15.96/roll)
- **Source:** Amazon.de (eSUN Official Store) — *not AliExpress*
- **Link:** Amazon.de — eSUN ePLA-LW 1.75 mm 1 kg Black (ASIN B09VSMMLKB; part ePLA-LW-B1KG-EU)

| Spec | Value |
|------|-------|
| Material | PLA-LW (active-foaming PLA) |
| Diameter / tolerance | 1.75 mm, ±0.05 mm |
| Spool | 1 kg |
| Density | **0.54 g/cm³** foamed (260–270 °C); 1.2 g/cm³ unfoamed |
| Foam onset | ~210 °C (none below); max foam 122% @ 260–270 °C |
| Print temp | 190–270 °C (190–210 unfoamed, 210–270 foaming) |
| Bed temp | 45–60 °C |
| Print speed | 40–100 mm/s (≈40 recommended, constant) |
| HDT (0.45 MPa) | **53 °C** |
| Tensile / flexural | 32.2 / 41.31 MPa; flex modulus 1701 MPa (unfoamed) |
| Weight saving | ~55% vs normal PLA (1 roll ≈ 2.2 rolls normal PLA by volume) |

**Foam rate vs nozzle temp** (≈40 mm/s, 0.2 mm layer):

| °C | 200 | 220 | 240 | 250 | 260 | 270 | 280 |
|----|-----|-----|-----|-----|-----|-----|-----|
| Foam % | 0 | 11 | 82 | 100 | 122 | 122 | 82 |
| Density g/cm³ | 1.2 | 1.08 | 0.66 | 0.6 | **0.54** | 0.54 | 0.66 |
| Extrusion % | 100 | 90 | 55 | 50 | 45 | 45 | 55 |

- **Notes:** tune extrusion-rate down to match foam % (e.g. ~45% @ 270 °C). **Retraction barely works**
  (foams in the hot end) → stringing is normal; design to minimise it. Matte surface, easy to sand/
  paint. ⚠️ Needs an **all-metal hotend for >250 °C** (PTFE-lined limited to <250 °C). Models yellow
  after hot foaming.
- **Colour plan:** black rolls are for **testing + the first airframe**. Black has a low HDT (~53 °C)
  and can soften/deform in strong sun — acceptable here (weak Finnish sun + test use only). Once the
  airframe flies well, switch to the **final colour** — see the decision in
  [Materials & Airframe](../docs/09-materials-airframe.md#final-airframe-colour-gray-vs-paint).

---

### 304 stainless steel balls 4 mm — 3BSM ball race
- **Category:** Hardware (loose bearing balls)
- **Status:** 🛒 in cart (100 pcs)
- **Used for:** **3BSM swivel ball race** — loose balls in a printed groove for smooth 360° nozzle
  rotation — [Propulsion → 3BSM](../docs/06-propulsion.md#3bsm--three-bearing-swivel-module)
- **Variant / qty:** 4 mm · 100 pcs
- **Price:** €3.54
- **Link:** https://www.aliexpress.com/item/1005008768287413.html

| Spec | Value |
|------|-------|
| Diameter | 4 mm |
| Material | 304 stainless steel |
| Properties | high precision/hardness, smooth, good roundness, corrosion-resistant |
| Weight | ~0.26 g each (steel, 4 mm) |

- **Notes:** 4 mm chosen deliberately for smoother 3BSM rotation (see
  [Materials → bearings](../docs/09-materials-airframe.md#bearings--3bsm-rotation)). Design the
  printed race groove around the 4 mm ball diameter. 304 is non-magnetic + rust-resistant. 100 pcs
  → race fill + plenty of spares.

---

### MR62ZZ deep-groove ball bearing (2×6×2.5 mm) — small shafts / backup
- **Category:** Bearing (deep-groove, shielded)
- **Status:** 🛒 in cart (10 pcs)
- **Used for:** small shafts / gears / **backup** for the 3BSM (the main swivel uses the 4 mm ball
  race) — [Materials → bearings](../docs/09-materials-airframe.md#bearings--3bsm-rotation)
- **Variant / qty:** MR62ZZ 2×6×2.5 · 10 pcs
- **Price:** €3.93 / 10 pcs
- **Link:** https://www.aliexpress.com/item/1005008226968788.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D

| Spec | Value |
|------|-------|
| Bore (ID) | 2 mm |
| OD | 6 mm |
| Width | 2.5 mm |
| Type | single-row deep-groove, pre-lubricated |
| Shields | ZZ (double metal shield) |
| Material | bearing (chrome) steel |
| Brand | FUSHI |
| Weight | ~0.7 g each (est.) |

- **Notes:** small (2 mm bore) — suits a thin shaft / gear pivot, **not** the main 3BSM swivel
  (that's the loose 4 mm ball race). ZZ shields keep debris out. Listing also offers MR52ZZ
  (2×5×2.5), 692ZZ (2×6×3), MR72ZZ (2×7×3) variants.

---

### Carbon fibre rod 2 × 250 mm — door joints / light mechanical linkages
- **Category:** Structural (solid CF rod)
- **Status:** 🛒 in cart (10 pcs)
- **Used for:** **joints & mechanical linking of light F35B parts** (gear/lift-fan/canopy door hinges
  & links, light pushrods) — solid rod in compression/tension —
  [Materials & Airframe](../docs/09-materials-airframe.md#carbon-fibre--structural-rods--tubes)
- **Variant / qty:** 2 mm dia × 250 mm · 10 pcs
- **Price:** €3.75 / 10 pcs (€14.94 list, −74%)
- **Link:** https://www.aliexpress.com/item/1005010320255002.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D

| Spec | Value |
|------|-------|
| Form | solid round rod |
| Diameter | 2 mm |
| Length | 250 mm |
| Qty | 10 pcs |
| Material | pure carbon fibre |
| Properties | high strength, light (~1/5 steel weight), corrosion-resistant, electrically conductive |

- **Notes:** solid rod (not tube) — the rule is **rods for linkages/joints** (compression/tension),
  **tubes for spars** (stiffer per gram). Earmarked for **light door joints / mechanical links** on the
  F35B. Conductive — keep clear of exposed electronics. Cuts with a rotary tool / fine hacksaw; wear a
  mask (CF dust). 10 pcs → plenty. ⚠️ Note: a **separate** 2×250 mm rod order (EasyHome1) is for an
  unrelated project — not this build.

---

### Carbon fibre tube 500 × 8 × 6 mm (×16) — main spars / spine
- **Category:** Structural (3K CF tube, hollow)
- **Status:** 🛒 in cart (16-pack)
- **Used for:** **main spars & fuselage spine** — 500 mm tubes joined in pairs with 6 mm sleeves into
  ~900 mm runs — [Materials & Airframe → spar plan](../docs/09-materials-airframe.md#spar-plan-final--16-50086-mm-joined-with-6-mm-sleeves)
- **Variant / qty:** 8 mm OD / 6 mm ID × 500 mm · 16 pcs (one "lot")
- **Price:** €33.71 (8×6 mm variant; listing's €12.72 base price is the 3×2 mm size)
- **Link:** https://www.aliexpress.com/item/4000086818185.html

| Spec | Value |
|------|-------|
| Form | 3K carbon fibre tube (hollow, woven) |
| Outer diameter | 8 mm |
| Inner diameter | 6 mm |
| Wall thickness | **1 mm** |
| Length | 500 mm (0.5 m) |
| Qty | 16 pcs |
| Brand | U-Angel-1988 |
| Note | ID tolerance can run ~+0.2 mm (positive) per reviews |

- **Notes:** tubes for spars (stiffer per gram than solid rod). Each full run is **two 500 mm tubes
  joined** with the owned **6 mm OD / 3 mm ID** tube as a press-fit inner sleeve (~0 mm gap), bonded
  with **2-part epoxy** (not CA) — see the [joining method](../docs/09-materials-airframe.md#joining-method-press-fit-sleeve--epoxy).
  ~4 full runs need 8 tubes min; 16-pack gives all runs + spares. The 6 mm ID is sized to accept the
  sleeve. Conductive + CF dust — mask when cutting.

---

### PU wheel 1.5" / 38 mm (×2) — nose/front gear
- **Category:** Hardware (landing-gear wheel)
- **Status:** 🛒 in cart (1 pair)
- **Used for:** **front / nose landing gear wheels** —
  [Materials & Airframe → landing gear](../docs/09-materials-airframe.md#landing-gear-hardware)
- **Variant / qty:** 1.5 inch / 38 mm · 2 pcs (one pair)
- **Price:** €2.50 / pair
- **Link:** https://www.aliexpress.com/item/1005010083954415.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D

| Spec | Value |
|------|-------|
| Diameter | 38 mm (1.5"; listing text says 37 mm) |
| Width / thickness | 15 mm |
| Hub bore | **2.1 mm** |
| Weight | ~4 g each |
| Tyre | PU rubber, lightweight foam-style |
| Hub | plastic |
| Brand / model | NoEnName_Null · LT602 |

- **Notes:** 2.1 mm bore → suits a **2 mm axle** (CF rod or wire). Standard RC-plane wheel, no O-ring
  tricks. **The F35B nose-gear wheel** (currently in cart) — scale-matched. F35B **main gear** is a
  larger wheel ordered later (~55/56 mm). Same listing scales 1.0″–5.0″.

---

### PU wheels 1.75″ (45 mm) + 2.0″ (50 mm) — trainer landing gear
- **Category:** Hardware (landing-gear wheels)
- **Status:** ✅ owned (2 + 2 pcs · ordered 7 Apr 2026)
- **Used for:** **RC trainer plane** — 1× **45 mm** as the trainer **nose** wheel, 2× **50 mm** as the
  trainer **main** gear. **Not used on the F35B** (45 mm off-scale; F35B nose = 38 mm, main = larger,
  ordered later) — [Materials & Airframe → landing gear](../docs/09-materials-airframe.md#landing-gear-hardware)
- **Variant / qty:** 1.75″/45 mm ×2 + 2.0″/50 mm ×2 (same LT602 listing, two sizes)
- **Price:** **€4.59** (45 mm + 50 mm pairs)
- **Source:** AliExpress — PU rubber wheel LT602 (1.75″ + 2.0″)

| Size | Ø | Thick | Bore | Weight |
|------|-----|-------|------|--------|
| 1.75″ | 43–45 mm | 15 mm | **2.1 mm** | ~5 g |
| 2.0″ | 50 mm | 19 mm | **2.6 mm** | ~7 g |

- **Notes:** PU rubber, plastic hub — same family as the 38 mm nose-gear wheel above. In use on the
  **trainer** (45 mm nose + 2× 50 mm main). **F35B uses the 38 mm for the nose** and a larger main
  wheel (plan ~55/56 mm, ordered later when cheap/in stock) — the 45 mm is off-scale for the F35B.
  ⚠️ Bores differ: 1.75″ = **2.1 mm** (2 mm axle), 2.0″ = **2.6 mm** (thicker axle / bushing).

---

### Deli 502 super glue (CA) — 15 g × 3 — fast bonds / panels
- **Category:** Adhesive (cyanoacrylate, thin/instant)
- **Status:** 🛒 in cart (3 bottles)
- **Used for:** **fast foam/CF tacking, panels, small parts** — *not* spar joints (use epoxy) —
  [Materials & Airframe → adhesives](../docs/09-materials-airframe.md#adhesives--misc)
- **Variant / qty:** 15 g · 3 bottles
- **Price:** €6.54 (€3.48 item + €3.06 shipping; ~€2.18/bottle)
- **Link:** https://www.aliexpress.com/item/1005010806670083.html

| Spec | Value |
|------|-------|
| Type | cyanoacrylate (CA, "502"), thin/instant |
| Net weight | 15 g per bottle (×3) |
| Bonds | metal, plastic, wood, rubber, paper, leather, ceramic |
| Set time | ~10 s pressure; full cure slower |
| Brand / model | Deli 502 (No. 7147) |
| Hazard | ⚠️ H315 skin / H319 eye irritant; bonds skin in seconds |

- **Notes:** ⚠️ **CA is too brittle for spar joints** — those use **2-part epoxy** (works in shear, not
  tension). Use 502 for quick tacks, panel/diffuser bonding, and non-structural parts. One drop per
  in², clamp briefly. Keep tip clear; store cool/dry. Thin CA wicks into tight gaps (capillary).

---

### Carbon fibre tube 6 OD / 3 ID / 400 mm (×10) — joining sleeves
- **Category:** Structural (CF tube, hollow)
- **Status:** ✅ owned (2× 5-pack = 10 pcs · ordered 12 May 2026)
- **Used for:** **press-fit inner sleeves** to join the 500 mm 8 mm spar tubes (6 mm OD → 6 mm ID =
  ~0 mm-gap fit), plus secondary structure / 3BSM supports / ribs —
  [Materials & Airframe → joining method](../docs/09-materials-airframe.md#joining-method-press-fit-sleeve--epoxy)
- **Variant / qty:** 6 mm OD / 3 mm ID × 400 mm · 10 pcs (2 packs of 5)
- **Price:** €12.58 (€6.29 × 2 packs)
- **Link:** https://www.aliexpress.com/item/1005008542386669.html

| Spec | Value |
|------|-------|
| Form | hollow round CF tube |
| Outer diameter | 6 mm |
| Inner diameter | 3 mm |
| Wall thickness | **1.5 mm** |
| Length | 400 mm |
| Qty | 10 pcs |
| Material | carbon fibre |

- **Notes:** the **6 mm OD slides into the 8 mm spar tube's 6 mm ID** as a 0 mm-gap interference fit —
  bond with **2-part epoxy** (shear), cut ~80–100 mm lengths (~50 mm into each side). See the
  [8 mm spar card](#carbon-fibre-tube-500--8--6-mm-16--main-spars--spine) and
  [joining method](../docs/09-materials-airframe.md#joining-method-press-fit-sleeve--epoxy). Also handy
  for 3BSM supports, ribs/formers, secondary structure. Conductive + CF dust — mask when cutting.

---

### Neodymium disc magnets N35 5 × 2 mm (×100) — panel / hatch closures
- **Category:** Hardware (permanent magnets)
- **Status:** ✅ owned (100 pcs · ordered 2 Apr 2026)
- **Used for:** **removable panels / hatches** (battery hatch, canopy, access covers) — magnets
  embedded in printed parts — [Materials & Airframe → magnets](../docs/09-materials-airframe.md#magnets)
- **Variant / qty:** 5 mm dia × 2 mm · 100 pcs
- **Price:** **€5.22** (incl. shipping)
- **Source:** AliExpress — N35 NdFeB round magnets (5 × 2 mm, 100 pc)

| Spec | Value |
|------|-------|
| Material | NdFeB neodymium, **grade N35** |
| Coating | **Ni–Cu–Ni** triple nickel plating (corrosion-resistant) |
| Shape / size | round disc, **5 mm dia × 2 mm** |
| Qty | 100 pcs |
| Tolerance | ±0.6 mm |
| Max operating temp | **80 °C** (176 °F) |
| Composition (lab) | Fe 64.8 · Nd 4.40 · Gd 3.45 · Pr 1.80 · B 0.97 % — no Sm/Tb/Dy/Lu/Sc/Y |
| Certification | RoHS; Ningbo Customs report 2500004639 (2025-09-17, tested on a 6×3 mm sample of the same family) |

- **Notes:** glue pairs into printed seats for magnetic closures (**mind polarity — mark before
  gluing**). ⚠️ **Keep away from any compass/magnetometer** (GPS-compass module) and the steel ball
  race to avoid interference/attraction. ⚠️ **80 °C limit** — keep clear of EDF/ESC hot spots.
  100 pcs → many hatches + spares. **Ni–Cu–Ni plated** → corrosion-resistant; CA/epoxy bonds to the
  nickel fine. ⚠️ The customs lab measured **~10% total rare-earth** (Nd+Pr+Gd) — low for a sintered
  N35 — so don't over-assume pull force; test hold strength on the actual parts.

---

### Nylon zip ties 2.5 × 150 mm (×200, black) — wiring / harness management
- **Category:** Hardware (cable ties)
- **Status:** ✅ owned (200 pcs · ordered 2 Apr 2026)
- **Used for:** **wire-harness bundling, strain relief, securing cables/components** — general assembly
- **Variant / qty:** black · 2.5 × 150 mm · 200 pcs
- **Price:** **€3.08**
- **Source:** AliExpress — nylon self-locking cable ties (2.5 × 150 mm, black, 200 pc)

| Spec | Value |
|------|-------|
| Material | nylon (self-locking) |
| Width | 2.5 mm |
| Length | 150 mm |
| Colour | black |
| Qty | 200 pcs |

- **Notes:** general wiring/harness management — bundle ESC/servo/EDF leads, strain-relief, tidy runs.
  Black is less visible than white. 200 pcs → plenty. Trim flush after cinching. Listing scales
  100–1000 pcs and 100/150/200 mm lengths.

---

### Polyimide (Kapton) high-temp tape 15 mm × 30 m — insulation / heat masking
- **Category:** Consumable (polyimide film tape)
- **Status:** ✅ owned (1 roll · ordered 1 Apr 2026)
- **Used for:** **high-temp electrical insulation & masking** — protect wiring/LW-PLA near ESC/EDF
  heat, insulate LiPo tabs/solder joints, mask during soldering or painting — general
- **Variant / qty:** 15 mm wide × 30 m · 1 roll (model G536)
- **Price:** **€2.72**
- **Source:** AliExpress — PI gold-finger polyimide tape (15 mm × 30 m)

| Spec | Value |
|------|-------|
| Film | polyimide (PI), amber/brown transparent |
| Adhesive | silicone, **no residue** on removal |
| Width × length | 15 mm × 30 m |
| Temp rating | **220–280 °C** continuous · 300 °C short-term |
| Properties | electrical insulation · solvent / acid-alkali / radiation resistant · anti-static |
| Release liner | fluoroplastic |

- **Notes:** Kapton-type tape for high-temp **electrical insulation** and **masking** — protect LW-PLA
  and wiring from ESC/EDF heat, insulate LiPo tabs/solder joints, mask during soldering/painting
  (peels clean, no residue). Cut with scissors (too tough to tear). 30 m → ample.

---

### Airplac 5 mm foam board 50 × 70 cm (×2) — trainer airframe
- **Category:** Material (paper-faced foam board / kapaline) — **trainer-only**
- **Status:** ✅ owned (2 pcs · 1 used on the trainer, 1 spare · ordered 2 Jun 2026)
- **Used for:** **Phase 1 foamboard trainer** airframe — *not* the F35B (which is 3D-printed LW-PLA)
- **Variant / qty:** 5 mm · 50 × 70 cm · 2 sheets
- **Price:** €14.93 total (€4.99 ea + €4.95 shipping)
- **Source:** **Kärkkäinen** (karkkainen.com) — *not AliExpress* (EAN 3555980100693, art. 103271679)

| Spec | Value |
|------|-------|
| Material | paper-faced lightweight foam board (kapaline) |
| Thickness | 5 mm |
| Sheet size | 50 × 70 cm |
| Qty | 2 (1 used, 1 spare) |
| Working | cuts with a hobby / mat knife |

- **Notes:** trainer-only airframe material — the F-35B airframe is **3D-printed LW-PLA**, so this
  won't be used on it. One sheet already consumed building the trainer; one spare remains (repairs /
  another foamboard build). Listing also offers 3 mm and smaller sizes.

---

### Heat-shrink tubing kit 800 pcs (1–13 mm, 2:1) — wire insulation
- **Category:** Consumable (heat-shrink tubing, assorted)
- **Status:** ✅ owned (800-pc box · ordered 2 Apr 2026)
- **Used for:** **insulating solder joints, strain relief, bundling/colour-coding wires** — general
- **Variant / qty:** mixed-size box, **800 pcs** (1.0–13.0 mm)
- **Price:** **€5.83**
- **Source:** AliExpress — 2:1 heat-shrink tube kit (800-pc box, mixed)

| Spec | Value |
|------|-------|
| Material | PE / cross-linked polyethylene |
| Shrink ratio | **2:1** |
| Sizes | 1.0 / 1.5 / 2.0 / 2.5 / 3.0 / 3.5 / 4.0 / 5.0 / 6.0 / 7.0 / 10 / 13 mm |
| Length | 45 mm pcs (40 mm for 3.5 mm) |
| Shrink temp | ≥84 °C start · ≥120 °C full |
| Op temp | −55 to +125 °C |
| Dielectric | 15 kV · flame-retardant |
| Colours | black + red / yellow / green / blue |

- **Notes:** insulate/strengthen solder joints (ESC/EDF/servo/LED leads), strain-relief, colour-code
  wiring. 2:1 → pick a size ~1.5–2× the joint OD. Shrink with a heat gun. ⚠️ When shrinking near
  LW-PLA keep the gun moving (the plastic softens ~53 °C). 800 pcs → ample. Pairs with the
  [Kapton tape](#polyimide-kapton-high-temp-tape-15-mm--30-m--insulation--heat-masking).

---

> Remaining stubs — paste product pages to card:
> stainless button-head screw kit (600 pc).
> *(6805ZZ thin-section bearings dropped — the 3BSM uses the owned 4 mm loose ball race instead.)*
> *(Frosted PP diffuser sheet is carded under [lighting.md](lighting.md).)*

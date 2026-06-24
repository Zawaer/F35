# Components — Structural & Hardware

Cards for filament, carbon tube/rod, bearings, balls, fasteners, wheels, and adhesives. See the
[template & field guide](README.md). Build context: [Materials & Airframe](../docs/09-materials-airframe.md).

---

### eSUN LW-PLA (ePLA-LW) — airframe filament
- **Category:** Filament (lightweight / foaming PLA)
- **Status:** ✅ owned (2 rolls, black)
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

### Carbon fibre rod 2 × 250 mm — pushrods / linkages
- **Category:** Structural (solid CF rod)
- **Status:** 🛒 in cart (10 pcs)
- **Used for:** **pushrods / control linkages** (solid rod for compression/tension) —
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

- **Notes:** solid rod (not tube) — the rule is **rods for pushrods/linkages** (compression/tension),
  **tubes for spars** (stiffer per gram). Conductive — keep clear of exposed electronics. Cuts with a
  rotary tool / fine hacksaw; wear a mask (CF dust). 10 pcs is plenty for all control linkages + spares.

---

### Carbon fibre tube 500 × 8 × 6 mm (×16) — main spars / spine
- **Category:** Structural (3K CF tube, hollow)
- **Status:** 🛒 in cart (16-pack)
- **Used for:** **main spars & fuselage spine** — 500 mm tubes joined in pairs with 6 mm sleeves into
  ~900 mm runs — [Materials & Airframe → spar plan](../docs/09-materials-airframe.md#spar-plan-final--16-50086-mm-joined-with-6-mm-sleeves)
- **Variant / qty:** 8 mm OD / 6 mm ID × 500 mm · 16 pcs (one "lot")
- **Price:** €33.71 (8×6 mm variant; listing's €12.72 base price is the 3×2 mm size)
- **Link:** https://www.aliexpress.com/item/4000086818185.html?mp=1

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
  tricks. This pair is for the **front gear**; remaining wheels (main gear) ordered later. Same listing
  scales 1.0″–5.0″ if a different size is needed.

---

### Deli 502 super glue (CA) — 15 g × 3 — fast bonds / panels
- **Category:** Adhesive (cyanoacrylate, thin/instant)
- **Status:** 🛒 in cart (3 bottles)
- **Used for:** **fast foam/CF tacking, panels, small parts** — *not* spar joints (use epoxy) —
  [Materials & Airframe → adhesives](../docs/09-materials-airframe.md#adhesives--misc)
- **Variant / qty:** 15 g · 3 bottles
- **Price:** €6.54 (€3.48 item + €3.06 shipping; ~€2.18/bottle)
- **Link:** https://www.aliexpress.com/item/1005010806670083.html?mp=1

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
- **Status:** ✅ owned (2× 5-pack = 10 pcs)
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

> Remaining stubs — paste product pages to card:
> stainless button-head screw kit (600 pc).
> *(6805ZZ thin-section bearings dropped — the 3BSM uses the owned 4 mm loose ball race instead.)*
> *(Frosted PP diffuser sheet is carded under [lighting.md](lighting.md).)*

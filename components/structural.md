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

> Remaining stubs — paste product pages to card:
> Known so far: CF tube 8 OD / 6 ID / 500 mm (×16, main spars), CF tube 6 OD / 3 ID / 400 mm
> (×10 owned, joining sleeves), CF rod 2 × 250 mm (×10, linkages), MR62ZZ bearing (2×6×2.5),
> 6805ZZ option, 4 mm steel balls (3BSM race), stainless screw kit, 38 mm PU wheel,
> Deli 502 CA glue. *(Frosted PP diffuser sheet is carded under [lighting.md](lighting.md).)*

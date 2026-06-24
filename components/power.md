# Components — Power

Cards for batteries, BEC/regulators, connectors, and wire. See the [template & field guide](README.md).
Build context: [Power System](../docs/02-power-system.md).

---

### Silicone wire (high-strand, 0.08 mm TS) — power & servo wiring
- **Category:** Wire (silicone-jacket, fine-strand tinned copper)
- **Status:** 🛒 in cart (10AWG); 18AWG & 22AWG bought as separate variants/listings
- **Used for:** **10AWG** = main EDF power; **18AWG** = battery tap + roll-post EDF; **22AWG** =
  servo cables — [Power System](../docs/02-power-system.md)

**Purchases** (same fine-strand silicone family, bought as separate gauge listings):

| Gauge | Qty | Price | Link |
|-------|-----|-------|------|
| 10 AWG | 2 m (1 m red + 1 m black) | €5.01 | https://www.aliexpress.com/item/1005008830721448.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D |
| 18 AWG | 2 m (1 m red + 1 m black) | €1.96 | https://www.aliexpress.com/item/1005007468075329.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D |
| 22 AWG | 10 m (5 m red + 5 m black) | €3.58 | https://www.aliexpress.com/item/1005007468087479.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D |

| Spec (10 AWG) | Value |
|------|-------|
| Conductor | 1050 × 0.08 mm strands, Ø2.92 mm, 5.28 mm² |
| Resistance | 6.30 Ω/km |
| Insulation | silicone, 1.25 mm wall, OD 5.50 mm |
| Rated current | **172 A** |
| Rated voltage | 600 V |
| Temp range | −60 to +200 °C |
| Weight (est.) | ~50 g/m (copper + jacket) |

**Datasheet — gauges used in the build** (same silicone family):

| AWG | Strands | mm² | Ω/km | OD | Rated A | Build use |
|-----|---------|-----|------|-----|---------|-----------|
| 10 | 1050×0.08 | 5.28 | 6.30 | 5.50 mm | 172 A | main EDF power (89 A) |
| 18 | 150×0.08 | 0.75 | 39.5 | 2.30 mm | 24.5 A | battery tap / roll-post EDF (~11–20 A) |
| 22 | 60×0.08 | 0.30 | 88.6 | 1.70 mm | 9.8 A | servo cables (~1 A) |

- **Notes:** all three gauges sit **well within** their rated currents for their roles — see the doc
  correction below. Fine-strand silicone = very flexible, solders easily, 200 °C rated (survives
  near the ESC/EDF). Estimated weights: ~50 g/m (10AWG), ~10 g/m (18AWG), ~5 g/m (22AWG).
- **✅ Corrects the power doc:** the manufacturer rates **10 AWG at 172 A** (RC silicone wire is
  rated far above NEC chassis-wiring figures, and 10 AWG for 80–100 A ESCs is standard RC practice).
  So the earlier "10 AWG marginal at 89 A, keep <200 mm, 8 AWG textbook" caution was overly
  conservative — **10 AWG is adequate** for the main EDF. 18 AWG (24.5 A) likewise comfortably
  covers the ~20 A BEC-tap peak. Updated in [Power System → wire gauge plan](../docs/02-power-system.md#wire-gauge-plan-final).

---

### CNHL MiniStar 850mAh 3S 70C — trainer + roll-post EDF battery
- **Category:** LiPo battery
- **Status:** ✅ ordered (2-pack)
- **Used for:** Phase 1 trainer prop plane; Phase 3 **roll-post 30mm EDFs** — [Propulsion](../docs/06-propulsion.md)
- **Variant / qty:** "2 Packs … 850mAh 3S" · 2 batteries
- **Price:** €14.28 (with coupon; €22.94 list) + €10.38 shipping
- **Source:** **ChinaHobbyLine** (not AliExpress)
- **Link:** ChinaHobbyLine — CNHL MiniStar 850mAh 11.1V 3S 70C with XT30U (stock # 85703G3)

| Spec | Value |
|------|-------|
| Weight | ~80 g (±5 g) each |
| Dimensions | 25 × 30 × 62 mm (±1–5 mm) |
| Chemistry / cells | LiPo, 3S1P (11.1 V nominal) |
| Capacity | 850 mAh |
| Discharge | 70C continuous (≈59.5 A) / 140C burst |
| Charge rate | 5C max (≈4.25 A) |
| Output connector | XT30U (stock) → **re-soldered to XT60H** by the user |
| Balance connector | JST-XH |
| Lead wire | 14 AWG |
| Stock # | 85703G3 |

- **Notes:** 70C × 0.85 Ah ≈ **59.5 A** continuous — ample for two 30 mm roll-post EDFs (~22 A total,
  ~37% of capability). For the Phase 1 trainer it's a small/light pack — note the earlier trainer
  spec assumed 1500–2200 mAh, so 850 mAh means shorter flights (fine for a light foamboard trainer).
- **Connector:** shipped with XT30U, but the user **cut it off and soldered XT60H** on both packs —
  so roll-post power is **XT60H** (matches the docs). See the XT60H connector card below.

---

### XT60H connector (AOKIN) — battery/ESC power connector
- **Category:** Connector (2-pin power, bullet + sheath)
- **Status:** ✅ owned
- **Used for:** roll-post 3S 850 mAh packs (re-soldered on) + roll-post ESC power; general battery
  connectors — [Power System](../docs/02-power-system.md)
- **Variant / qty:** 10 pair with cover · 1 set (10 pairs)
- **Price:** €3.84 (set of 10 pairs)
- **Link:** https://www.aliexpress.com/item/... (AOKIN XT60H, 10 pair with cover)

| Spec | Value |
|------|-------|
| Type | XT60H (XT60 + insulating sheath / cover) |
| Rated current | 30 A continuous, **60 A max** |
| Rated voltage | DC 500 V |
| Contact resistance | 0.5 mΩ |
| Metal | gold-plated copper |
| Insulator | PA nylon, flame-retardant UL94 V0 |
| Wire size (max) | 12 AWG |
| Working temp | −20 to +120 °C |
| Protection | IP40 |
| Mate cycles | 1000 |
| Dimensions | male ~9.2 × 16.4 × 23.5 mm; pin spacing 7.2 mm; +black sheath |
| Weight (est.) | ~7–8 g per mated pair (incl. sheath) |

- **Notes:** XT60-compatible; the "H" adds a clip-on insulating sheath over the solder cups. Needs a
  decent iron + flux; fits ~2.5 mm² (≈12–14 AWG) wire. 60 A max suits the roll-post packs and most
  3S/6S use here.

---

### CNHL G+Plus 5000mAh 6S 70C (EC5) — main EDF battery
- **Category:** LiPo battery
- **Status:** 🔄 **borrowed** (school drone club) — not owned outright
- **Used for:** main (rear) EDF + 18AWG system tap — [Power System](../docs/02-power-system.md)
- **Variant / qty:** 6S 5000 mAh 70C, EC5 · (school order had 2)
- **Price:** €58.82 (school order; list €60.32)
- **Source:** ChinaHobbyLine
- **Link:** ChinaHobbyLine — CNHL G+Plus 5000mAh 22.2V 6S 70C EC5 (stock 500706EC5)

| Spec | Value |
|------|-------|
| Weight | **~714 g** (±5 g) |
| Dimensions | 49 × 51 × 149 mm (H×W×L) |
| Chemistry | LiPo, graphene (G+Plus) |
| Cells | 6S1P, 22.2 V nominal (25.2 V full) |
| Capacity | 5000 mAh |
| Discharge | 70C continuous (≈350 A) / 140C burst |
| Charge rate | 5C max (≈25 A) |
| Output connector | EC5 |
| Balance | JST-XH |
| Lead wire | 10 AWG |
| Stock # | 500706EC5 |

- **Notes:** feeds ESC 1 (main EDF ~89 A) + the system tap to the PDB. 70C × 5 Ah ≈ 350 A theoretical
  → huge headroom over the ~94 A total draw (matches the build's earlier ~11.4 mΩ IR measurement).
  **Heaviest single item (~714 g)** — dominant CG/AUW factor (see
  [CG](../docs/01-project-overview.md#cg-the-central-challenge)).

### CNHL 2700mAh 6S 40C (XT60) — lift EDF battery
- **Category:** LiPo battery
- **Status:** 🔄 **borrowed** (school drone club)
- **Used for:** lift (front) EDF — [Power System](../docs/02-power-system.md)
- **Variant / qty:** 6S 2700 mAh 40C, XT60 · (school order had 4)
- **Price:** €24.06 (school order; list €31.07)
- **Source:** ChinaHobbyLine
- **Link:** ChinaHobbyLine — CNHL 2700mAh 22.2V 6S 40C XT60 (stock 270406XT60)

| Spec | Value |
|------|-------|
| Weight | **~454 g** (±5 g) |
| Dimensions | 45 × 40 × 138 mm |
| Chemistry | LiPo |
| Cells | 6S1P, 22.2 V nominal |
| Capacity | 2700 mAh |
| Discharge | 40C continuous (≈108 A) / 80C burst |
| Charge rate | 5C max (≈13.5 A) |
| Output connector | XT60 |
| Balance | JST-XH |
| Lead wire | 12 AWG |
| Stock # | 270406XT60 |

- **Notes:** feeds ESC 2 (lift EDF). 40C × 2.7 Ah ≈ **108 A** continuous — covers the lift EDF (which
  mostly runs in hover). ⚠️ **40C is lower than the main pack's 70C** — adequate for the lift draw
  but don't push it as hard. Placed forward near the lift fan for CG balance. ~454 g.

> **Battery weight note:** main 714 g + lift 454 g = **~1168 g of battery** on a ~3185 g AUW (~37%).
> Both are **borrowed from the school drone club** — an availability/return constraint to plan
> around, and the packs are larger/heavier than a bespoke choice might be (worth revisiting for CG).

### HOTA D6 Pro — LiPo charger (bench equipment)
- **Category:** Charger (AC/DC dual-channel smart charger) — bench tool, not on-aircraft
- **Status:** 🔄 **borrowed** (school drone club)
- **Used for:** charging/balancing all LiPo packs (main 5000 mAh EC5, lift 2700 mAh XT60, roll-post
  850 mAh) — [Power System → Charging](../docs/02-power-system.md#charging)
- **Variant / qty:** EU plug · 1
- **Price:** €105.96 + €3.18 shipping (list €111.80)
- **Source:** Banggood
- **Link:** Banggood — HOTA D6 Pro AC 200W DC 650W 15A×2 dual-channel charger

| Spec | Value |
|------|-------|
| Weight | ~555–575 g *(listing inconsistent: text 555 g, spec table 575 g)* |
| Dimensions | 108 × 105 × 76 mm |
| Input | AC 100–240 V / DC 6.5–30 V |
| Charge current | 0.1–15 A × 2 channels |
| Charge power | DC 325 W × 2 (650 W, needs >24 V DC in); **AC 200 W total** |
| Discharge | internal 15 W × 2; external 325 W × 2; 0.1–3 A (int) / 1–15 A (ext) |
| Balance current | 1600 mA × 2 |
| Battery support | LiPo/LiHV/LiFe/LiIon 1–6S; NiMH/NiCd/NiZn 1–16S; Pb 2–24 V |
| Output connector | **XT60 × 2** |
| Balance connector | JST-XH |
| Extras | 2.8" 320×240 screen, USB 5 V/2.1 A, Qi wireless pad, IR measurement (while charging) |

- **Notes:** dual channel → charge main + lift packs at once. ⚠️ On **AC it's 200 W total**; the full
  650 W / 15 A×2 needs a **DC supply >24 V** (e.g. a 600–800 W PSU) — fine on AC for moderate C-rates.
  ⚠️ Charger output is **XT60**, but the **main 5000 mAh pack is EC5** → need an **EC5→XT60 charge
  adapter**. Both packs use JST-XH balance leads (match). Reads pack IR while charging. Borrowed.

### Racepow S21700FJ 4000mAh 30A — transmitter cells (Li-ion 21700)
- **Category:** Li-ion cell (21700) — **transmitter power, not aircraft**
- **Status:** ✅ owned (2 cells)
- **Used for:** powering the [Jumper T14 transmitter](flight-control.md) (2× 21700 in series)
- **Variant / qty:** 2 cells
- **Price:** €4.09 each (€8.18 for 2)
- **Source:** Rotorama

| Spec | Value |
|------|-------|
| Chemistry / size | Li-ion, 21700 |
| Capacity | 4000 mAh |
| Dimensions | 21.3 × 70.4 mm |
| Weight | 68 g each |
| Voltage | 4.2 V max / 2.5 V min (~3.6–3.7 V nominal) |
| Discharge | up to 30 A |
| Charge | 0.2–1C |
| Energy density | 217 Wh/kg |
| Protection | none (unprotected cells) |

- **Notes:** these power the **transmitter**, not the aircraft — listed here only to keep all cells
  together. Charged in-radio via the T14's USB-C (10 W). ⚠️ Unprotected cells — rely on the radio's
  charge management; don't over-discharge below 2.5 V.

---

## Still to card (paste product pages)

LM2596 buck (owned) · other connectors (AS150 / XT90 / EC5 / bullet for EDF motors) ·
EC5→XT60 charge adapter (needed for charging the main pack).

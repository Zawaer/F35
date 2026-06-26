# Components — Power

Cards for batteries, BEC/regulators, connectors, and wire. See the [template & field guide](README.md).
Build context: [Power System](../docs/02-power-system.md).

---

### Silicone wire (high-strand, 0.08 mm TS) — power & servo wiring
- **Category:** Wire (silicone-jacket, fine-strand tinned copper)
- **Status:** ✅ owned (all three gauges: 10 / 18 / 22 AWG · ordered 24 Jun 2026)
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
- **Used for:** Phase 1 trainer prop plane; Phase 2 **roll-post 30mm EDFs** — [Propulsion](../docs/06-propulsion.md)
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

- **Notes:** 70C × 0.85 Ah ≈ **59.5 A** continuous — **one pack feeds both roll-post EDFs** (decided):
  ~22 A at nominal, ~29 A at full 12.6 V ≈ **34C** — well within 70C. Full-throttle runtime ~2 min,
  but roll posts run in short hover bursts so capacity is fine. The **2nd pack is a spare**; per-side
  two-pack split rejected (a dead pack → uncommanded roll — see
  [Propulsion → roll-post power](../docs/06-propulsion.md#roll-post-power--wiring)). Trainer use:
  small/light pack (earlier spec assumed 1500–2200 mAh, so 850 mAh = shorter flights — fine).
- **Connector:** shipped with XT30U, but the user **cut it off and soldered XT60H** on both packs —
  so roll-post power is **XT60H** (matches the docs). See the XT60H connector card below.

---

### XT60H connector (AOKIN) — battery/ESC power connector
- **Category:** Connector (2-pin power, bullet + sheath)
- **Status:** ✅ owned (ordered 17 Apr 2026)
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

### CNHL G+Plus 5000mAh 6S 70C (EC5) ×2 — main + lift EDF battery
- **Category:** LiPo battery
- **Status:** 🔄 **borrowed** (school drone club; school order 9 Apr 2026) — not owned outright
- **Used for:** **main (rear) EDF + lift (front) EDF** — one pack each — plus an 18AWG system tap off
  the **lift** pack — [Power System](../docs/02-power-system.md)
- **Variant / qty:** 6S 5000 mAh 70C, **EC5** · **2 in use (main + lift)** — each plugs straight into a
  Skywalker 100A ESC (also EC5)
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

- **Notes:** one pack per fan, each wired **direct to its ESC** (no FC in the high-current path); the
  **lift** pack also carries the 18AWG avionics tap to the PDB. 70C × 5 Ah ≈ 350 A theoretical → huge headroom over each EDF's ~94 A peak. **~714 g each (×2 ≈ 1.43 kg)** — dominant CG/AUW factor; the lift pack is
  **+260 g** vs the old 2700 mAh, shifting CG forward (see
  [CG](../docs/01-project-overview.md#cg-the-central-challenge)).
- **IR baseline (2 Jun 2026, during charge, HOTA D6 Pro):**
  C1 1.5 · C2 1.9 · C3 1.5 · C4 2.2 · C5 2.1 · C6 2.2 mΩ — pack total ~11.4 mΩ. Healthy, balanced (0.7 mΩ spread).

### CNHL 2700mAh 6S 40C (XT60) — spare / fallback lift battery
- **Category:** LiPo battery
- **Status:** 🔄 **borrowed** (school drone club; school order 9 Apr 2026)
- **Used for:** **spare / fallback** — the lift fan now runs a 2nd 5000 mAh pack; this is the lighter
  alternative — [Power System](../docs/02-power-system.md)
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

- **Notes:** **no longer the primary lift battery** — the lift fan now uses a 2nd 5000 mAh pack
  (matched pair). Kept as a **lighter fallback (454 g vs 714 g)** if the +260 g forward weight upsets
  CG: revert to *2700 lift + 5000 main*, or go *2× 2700* (lightest, shortest flight). 40C × 2.7 Ah ≈
  **108 A** — adequate for the lift EDF if used; don't push as hard as the 70C packs.
- **IR baseline (2 Jun 2026, during charge — captured early so may read slightly high, HOTA D6 Pro):**
  C1 5.8 · C2 5.9 · C3 4.5 · C4 6.3 · C5 4.6 · C6 4.8 mΩ — pack total ~31.9 mΩ. Normal for a 40C/2700 mAh cell. 1.8 mΩ spread is fine; recheck at rest for a cleaner baseline.

> **Battery weight note:** main 714 g + lift 714 g = **~1428 g of battery** on a ~3445 g AUW (~41%).
> Both are **borrowed from the school drone club** — an availability/return constraint to plan
> around, and the packs are larger/heavier than a bespoke choice might be (worth revisiting for CG).

### HOTA D6 Pro — LiPo charger (bench equipment)
- **Category:** Charger (AC/DC dual-channel smart charger) — bench tool, not on-aircraft
- **Status:** 🔄 **borrowed** (school drone club; school order 9 Apr 2026)
- **Used for:** charging/balancing all LiPo packs (main + lift 5000 mAh EC5, roll-post
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
  ⚠️ Charger output is **XT60**, but the **main 5000 mAh pack is EC5** → bridged by the owned
  **XT60↔EC5 adapter** (carded below). Both packs use JST-XH balance leads (match). Reads pack IR
  while charging. Borrowed.

### Racepow S21700FJ 4000mAh 30A — transmitter cells (Li-ion 21700)
- **Category:** Li-ion cell (21700) — **transmitter power, not aircraft**
- **Status:** ✅ owned (2 cells · ordered 10 Nov 2025)
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

### LiPo battery straps (hook-and-loop, 200 & 300 mm) ×10 — battery tie-down
- **Category:** Hardware (hook-and-loop battery strap)
- **Status:** ✅ owned (10 pcs total — two orders)
- **Used for:** securing **LiPo packs** (main + lift 5000 mAh, roll-post/trainer 850 mAh) to
  their printed trays — [Power System](../docs/02-power-system.md)
- **Variant / qty:** **5× 300 × 20 mm** (SIRENXI, ordered 17 Apr 2026) + **5× 200 × 20 mm** (Eastern
  Aviation, black, ordered 2 Apr 2026)
- **Price:** €3.25 (300 mm) + €2.95 (200 mm) ≈ **€6.20 total**
- **Source:** AliExpress — SIRENXI (300 mm) & Eastern Aviation (200 mm) nylon battery straps

| Spec | Value |
|------|-------|
| Type | hook-and-loop (Velcro) tie-down strap, self-locking buckle |
| Sizes | 300 × 20 mm (×5) · 200 × 20 mm (×5) |
| Qty | 10 total |
| Material | nylon, **anti-skid** face |

- **Notes:** wrap a pack to its printed tray/floor; the anti-skid face stops it sliding. **300 mm**
  girths the 5000 mAh packs (main + lift, ~20 cm cross-section perimeter) with overlap; **200 mm**
  suits the smaller roll-post / trainer 850 mAh packs. Reusable, no tools. Use alongside a printed battery tray +
  CG positioning (see [CG](../docs/01-project-overview.md#cg-the-central-challenge)).

---

### LiPo safety bag (fireproof) — charging / storage
- **Category:** Safety equipment (fireproof LiPo bag) — **bench, not on-aircraft**
- **Status:** ✅ owned (1 · ordered 1 Apr 2026)
- **Used for:** **safe LiPo charging & storage** — contains a pack fire; for all the build's LiPos
  (main + lift 5000, roll-post/trainer 850 mAh) — [Power System → Charging](../docs/02-power-system.md#charging)
- **Variant / qty:** type4 · 1 pc
- **Price:** **€4.70**
- **Source:** AliExpress — ARRIS-style LiPo Guard safety bag

| Spec | Value |
|------|-------|
| Material | fibreglass (glass-fibre), fire-retardant |
| Dimensions | ~215 × 155 × 115 mm (type4 — confirm on arrival) |
| Closure | hook-and-loop flap |
| Function | fireproof / explosion-resistant, high-temp |
| Colour | silver |

- **Notes:** **always charge/store LiPos in the bag** on a non-flammable surface; never leave a
  charging pack unattended. Big enough for the main 5000 mAh 6S pack (~149 mm long). Reduces (not
  eliminates) damage if a pack vents/ignites. Bench safety gear — not flown. Pairs with the HOTA D6
  Pro charging workflow.

---

### Amass/JHEMCU Smoke Stopper (XT30/XT60, 1–6S) — bench first-power-up fuse
- **Category:** Safety tool (inline resettable fuse) — **bench, not on-aircraft**
- **Status:** ✅ owned (1 · ordered 17 Apr 2026) — bought for the school drone club; usable here as a bench tool
- **Used for:** **smoke-testing new wiring** on first power-up — catches dead shorts before releasing
  the magic smoke — [Power System](../docs/02-power-system.md)
- **Variant / qty:** XT30 & XT60 · 1
- **Price:** €2.79 (already EUR-priced)
- **Source:** AliExpress — JHEMCU/Amass Smoke Stopper

| Spec | Value |
|------|-------|
| Connectors | XT30 **&** XT60 (input + output) |
| Input voltage | 1–6S (3–30 V) |
| Trip current | **1.0 A** |
| Hold current | **0.5 A** |
| Type | resettable PTC fuse, inline battery → device |
| Indicator | green = OK · red = tripped |
| Weight | 14.1 g |

- **Notes:** plug **in series between battery and device** for a first "smoke test" — a short trips
  the fuse (red) instead of frying the board. **Not planned for the F-35B**: the avionics are simple,
  and it's **XT30/XT60, not EC5** (won't fit the 5000 mAh packs). ⚠️ **Bench/no-load only** anyway — the
  0.5 A hold / 1.0 A trip is far below any motor/EDF draw. Kept as general bench / drone-club gear.

---

### XT60↔EC5 charge adapter (XT60F → EC5M) ×4 — charge the EC5 main pack
- **Category:** Connector (charge adapter)
- **Status:** ✅ owned (4 pcs · ordered 14 Apr 2026)
- **Used for:** **charging the EC5 main 5000 mAh pack** on the HOTA D6 Pro (XT60 output) —
  [Power → Charging](../docs/02-power-system.md#charging)
- **Variant / qty:** XT60 female → EC5 male · 4 pcs
- **Price:** €8.21 / 4 pcs (already EUR-priced)
- **Source:** AliExpress — XT60↔EC5/XT90/T/TRX adapter set (XT60F-EC5M)

| Spec | Value |
|------|-------|
| Adapter | **XT60 female → EC5 male** |
| Qty | 4 |
| Path | charger XT60 lead → adapter → EC5 pack |
| Listing | also XT30 / XT90 / EC3 / T(Deans) / TRX variants |

- **Notes:** the HOTA D6 Pro outputs **XT60** but the **main 5000 mAh pack is EC5** — this adapter
  bridges them so the main pack can be charged/balanced. Resolves the previously-flagged adapter gap.
  Bought for the drone-club packs (the main pack is borrowed from the club). **Charge-only** — fine for
  the ≤15 A charge current.

---

### LiPo voltage tester + low-voltage buzzer alarm (1–8S) — field battery check
- **Category:** Tool (cell-voltage meter + LVC buzzer) — **field/bench, not on-aircraft**
- **Status:** ✅ owned (1 · ordered 1 Apr 2026)
- **Used for:** **field per-cell voltage check + audible low-voltage alarm** — plug onto the balance
  lead to verify charge / catch a sagging cell — [Power System](../docs/02-power-system.md)
- **Variant / qty:** 1–8S · 1
- **Price:** **€1.40**
- **Source:** AliExpress — 1–8S LiPo voltage tester / buzzer alarm

| Spec | Value |
|------|-------|
| Cells | 1–8S (LiPo / Li-ion / LiMn / LiFe) |
| Per-cell display | 0.5–4.5 V (±0.01 V) |
| Total display | 0.5–36 V |
| Alarm | buzzer + red LED below set threshold (2–8S) |
| Alarm set | OFF / 2.7–3.8 V (default 3.3 V, saved) |
| Protection | reverse-connection |
| Size / weight | 40 × 25 × 11 mm · 9 g |
| Connection | plugs onto **JST-XH balance lead** |

- **Notes:** plug onto a pack's balance lead → shows each cell + total, and **buzzes if a cell drops
  below the set voltage** — leave it on during ground/hover tests as a live low-voltage warning.
  **Better than a multimeter for the field**: pocket-sized (9 g), reads **all cells at once**, audible
  alarm a meter can't do. (A multimeter still wins for bench work — continuity, current, arbitrary
  points.) Works on all the build's packs (3S/6S, JST-XH balance). Not flown.

---

## Still to card (paste product pages)

LM2596 buck (owned) · other connectors (AS150 / XT90 / EC5 / bullet for EDF motors).

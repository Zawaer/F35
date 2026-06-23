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

## Still to card (paste product pages)

6S 5000 mAh main battery (ChinaHobbyLine) · 6S 2700 mAh lift · 3S 850 mAh roll-post packs ·
LM2596 buck (owned) · connectors (AS150/XT90/EC5/XT60/XT30/bullet).

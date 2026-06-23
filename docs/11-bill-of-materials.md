# Bill of Materials

Master parts list for the Phase 3 F-35B. The tables below reflect the **final AliExpress cart**
(reviewed 23–24 Jun 2026) plus the gaps flagged during that review. Status: ✅ in cart / owned ·
🛒 to add · ⚠️ needs checking. Prices ≈ as seen (€, AliExpress, VAT incl.).

> Cross-references: [Power](02-power-system.md) · [Propulsion](06-propulsion.md) ·
> [Servos](05-servos.md) · [Materials](09-materials-airframe.md) · [Sensors](07-sensors-monitoring.md) ·
> [Lighting](08-lighting.md)

> **Cart totals (snapshot):** subtotal **€210.13**, shipping €14.52, VAT adj −€24.90,
> **customs estimate €47.53**, **total ≈ €243.65**. ⚠️ Customs is ~22% of subtotal — China→Finland
> shipments incur it; budget for it.

## In the cart

| Part | Variant | Qty | €/unit | Use |
|------|---------|-----|--------|-----|
| NEEBRC digital micro servo | 2g plastic gear (M005) | 4 | 4.11 (set) | Small door servos |
| Carbon fibre solid rod | 2×250 mm, 10 pcs | 1 | 3.75 | Pushrods / linkages |
| COB LED strip 12V | green, 3 mm, 1 m | 1 | 2.68 | Accent / nav strip lighting |
| Ball bearing | MR62ZZ 2×6×2.5 mm, 10 pcs | 1 | 3.93 | ⚠️ 3BSM — likely too small (see below) |
| PU rubber wheel | 1.5" / 38 mm | 1 | 2.50 | Landing gear (front) |
| Silicone wire 22AWG | red+black, 10 m | 1 | 3.58 | All servo cables |
| NTC thermistor | 100K B3950, 10 pcs | 2 | 1.30 | Temperature sensing |
| TFT LCD | 1.47" ST7789, 12-pin SPI | 1 | 3.40 | Cockpit display |
| LED bulb 1156 BA15S | P21W, yellow, 12–48V | 1 | 4.11 | Afterburner glow |
| Aluminium heatsink | 14×14×6 mm, 10 pcs | 1 | 2.68 | LED driver cooling |
| ACS712 current sensor | 20A, 3 pcs | 1 | 3.40 | FC/servo rail + roll-post EDFs |
| Carbon fibre tube | 500×8×6 mm (8 OD/6 ID), 16 pcs | 1 | 33.71 | Main spars (joined) |
| Frosted PP sheet | 100×200×0.5 mm, 10 pcs | 1 | 3.83 | LED diffuser |
| 3W LED | white 6500K, 10 pcs | 1 | 1.48 | Strobe / landing accents |
| 3W LED | green 520nm, 10 pcs | 1 | 1.82 | Starboard nav |
| 3W LED | red 625nm, 10 pcs | 1 | 1.82 | Port nav |
| LED driver 700mA | 3W, PWM, constant-current | 4 | 0.70 | Nav lights + strobes |
| 10W LED | 5050 XML-T6, 6500K, 12 mm | 1 | 5.85 | Landing light |
| LED driver 3A | adjustable CC step-down, PWM | 1 | 7.42 | 10W landing light |
| Super glue (Deli 502) | 15 g, 3 bottles | 1 | 3.58 | CA bonding |

### Also in the cart (the unticked state was a UI glitch — all will be ordered)

| Part | Variant | Qty | €/unit | Note |
|------|---------|-----|--------|------|
| Silicone wire 18AWG | red+black, 2 m | 1 | 1.96 | Battery tap to PDB |
| Silicone wire 10AWG | red+black, 2 m | 1 | 5.01 | Main EDF power |
| Servo extension | 200 mm, 10 pcs | 1 | 2.68 | ⚠️ may want 300 mm for some runs |
| 30mm ducted fan EDF | QF1611, 7000KV, 3S (incl. 20A ESC) | 2 | 15.85 | Roll-post motors |
| Feetech STS3032M | 6V 4.5 kg·cm, magnetic encoder | **1** | 34.62 | 3BSM nozzle (sections gear-linked — one servo suffices) |
| FFC/FPC adapter board | 12P, 0.5 mm → 2.54 mm ZIF, 5 pcs | 1 | 2.95 | For cockpit TFT cable |
| IRLZ44N MOSFET | TO-220, 10 pcs | 1 | 2.93 | Switch COB strip / landing light |
| Stainless steel balls | 4 mm, 100 pcs | 1 | 3.54 | 3BSM ball race (see note) |
| CD74HC4067 | 16-channel analog multiplexer | 1 | 1.74 | Expands ADC for NTC thermistors |
| FVT LittleBee 20A ESC | BLHeli_S, DSHOT | 2 | 5.81 | Roll-post EDFs (almost sold out ⚠️) |

## Gaps — ordering later (budget)

| Item | Why | Status |
|------|-----|--------|
| 2 mm bullet connectors | EDF motor connections | 🛒 later |
| Standard RC plane wheels (rear) | Main/rear gear; front 38 mm in cart | 🛒 later |
| MG90S (spares) | Optional spares | 🛒 optional |
| 8AWG (optional) | 10AWG is marginal at 89A main-EDF | ⚠️ optional |

> **STS3032:** only **1** needed — the 3BSM sections are gear-linked, so one smart servo rotates the
> whole nozzle (yaw is a separate MG90S/SG90). The single unit already in the cart is sufficient.
>
> **10W landing-light heatsink:** the **two 14×14×6 mm** heatsinks on hand are **adequate** — it's a
> landing light (brief bursts). At full 3 A (~7–8 W heat, still air) they give ~1–2 min continuous
> from cold before the junction nears its 150 °C limit; real use is 10–30 s with gear-bay airflow.
> Mount the LED to **metal, not LW-PLA**. Only go ≥20×20 mm (or PWM-dim to ~1–1.5 A) for *continuous* use.

### Already covered (no purchase needed)

| Item | Source |
|------|--------|
| MicroSD card | Owned — fitting **later** |
| LM2596 buck converter | Owned (×1) |
| Signal/data wire (~28–30AWG) | ~50 m red + black at school — no coloured set being bought |
| 10kΩ resistors + general resistors/caps | Electronics starter kit + school stock (kit has 10× 10K, 10× 1K, etc.) |
| LiPo low-voltage alarms | Not used — monitoring pack voltage via FC/PDB telemetry instead |
| BA15S bulb socket | Optional — solder leads to the bulb base / print a holder in the afterburner housing |
| 2 mm carbon rod (linkages) | Have 2×250 mm rod 10-pack |
| XT60 connectors | Owned — reusing from 3S 850 mAh packs (roll-post power) |

## Already owned (not in cart)

| Part | Qty | Use |
|------|-----|-----|
| CoreWing F405 WING V2 stack | 1 | FC + PDB + wireless |
| QX-Motor 70mm EDF | 2 | Main + lift |
| 6S 5000 mAh / 2700 mAh LiPo | 1 each | Main / lift EDF |
| NEEBRC 28g (12kg) / 21g (9kg) | 2 / 2 | Flaperons / stabilators |
| MG90S | 7 | Rudders, nose steer, 3BSM yaw, vane box, roll-post doors |
| SG90 | 12 | Misc doors / cosmetics |
| MG996R | 4 | Avoided (too heavy) — spares |
| Carbon tube 6 OD / 3 ID, 400 mm | 10 | Spar joining sleeves + secondary structure |
| Raspberry Pi Pico (RP2040) | 1 | Secondary I/O — see [Pico](04-raspberry-pi-pico.md) |

## Notes

- The **roll-post 30mm EDFs** ship *with* a 20A ESC, yet 2× separate **LittleBee 20A** ESCs are
  also in the cart — decide whether the bundled ESCs suffice and drop the LittleBees, or keep them
  for DSHOT/BLHeli_S response. See [Propulsion](06-propulsion.md#roll-control).
- **3BSM rotation:** uses **4 mm loose steel balls** in a printed race for smooth swivel (the
  4 mm size is intentional). **MR62ZZ** bearings are kept for backup / small gears, not the main
  swivel. See [Materials](09-materials-airframe.md#bearings--3bsm-rotation).
- **Temperature sensing changed** to NTC 100K + CD74HC4067 mux (was DS18B20). See
  [Sensors](07-sensors-monitoring.md).

## Open questions / TODO

- Order bullet connectors + rear wheels later (budget) — not blocking the main order.
- Confirm whether the bundled roll-post-EDF ESCs replace the LittleBees.

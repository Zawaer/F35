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

### Items in cart but not yet selected (✅ confirmed needed — tick them)

| Part | Variant | Qty | €/unit | Note |
|------|---------|-----|--------|------|
| Silicone wire 18AWG | red+black, 2 m | 1 | 1.96 | Battery tap to PDB |
| Silicone wire 10AWG | red+black, 2 m | 1 | 5.01 | Main EDF power |
| Servo extension | 200 mm, 10 pcs | 1 | 2.68 | ⚠️ may want 300 mm for some runs |
| 30mm ducted fan EDF | QF1611, 7000KV, 3S (incl. 20A ESC) | 2 | 15.85 | Roll-post motors |
| Feetech STS3032M | 6V 4.5 kg·cm, magnetic encoder | **3** | 34.62 | ⚠️ only **1** in cart — need **+2** (€69 gap) |
| FFC/FPC adapter board | 12P, 0.5 mm → 2.54 mm ZIF, 5 pcs | 1 | 2.95 | For cockpit TFT cable |
| IRLZ44N MOSFET | TO-220, 10 pcs | 1 | 2.93 | Switch COB strip / landing light |
| Stainless steel balls | ⚠️ 4 mm, 100 pcs | 1 | 3.54 | ⚠️ earlier decided **3 mm** for 3BSM races |
| CD74HC4067 | 16-channel analog multiplexer | 1 | 1.74 | Expands ADC for NTC thermistors |
| FVT LittleBee 20A ESC | BLHeli_S, DSHOT | 2 | 5.81 | Roll-post EDFs (almost sold out ⚠️) |

## Gaps to add before ordering (flagged in cart review)

| Item | Why | Status |
|------|-----|--------|
| **2× more STS3032M** | Need 3 total for 3BSM | ❌ critical |
| LM2596 buck converter (5 pc) | 6V→4.0V rail for small door servos | ❌ |
| MicroSD card 8–16 GB | ArduPilot blackbox logging | ❌ |
| MG90S (5 pc) | Need 1 more + spares | ❌ |
| 28AWG wire, 7 colours, 5 m each | All signal/data/sensor wiring | ❌ |
| 2 mm bullet connectors | EDF motor connections | ❌ |
| XT30 connectors | Roll-post ESC power | ❌ |
| 10kΩ resistors | NTC voltage dividers + STS3032 half-duplex | ❌ |
| Resistor assortment | Voltage dividers | ❌ |
| O-ring assortment | Wheels | ❌ |
| LiPo alarms ×4 | Battery safety | ❌ |
| BA15S bulb socket | Afterburner mounting | ❌ |
| 2 mm carbon rod | Linkages (have 2×250 mm rod pack — may suffice) | ⚠️ |
| Rear wheel ~50 mm | Front 38 mm in cart; confirm rear size | ⚠️ |
| Larger heatsink (≥20×20 mm) for 10W LED | 14×14 too small alone (or stack two) | ⚠️ |
| 8AWG (optional) | 10AWG is marginal at 89A main-EDF | ⚠️ |

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
- **Bearings:** MR62ZZ (2×6×2.5) is in the cart but flagged as marginal for the 3BSM centre shaft;
  MR115ZZ (5×11×4) was recommended as a better fit. The big 3BSM section bearings are still the
  **6805ZZ** sizing — confirm what's actually needed. See [Materials](09-materials-airframe.md#bearings-3bsm).
- **Temperature sensing changed** to NTC 100K + CD74HC4067 mux (was DS18B20). See
  [Sensors](07-sensors-monitoring.md).

## Open questions / TODO

- Add the 2× STS3032M and the gap items above, then re-total.
- Resolve steel-ball size (3 vs 4 mm) and 3BSM bearing choice.
- Confirm whether bundled roll-post ESCs replace the LittleBees.

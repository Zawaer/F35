# Bill of Materials

Master parts list for the F-35B build. This **mirrors the component cards** in
[`components/`](../components/) — those cards are the source of truth (full specs, links, order
dates). Status: ✅ owned/ordered · 🛒 in cart (to buy) · 🔄 borrowed. Prices in € (AliExpress VAT
incl., or the listed source). USD orders were converted at the order-date rate; see the cards.

> Cross-references: [Power](02-power-system.md) · [Propulsion](06-propulsion.md) ·
> [Servos](05-servos.md) · [Materials](09-materials-airframe.md) · [Sensors](07-sensors-monitoring.md) ·
> [Lighting](08-lighting.md) · [Flight Controller](03-flight-controller.md)

> ⚠️ **Customs:** China→Finland AliExpress orders incur ~22% import VAT/customs — budget for it on the
> in-cart total.

## ✅ Owned / ordered

### Propulsion (F-35B + trainer)
| Part | Qty | € | Notes |
|------|-----|---|-------|
| QX-Motor 70 mm EDF QF3027 2200KV 6S (1 CW + 1 CCW) | 2 | 105.14 | Main + lift fan · 12 May 2026 |
| Hobbywing Skywalker 100A V2 ESC | 2 | 70.26 | Main + lift EDF ESCs · 12 May 2026 |
| A2212 2200KV power kit (motor + 40A ESC + 2× SG90 + props) | 1 | 18.46 | Phase-1 trainer · 12 May 2026 |
| XXD A2212 1400KV + 30A ESC | 1 | 11.10 | Trainer (low-KV option) · 17 Apr 2026 |
| EP-6035 propellers | 4 | 1.75 | Trainer prop spares · 7 Apr 2026 |
| Gemfan 8×4 propellers | 2 | 3.34 | Trainer (1400KV) · 17 Apr 2026 |
| QX-Motor 30 mm EDF QF1611 7000KV 3S | 2 | 39.06 | Roll-post thrusters (bundled ESCs = spares) · 24 Jun 2026 |
| FVT LittleBee 20A ESC (BLHeli_S) | 2 | 11.56 | Roll-post chosen ESCs · 24 Jun 2026 |

### Servos & linkage hardware
| Part | Qty | € | Notes |
|------|-----|---|-------|
| NEEBRC NB-S011M 12 kg metal-gear servo | 2 | 15.75 | Flaperons · 2 Apr 2026 (measured 28 g) |
| NEEBRC NB-S007M 9 kg metal-gear servo | 2 | 11.54 | Stabilators · 1 Apr 2026 (21 g) |
| MG90S 9 g metal-gear servo | 10 | 19.41 | Rudders / 3BSM yaw / vane box · 7 Apr 2026 |
| SG90 9 g servo (180°) | 10 | 10.34 | Doors / cosmetic · 2 Apr 2026 |
| MG996R 13–15 kg servo | 4 | 8.97 | Spare / high-torque · 23 Mar + 1 Apr 2026 |
| Servo extension 300 mm | 10 | 2.72 | Long airframe runs · 2 Apr 2026 |
| Servo Y-extension cable 150 mm | 3 | 2.63 | Paired-servo splitter · 7 Apr 2026 |
| Magnetic snap-on 3-pin cable (pair) | 1 | 2.78 | Experimental removable-wing link · 7 Apr 2026 |
| Pushrod linkage stoppers D1.3 mm | 20 | 3.65 | Thin-wire links · 7 Apr 2026 |
| Control horns + clevises (nylon, 21 mm) | 20 sets | 2.70 | Control surfaces · 7 Apr 2026 |
| Z-bend pushrod wires 1.2 mm × 200 mm | 40 | 4.54 | Light pushrods · 7 Apr 2026 |
| 3CH servo / ESC tester (CCPM) | 1 | 2.05 | Bench tool · 1 Apr 2026 |
| Feetech STS3032 360° servo (magnetic encoder) | 1 | 34.62 | 3BSM nozzle rotation · 24 Jun 2026 |
| NEEBRC M005 "2g" (plastic gear) | 4 | 16.44 | Light doors · 24 Jun 2026 |
| Servo extension 200 mm | 10 | 2.68 | Shorter runs · 24 Jun 2026 |

### Power
| Part | Qty | € | Notes |
|------|-----|---|-------|
| CNHL MiniStar 850 mAh 3S 70C | 2 | 14.28 | Trainer + roll-post packs (ordered) |
| XT60H connectors (10-pair set) | 1 | 3.84 | Roll-post power · 17 Apr 2026 |
| Racepow 21700 4000 mAh cells | 2 | 8.18 | T14 transmitter cells · 10 Nov 2025 |
| LiPo battery straps (200 + 300 mm) | 10 | 6.20 | Pack tie-downs · 2 + 17 Apr 2026 |
| LiPo safety bag (fireproof) | 1 | 4.70 | Charging/storage · 1 Apr 2026 |
| Amass/JHEMCU smoke stopper | 1 | 2.79 | Bench first-power-up fuse · 17 Apr 2026 |
| XT60↔EC5 charge adapter | 4 | 8.21 | Charge the EC5 5000 mAh packs · 14 Apr 2026 |
| LiPo voltage tester + buzzer (1–8S) | 1 | 1.40 | Field battery check · 1 Apr 2026 |
| LM2596 buck converter | 1 | — | Had on hand (2g-servo 4 V rail) |

### Flight control & electronics
| Part | Qty | € | Notes |
|------|-----|---|-------|
| CoreWing F405 WING V2 stack | 1 | 66.88 | FC + PDB + wireless · 9 Apr 2026 |
| WeAct Studio RP2040 (avionics) + Raspberry Pi Pico (servo bank) | 1 + 1 | — | Secondary I/O — both owned; WeAct: sensors/LEDs/display, Pico: ~8–10 servo PWM channels |
| Jumper T14 CNC Hall ELRS transmitter | 1 | 123.09 | Radio · 10 Nov 2025 |
| Jumper T14 rocker switch mod | 1 set | 6.51 | Extra TX switches · 9 Apr 2026 |
| RadioMaster RP3 ELRS RX | 1 | 22.03 | On-aircraft RX · 1 Apr 2026 |
| Electronics starter kit (~230 pcs) | 1 | 2.88 | Resistors/headers/proto · 1 Apr 2026 |
| 40-pin breakable headers | 30 | 2.23 | Pico/FC pins · 1 Apr 2026 |
| Dupont jumper wires 15 cm | 240 | 7.87 | Prototyping · 2 Apr 2026 |
| Breadboards MB-102 + 400-pt | 1 ea | 3.79 | Bench prototyping · 1 Apr 2026 |

### Lighting
| Part | Qty | € | Notes |
|------|-----|---|-------|
| 3W LED — white 6500K | 10 | 1.48 | Strobe / landing fallback · 24 Jun 2026 |
| 3W LED — red 625 nm | 10 | 1.82 | Port nav · 24 Jun 2026 |
| 3W LED — green 520 nm | 10 | 1.82 | Starboard nav · 24 Jun 2026 |
| 10W LED 5050 XML-T6 6500K | 1 | 5.85 | Landing light · 24 Jun 2026 |
| COB LED strip 12V (green, 3 mm, 1 m) | 1 | 2.68 | Formation lights · 24 Jun 2026 |
| ACELEX 3W 700mA LED driver | 4 | 5.16 | Nav / strobe drivers · 24 Jun 2026 |
| eletechsup LD2740SC 3A LED driver | 1 | 7.42 | 10W landing-light driver · 24 Jun 2026 |
| IRLZ44N MOSFET (TO-220) | 10 | 3.93 | COB-strip / load switch · 24 Jun 2026 |
| Frosted PP diffuser sheet 100×200×0.5 | 10 | 5.41 | LED diffuser · 24 Jun 2026 |
| Aluminium heatsink 14×14×6 mm | 10 | 2.68 | LED cooling · 24 Jun 2026 |
| YiRui 1156 BA15S P21W bulb (yellow) | 2 | 4.11 | Afterburner glow · 24 Jun 2026 |

### Sensors
| Part | Qty | € | Notes |
|------|-----|---|-------|
| Load cell 10 kg + HX711 | 1 set | 3.29 | Bench thrust test (not flown) · 2 Apr 2026 |
| NTC thermistor 100K B3950 | 20 | 3.56 | Temperature sensing (mux) · 24 Jun 2026 |
| ACS712 20A current sensor | 3 | 3.40 | FC/servo rail + roll-post EDFs · 24 Jun 2026 |
| CD74HC4067 16-ch analog mux | 1 | 1.74 | Expands ADC for NTCs · 24 Jun 2026 |
| 1.47" ST7789 TFT (12-pin SPI) | 1 | 3.40 | Cockpit display · 24 Jun 2026 |
| FFC/FPC adapter board 12P ZIF | 5 | 2.95 | Screen cable breakout · 24 Jun 2026 |

### Structural & consumables
| Part | Qty | € | Notes |
|------|-----|---|-------|
| eSUN LW-PLA filament (black) | 2 rolls | 31.94 | Airframe · 19 May 2026 |
| CF tube 6 OD / 3 ID / 400 mm | 10 | 12.58 | Spar joining sleeves · 12 May 2026 |
| PU wheels 1.75″ + 2.0″ (45/50 mm) | 2 + 2 | 4.59 | Trainer main gear / F35B backup · 7 Apr 2026 |
| N35 neodymium magnets 5 × 2 mm | 100 | 5.22 | Panel/hatch closures · 2 Apr 2026 |
| Nylon zip ties 2.5 × 150 mm (black) | 200 | 3.08 | Harness management · 2 Apr 2026 |
| Polyimide (Kapton) tape 15 mm × 30 m | 1 | 2.72 | High-temp insulation · 1 Apr 2026 |
| Heat-shrink tubing kit (1–13 mm) | 800 | 5.83 | Wire insulation · 2 Apr 2026 |
| Airplac 5 mm foam board 50 × 70 cm | 2 | 14.93 | Trainer airframe (1 used) · Kärkkäinen, 2 Jun 2026 |
| Silicone wire 10 AWG | 2 m | 5.01 | Main EDF power · 24 Jun 2026 |
| Silicone wire 18 AWG | 2 m | 1.96 | Battery tap / roll-post · 24 Jun 2026 |
| Silicone wire 22 AWG | 10 m | 3.58 | Servo cables · 24 Jun 2026 |
| CF tube 500 × 8 × 6 mm | 16 | 33.71 | Main spars (joined) · 24 Jun 2026 |
| CF solid rod 2 × 250 mm | 10 | 3.75 | Door joints / light linkages · 24 Jun 2026 |
| 304 stainless balls 4 mm | 100 | 3.54 | 3BSM loose ball race · 24 Jun 2026 |
| MR62ZZ ball bearing | 10 | 3.93 | Backup / small gears · 24 Jun 2026 |
| PU wheel 38 mm (1.5″) | 2 | 2.50 | F35B nose gear · 24 Jun 2026 |
| Deli 502 CA glue (15 g) | 3 | 6.54 | Fast bonds · 24 Jun 2026 |

## 🔄 Borrowed (school drone club — ordered 9 Apr 2026)
| Part | Qty | € | Notes |
|------|-----|---|-------|
| CNHL G+Plus 5000 mAh 6S 70C (EC5) | 2 | 58.82 | Main + lift EDF (one each) |
| CNHL 2700 mAh 6S 40C (XT60) | 1 | 24.06 | Spare / fallback lift pack |
| HOTA D6 Pro charger | 1 | 105.96 | Bench (Banggood) |

## Buy later / gaps
| Item | Why | Status |
|------|-----|--------|
| MicroSD card — Maxell 32GB SDHC Class 10 | ArduPilot blackbox logging (SDHC ≤32GB, FAT32 — no SDXC). [Tokmanni €10.99](https://www.tokmanni.fi/muistikortti-32gb-micro-sd-4902580745264) · [Puuilo €12.99](https://www.puuilo.fi/maxell-micro-sdhc-muistikortti-32gb-class-10-adapteri) (backup if Tokmanni OOS) | 🛒 when needed |
| GPS module | ArduPilot VTOL altitude / position hold (EKF) | 🛒 later — post-validation, budget |
| Downward rangefinder / lidar | Precise low-altitude hover hold (TF-Luna / VL53L1X) | 🛒 later — post-validation, budget |
| 2 mm bullet connectors | EDF motor leads | 🛒 later |
| Main / rear landing wheels (55–56 mm) | F35B main gear (38 mm nose ordered) | 🛒 later |
| Matek 150A current sensor | Main/lift EDF current logging (>20A) | ⚠️ optional |
| Stainless button-head screw kit (600 pc) | General fasteners | 🛒 to card |
| Biltema Pika Epoksi 2×21 g (€3.55) | Spar joints + tube sockets (CA too brittle) — [Biltema](https://www.biltema.fi/rakentaminen/liimat/epoksiliimat/pika-epoksi-2-x-21-g-2000050118) | 🛒 to buy |

## Key decisions
- **Roll-post ESCs:** use the 2× FVT **LittleBee 20A** (cheap, BLHeli_S/DSHOT); the 20A ESCs bundled
  with the 30 mm EDFs are kept as **spares**.
- **3BSM rotation:** **4 mm loose steel ball race** (printed groove); MR62ZZ = backup; **6805ZZ
  dropped** (not bought). One **STS3032** suffices (sections gear-linked); yaw is a separate MG90S/SG90.
- **Temperature:** NTC 100K + CD74HC4067 mux (one shared 47 kΩ divider); **DS18B20 dropped**.
- **Current:** 3× ACS712 20A owned — **2 used** (both roll-post EDFs), 1 spare; avionics-tap current
  read by the PDB. Read via 2 spare mux channels. Main/lift EDF current **not logged** in v1 (Matek
  150A optional, buy-later).
- **Batteries:** **two 5000 mAh 6S** packs (one per fan) — lift +260 g vs the old 2700 mAh (now spare),
  AUW ~3445 g. Fallbacks: 2700 lift + 5000 main, or 2× 2700.
- **Secondary controller:** **two RP2040 boards** — WeAct Studio (avionics: sensors + screen + LEDs)
  + Raspberry Pi Pico (servo bank: ~8–10 PWM channels); one board can't fit the pin/ADC budget. No
  spare. ESP32-S3 stash kept for bench/ground tooling.

## Related
[Power System](02-power-system.md) · [Propulsion](06-propulsion.md) · [Servos](05-servos.md) ·
[Sensors & Monitoring](07-sensors-monitoring.md) · [Materials & Airframe](09-materials-airframe.md)

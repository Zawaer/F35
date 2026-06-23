# Bill of Materials

Master parts list for the Phase 3 F-35B. Status: ✅ owned · 🛒 to buy · 🛒 Maybe (conditional) ·
🛒 Local (local pickup). Prices are approximate (€, mostly AliExpress / local Finland).

> Cross-references: [Power](02-power-system.md) · [Propulsion](06-propulsion.md) ·
> [Servos](05-servos.md) · [Materials](09-materials-airframe.md) · [Sensors](07-sensors-monitoring.md) ·
> [Lighting](08-lighting.md)

## Priority buy order

| # | Item | Why |
|---|------|-----|
| 1 | 2× Hobbywing 100A V2 ESC | Can't test EDFs without |
| 2 | 6805ZZ bearings | Needed before 3BSM modeling |
| 3 | ELRS receiver | Needed to configure FC |
| 4 | LW-PLA + PETG filament | Airframe build |
| 5 | CF tube 10×6.1 mm (or local Al tube) | Wing spars |
| 6 | Raspberry Pi Pico | Secondary servos |
| 7 | NEEBRC servos (if any gap) | When airframe ready |
| 8 | Landing-gear hardware | Late build stage |
| 9 | Roll-post motors | Confirmed needed (no bleed air) |
| 10 | Finishing materials | Last stage |

## Propulsion / power

| Part | Qty | Status | Notes |
|------|-----|--------|-------|
| Hobbywing 100A V2 ESC | 2 | 🛒 | EDF main + lift |
| QX-Motor 70mm EDF | 2 | (own/order) | Main + lift, 6S |
| Roll-post micro motor (30mm EDF or 2812+3") | 2 | 🛒 | Wingtip roll, no bleed air |
| Roll-post ESC 10–15A | 2 | 🛒 | For wingtip motors |
| 6S 5000 mAh LiPo | 1 | (own) | Main EDF + system tap |
| 6S 2700 mAh LiPo | 1 | (own) | Lift EDF |
| Hobbywing 3A UBEC | 1–2 | 🛒 | €1.68, VTOL servo rail (if split needed) |
| 18AWG silicone wire | 1 m | 🛒 | Battery tap |
| 10AWG silicone wire | — | 🛒 | EDF/ESC main leads |
| XT90 connector pairs | 4 | 🛒 | ESC connections |
| EC5→XT90 adapter | 2 | 🛒 | 5000 mAh to ESC |
| XT60→XT90 adapter | 2 | 🛒 | Charger to batteries |
| AS150 connector | — | 🛒 Maybe | Only if consolidating to single battery |
| Heat shrink assorted | 1 pack | 🛒 | Everywhere |

## Flight control / electronics

| Part | Qty | Status | Notes |
|------|-----|--------|-------|
| CoreWing F405 WING V2 stack | 1 | (own) | FC + PDB PLUS + wireless |
| ELRS receiver | 1 | 🛒 | USART6 on F405 |
| Raspberry Pi Pico | 1 | 🛒 | ~€4, secondary servos + temp + LEDs |
| DS18B20 temp sensor | 20 pack | 🛒 | ~€4, 4 used + spares |
| Matek 150A current sensor | 2 | (own/order) | Per battery lead |
| INA219 power monitor | 1 | 🛒 Maybe | Optional servo-rail current logging |
| 4.7kΩ resistor | 5 | 🛒 | DS18B20 pull-up |
| 10kΩ resistor | 5 | 🛒 | STS3032 UART half-duplex |
| Servo extension 30 cm | 10 | 🛒 | Flight-surface servos |
| Servo Y-splitter | 2 | 🛒 | If merging signals |
| Dupont connector kit | 1 | 🛒 | General wiring |

## Servos

| Part | Qty | Status | Notes |
|------|-----|--------|-------|
| NEEBRC 12kg (28g) | 2 | ✅ | Flaperons |
| NEEBRC 9kg (21g) | 2 | ✅ | Stabilators |
| MG90S | 7 | ✅ | Rudders, nose steer, 3BSM yaw, vane box, roll-post doors |
| SG90 | 12 | ✅ | Gear doors, lift-fan doors, canopy, nozzle |
| Feetech STS3032 | 3 | ✅ ordered | 3BSM sections (2) + spare |
| MG996R | 4 | ✅ | Avoided in build (too heavy) — spares/other projects |

## 3BSM mechanism

| Part | Qty | Status | Notes |
|------|-----|--------|-------|
| 6805ZZ bearing (37×25×7) | 10 pack | 🛒 | Buy before modeling |
| PETG filament | 1–2 rolls | 🛒 | 3BSM sections |
| ABS/ASA filament | 1 roll | 🛒 | Motor mounts, heat parts |
| M2 / M3 screw kit (600 pc) | 1 | 🛒 | General + 3BSM assembly |
| Linkage rods 2 mm + clevises | pack | 🛒 | Servo linkages |
| M2 threaded rod 500 mm | 1 | 🛒 | Adjustable linkages |

## Airframe materials

| Part | Qty | Status | Notes |
|------|-----|--------|-------|
| LW-PLA filament | 2–3 rolls | 🛒 | Main airframe |
| PETG filament | 1–2 rolls | 🛒 | Structural |
| ASA filament | 1 roll | 🛒 | Heat-critical |
| CF tube 10×6.1 mm 500 mm | 4 | 🛒 | Wing spars (joined) |
| CF rod 4 mm 500 mm | 4 | 🛒 | Spar sleeve joints |
| CF rod 1.5–2 mm 500 mm | pack | 🛒 | Pushrods |
| Aluminium tube 10 mm 1000 mm | 2 | 🛒 Local | Wing spars (CF alt), Bauhaus |
| Plywood 3 mm sheet | small | 🛒 | Reinforcement plates |
| Thin CA glue | 2 | 🛒 | Foam/CF bonding |
| Thick CA glue | 1 | 🛒 | Gap filling |
| CA accelerator | 1 | 🛒 | Cure speed |
| 30-min epoxy | 2 | 🛒 | Structural bonds |
| M2/M3 nyloc nuts | pack | 🛒 | Vibration-prone joints |
| Threadlocker (Loctite blue) | 1 | 🛒 | Prevent loosening |

## Landing gear

| Part | Qty | Status | Notes |
|------|-----|--------|-------|
| Custom 3D-printed retracts | 3 | 🛒 design | Over-centre lock + 90° wheel twist; no COTS units |
| Wheels | 3 | 🛒 | Main ×2 + nose |
| Strut wire 3–4 mm | 3 | 🛒 | Or complete strut set |

## Lighting

| Part | Qty | Status | Notes |
|------|-----|--------|-------|
| 3W LED red / green / white | 10 each | ✅ | Nav + strobe |
| 3W 700mA PWM LED driver | 3–4 | 🛒 | €1.86 each |
| Heatsink 7×7×6 mm | few | 🛒 | For 3W LEDs/strobes |

## Tools

| Tool | Status |
|------|--------|
| Clamp meter (e.g. SNAKOL SK-203) | 🛒 — EDF testing |
| Digital calipers | 🛒 if not owned (~€8, essential for printing) |
| Soldering iron (fine tip) | ✅ |
| Heat gun | 🛒 if not owned |
| Hex driver set M2/M3 | 🛒 if not owned |

## Open questions / TODO

- Confirm whether QX-Motor EDFs and Matek sensors are already in hand or still to order.
- Resolve CF vs local aluminium spar purchase.
- Finalise roll-post motor choice (30mm micro EDF vs prop) — see [Propulsion](06-propulsion.md#roll-control).

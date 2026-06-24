# Components — Servos

Cards for all servos. See the [template & field guide](README.md).
Build context: [Servos](../docs/05-servos.md).

---

### Feetech STS3032 (STS3032M) — 3BSM serial-bus smart servo
- **Category:** Servo (TTL serial-bus, magnetic encoder, 360°)
- **Status:** ✅ owned
- **Used for:** **3BSM nozzle rotation** — one servo drives all gear-linked sections — [Servos](../docs/05-servos.md#3bsm-actuation--single-sts3032--gear-linked-sections)
- **Variant / qty:** STS3032M · 1
- **Price:** €34.62
- **Link:** https://www.aliexpress.com/item/1005008704310197.html?mp=1

| Spec | Value |
|------|-------|
| Weight | 20.6 ±1 g |
| Body size | 23.2 × 12.1 × 28.5 mm (~32 mm length incl. mounting tabs) |
| Torque | 4.5 kg·cm @ 6 V |
| Speed | 0.09 s/60° @ 6 V (stall ~111 RPM) |
| Voltage | 4.8–6 V (operating 4–7.4 V) |
| Current | ~150 mA @ 6 V running |
| Motor | coreless |
| Gear | metal (copper + steel), ball bearings |
| Horn | 25T, OD 4.95 mm (M2.3 spline) |
| Sensor | 12-bit magnetic encoder (4096 pos, 0.088° resolution) |
| Rotation | 360° absolute (0–4096); ±7-turn multi-turn (turns not saved on power loss) |
| Interface | **TTL half-duplex serial bus**, 38400 bps–1 Mbps; up to 253 IDs daisy-chained |
| Feedback | position, speed, load, voltage, current, temperature |
| Modes | position / speed closed-loop / speed open-loop / step |
| Protection | overheat / overcurrent / overvoltage / overload (self-unload) |
| Includes | servo, 25T metal + plastic horns, screws, TTL bus adapter board, cables |

- **Notes:** continuous 360° rotation *with* absolute position feedback — why it suits the 3BSM
  (standard PWM servos can't). Half-duplex bus → uses the **10kΩ resistor** UART trick (covered by
  the kit). Power from the 6 V servo rail. Built-in temp/current feedback is a bonus for monitoring.
- **⚠️ Listing inconsistencies:** case material — title says **"Metal Case"** but the description
  says **engineering-plastic / "Plastic Case"** (the docs had assumed metal; verify on the unit).
  Gear ratio quoted as both **1:205** and **1:345**. Body dims 23.2×12.1×28.5 mm vs the "32×12×27.5"
  figure (latter includes mounting tabs).

---

### NEEBRC NB-M005 "2g" — door micro servo
- **Category:** Servo (micro, PWM, coreless)
- **Status:** ✅ owned (4 pcs)
- **Used for:** lightweight **doors** (gear doors / lift-fan doors) — [Servos](../docs/05-servos.md)
- **Variant / qty:** 2g Plastic Gear · 4
- **Price:** €4.11 each (€16.44 for 4)
- **Link:** https://www.aliexpress.com/item/1005010177333036.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D

| Spec | Value |
|------|-------|
| Weight | ~3.3 g (plastic gear; "2g" is just the model name) |
| Size | 16.7 × 8.2 × 17 mm |
| Torque | ~0.3 kgf·cm |
| Speed | 0.08 s/60° @3.7 V · 0.06 s/60° @4.2 V |
| Voltage | **3.7–4.2 V** (1S; **max 4.2 V**) |
| Stall current | ≤320 mA @3.7 V / ≤350 mA @4.2 V |
| No-load current | ≤50–60 mA |
| Travel | 180° ±10° (500–2500 µs) |
| Interface | PWM |
| Motor / gear / case | coreless / plastic / ABS |
| Connector | JR 3-pin, ~145–200 mm lead |

- **Voltage = 3.7–4.2 V (max 4.2 V).** The spec image, the dimension-sheet table, and the
  speed/current figures all agree on 3.7–4.2 V — and a 2 g micro servo can't take 6 V — so the
  conflicting "4.8–6 V" text/label on the listing is **wrong, disregarded**. **Power via the LM2596
  at 4.0 V** (safely below the 4.2 V max); **never on the 6 V servo rail.** See
  [Servos — small servo voltage](../docs/05-servos.md).

---

### Servo extension cable (JR/Futaba 3-pin) — 200 mm ×10
- **Category:** Cable (servo extension lead)
- **Status:** ✅ owned
- **Used for:** extending servo leads to the FC/Pico across the airframe — [Servos](../docs/05-servos.md)
- **Variant / qty:** 200 mm · 1 set (10 cables)
- **Price:** €2.68 / 10 pcs
- **Link:** https://www.aliexpress.com/item/1005007480672910.html?mp=1&sourceType=570&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D

| Spec | Value |
|------|-------|
| Type | 3-pin JR/Futaba servo extension (signal / + / −) |
| Length | 200 mm |
| Qty | 10 |
| Wire | thin gauge (~26–28 AWG); random colour set (BRW or YRB) |

- **Notes:** ⚠️ **200 mm may be short** for the longest runs (e.g. wingtip → FC on a ~1 m fuselage) —
  the BOM had flagged wanting 300 mm; daisy-chain two or order longer if needed. Thin signal wire is
  fine for servo PWM current.

---

## Still to card (paste product pages)

NEEBRC 28g (12 kg flaperons) · NEEBRC 21g (9 kg stabilators) · MG90S (rudders/VTOL) · SG90 (doors) ·
NEEBRC S002 4.3g (door micro servo) · MG996R (spare). Owned-summary specs in
[Servos doc inventory](../docs/05-servos.md#inventory-on-hand).

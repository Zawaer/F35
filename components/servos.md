# Components — Servos

Cards for all servos. See the [template & field guide](README.md).
Build context: [Servos](../docs/05-servos.md).

---

### Feetech STS3032 (STS3032M) — 3BSM serial-bus smart servo
- **Category:** Servo (TTL serial-bus, magnetic encoder, 360°)
- **Status:** 🛒 in cart
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
- **Status:** 🛒 in cart (4 pcs)
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
- **Status:** 🛒 in cart
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

### SG90 9g micro servo (180°) ×10 — doors / cosmetic actuation
- **Category:** Servo (micro, PWM, analog)
- **Status:** ✅ owned (10 pcs · ordered 2 Apr 2026)
- **Used for:** lightweight **doors / cosmetic actuation** — gear doors, lift-fan doors, roll-post
  inlet/outlet doors; candidate for the **3BSM yaw tilt** — [Servos](../docs/05-servos.md)
- **Variant / qty:** 180° · 10 pcs
- **Price:** $11.93 → **€10.34** (@ €0.8664/$, 2 Apr 2026; ~€1.03/servo)
- **Source:** AliExpress — PYLRC SG90 (180°, 10 pcs)

| Spec | Value |
|------|-------|
| Weight | 10 g ±5% |
| Size | 22.4 × 12.5 × 22.8 mm |
| Torque (lock) | 1.3–1.6 kg·cm @ 4.8–6 V |
| Speed (no load) | 0.09 s/60° |
| Voltage | 4.8–6 V |
| No-load current | 90 mA |
| Lock current | 750 mA ±10% |
| Travel | **180° ±3°** (500–2500 µs) |
| Midpoint | 1500 µs (centering ≤1°) |
| Dead band | 8 µs |
| Interface | PWM · JR 3-pin |
| Gear / motor | plastic gear / brushed |
| Brand | PYLRC |

- **Notes:** standard hobby **SG90** — runs on the **6 V servo rail** (unlike the 1S-only NEEBRC 2 g
  door servos). 180° variant (the listing also sells a 360° continuous-rotation version — not this).
  Ships with horns + screws. 10 pcs → doors + spares.

---

### MG90S 9g metal-gear servo ×10 — rudders / 3BSM yaw / vane box
- **Category:** Servo (micro, PWM, metal gear, ball-bearing)
- **Status:** ✅ owned (10 pcs = 2× 5-pack · ordered 7 Apr 2026)
- **Used for:** higher-load control vs SG90 — **rudders, 3BSM yaw tilt (±~15°), lift-fan vane box** —
  [Servos](../docs/05-servos.md)
- **Variant / qty:** all-metal gear · 5 pcs × 2 = 10
- **Price:** $22.68 → **≈ €19.65** ($11.34 / 5-pack; @ ~€0.8664/$, ~€1.97/servo)
- **Source:** AliExpress — Skyquist MG90S (all-metal, 5 pcs × 2)

| Spec | Value |
|------|-------|
| Weight | 12 g |
| Size | 22.6 × 12.1 × 22.5 mm (mount span ~33 mm) |
| Torque | 1.6 kg·cm @ 4.8 V · **1.8 kg·cm @ 6.0 V** |
| Speed | 0.10 s/60° @ 4.8 V · 0.09 s/60° @ 6.0 V |
| Voltage | 4.8–6.0 V |
| Stall current | 700 mA @ 4.8 V · 900 mA @ 6.0 V (±50 mA) |
| Idle current | 4 ±1 mA |
| Travel | 90°±5° (1000–2000 µs); ~145–180° at 800–2500 µs |
| Neutral | 1500 µs · centering ≤1° |
| Dead band | ~3–5 µs |
| Gear / bearing | **all-metal gear · full ball bearing** |
| Interface | PWM · JR/FP 3-pin, 250 mm lead |
| Brand | Skyquist |

- **Notes:** metal-gear **upgrade of the SG90** (same footprint) — stronger (1.8 vs ~1.5 kg·cm) and
  more durable for load-bearing control surfaces. Runs on the **6 V servo rail**. Ships with horns +
  screws. 10 pcs → rudders + 3BSM yaw + vane box + spares. ⚠️ Listing dead-band quoted 5 µs (text)
  vs ≤3 µs (datasheet drawing).

---

### NEEBRC NB-S011M 12 kg metal-gear servo ×2 — flaperons
- **Category:** Servo (standard-size digital, metal gear, waterproof)
- **Status:** ✅ owned (2 pcs · ordered 2 Apr 2026)
- **Used for:** **flaperons** (high-torque primary control surfaces) — [Servos](../docs/05-servos.md)
- **Variant / qty:** 12 kg metal gear · 2 pcs
- **Price:** $18.18 → **€15.75** ($9.09 each; @ €0.8664/$, 2 Apr 2026)
- **Source:** AliExpress — NEEBRC NB-S011M (12 kg, model N1045); original listing gone

| Spec | Value |
|------|-------|
| Weight | **28 g** (measured; listing said 21 g) |
| Size | 42.3 × 15.4 × 32.1 mm |
| Torque | **12.1 kg·cm** (max) |
| Speed | ≤0.16 s/60° @ 4.8 V · ≤0.14 s/60° @ 6.0 V |
| Voltage | 4.8–6.0 V |
| Stall current | ≤1900 mA @ 4.8 V · ≤2500 mA @ 6.0 V |
| No-load current | ≤120–130 mA |
| Travel | 180° ±10° (500–2500 µs); mech. limit 360° |
| Dead band | ≤1 µs |
| Motor / gear | core motor · **metal gear**, waterproof |
| Horn spline | **25T / Ø5.77 mm** |
| Interface | PWM · JR 3-pin, 250 mm lead |
| Brand / model | NEEBRC NB-S011M (N1045) |

- **Notes:** strong **12 kg·cm** digital servo for the **flaperons**. ⚠️ **High stall current
  (~2.5 A @ 6 V)** — factor into servo-rail BEC headroom for the worst case (see
  [Power → servo rail](../docs/02-power-system.md#servo-rail-headroom--the-marginal-case)). Runs on
  the 6 V rail. 25T spline horns + brass bushings included. Standard-size body (42 mm) — much
  heavier/larger than the SG90/MG90S micros. **Measured 28 g** (the listing's 21 g was low — the
  earlier "28 g" stub estimate was right).

---

### NEEBRC NB-S007M 9 kg metal-gear servo ×2 — stabilators
- **Category:** Servo (mini digital, metal gear, waterproof)
- **Status:** ✅ owned (2 pcs · ordered 1 Apr 2026)
- **Used for:** **stabilators** (all-moving horizontal tail) — [Servos](../docs/05-servos.md)
- **Variant / qty:** 21 g / 9 kg metal gear · 2 pcs
- **Price:** $13.38 → **≈ €11.59** (~$6.69 each; @ ~€0.8664/$, ~1 Apr 2026)
- **Source:** AliExpress — NEEBRC NB-S007M (21 g / 9 kg)

| Spec | Value |
|------|-------|
| Weight | **21 g** (measured; listing 20.7 g) |
| Size | 29.6 × 13.2 × 40 mm |
| Torque | **9 kg·cm** (max) |
| Speed | ≤0.10 s/60° @ 4.8 V · ≤0.12 s/60° @ 6.0 V ⚠️ |
| Voltage | 4.8–6.0 V |
| Stall current | ≤1500 mA @ 4.8 V · ≤1800 mA @ 6.0 V |
| No-load current | ≤200–210 mA |
| Travel | 180° ±10° (1000–2000 µs); mech. limit 360° |
| Dead band | ≤1 µs |
| Motor / gear | core motor · **metal gear**, waterproof |
| Interface | PWM · JR 3-pin, 250 mm lead |
| Brand / model | NEEBRC NB-S007M |

- **Notes:** 9 kg·cm digital servo for the **stabilators** — a step down from the 12 kg
  [NB-S011M flaperon servo](#neebrc-nb-s011m-12-kg-metal-gear-servo-2--flaperons) (smaller body,
  20.7 g vs 21 g but 29.6 × 40 mm). Runs on the 6 V rail; ⚠️ stall ~1.8 A @ 6 V — include in the
  servo-rail BEC budget. Horns + accessories included. ⚠️ Listing speed figures look swapped (6 V is
  normally faster than 4.8 V). Order line showed $6.99 ea but the total billed $13.38 (~$6.69 ea).

---

### Servo Y-extension cable (JR/Futaba 3-pin) — 150 mm ×3
- **Category:** Cable (servo Y-splitter lead)
- **Status:** ✅ owned (3 pcs · ordered 7 Apr 2026)
- **Used for:** driving **two servos from one FC/Pico channel** (paired doors / mirrored surfaces that
  move together) — [Servos](../docs/05-servos.md)
- **Variant / qty:** 150 mm Y-lead · 3 pcs
- **Price:** $3.07 → **≈ €2.66** (@ ~€0.8664/$, 7 Apr 2026; listed $3.29)
- **Source:** AliExpress — RC Servo Y Extension Cable (150 mm, 3 pcs)

| Spec | Value |
|------|-------|
| Type | **Y-splitter** — 1 male → 2 female, JR/Futaba 3-pin |
| Length | 150 mm |
| Qty | 3 |
| Wire | thin gauge (~26–28 AWG) |
| Brand | NoEnName_Null |

- **Notes:** a **Y-cable** (not a straight extension — see the
  [200 mm extension card](#servo-extension-cable-jrfutaba-3-pin--200-mm-10)) — parallels two servos
  onto one channel so both get the same PWM. Good for **paired doors / mirrored surfaces** that always
  move together. ⚠️ Both servos get the **same signal** (no independent trim) and **share BEC current**
  — fine for matched low-load servos; for opposed travel, reverse one servo mechanically. Short at
  150 mm.

---

### MG996R 13–15 kg metal-gear servo ×2 — spare / high-torque
- **Category:** Servo (standard-size digital, metal gear, ball-bearing)
- **Status:** ✅ owned (2 pcs · ordered 23 Mar 2026)
- **Used for:** **spare / general high-torque** standard servo (heavy control surfaces, bench/testing)
  — [Servos](../docs/05-servos.md)
- **Variant / qty:** MG996R · 180° · 2 pcs
- **Price:** €3.21 / 2 pcs (~€1.60 each; already EUR-priced)
- **Source:** AliExpress — HORNAXYS/HNX MG996R (180°, 2 pcs)

| Spec | Value |
|------|-------|
| Weight | ~55 g (typical MG996R) |
| Size | 40 × 19 × 43 mm |
| Torque | 13 kg·cm @ 4.8 V · **15 kg·cm @ 6.0 V** |
| Speed | 0.17 s/60° @ 4.8 V · 0.14 s/60° @ 6.0 V |
| Voltage | **4.8–7.2 V** |
| Motor / gear | coreless · **all-metal gear · double ball bearing** |
| Travel | 180° |
| Horn spline | 25T |
| Interface | PWM · JR 3-pin, 300 mm lead |
| Brand | HORNAXYS / HNX (MG996R clone) |

- **Notes:** classic **MG996R** standard servo — strongest of the owned servos (15 kg·cm @ 6 V) but
  also the **heaviest (~55 g)**, so it's the **spare / high-torque** option rather than a primary
  flight surface (the lighter 9/12 kg NEEBRC servos do the stabilators/flaperons). Tolerates up to
  7.2 V; runs fine on the 6 V rail. ⚠️ MG996R stall draw can be ~2.5 A — mind the BEC. 25T horns
  included.

---

### Magnetic snap-on 3-pin cable (1 pair, 20 cm) — experimental quick-disconnect
- **Category:** Connector (magnetic pogo-pin, 3-pin servo)
- **Status:** ✅ owned (1 pair · ordered 7 Apr 2026) — **experimental / bought to test**
- **Used for:** idea: **quick-disconnect for removable wings** — pass servo signal (+ low-current
  power) across a wing/fuselage joint that auto-separates when the wing comes off — [Servos](../docs/05-servos.md)
- **Variant / qty:** 1 pair · 20 cm leads
- **Price:** $3.25 → **≈ €2.82** (@ ~€0.8664/$, 7 Apr 2026)
- **Source:** AliExpress — 9IMOD magnetic model cable (1 pair, 20 cm)

| Spec | Value |
|------|-------|
| Type | **magnetic snap-on** connector, pogo-pin, **3-pin** |
| Halves | 1 pair (mate magnetically, polarity-protected) |
| Ends | JR/Futaba servo 3-pin (signal / + / −) |
| Lead length | 20 cm each side |
| Pins | ZH1.5 / 2.54 mm, 3P |
| Insulation | soft rubber wire |

- **Notes:** **exploratory** — one pair bought to test the concept of **removable wings** with an
  auto-disconnecting servo link (magnets pull apart cleanly if a wing detaches). Polarity-keyed so it
  can't mate wrong. ⚠️ **Pogo-pin current is limited** — fine for servo signal + a couple of LEDs,
  *not* for EDF/high-current rails. Not yet committed to the design; if removable wings are adopted,
  buy more pairs (one per servo/signal crossing). Soft leads route easily.

---

### 3CH servo tester / ESC checker (CCPM) + AA holder — bench tool
- **Category:** Tool (servo/ESC tester) — **bench tool, not on-aircraft**
- **Status:** ✅ owned (1 · ordered 1 Apr 2026) — **bought for testing**
- **Used for:** **bench-testing PWM servos & ESCs** without a TX/RX — sweep / center / manual; drive
  an ESC throttle to spin a motor — [Servos](../docs/05-servos.md)
- **Variant / qty:** 3CH digital tester + 4× AA battery holder · 1
- **Price:** $2.38 → **≈ €2.06** (@ ~€0.8664/$, 1 Apr 2026)
- **Source:** AliExpress — wishiot 3CH servo tester / CCPM consistency master

| Spec | Value |
|------|-------|
| Channels | 3 (CCPM consistency master) |
| Modes | **Manual** (knob) · **Neutral** (center) · **Automatic** (sweep) |
| Output signal | 1.5 ms ±0.5 ms (1.0–2.0 ms PWM) |
| Input | DC 4.2–6.0 V (4× AA holder included; cells not) |
| Output current | ≤15 mA @ 5 V |
| Size | 46 × 32 × 17 mm |
| Brand | wishiot |

- **Notes:** **bench tool** — center/sweep a servo or drive an ESC throttle without the radio. ⚠️
  Connect the battery holder to the **IN** side, not OUT. PWM only → tests the **SG90 / MG90S / NEEBRC
  / MG996R PWM servos and the ESCs** (LittleBee, Skywalker, EDF ESCs), but **not the STS3032**
  (serial-bus, needs its own driver/software). Good for setting servo neutrals and checking EDF
  spin-up direction. Lights blue when on.

---

## Still to card (paste product pages)

NEEBRC S002 4.3g (door micro servo). Owned-summary specs in
[Servos doc inventory](../docs/05-servos.md#inventory-on-hand).

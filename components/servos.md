# Components — Servos

Cards for all servos. See the [template & field guide](README.md).
Build context: [Servos](../docs/05-servos.md).

---

### Feetech STS3032 (STS3032M) — 3BSM serial-bus smart servo
- **Category:** Servo (TTL serial-bus, magnetic encoder, 360°)
- **Status:** ✅ owned (1 pc · ordered 24 Jun 2026)
- **Used for:** **3BSM nozzle rotation** — one servo drives all gear-linked sections — [Servos](../docs/05-servos.md#3bsm-actuation--single-sts3032--gear-linked-sections)
- **Variant / qty:** STS3032M · 1
- **Price:** €34.62
- **Link:** https://www.aliexpress.com/item/1005008704310197.html

| Spec | Value |
|------|-------|
| Weight | 20 g ±0.2 |
| Body size | 23.2 × 12.1 × 28.5 mm (~32 mm length incl. mounting tabs) |
| Torque | 4.0 kg·cm @ 4.8 V · **4.5 kg·cm @ 6 V** |
| Speed | 0.10 s/60° @ 4.8 V · **0.09 s/60° @ 6 V** |
| Voltage | 4.8–6 V |
| Idle current | 4.8 mA @ 4.8 V · 6 mA @ 6 V |
| No-load current | 125 mA @ 4.8 V · **150 mA @ 6 V** |
| Stall current | 900 mA @ 4.8 V · **1200 mA @ 6 V** |
| Case | **Aluminium alloy** (confirmed from datasheet) |
| Motor | Coreless (空心杯马达) |
| Gear | Metal gear · 2 ball bearings |
| Horn | 25T spline · plastic/POM horn |
| Sensor | Magnetic encoder · 12-bit (4096 pos/rev, 0.088°/step) |
| Rotation | 360° continuous (0–4096 counts) |
| Interface | **TTL half-duplex serial bus**, 38400 bps–1 Mbps; ID range 0–253 |
| Feedback | position, temperature, speed, voltage, load |
| Connector | 200 mm ±5 mm |

- **Notes:** continuous 360° rotation *with* absolute position feedback — why it suits the 3BSM
  (standard PWM servos can't). Half-duplex bus → uses the **10kΩ resistor** UART trick (covered by
  the kit). Power from the 6 V servo rail. Built-in temp/load feedback is a bonus for monitoring.
  ⚠️ **Stall current is 1.2 A @ 6 V** — higher than the ~300 mA estimate; factor into servo-rail budget.
  Gear ratio inconsistency (1:205 vs 1:345 in listing) unresolved but irrelevant to usage.

---

### NEEBRC M005 "2g" (plastic gear) — door micro servo
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

### Servo extension cables (JR/Futaba 3-pin) — 200 & 300 mm, ×10 each
- **Category:** Cable (servo extension lead)
- **Status:** **300 mm ✅ owned** (ordered 2 Apr 2026) · **200 mm ✅ owned** (ordered 24 Jun 2026)
- **Used for:** extending servo leads to the FC/Pico across the airframe — [Servos](../docs/05-servos.md)
- **Variant / qty:** 200 mm ×10 + 300 mm ×10
- **Price:** 200 mm €2.68 · 300 mm **€2.72** (owned, U-Angel-1988)
- **Link:** [200 mm](https://www.aliexpress.com/item/1005007480672910.html) · 300 mm = U-Angel-1988 X501

| Spec | Value |
|------|-------|
| Type | 3-pin JR/Futaba servo extension (signal / + / −) |
| Lengths | 200 mm (×10) · 300 mm (×10) |
| Qty | 10 each |
| Wire | thin gauge (~0.35 mm² ≈ 22 AWG per listing); random colour |

- **Notes:** extend servo leads across the ~1 m airframe. The **300 mm (owned)** covers the long
  wingtip → FC runs that 200 mm can't — resolving the earlier "200 mm may be short" concern; the
  **200 mm (ordered 24 Jun 2026)** suits shorter hops. Thin signal wire is fine for servo PWM current; daisy-chain
  for even longer runs.

---

### SG90 9g micro servo (180°) ×10 — doors / cosmetic actuation
- **Category:** Servo (micro, PWM, analog)
- **Status:** ✅ owned (10 pcs · ordered 2 Apr 2026)
- **Used for:** lightweight **doors / cosmetic actuation** — gear doors, lift-fan doors, roll-post
  inlet/outlet doors; candidate for the **3BSM yaw tilt** — [Servos](../docs/05-servos.md)
- **Variant / qty:** 180° · 10 pcs
- **Price:** **€10.34** (~€1.03/servo)
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

### MG90S 9g metal-gear servo ×12 — rudders / 3BSM yaw / vane box
- **Category:** Servo (micro, PWM, metal gear, ball-bearing)
- **Status:** ✅ owned (10 pcs = 2× 5-pack, ordered 7 Apr 2026 · +2 pcs from STUHI hardware lab, 11 Jul 2026)
- **Used for:** higher-load control vs SG90 — **rudders, 3BSM yaw tilt (±~15°), lift-fan vane box** —
  [Servos](../docs/05-servos.md)
- **Variant / qty:** all-metal gear · 5 pcs × 2 (ordered) + 2 (STUHI) = 12
- **Price:** **€19.41** (2× 5-pack; ~€1.94/servo) — the 2 STUHI units were free
- **Source:** AliExpress — Skyquist MG90S (all-metal, 5 pcs × 2) + 2 from STUHI hardware lab

| Spec | Value |
|------|-------|
| Weight | 12 g |
| Size | 22.6 × 12.1 × 22.5 mm (mount span ~33 mm) |
| Torque | 1.6 kg·cm @ 4.8 V · **1.8 kg·cm @ 6.0 V** |
| Speed | 0.10 s/60° @ 4.8 V · 0.09 s/60° @ 6.0 V |
| Voltage | 4.8–6.0 V |
| Stall current | 700 mA @ 4.8 V · 900 mA @ 6.0 V (±50 mA) |
| Idle current | 4 ±1 mA |
| No-load running current | ~90 mA (confirmed across multiple MG90S manufacturer datasheets) |
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
- **Price:** **€15.75** (~€7.88 each)
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
  [Power → servo rail](../docs/02-power-system.md#servo-rail-headroom)). Runs on
  the 6 V rail. 25T spline horns + brass bushings included. Standard-size body (42 mm) — much
  heavier/larger than the SG90/MG90S micros. **Measured 28 g** (the listing's 21 g was low — the
  earlier "28 g" stub estimate was right).

---

### NEEBRC NB-S007M 9 kg metal-gear servo ×2 — stabilators
- **Category:** Servo (mini digital, metal gear, waterproof)
- **Status:** ✅ owned (2 pcs · ordered 1 Apr 2026)
- **Used for:** **stabilators** (all-moving horizontal tail) — [Servos](../docs/05-servos.md)
- **Variant / qty:** 21 g / 9 kg metal gear · 2 pcs
- **Price:** **€11.54** (~€5.77 each)
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
  normally faster than 4.8 V). (Order-line unit price ran higher than the billed total — effective
  ≈ €5.77 each.)

---

### Servo Y-extension cable (JR/Futaba 3-pin) — 150 mm ×3
- **Category:** Cable (servo Y-splitter lead)
- **Status:** ✅ owned (3 pcs · ordered 7 Apr 2026)
- **Used for:** driving **two servos from one FC/Pico channel** (paired doors / mirrored surfaces that
  move together) — [Servos](../docs/05-servos.md)
- **Variant / qty:** 150 mm Y-lead · 3 pcs
- **Price:** **€2.63**
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

### MG996R 13–15 kg metal-gear servo ×4 — spare / high-torque
- **Category:** Servo (standard-size digital, metal gear, ball-bearing)
- **Status:** ✅ owned (4 pcs total — two orders)
- **Used for:** **spare / general high-torque** standard servo (heavy control surfaces, bench/testing)
  — [Servos](../docs/05-servos.md)
- **Variant / qty:** MG996R · 180° · **2× (HNX, 23 Mar 2026) + 2× (JYJD, 1 Apr 2026) = 4 pcs**
- **Price:** €3.21 (HNX) + €5.76 (JYJD) ≈ **€8.97 total** (~€2.24 each)
- **Source:** AliExpress — HORNAXYS/HNX + JYJD MG996R (180°)

| Spec | Value |
|------|-------|
| Weight | ~55–56 g |
| Size | 40 × 19 × 43 mm |
| Torque | 13 kg·cm @ 4.8 V · **15 kg·cm @ 6.0 V** |
| Speed | 0.17 s/60° @ 4.8 V · 0.14 s/60° @ 6.0 V |
| Voltage | **4.8–7.2 V** |
| Motor / gear | coreless · **all-metal gear · double ball bearing** |
| Travel | 180° |
| Horn spline | 25T |
| Interface | PWM · JR 3-pin, 300 mm lead |
| Brand | HORNAXYS/HNX · JYJD (MG996R clones) |

- **Notes:** classic **MG996R** standard servo — strongest of the owned servos (15 kg·cm @ 6 V) but
  also the **heaviest (~55 g)**, so it's the **spare / high-torque** option rather than a primary
  flight surface (the lighter 9/12 kg NEEBRC servos do the stabilators/flaperons). Tolerates up to
  7.2 V; runs fine on the 6 V rail. ⚠️ MG996R stall draw can be ~2.5 A — mind the BEC. ✅ **Gears
  confirmed all-metal** (opened and checked both orders). 25T horns included. 4 pcs total → plenty
  of spares.

---

### Magnetic snap-on 3-pin cable (1 pair, 20 cm) — experimental quick-disconnect
- **Category:** Connector (magnetic pogo-pin, 3-pin servo)
- **Status:** ✅ owned (1 pair · ordered 7 Apr 2026) — **experimental / bought to test**
- **Used for:** idea: **quick-disconnect for removable wings** — pass servo signal (+ low-current
  power) across a wing/fuselage joint that auto-separates when the wing comes off — [Servos](../docs/05-servos.md)
- **Variant / qty:** 1 pair · 20 cm leads
- **Price:** **€2.78**
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
- **Price:** **€2.05**
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

### Pushrod linkage stoppers D1.3 mm (×20) — servo linkage clamps
- **Category:** Hardware (pushrod linkage stopper)
- **Status:** ✅ owned (2× 10 = 20 pcs · ordered 7 Apr 2026)
- **Used for:** clamping **thin pushrod wires to servo arms/horns** — trainer control linkages;
  possible F35B light/secondary surfaces — [Servos](../docs/05-servos.md)
- **Variant / qty:** D1.3 mm hole · 20 pcs (2× 10)
- **Price:** **€3.65** (2 packs of 10)
- **Source:** AliExpress — Realhawk pushrod connectors / linkage stoppers (D1.3 mm)

| Spec | Value |
|------|-------|
| Type | linkage stopper (grub-screw pushrod clamp) |
| Hole Ø | **1.3 mm** (fits 1.0–1.3 mm pushrod wire) |
| Qty | 20 |
| Weight | ~0.7 g each |
| Material | metal, nickel-plated |
| Fixing | set screw + nut |

- **Notes:** clamps a thin steel pushrod wire to a servo horn and locks the throw with a grub screw —
  standard RC linkage hardware. **D1.3 = thin 1.0–1.3 mm wire**, *not* the F35B's 2 mm CF rods (those
  use clevises / M2 — see [Materials → fasteners](../docs/09-materials-airframe.md#fasteners)). Bought
  for the trainer; usable on the F-35B for **light/secondary surfaces** with thin-wire links. 20 pcs →
  plenty. The listing also offers D1.8 / 2.1 / 3.1 mm for thicker rods.

---

### Control horns + clevises (nylon, 21 mm) ×20 sets — control-surface linkages
- **Category:** Hardware (control horn + clevis)
- **Status:** ✅ owned (2× 10 = 20 sets · ordered 7 Apr 2026)
- **Used for:** **control-surface linkages** — horn on the surface, clevis on the pushrod (rudder,
  ailerons/flaperons, elevators/stabilators); trainer + usable on F35B — [Servos](../docs/05-servos.md)
- **Variant / qty:** medium lock-on horn + 21 mm clevis · 20 sets
- **Price:** **€2.70** (2 packs of 10)
- **Source:** AliExpress — medium lock-on nylon control horn + clevis set (21 mm)

| Spec | Value |
|------|-------|
| Horn | nylon, **lock-on** (serrated + backplate, no glue) |
| Horn height | 18 mm from base · base 12 × 8 mm |
| Max surface thickness | 6 mm |
| Clevis | nylon, **3.2 × 5.4 × 21 mm**, threaded / push-fit rod |
| Clevis fixing | side shaft for a **2 mm grub screw** |
| Qty | 20 sets |

- **Notes:** standard fixed-wing linkage hardware — the **lock-on horn** clips onto the control surface
  (no glue) and the **clevis** joins the pushrod with a 2 mm grub screw. More F35B-relevant than the
  [D1.3 stoppers above](#pushrod-linkage-stoppers-d13-mm-20--servo-linkage-clamps) (the grub-screw
  clevis suits a wider rod range). 20 sets → flaperons + stabilators + rudder + spares. Pairs with the
  [2 mm CF rod / M2 linkage hardware](../docs/09-materials-airframe.md#fasteners).

---

### Z-bend pushrod wires 1.2 mm × 200 mm — control pushrods
- **Category:** Hardware (pushrod / pull rod)
- **Status:** ✅ owned (16 pcs remaining — bought 40, sold 20 to friend, used 4 on trainer)
- **Used for:** **control-surface pushrods** — Z-bend hooks into the servo arm, far end into a linkage
  stopper/clevis; trainer + F35B light surfaces — [Servos](../docs/05-servos.md)
- **Variant / qty:** 1.2 mm dia × 200 mm, Z-type · 16 pcs remaining
- **Price:** **€4.54** (2 packs of 20 + shipping)
- **Source:** AliExpress — Sparkhobby Z-type steering rod (1.2 mm × 200 mm)

| Spec | Value |
|------|-------|
| Material | stainless steel |
| Diameter | **1.2 mm** |
| Length | 200 mm |
| End | pre-formed **Z-bend** (servo-arm end) |
| Qty | 16 (remaining) |

- **Notes:** the thin steel pushrod that **pairs with the
  [D1.3 mm linkage stoppers](#pushrod-linkage-stoppers-d13-mm-20--servo-linkage-clamps)** (1.2 mm fits
  the 1.0–1.3 mm range). Z-bend clicks into the servo horn; cut to length and clamp the far end. For
  **light/secondary control surfaces** (the F35B's primary surfaces use 2 mm CF rods). 40 pcs → ample.
  ⚠️ Thin 1.2 mm wire flexes under load — keep runs short or use only for low-force surfaces.
  ⚠️ Only 16 remaining — may need to reorder before full surface count is wired up.

---


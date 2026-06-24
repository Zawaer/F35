# Components — Propulsion

Cards for EDFs, motors, and ESCs. See the [template & field guide](README.md).
Build context: [Propulsion](../docs/06-propulsion.md).

---

### QX-Motor 30 mm EDF, QF1611 7000KV (3S) + 20A ESC ×2 — roll posts
- **Category:** Propulsion (ducted fan + brushless motor + ESC bundle)
- **Status:** 🛒 in cart (2 pcs)
- **Used for:** **wingtip roll-post thrusters** for hover roll authority (quadcopter mix) —
  [Propulsion → roll control](../docs/06-propulsion.md#roll-control)
- **Variant / qty:** 30 mm 6-blade EDF · QF1611 **7000KV** · 3S · bundled 20A ESC · 2 pcs
- **Price:** €39.06 total (€15.79 ×2 + €7.48 shipping; ~€19.53/unit delivered)
- **Link:** https://www.aliexpress.com/item/1005007548588279.html

| Spec | Value |
|------|-------|
| Fan | 30 mm, **6-blade**, all-composite, factory dynamic-balanced |
| Motor | QF1611 outrunner, **9N6P**, 7000KV |
| Cells | 2–4S LiPo (run on **3S** here) |
| Shaft / mount | 1.5 mm shaft · 4× M1.5 on Ø8 mm bolt circle |
| Motor weight | 21.8 g (bare motor; listing's "168 g" is packaged/shipping) |
| Max continuous | 160 W / 20 A (per 10 s rating) |
| Bundled ESC | 20A (no BEC info given) |
| Duct dims | Ø37.5 mm housing · Ø34 mm fan bore · 50 mm long (22 mm motor section) |

**Performance @ 7000KV, 3S (manufacturer table, 11.1 V):**

| Volts | Amps | Watts | Thrust | Efficiency |
|-------|------|-------|--------|-----------|
| 11.1 V | **11.2 A** | 124.3 W | **220 g** (7.76 oz) | 1.77 g/W |

- **Notes:** ~220 g raw → **~165 g after duct losses**, ~11.2 A draw — drives the wingtip roll posts.
  30 mm chosen over 40 mm (40 mm = more thrust/weight/cost than the roll task needs). At 11.2 A the
  bundled **20A ESC runs ~56%** — no heatsink needed; **decision: the build uses the 2× FVT LittleBee
  20A** (BLHeli_S/DSHOT) instead, so these bundled 20A ESCs are kept as **spares**. Motor leads use
  **2 mm bullet** connectors; powered from a 3S 850 mAh pack via **XT60H** (see
  [power.md](power.md)). Reverse spin by swapping any two motor leads.

---

### FVT LittleBee Spring 20A ESC (BLHeli_S) ×2 — roll-post ESCs (chosen)
- **Category:** Propulsion (brushless ESC)
- **Status:** 🛒 in cart (2 pcs)
- **Used for:** **roll-post 30 mm EDFs** — the **chosen** roll-post ESCs (over the EDFs' bundled 20A) —
  [Propulsion → roll control](../docs/06-propulsion.md#roll-control)
- **Variant / qty:** LittleBee Spring **20A** · 2 pcs
- **Price:** €11.56 total (€5.78 ×2)
- **Link:** https://www.aliexpress.com/item/1005007038091583.html

| Spec | Value |
|------|-------|
| Cells | 2–4S LiPo |
| Continuous / burst | **20 A** / 25 A (10 s) |
| BEC | **none** (no 5 V out) |
| Firmware | **BLHeli_S** (Bootloader + firmware) |
| Protocols | DSHOT, Oneshot125/42, Multishot, Muted |
| Main IC | SILABS EFM8BB21F16, 48 MHz MCU; N-fets both sides, dedicated gate driver |
| Size / weight | 23.5 × 12 × 4 mm · ~4 g (incl. wires) |
| Brand | Favourite (FVT) |

- **⚠️ Connectors — none fitted (as received):** the **motor end is bare PCB solder pads** (3 pads, no
  wires) and the battery end is **bare tinned power leads**. So: solder the EDF's three motor leads
  **directly to the pads** (no 2 mm bullets needed/possible there), and solder a **XT60H** (roll-post
  standard) onto the power leads. This differs from the bundled-ESC wiring assumption in the
  [30 mm EDF card](#qx-motor-30-mm-edf-qf1611-7000kv-3s--20a-esc-2--roll-posts) above.
- **Notes:** at ~11.2 A on a 20A ESC → ~56% load, no heatsink. **No BEC**, so it can't power the RX/FC
  rail — fine here (FC has its own supply). **Decision: these are the roll-post ESCs** (cheap +
  BLHeli_S/DSHOT response); the EDFs' bundled 20A ESCs become spares.

---

### QX-Motor 70 mm EDF, QF3027 2200KV (6S) ×2 (1 CW + 1 CCW) — main + lift fan
- **Category:** Propulsion (ducted fan + brushless motor)
- **Status:** ✅ owned (2 pcs: **one CW + one CCW** · ordered 12 May 2026)
- **Used for:** **main rear EDF** (thrust-vectored via 3BSM) + **front lift fan** —
  [Propulsion → Phase 2](../docs/06-propulsion.md#phase-2--edf-propulsion)
- **Variant / qty:** 70 mm 12-blade EDF · QF3027 **2200KV** · 6S · 2 pcs (1× CW, 1× CCW)
- **Price:** €105.14 total (€52.57 each)
- **Link:** https://www.aliexpress.com/item/1005006621270183.html

| Spec | Value |
|------|-------|
| Fan | 70 mm, **12-blade**, composite, factory dynamic-balanced |
| Motor | QF3027 outrunner, **12N10P**, 2200KV |
| Cells | **6S** LiPo |
| Shaft / motor dia | 4.0 mm shaft · 30 mm motor |
| Weight | **209 g** (motor; fan/duct extra) |
| Max continuous | **2200 W / 89 A** (per 10 s rating) |
| Recommended ESC | **100A** (Hobbywing 100A V2 planned, not yet carded) |
| Duct dims | Ø84 mm fan · Ø73.5 mm housing · 93 mm long |

**Performance @ 2200KV, 6S (manufacturer table):**

| Volts | Amps | Watts | Thrust | Efficiency |
|-------|------|-------|--------|-----------|
| 14.8 V | 37.0 A | 548 W | 1290 g | 2.36 g/W |
| 22.2 V (nom) | 72.0 A | 1598 W | **2700 g** | 1.69 g/W |
| 25.2 V (full) | **89.0 A** | 2243 W | **3300 g** | 1.47 g/W |

- **CW + CCW pairing:** deliberately **one of each rotation** so the main EDF and lift fan spin
  opposite ways — their reaction torques partially cancel and ArduPilot can use the differential for
  yaw trim in hover. Keep track of which is which when mounting.
- **Notes:** ~3300 g peak each at full 6S; ~72–89 A normal draw (peaks ~100 A) → each needs a **100A
  ESC** on its own pack (main + lift each a 5000 mAh pack — see [power.md](power.md)). Already produces a
  convincing jet sound across the throttle range. **Out of ACS712 range** (89 A ≫ 20 A) so EDF current
  isn't logged — rely on ESC thermal protection. Reverse spin by swapping any two motor leads.

---

### Hobbywing Skywalker 100A V2 ESC ×2 — main + lift EDF ESCs
- **Category:** Propulsion (brushless ESC, with UBEC)
- **Status:** ✅ owned (2 pcs · ordered 12 May 2026)
- **Used for:** **main EDF + lift-fan EDF** (one each, individual not 4-in-1) —
  [Propulsion → Phase 2](../docs/06-propulsion.md#phase-2--edf-propulsion)
- **Variant / qty:** Skywalker **100A V2** · 2 pcs
- **Price:** €70.26 total (€29.74 ×2 + €10.78 shipping)
- **Link:** https://www.aliexpress.com/item/1005009269823714.html

| Spec | Value |
|------|-------|
| Continuous / peak | **100 A / 120 A** |
| Input | **3–6S** LiPo |
| BEC (UBEC) | **switching 5 V / 7 A** |
| Processor | 32-bit ARM M0 @ 96 MHz (up to 300k RPM, 2-pole) |
| Input wires | 10AWG ×2 (red/black), 150 mm, **bare** (fit pack connector) |
| Output wires | 12AWG ×3, 100 mm → **4.0 mm gold bullet (female)** |
| Size / weight | 85 × 36 × 9 mm · **92 g** |
| Programming | transmitter / LED program box / program port — **no firmware upgrade** |
| Features | DEO active freewheeling, reverse brake (HW patent), search mode, thermal/LVC/signal-loss protection |

- **⚠️ Signal protocol — PWM only:** the Skywalker V2 is a **standard PWM airplane ESC (no DSHOT)**.
  ArduPilot drives it over PWM — fine for the main/lift EDFs (unlike the roll-post
  [LittleBee](#fvt-littlebee-spring-20a-esc-blheli_s-2--roll-post-esc-option), which is BLHeli_S/DSHOT).
- **Notes:** 100A/120A comfortably covers each 70 mm EDF's ~89 A peak (~12–26% margin). **Has a 5 V/7A
  UBEC** — can power the RX/servo rail (decide whether to use it or the FC's own supply; avoid
  back-feeding two BECs). Output **4 mm bullets** mate to the EDF motor leads; input is **bare 10AWG**
  → terminate with the main-pack connector (see [power.md](power.md)). Configure 6S, set LVC, and the
  brake/timing to taste via the transmitter or LED box.

---

### A2212 2200KV power kit (motor + 40A ESC + 2× SG90 + props) — Phase 1 trainer
- **Category:** Propulsion (trainer power-kit bundle)
- **Status:** ✅ owned (1 kit · ordered 12 May 2026)
- **Used for:** **Phase 1 foamboard trainer** (learn to fly + validate FC/RX before VTOL) — *not* the
  F-35B itself — [Propulsion → Phase 1](../docs/06-propulsion.md#phase-1--trainer-prop-plane)
- **Variant / qty:** 2212 **2200KV** · 40A ESC · **XT60** · 1 kit
- **Price:** €18.46 total (€17.53 + €0.93 shipping)
- **Link:** https://www.aliexpress.com/item/1005005265001463.html

**Kit contents:**

| Item | Spec |
|------|------|
| Motor | **A2212 2200KV** outrunner · 2–3S · max 342 W · Ø27.5 × 38 mm · 3.17 mm shaft · Ri 0.033 Ω |
| ESC | **40A / 55A burst** · 2–3S · BEC **linear 5 V / 3 A** · **XT60** input · 3.5 mm bullet output |
| Servos | **2× SG90** 9 g · 1.5 kg·cm · 0.12 s/60° · 4.8–6 V |
| Props | 2× **6035** (6×3.5") orange |
| Hardware | aluminium X prop-adapter, collets, mounting screws, battery strap |

- **Notes:** matches the Phase 1 plan (A2212 2200KV, 30–40 A ESC, 5×4–6×4 prop). Runs on the
  **CNHL MiniStar 850 mAh 3S** (see [power.md](power.md)); ESC BEC powers the RX/servos. ⚠️ The ESC
  is **2–3S only** — do **not** run it on 4S. Props are fragile (buy spares). ESC needs airflow to
  stay cool. The bundled **SG90 servos** are for the trainer's control surfaces — distinct from the
  F-35B's [3BSM/door servos](../docs/05-servos.md). Trainer is built; awaiting runway re-flight.

---

### XXD A2212 1400KV + 30A ESC — trainer (low-KV / bigger-prop option)
- **Category:** Propulsion (brushless motor + ESC)
- **Status:** ✅ owned (1 set · ordered 17 Apr 2026)
- **Used for:** **Phase 1 trainer** — a **lower-KV (1400KV)** alternative to the kit's 2200KV motor
  (more torque, larger/slower prop) — [Propulsion → Phase 1](../docs/06-propulsion.md#phase-1--trainer-prop-plane)
- **Variant / qty:** A2212 1400KV + 30A ESC · 1 set
- **Price:** €11.10 (already EUR-priced)
- **Source:** AliExpress — XXD A2212 1400KV + 30A ESC

| Spec | Value |
|------|-------|
| Motor | XXD A2212, **1400KV**, 47 g, Ø27.5 × 30 mm, 3.17 mm shaft |
| Cells (motor) | 2–3S LiPo |
| Current | ~1.4 A no-load · peak 14–22 A |
| ESC | **30A** continuous / 40A max (<10 s) · BEC **5 V / 3 A** |
| ESC cells | 2–3S LiPo / 4–10 NiMH (auto-detect) |
| ESC LVC | slow at 3.0 V/cell, cutoff 2.9 V/cell · brake on/off |
| ESC size/weight | 45 × 24 × 9 mm · 23 g |
| Includes | motor + 30A ESC + X-mount, prop adapter, bullets, screws |

- **Notes:** same A2212 frame as the **trainer 2200KV kit above** but **1400KV** (vs 2200KV) → lower
  RPM/V, **more torque, swings a bigger prop**, lower top speed — a calmer trainer setup or spare. 30A
  ESC (vs the kit's 40A) is ample at the A2212's ~10–15 A. **2–3S only — not 4S.** ⚠️ Prop sizing
  differs from the 2200KV: 1400KV typically wants a larger prop (~8–9″ on 3S vs the kit's ~6″) — pick
  accordingly. Trainer-only.

---

### EP-6035 propellers (6×3.5") ×4 — trainer spares
- **Category:** Propulsion (propeller)
- **Status:** ✅ owned (4 pcs · ordered 7 Apr 2026)
- **Used for:** **Phase 1 trainer** props — spares/replacements for the A2212 kit's 6035 props
  (fragile, break on hard landings) — [Propulsion → Phase 1](../docs/06-propulsion.md#phase-1--trainer-prop-plane)
- **Variant / qty:** EP-6035 (6×3.5") · 4 pcs
- **Price:** **€1.75**
- **Source:** AliExpress — EP-6035 GWS-style direct-drive prop (4 pc)

| Spec | Value |
|------|-------|
| Size | **6035** = 6″ dia × 3.5″ pitch |
| Type | direct-drive electric prop (GWS EP replacement) |
| Qty | 4 |
| Bore | macro-bore + **adapter gaskets** (3.0/3.2/3.5/4.0/4.8/5.0/6.0/6.3 mm) |
| Material | nylon / composite |

- **Notes:** matches the A2212 kit's **6035** props (Phase 1 plan was 5×4–6×4) — these are **spares**
  since props break easily on hard landings. Fit the A2212's 3.17 mm shaft via the included gasket.
  Trainer-only — the F-35B is EDF (no props). ⚠️ Balance before use to cut vibration.

---

### Gemfan 8×4 propellers (2 pcs) — trainer (for the 1400KV motor)
- **Category:** Propulsion (propeller)
- **Status:** ✅ owned (2 pcs · ordered 17 Apr 2026)
- **Used for:** **Phase 1 trainer** — larger prop suited to the **A2212 1400KV** motor (low-KV wants a
  bigger prop) — [Propulsion → Phase 1](../docs/06-propulsion.md#phase-1--trainer-prop-plane)
- **Variant / qty:** 8.0 × 4.0″ · 2 pcs
- **Price:** €3.34 / 2 pcs (already EUR-priced)
- **Source:** AliExpress — Gemfan-style "Horse Blade" fibreglass-nylon prop (8×4)

| Spec | Value |
|------|-------|
| Size | **8 × 4″** (8″ dia, 4″ pitch) |
| Material | fibreglass-reinforced nylon, high-strength |
| Qty | 2 |
| Type | direct-drive, 2-blade |
| Brand | EVYVKV (Gemfan "Horse Blade" style) |

- **Notes:** the **bigger prop for the low-KV A2212 1400KV** set (vs the 6035 on the 2200KV kit) — 8×4
  is a sensible match for 1400KV on 3S. Fibreglass-nylon is stiffer/stronger than plain GWS EP props.
  ⚠️ Check the bore fits the A2212's 3.17 mm shaft (use the motor's prop adapter); balance before
  flight. Trainer-only.

---

> All known propulsion parts are now carded (+ trainer prop spares).

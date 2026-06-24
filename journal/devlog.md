# Devlog

Freeform build journal — newest entry on top. Progress, CAD, things tried-and-ditched, photos,
half-formed ideas. No template to fill; a one-line entry is fine. The crisp "we changed X because Y"
records go in [decisions.md](decisions.md); this is the looser narrative around them.

**Entry format:** `## YYYY-MM-DD — short title`, then a few bullets. Drop images in
`journal/img/` and link them inline.

---

## 2026-06-24 — Big AliExpress order placed; all in-cart parts ordered

- Ordered everything that was in the cart in one go. Covers:
  - **Lighting** — 3× nav LEDs (white/red/green 3W ×10 each), 10W landing-light, green COB strip (1 m),
    4× ACELEX 700mA drivers, LD2740SC 3A driver, 10× IRLZ44N MOSFET, PP diffuser sheet, 14×14×6 mm
    heatsinks, 2× YiRui 1156 BA15S yellow bulb (afterburner).
  - **Sensors / display** — 20× NTC 100K B3950, 3× ACS712-20A, CD74HC4067 mux board, 1.47″ ST7789 TFT,
    5× 12P FFC adapter.
  - **Servos** — Feetech STS3032 360° (magnetic encoder, 3BSM nozzle), 4× NB-M005 2g micro (light
    doors), 10× 200 mm servo extension.
  - **Roll-post propulsion** — 2× 30 mm EDF 7000KV 3S (bundled ESCs = spares), 2× FVT LittleBee 20A.
  - **Wire** — 10 AWG (2 m), 18 AWG (2 m), 22 AWG (10 m).
  - **Structural** — CF tube 500×8×6 mm ×16, CF rod 2×250 mm ×10, 4 mm steel balls ×100, MR62ZZ ×10,
    38 mm nose wheel ×2, CA glue ×3.
- BOM "In cart" section cleared — all items now in **Owned / ordered** with this date.

## 2026-06-24 — Power architecture & monitoring locked in

- Settled the whole power tree: **two 6S 5000 mAh packs** (one per fan, matched pair), EDFs wired
  **battery → ESC → motor directly** (no high current through the FC), and an **18 AWG avionics tap
  off the lift pack** into the CoreWing PDB for the three BEC rails. Lift pack does double duty
  (hover + avionics) → it's a single point of failure for the electronics, so always fly it connected.
- Monitoring plan finalised: **NTC 100K thermistors through a CD74HC4067 mux** (13 channels, shared
  47 kΩ divider), **3× ACS712 20A** (two on the roll-post EDFs with a ÷0.66 divider, one spare), and
  **resistor dividers** for pack voltage (main 100 k/10 k ×11; 850 mAh 10 k/2 k ×6). Lift voltage
  comes free through the PDB.
- Confirmed the **servo BEC is 8 A continuous** (not the 4 A the product text implied) → no UBEC split.
- Decided **not** to use the smoke stopper here (simple avionics, and it's XT30/XT60 not EC5), and to
  tap voltage dividers at the **ESC power joint, never the balance leads**.
- Started this journal + the [decision log](decisions.md) to stop losing the *why* behind reversals
  (the DS18B20 → NTC switch was the trigger — that reasoning had been deleted from the docs).

## (undated) — Trainer prop-plane, first flight

- The Phase-1 trainer's maiden throw didn't go well: it flew ~1 s, dropped, and broke. Read as a
  **bad throw / not enough launch speed**, not an airframe fault — needs a proper launch (more speed,
  flatter attitude) next attempt. Logged here so the lesson survives the rebuild.

---

<!-- New entries go ABOVE this line, newest first. Template:

## YYYY-MM-DD — title
- what I did / tried
- what worked, what didn't
- decisions → also add a row to decisions.md
- ![caption](img/file.jpg)

-->

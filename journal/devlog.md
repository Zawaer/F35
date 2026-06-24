# Devlog

Freeform build journal — newest entry on top. Progress, CAD, things tried-and-ditched, photos,
half-formed ideas. No template to fill; a one-line entry is fine. The crisp "we changed X because Y"
records go in [decisions.md](decisions.md); this is the looser narrative around them.

**Entry format:** `## YYYY-MM-DD — short title`, then a few bullets. Drop images in
`journal/img/` and link them inline.

---

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

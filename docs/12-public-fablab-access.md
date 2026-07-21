# Public Fab Lab / Makerspace Access (Helsinki Region)

> **Context:** Toivo is 17, a student at Otaniemen lukio — not affiliated with Aalto University or
> any other institution running these spaces. This doc is a survey of every public/semi-public
> fabrication venue in the Helsinki capital region reachable as a non-affiliated minor, so machine
> choices for this build (laser cutting, CNC, vinyl cutting, vacuum forming, PCB milling — anything
> beyond the owned [2× Bambu P2S](09-materials-airframe.md#printing-hardware) and hand tools) aren't
> limited to guessing. Complements the Aalto-Fablab-specific notes already in
> [Materials & Airframe](09-materials-airframe.md) and [Pico](04-raspberry-pi-pico.md).
>
> **Compiled 21 July 2026** from live web research (library booking pages, Varaamo/Timmi listings,
> Omnia/Aalto/hacklab sites). ⚠️ **Fleets, hours, and prices change — re-check the live booking page
> before relying on any specific machine for a project.** Rows marked ⚠️ below had unconfirmed specs,
> prices, or age policy at research time; see [Open questions / to verify](#open-questions--to-verify-manually)
> before committing to one.

## Quick verdict — which venue for what

| Venue | Access for a 17yo non-affiliated student | Cost | Best for |
|---|---|---|---|
| **[Oodi library](#oodi--kaupunkiverstas--konehuone-helsinki)** | ✅ **Confirmed — Helmet library card already in hand.** No remaining unknowns. | Free use, cheap materials | **Only public laser cutter / UV printer / large-format printer** in the region |
| **[Omnia Makerspace](#omnia-makerspace-espoo-otaniemi)** | Likely yes — open policy stated, but minimum-age rule unpublished. ⚠️ **Confirm by email first** | Free use, generous free-material allowance | Closest venue to school; 2 laser cutters, 2× Bambu H2S, vinyl/UV/sublimation |
| **[Aalto Fablab](#aalto-fablab-espoo-otaniemi)** | **Public Open Days only** (schedule currently unconfirmed); closed for summer until 29 Aug 2026 | Free to use machines | **Most capable equipment overall** — best CNC (Recontech 1312), 80 W laser, SLA, vacuum forming, PCB milling — access is the bottleneck |
| **[Espoo libraries](#espoo-libraries-iso-omena--sello--tapiola--entresse--lippulaiva)** | Yes, self-service via Espoo Varaamo | Free | Wood workshop (Iso Omena, 18+ for independent use), ABS/PC-capable 3D printing, sewing |
| **[Vantaa libraries](#vantaa-libraries-paja--värkkäämö)** | Yes, library card required | Free | General 3D printing (Ultimaker), Cricut/vinyl cutting, sewing |
| **[Helsinki Hacklab](#helsinki-hacklab-independent-hackerspace)** | Yes — dedicated under-18 policy, likely needs guardian involvement. Membership required to use tools | €42/year (or €40/month for 24/7 key access) | Biggest independent laser (~1600×900 mm bed) + a second laser + CNC, if membership is worth it |
| **[Kauniainen DigiLab](#kauniainen-digilab)** | Yes — open to all residents, all ages | Free | Only option in Kauniainen; monthly open-door slots only |
| Aalto Design Factory | **No** — Aalto-community only | N/A | Skip |
| Myyrmäen nuorisotila | Maybe (ages 10–17) — equipment survival post-relocation unconfirmed | Free | Call ahead before relying on it |
| Helsingin Pyöräpaja | Yes, no digital fabrication | Free | Bikes only — not relevant here |

## Venues in detail

### Aalto Fablab (Espoo, Otaniemi)

**Otakaari 7, 02150 Espoo.** Day-to-day reserved for Aalto students/staff/researchers with machine
permits (self-service TakeOut booking needs an `@aalto.fi` email). Non-Aalto access is **Public Open
Day walk-in only** — no minimum age or guardian rule published, but the current weekly schedule is
unconfirmed (Aalto's own pages disagree: Mon–Fri 9–16 vs 10–16 vs an older Thursday 12–16 slot).
⚠️ **Email fablab@aalto.fi to confirm the current schedule** — this is the actual access gate. A
non-Aalto membership agreement may also be possible; fee unpublished. **Closed for summer break
22 Jun – 28 Aug 2026.**

| Category | Machine | Model | Key specs | Materials | Notes |
|---|---|---|---|---|---|
| Laser cutter | CO2 laser | Epilog Fusion Pro 48, 80 W | Bed ≈1219×914 mm, max Z-depth ≈311 mm, IRIS camera positioning | Wood, acrylic, leather, cardboard | ⚠️ Bed/Z-depth are Epilog's general spec, not Aalto-confirmed |
| Vinyl cutter | Vinyl cutter | Roland GX-24 | Cut width ~58 cm, load width up to ~70 cm | Vinyl | — |
| Print & cut | Vinyl printer/cutter | Roland BN2-20A | Print+cut width up to ~51 cm, CMYK eco-solvent, 1440 dpi | Vinyl | — |
| 3D printer ×3 | FDM | Prusa MK4 | Build volume 250×210×220 mm | PLA/PETG/ABS | ⚠️ ~€0.07/g PLA from a stale 2020 price list |
| 3D printer ×3 | FDM | Prusa Mini | Build volume not Aalto-confirmed | PLA/PETG | ⚠️ |
| 3D printer ×1 | FDM | Ultimaker 2+ Extended | 223×223×305 mm | PLA/ABS/CPE | — |
| 3D printer ×2 | FDM | Ultimaker 2+ Connect | Not separately confirmed | PLA/ABS/CPE | ⚠️ |
| 3D printer ×1 | FDM | Ultimaker 3 Extended | ~215×215×300 mm (general spec) | PLA/ABS/CPE | ⚠️ |
| 3D printer | SLA resin | Formlabs Form 2 | Build volume 145×145×175 mm | Formlabs resins | Basic resin €0.22/ml ex VAT — 2022 list |
| 3D printer | SLA resin | Formlabs Form 3 | Build volume 145×145×185 mm | Formlabs resins | Same 2022 price list |
| **CNC** | 3-axis CNC mill | **Recontech 1312** | Work area 1200×1200 mm XY, max Z 900 mm, spindle to 20,000 rpm, vacuum table | Wood, soft materials only | **Most capable CNC found across every venue researched** — the standout reason to pursue Aalto access |
| CNC / PCB | PCB milling | Bungard CCD/2 | Work area ~270×325×38 mm, ±1 mil accuracy (general spec) | PCB substrate | ⚠️ |
| CNC / precision milling | Precision mill | Roland Modela MDX-40 | Work area 305×305 mm, 100 W spindle, 15,000 rpm | Plastics, wood, wax (no metal) | — |
| CNC / precision milling | Precision mill | Roland monoFab SRM-20 | Work area 203×152×60 mm (general spec) | Plastics, wood, wax | ⚠️ |
| **Vacuum forming** | Vacuum former | **CR Clarke 750FLB** | Sheet 508×458 mm, forming aperture 432×482 mm, max mould height 150 mm, max material 6 mm | Polystyrene sheet | Already the [canopy plan's better option](09-materials-airframe.md#forming-method--diy-vacuum-forming-default-or-aalto-fablab-better-if-accessible). 1 mm sheet 27×47 cm ≈ €1.01 incl. VAT — 2022 list |
| Vacuum forming | Profile cutter | CR Clarke 145 | Not published | — | ⚠️ |
| Electronics | Workbench | Not published | Microscope, soldering stations, oscilloscope, power supply, logic analyzer, components stock | — | ⚠️ |

### Oodi – Kaupunkiverstas / Konehuone (Helsinki)

**Töölönlahdenkatu 4, 00100 Helsinki.** Open to the public with just a **Helmet library card** — no
Aalto/Espoo affiliation needed. ✅ **Already have a Helmet card — this venue is fully unblocked, no
access unknowns left.** First laser-cutter use requires a guided "opastettu aika" session. Booked via
`varaamo.hel.fi`.

| Category | Machine | Model | Key specs | Materials | Cost |
|---|---|---|---|---|---|
| Laser cutter | CO2 laser | Epilog Fusion M2, 75 W | Area 1016×711 mm, max height 336 mm, 75–1200 dpi | Acrylic, wood, leather, paperboard (cut); glass/metal (engrave only) | Free use; plywood €14/3×600×600mm, acrylic €10–17, paperboard €2 |
| UV printer | Benchtop UV flatbed | Roland VersaUV LEF2-series ⚠️ | Max object 538×360×100 mm, 1440 dpi | Flat rigid objects | ~€1 phone case, €12 full-area, min €0.50 |
| Large-format printer | Inkjet | Roland SG-540 | Print width ~1300 mm, CMYK, up to 900 dpi | Poster paper, sticker vinyl | €15/printed metre, min €7.50 |
| Vinyl cutter | Cutter + heat press | Roland CAMM (GX-24-class) ⚠️ | Monochrome stickers + fabric-transfer | 3M Scotchcal vinyl, Stahl's Sportsfilm | Not itemized |
| 3D printer | FDM | UltiMaker S3 (2–3 units) ⚠️ | Dual extrusion, 230×190×200 mm, 2.85 mm filament | PLA | €0.70/print, max 4 hr session |
| Textile | Sewing + overlock | Not published | 2 sewing machines + 2 overlockers | Standard fabrics | Free |
| Other | Button maker, wire binder, A3 scanner, electronics bench | Various | Soldering iron, multimeter, oscilloscope, signal generator | Lead-free solder provided | Free |

This is the **only public laser cutter, UV printer, and large-format printer left in the region** —
Iso Omena's laser was retired in favour of more 3D printers.

### Omnia Makerspace (Espoo, Otaniemi)

**Otakaari 5, 02150 Espoo (A Grid building)** — the closest venue to Otaniemen lukio. Site states
open to "anyone interested," with **no published minimum age or guardian rule**, but this is
unconfirmed for a non-Omnia minor. ⚠️ **Email makerspace@omnia.fi before assuming solo access.**
Booking is per-device via Microsoft Bookings, 1–4 hr slots.

| Category | Machine | Model | Key specs | Materials | Cost |
|---|---|---|---|---|---|
| 3D printer ×2 | FDM | Bambu Lab H2S | 340×320×340 mm, nozzle to 350 °C, active chamber heat to 65 °C | **PLA only** (facility policy) | 300 g PLA free, then ask staff |
| 3D printer | FDM | Ultimaker 3 | Build vol. not published (mfr ~215×215×200 mm) | PLA/ABS/CPE (site-stated) | Same free allowance |
| 3D printer | FDM | Ultimaker 2+ | ~223×223×205 mm (mfr spec) | PLA/ABS/CPE/nylon (site-stated) | Same free allowance |
| 3D printer | FDM ("MANU") | Brand/model unpublished ⚠️ | Described as industrial-grade, 20+ hr continuous prints | PLA | Same free allowance |
| 3D printer | SLA resin | Anycubic Photon M7 Pro | Specs not published (page reuses older model text) ⚠️ | Phrozen 4K resin | 200 g resin free, then ask staff |
| Laser cutter | CO2 | Epilog "Helix-24," 60 W | Bed 609×452 mm, max ~8 mm material | Wood, acrylic, textiles (cut) | 1 sheet free, then ask staff. ⚠️ Was showing "out of order" at research time |
| Laser cutter | CO2 (newest, ~Mar 2026) | xTool P3, 80 W | Area 915×458 mm, AutoLift bed to 220 mm tall | Wood, acrylic, leather | 1 sheet free, then ask staff |
| Print & cut | Vinyl printer/cutter + heat press | Roland VersaSTUDIO BN-20 | Media 150–515 mm, max print 480 mm, CMYK+Metallic | Vinyl, heat-transfer film | 100×48 cm free, then ask staff |
| Sublimation | Dye-sub transfer | Epson SureColor SC-F100 (~Feb 2026) | Not published | Polyester/sublimation blanks | Not published |
| VR | Headset | HTC Vive Pro | — | — | Free |
| Studio | Video/photo (~30 m²) | Canon EOS R + lighting/audio kit | Bookable 1/2/4/6 hr | — | Free |
| Electronics | Robotics/electronics kits + soldering table | Brands unpublished ⚠️ | — | — | Free (assumed) |

No CNC router/mill and no dedicated sewing machine at this venue.

### Espoo libraries (Iso Omena / Sello / Tapiola / Entresse / Lippulaiva)

All booked via `varaamo.espoo.fi`, free, self-service.

| Venue | Notable equipment | Notes |
|---|---|---|
| **Iso Omena – Paja** | FDM: Prusa i3 MK3S+ (0.4 mm), Ultimaker 2+ (0.8 mm, "Totodile") — **PLA/ABS/polycarbonate**, unique among Espoo libraries. Wood workshop (hand & power tools). Vinyl cutter: Roland Camm-1 (GX-24/Servo class), up to 1000×600 mm | Wood workshop is **18+ for independent use**; minors need a guardian. Laser cutter (Epilog Fusion M2 32, 50 W) **retired**, dropped in favour of more 3D printers |
| **Sello – Paja** | FDM: Prusa i3 MK3S+ (black & white units; one ABS-dedicated). Sewing machine | One of only 2 Espoo library sites keeping 3D printers post-April-2026 centralisation. No laser/CNC |
| **Tapiola / Entresse – Paja** | Sewing machines only | 3D printers **removed 12 Apr 2026** |
| **Lippulaiva – "Solmu"** | Sewing machine, coverstitch, 2 overlockers, iron/board, clothes steamer | Most complete sewing setup in the Espoo library network. No laser/CNC |

### Vantaa libraries (Paja / Värkkäämö)

Various branches, booked via **Timmi 360** (`varaamo.vantaa.fi` / `timmi.vantaa.fi`), library card
required.

| Category | Equipment | Notes |
|---|---|---|
| 3D printer | Ultimaker 3 and Ultimaker S3 (PLA, STL sliced with Cura) | Only one reservation at a time |
| Textile | 2 sewing machines, overlocker(s); Värkkäämö also has 2 sergers + industrial machine, warp beams, winding device | Guided intro for first-time users |
| Cutting | Cricut Explore 3 (Värkkäämö); Roland CAMM GX-24-class vinyl cutter ⚠️ | Vantaa vinyl-cutter model inferred, not directly confirmed |
| Media | Adobe Creative Cloud workstation, graphics tablet, image/film scanner | — |

### Helsinki Hacklab (independent hackerspace)

**Takkatie 18 (back door), 00370 Pitäjänmäki, Helsinki.** Visitors can just show up on an **Open
Tuesday from 17:00**; actually *using* tools requires paid membership. Has a dedicated under-18
policy page — ⚠️ **read `helsinki.hacklab.fi/alle-18-vuotias` directly**, likely needs guardian
consent. Membership: **€42/year basic**, or €40/month for 24/7 "key access" (negotiable to ~€20/month
for students — not needed for casual use).

| Category | Machine | Model | Key specs | Materials | Notes |
|---|---|---|---|---|---|
| Laser cutter | CO2 | Redsail CM1690 (rebranded), reported ~150 W | Area ≈1600×900 mm, 32-bit DSP control | Wood, acrylic, paper, plastic, rubber, leather | ⚠️ Wattage from generic manufacturer spec, not Hacklab-confirmed |
| Laser cutter (2nd unit) | CO2 | Epilog Helix 24 ⚠️ | Not published — wiki page didn't render | — | Ask on Discourse/Matrix or visit an Open Tuesday |
| 3D printer | FDM (self-built) | "Prusa-i3-Erkki" | Build volume not published | — | — |
| 3D printer | FDM multi-tool | Prusa XL | 250×220×270 mm (mfr spec, unconfirmed) | PLA/PETG/ABS | — |
| General | Wood workshop, metal workshop, electronics room, sewing machines, CNC, PCB-making | Models not published ⚠️ | — | — | Biggest remaining gap — visit an Open Tuesday or ask directly |

### Kauniainen DigiLab

**Läntinen koulupolku 1–3, 02700 Kauniainen.** Open to all Kauniainen residents, daycare age to
retirees, via **monthly open-door sessions**: general equipment first Tuesday 14:00–17:00, VR trials
first Wednesday 14:00–15:30. Free municipal service. Equipment: 3D printing/modeling, VR headsets,
sticker/large-format printer, robotics kits, smart textiles, Micro:bit & small electronics — **no
brand/model/bed-size specs published anywhere**, and **no laser cutter or CNC**. Contact Erkki
Ylitalo (FI) or Kaj Kankaanpää (SV) via `kauniainen.fi` for specifics.

### Ruled out (Aalto Design Factory, youth centres, bike kitchen)

- **Aalto Design Factory** (Puumiehenkuja 5) — has the strongest non-Fablab equipment list seen
  (4-/3-axis CNC, lathes, water jet, Ultimaker S7/S6/S5, Fuse 1+ SLS, 80W+50W fiber laser, Bantam PCB
  mill) but is **confirmed restricted to the Aalto community**; public access is lobby/events only.
- **Myyrmäen nuorisotila** (youth centre, temporarily at Kilterin koulu) — free drop-in, ages 10–17,
  possibly one Ultimaker 3, but **unconfirmed whether it survived the Jan 2026 relocation**. Call
  ahead.
- **Helsingin Pyöräpaja** (Bike Kitchen) — free, no age restriction, but bicycle repair tools only,
  no digital fabrication. Closed for summer break 13.7–4.8.2026.

## Checked — dead ends

Investigated and ruled out entirely (no relevant public access, or no fabrication equipment), so they
don't get re-researched:

- **Metropolia UAS** (Myllypuro/Myyrmäki/Karaportti) — no evidence of public FabLab/open workshop access for outsiders/teens
- **AYY workshops** — Aalto-student-only guild workshops, nothing separate from Aalto Fablab/Design Factory
- **Urban Mill** (Otaniemi) — defunct as an independent venue, folded into Aalto Design Factory
- **Haaga-Helia** — only a marketing "Sales & eCom Lab," irrelevant
- **Kulttuuritehdas Vernissa** (Vantaa) — arts/film/music youth culture house, no fabrication tools
- **Pelitalo Sture** (Helsinki) — gaming centre only
- **Kontulan nuorten toimintakeskus Luuppi / "Askis"** — analog handicraft (wood/jewelry/ceramics), no digital fabrication
- Most Helsinki/Vantaa youth centres — analog crafts/arts/music, outside the library Paja network already covered
- **Kääntöpiiri** — literary translators' community, false lead from name similarity
- **Restarttaamo** — no venue found under this name in the region
- **Kaapelitehdas** (Cable Factory) — artist studios/event space, no public bookable fab equipment found
- **Suvilahti** — events/festival area, no maker facility
- **Seams Helsinki** (repair café) — sewing/textile repair only, same category as library sewing

## Open questions / to verify manually

The single biggest unknown across every venue is **age policy for a non-affiliated 17-year-old** —
confirm before planning a project around any venue.

| Venue | What's unconfirmed | Why it matters | Ask |
|---|---|---|---|
| Aalto Fablab | Current Public Open Day weekly schedule (3 Aalto pages disagree) | **This is the access gate** — top priority | fablab@aalto.fi |
| Aalto Fablab | Minimum age policy | Determines solo attendance | fablab@aalto.fi |
| Aalto Fablab | Non-Aalto membership fee (alternative to Open Days) | Could be a cheap workaround | fablab@aalto.fi |
| Aalto Fablab | Current (2026) filament/plywood/acrylic prices (only 2020/2022 lists found) | Budgeting | fablab@aalto.fi or ask on an Open Day |
| Aalto Fablab | Exact build volumes, Prusa Mini / Ultimaker 2+ Connect | Max part size | Ask staff on an Open Day |
| Omnia Makerspace | Minimum age / guardian rule for a non-Omnia visitor | Determines solo booking | makerspace@omnia.fi / 040 126 7624 |
| Omnia Makerspace | Overage pricing beyond free allowances | Budgeting bigger projects | makerspace@omnia.fi |
| Omnia Makerspace | Opening hours conflict (9–15 vs 10–15 across pages) | Booking windows | makerspace@omnia.fi |
| Omnia Makerspace | Ultimaker 3/2+ build volumes; "MANU" printer brand; Photon M7 Pro specs | Max part size | Ask on-site staff (Siim Saar, siim.saar@omnia.fi) |
| Omnia Makerspace | Live status of the Epilog Helix-24 laser (was "out of order") | Don't plan around it unconfirmed | Check live page or call ahead |
| Omnia Makerspace | Electronics/robotics kit brands & specs | Only if project needs it | makerspace@omnia.fi |
| Helsinki Hacklab | Under-18 access page content (fetch failed) | The real process to join at 17 | Read the page directly, or ask on an Open Tuesday |
| Helsinki Hacklab | CNC specs + second laser (Epilog Helix 24) specs | Real capability check | Visit an Open Tuesday / Discourse / Matrix |
| Helsinki Hacklab | Wood/metal workshop machine models | Only if project needs it | Visit an Open Tuesday |
| Kauniainen DigiLab | No brand/model/bed-size for any device | Suitability for a specific project | Erkki Ylitalo (FI) / Kaj Kankaanpää (SV), kauniainen.fi |
| Myyrmäen nuorisotila | Whether its Ultimaker 3 survived the Jan 2026 relocation | Don't plan around gone equipment | Call ahead |
| Oodi | 3D printer count disagrees (FB: 3, site: 2) | Expected wait times | Check varaamo.hel.fi live availability |
| Oodi | Exact Roland VersaUV LEF2 / CAMM vinyl-cutter sub-models | Minor — material compatibility only | oodi.kaupunkiverstas@hel.fi |
| Iso Omena | Exact wood-workshop machine models | Before relying on it for woodworking | Ask library staff |
| Sello / Tapiola / Entresse | Sewing machine brands/models | Minor | Ask branch staff |
| Vantaa Paja/Värkkäämö | Exact vinyl-cutter model (inferred, not confirmed) | Minor | Ask branch staff |
| Stadin ammattiopisto (Helsinki) / Varia (Vantaa) vocational schools | Whether either runs a public open workshop for hobbyists — unconfirmed either way | Could be an untapped resource (real machine shop, CNC, welding) | Call/email both directly |

## How to use this doc

This is a **planning reference**, not a decision — nothing here commits the build to any venue. When
a part of the build could use a laser cutter / CNC / vinyl cutter / vacuum former / etc., check this
table for the best-access option, verify the relevant row against the venue's live booking page, and
only then note the choice in the relevant subsystem doc (as already done for the canopy and TFT
filter in [Materials & Airframe](09-materials-airframe.md) and [Pico](04-raspberry-pi-pico.md)).

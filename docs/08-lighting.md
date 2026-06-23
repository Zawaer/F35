# Lighting

> **Current plan:** all lighting controlled by the **Pico/RP2040**. Nav/strobe lights use **3W
> LEDs** (red/green/white) on 700mA PWM constant-current drivers. A **10W landing light** runs on
> a 3A adjustable CC driver. An **automotive BA15S bulb** simulates the afterburner. A **12V COB
> strip** provides accent lighting, switched by an **IRLZ44N MOSFET**. Most lighting is powered
> from the PDB **12V VTX/CAM rail** — but see the afterburner power caveat.

## Inventory of light sources

| Light | Source | Driver | Power rail |
|-------|--------|--------|------------|
| Port nav | 3W LED red 625nm | 700mA CC, PWM | 12V VTX |
| Starboard nav | 3W LED green 520nm | 700mA CC, PWM | 12V VTX |
| Strobes | 3W LED white 6500K | 700mA CC, PWM | 12V VTX |
| Landing light | 10W LED 6500K (XML-T6, 3A) | 3A adjustable CC, PWM | 12V VTX |
| Afterburner | BA15S P21W 12V auto bulb | built-in CC IC (no driver) | servo BEC / dedicated tap ⚠️ |
| Accent | 12V COB strip (green, 3 mm) | IRLZ44N MOSFET switch | 12V VTX |

(3W LED stock: 10× each red/green/white. Diffusion via frosted **PP sheet** 0.5 mm.)

## Why 3W + PWM dimming

One LED type, brightness set per-channel by PWM on the driver: 3W @ 100% = bright strobe; @ ~30–40%
= nav-light level; @ ~10% = accent. High-power LEDs **cannot** connect directly to 12V (Vf
~3.2–3.4V) — each needs a **constant-current driver**, not a voltage regulator. A voltage regulator
on an LED causes thermal runaway → burnout.

## LED driver heat — power them from 12V, not 22V

The CC drivers are essentially linear: they dissipate the input–output voltage difference as heat.

- From **22.2V** battery: a 700mA driver wastes ~16.2V × 0.7A ≈ **11.3W each** (33.9W for three) —
  far too hot.
- From the **12V VTX rail**: ~6V dropout × 0.7A ≈ **2.9W each** — manageable. **This is why the 12V
  rail exists.**

**Heatsinks:** the 700mA/3A drivers need heatsinks. **14×14×6 mm** (black anodised — better
radiation than bare silver) suits the small drivers; 4 used, rest spare. The **10W landing-light**
driver/LED needs more (~400 mm²): use **two 14×14 stacked** or one **≥20×20 mm**, and **thermal-glue
the 10W LED to metal, never directly to LW-PLA** (LW-PLA softens ~60 °C). Landing light is
intermittent (approach/landing only), which eases cooling.

## Current budget (12V VTX/CAM rail, 2A)

| Load | Current |
|------|---------|
| Red + green nav (dimmed) | ~0.6–0.7A |
| White strobes ×2 | avg ~0.14A (10% duty), ~1.4A peak |
| COB strip | ~0.13A |
| 10W landing light | ~0.82A (intermittent) |

Nav + COB + strobe average ≈ **0.84A** ✅. Adding the landing light during approach pushes it up but
it's brief. The **afterburner bulb is the problem child**: rated 17–18W ≈ 1.4–1.5A, which alone
plus other loads exceeds the 2A rail.

### Afterburner power & the CANBUS-resistor mod

The BA15S P21W is an automotive LED bulb with a built-in **CANBUS load resistor** that *wastes*
power to fake an incandescent bulb's current draw for a car computer — useless here. **Remove it**
(open base, desolder the resistor that runs hot): actual LED draw drops from ~1.5A to **~0.7A**,
keeping it cool and within budget. Even so, **power the afterburner from the servo BEC or a
dedicated 12V tap, not the VTX rail** to avoid crowding it. Use the **BA15S** (straight pins,
180°) variant — easier to 3D-print a socket for than BAU15S (offset). Buy a **BA15S socket** for
mounting. Amber/yellow (~3000K) gives the right glow.

## Pico/RP2040 control

```
Pico GPIO (PWM) → driver PWM input → controls brightness/strobe
PDB 12V        → driver input      → LED output
Pico GPIO      → IRLZ44N gate      → switches 12V COB strip on/off
```

Pin assignments (design values): GPIO 10 (red), 11 (green), 12 (strobe), 15 (strobe-enable alt).
See [Pico pin map](04-raspberry-pi-pico.md#pin-map). The IRLZ44N is a logic-level MOSFET so a 3.3V
GPIO drives the gate directly.

```python
import machine, time
red_nav   = machine.PWM(machine.Pin(10)); red_nav.freq(1000)
green_nav = machine.PWM(machine.Pin(11)); green_nav.freq(1000)
red_nav.duty_u16(int(65535 * 0.4))
green_nav.duty_u16(int(65535 * 0.4))
strobe = machine.Pin(12, machine.Pin.OUT)
while True:
    strobe.on();  time.sleep_ms(50)
    strobe.off(); time.sleep_ms(950)
```

See [`code/pico/led_control.py`](../code/pico/led_control.py).

## Notes & TODO

- Remove the CANBUS resistor from the afterburner bulb on arrival; wire it to servo BEC / dedicated tap.
- Decide afterburner behaviour: throttle-reactive (brighter at high throttle) vs always-on.
- Confirm 10W landing-light heatsink (stack two 14×14 vs one ≥20×20) and metal mounting.
- Decide COB strip use (interior accent vs exterior) and final colour(s).
- Decide final strobe method (PWM dim vs hard enable) and flash pattern.

## Related

[Raspberry Pi Pico](04-raspberry-pi-pico.md) · [Power System](02-power-system.md) ·
[Bill of Materials](11-bill-of-materials.md)

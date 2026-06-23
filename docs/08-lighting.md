# Lighting

> **Current plan:** one LED type — **3W high-power LEDs** (red, green, white) — each on a 700mA
> constant-current step-down driver with PWM dimming, controlled by the **Pico**. Nav lights run
> constant at ~40% brightness; white strobes flash in software. Powered from the PDB **12V VTX/CAM
> rail**.

## Nav light scheme (scale-correct)

| Light | Colour | Location |
|-------|--------|----------|
| Port nav | Red | Left wingtip |
| Starboard nav | Green | Right wingtip |
| Strobe | White | Both wingtips (+ optional tail) |

## Why 3W + PWM dimming (not mixed 1W/3W)

A single LED type simplifies stocking and wiring; brightness is set per-channel by PWM on the
driver board:

- 3W @ 100% → bright strobe
- 3W @ ~30–40% → equivalent to a 1W nav light, not blinding at RC scale
- 3W @ ~10% → dim interior/accent

At a 700–800 mm wingspan, 1W strobes would actually be sufficient, but since the drivers dim, buying
all-3W and turning them down is simpler and more flexible. (Inventory: 10× each 3W red / green /
white on hand.)

> High-power LEDs **cannot** connect directly to 12V — their forward voltage is ~3.2–3.4V and
> they'd burn out instantly. Each LED/group needs a **constant-current driver**.

## Driver board

**3W 5–35V LED driver, 700mA constant current, PWM-dimmable, step-down (buck)** — ~€1.86 each.

| Spec | Value |
|------|-------|
| Input | 5–35 V (12V from PDB ✅) |
| Output | 700 mA constant current (matches a 3W LED) |
| Dimming | PWM input pin (driven by Pico GPIO) |
| Topology | Step-down → efficient, low heat |

**Quantity: 1 driver per LED channel** — typically 3–4: red nav, green nav, white strobe(s),
optional tail. ~€6–7 total for the driver set; ~€10 for the complete lighting system.

## Current budget (12V VTX/CAM rail, 2A)

| Load | Current |
|------|---------|
| 1W-equivalent red nav | ~350 mA |
| 1W-equivalent green nav | ~350 mA |
| 3W white strobe ×2 | ~700 mA each = 1400 mA |

All-on simultaneous peak ≈ 2.1 A would exceed the 2A rail — **but strobes flash** at ~10% duty:

- Average strobe current: 700 mA × 10% × 2 ≈ 140 mA
- Average nav current: ~700 mA
- **Average total ≈ 840 mA** ✅ comfortably within 2A
- Peak during a flash ≈ 2.1 A for milliseconds — fine.

## Pico control

```
Pico GPIO (PWM) → driver PWM input → controls brightness
PDB 12V        → driver input      → LED output
```

Nav lights held at constant duty; strobes flashed by timing. Pin assignments: GPIO 10 (red),
GPIO 11 (green), GPIO 12 (strobe), with GPIO 15 reserved for a hard on/off strobe-enable
alternative — see [Pico pin map](04-raspberry-pi-pico.md#pin-map).

```python
import machine, time
# Nav lights: constant dim
red_nav   = machine.PWM(machine.Pin(10)); red_nav.freq(1000)
green_nav = machine.PWM(machine.Pin(11)); green_nav.freq(1000)
red_nav.duty_u16(int(65535 * 0.4))
green_nav.duty_u16(int(65535 * 0.4))
# Strobe: ~1 Hz flash
strobe = machine.Pin(12, machine.Pin.OUT)
while True:
    strobe.on();  time.sleep_ms(50)
    strobe.off(); time.sleep_ms(950)
```

See [`code/pico/led_control.py`](../code/pico/led_control.py).

## Notes & TODO

- 3W LEDs need a small heatsink, especially the strobes in a tight wingtip — budget for 7×7×6 mm
  aluminium heatsinks.
- A 12V COB LED strip (~400 LED/m) was an earlier idea for navigation accent lighting; the
  discrete 3W LED + driver approach is the current plan.
- Decide final strobe method (PWM dim on GPIO 12 vs hard enable on GPIO 15) and flash pattern
  (single vs double-flash to mimic real aircraft).

## Related

[Raspberry Pi Pico](04-raspberry-pi-pico.md) · [Power System](02-power-system.md) ·
[Bill of Materials](11-bill-of-materials.md)

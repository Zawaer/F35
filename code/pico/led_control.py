"""Navigation light + strobe control for the Raspberry Pi Pico.

Drives constant-current 3W LED driver boards (700mA, PWM-dimmable) from the PDB 12V rail.
Nav lights run at a constant ~40% brightness; the white strobe flashes at ~1 Hz.
See docs/08-lighting.md and docs/04-raspberry-pi-pico.md.

Pins (GPIO -> LED driver PWM input):
    10 = red nav   (port wingtip)
    11 = green nav (starboard wingtip)
    12 = white strobe (wingtips)
    15 = strobe enable (alternative hard on/off method)
"""

import machine
import time

NAV_BRIGHTNESS = 0.40       # 0.0-1.0
STROBE_ON_MS = 50
STROBE_OFF_MS = 950         # ~1 Hz

red_nav = machine.PWM(machine.Pin(10))
green_nav = machine.PWM(machine.Pin(11))
strobe = machine.PWM(machine.Pin(12))

for pwm in (red_nav, green_nav, strobe):
    pwm.freq(1000)


def set_nav(brightness=NAV_BRIGHTNESS):
    duty = int(65535 * brightness)
    red_nav.duty_u16(duty)
    green_nav.duty_u16(duty)


def strobe_once():
    strobe.duty_u16(65535)
    time.sleep_ms(STROBE_ON_MS)
    strobe.duty_u16(0)
    time.sleep_ms(STROBE_OFF_MS)


if __name__ == "__main__":
    set_nav()
    while True:
        strobe_once()

# Pico firmware

MicroPython for the Raspberry Pi Pico — the F-35B's secondary I/O controller. See
[docs/04-raspberry-pi-pico.md](../../docs/04-raspberry-pi-pico.md) for the full role and pin map.

**No firmware yet** — it will be written once the actual components are in hand. The wiring and
divider recipes are recorded in the docs. Planned modules:

| Module | Purpose |
|------|---------|
| temperature | Read NTC 100K thermistors via a CD74HC4067 multiplexer on the ADC — single shared 47 kΩ divider on the mux SIG line (see [Sensors](../../docs/07-sensors-monitoring.md#temperature-sensing-ntc-100k--multiplexer)) |
| LED control | Nav-light dimming + white strobe pattern (see [Lighting](../../docs/08-lighting.md)) |

Still to do (when firmware is written):

- UART link to the F405 (PWM commands in, temperature telemetry out).
- Secondary PWM servo outputs (gear doors, lift-fan doors, canopy, nozzle).
- Combine temp + LED + servo loops into one `main.py` with the UART protocol.

Requires MicroPython on the Pico.

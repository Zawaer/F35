# Pico firmware

MicroPython for the Raspberry Pi Pico — the F-35B's secondary I/O controller. See
[docs/04-raspberry-pi-pico.md](../../docs/04-raspberry-pi-pico.md) for the full role and pin map.

| File | Purpose |
|------|---------|
| `temp_logger.py` | Read all DS18B20 temperature sensors on the GPIO 26 1-Wire bus (see [Sensors](../../docs/07-sensors-monitoring.md)) |
| `led_control.py` | Nav-light dimming + white strobe pattern (see [Lighting](../../docs/08-lighting.md)) |

These are reference/working snippets, not yet the integrated flight firmware. Still to do:

- UART link to the F405 (PWM commands in, temperature telemetry out).
- Secondary PWM servo outputs (gear doors, lift-fan doors, canopy, nozzle).
- Combine temp + LED + servo loops into one `main.py` with the UART protocol.

Requires MicroPython on the Pico; `onewire` and `ds18x20` are built-in modules.

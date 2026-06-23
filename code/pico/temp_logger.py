"""DS18B20 temperature logger for the Raspberry Pi Pico.

All DS18B20 sensors share one 1-Wire bus on GPIO 26 with a 4.7kOhm pull-up to 3.3V.
Each sensor has a unique 64-bit address; hardcode the addresses below after running
`scan_addresses()` once with sensors connected one at a time (see docs/07-sensors-monitoring.md).

Wiring:
    Pico 3.3V --- 4.7k --+-- DQ  (pin 2) all sensors
    Pico GPIO26 --------/
    Pico GND ------------ GND (pin 1) all sensors
    Pico 3.3V ----------- VDD (pin 3) all sensors
"""

import machine
import onewire
import ds18x20
import time

ONE_WIRE_PIN = 26

ow = onewire.OneWire(machine.Pin(ONE_WIRE_PIN))
ds = ds18x20.DS18X20(ow)

# Hardcode after labelling each physical sensor (placeholders — replace with real addresses).
SENSORS = {
    "ESC1": b"\x28\xff\x64\x1e\x16\x05\x00\x1c",
    "ESC2": b"\x28\xff\x64\x2a\x16\x05\x00\x1c",
    "BAT1": b"\x28\xff\x64\x3b\x16\x05\x00\x1c",
    # "BAT2": b"...",            # optional
    # "EXHAUST": b"...",         # optional EDF duct-exit sensor
}


def scan_addresses():
    """Print all sensor addresses currently on the bus.

    Connect ONE sensor at a time, run this, and record the printed address against
    the physical sensor (mark it with coloured heat-shrink). Repeat for each sensor.
    """
    found = ds.scan()
    for addr in found:
        print(addr)
    return found


def read_all():
    """Return {name: temp_celsius} for all hardcoded sensors."""
    ds.convert_temp()
    time.sleep_ms(750)  # 12-bit conversion time
    return {name: ds.read_temp(addr) for name, addr in SENSORS.items()}


if __name__ == "__main__":
    # If addresses are not yet known, discover them first.
    if not SENSORS:
        scan_addresses()
    else:
        while True:
            temps = read_all()
            print(", ".join("{}={:.1f}C".format(n, t) for n, t in temps.items()))
            # TODO: forward `temps` to the F405 over UART for ArduPilot blackbox logging.
            time.sleep(1)

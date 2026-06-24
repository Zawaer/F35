"""NTC thermistor temperature logger for the Raspberry Pi Pico (RP2040).

Reads up to 16 NTC 100K thermistors through a CD74HC4067 16-channel analog multiplexer.
Each NTC forms a divider with a 10kOhm resistor; the mux SIG output goes to one Pico ADC pin,
and four GPIOs select the channel. See docs/07-sensors-monitoring.md and docs/04-raspberry-pi-pico.md.

Divider:  3.3V --- 10k ---+--- NTC --- GND     (SIG taken at the junction, per channel)
Mux:      S0..S3 <- GPIO (channel select), SIG -> Pico ADC

NOTE: replaces the earlier DS18B20 1-Wire approach.
"""

import machine
import time

# --- wiring ---
SIG_ADC_PIN = 26                 # CD74HC4067 SIG -> Pico ADC
SELECT_PINS = (18, 19, 20, 21)   # S0..S3 channel-select GPIOs
SERIES_R = 100_000.0             # divider resistor (ohms) — set to the resistor actually fitted.
                                 # NTC is 100K B3950, so ~47-100K centres the room-to-100C range
                                 # far better than 10K (10K cramps the low/cold end).
VREF = 3.3

# --- NTC 100K B3950 constants (beta model) ---
NTC_R25 = 100_000.0
NTC_BETA = 3950.0
T25_K = 298.15

# Which mux channel is which sensor (label as you wire them).
SENSORS = {
    "ESC1": 0,
    "ESC2": 1,
    "BAT1": 2,
    # "BAT2": 3,
    # "EXHAUST": 4,
}

adc = machine.ADC(SIG_ADC_PIN)
select = [machine.Pin(p, machine.Pin.OUT) for p in SELECT_PINS]


def _set_channel(ch):
    for i, pin in enumerate(select):
        pin.value((ch >> i) & 1)
    time.sleep_us(50)  # let the mux settle


def read_raw(ch):
    _set_channel(ch)
    return adc.read_u16()


def read_temp_c(ch):
    """Convert one channel's divider reading to deg C via the NTC beta equation."""
    raw = read_raw(ch)
    v = raw / 65535.0 * VREF
    if v <= 0 or v >= VREF:
        return None
    r_ntc = SERIES_R * v / (VREF - v)          # NTC on the low side
    import math
    inv_t = 1.0 / T25_K + (1.0 / NTC_BETA) * math.log(r_ntc / NTC_R25)
    return 1.0 / inv_t - 273.15


def read_all():
    return {name: read_temp_c(ch) for name, ch in SENSORS.items()}


if __name__ == "__main__":
    while True:
        temps = read_all()
        print(", ".join("{}={:.1f}C".format(n, t) for n, t in temps.items() if t is not None))
        # TODO: forward `temps` to the F405 over UART for ArduPilot blackbox logging.
        time.sleep(1)

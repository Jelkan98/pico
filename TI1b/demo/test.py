from machine import Pin
import time

# Define LED pins
leds = [
    Pin(0, Pin.OUT),  # GP0
    Pin(1, Pin.OUT),  # GP2
    Pin(2, Pin.OUT),  # GP4
    Pin(3, Pin.OUT),  # GP5
    Pin(4, Pin.OUT)   # GP6
]

# Test function to light each LED in sequence
def test_sequence():
    while True:
        # Light each LED one by one
        for led in leds:
            led.value(1)
            time.sleep(0.5)
            led.value(0)
            time.sleep(0.2)

# Run the test
test_sequence()

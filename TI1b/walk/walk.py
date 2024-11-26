from machine import Pin
import time

led_pins = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT)
]

def clear_leds():
    for led in led_pins:
        led.off()

def kitt_pattern(delay_time):
    
    for i in range(len(led_pins)):
        clear_leds()
        led_pins[i].on()
        time.sleep(delay_time)
    
    
    for i in range(len(led_pins)-2, 0, -1):
        clear_leds()
        led_pins[i].on()
        time.sleep(delay_time)

delay = 0.1
while True:
    kitt_pattern(delay)
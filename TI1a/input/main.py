from machine import Pin
import time

led = Pin(20, Pin.OUT)      
gpio_red = Pin(18, Pin.IN, Pin.PULL_DOWN)    
gpio_green = Pin(19, Pin.IN, Pin.PULL_DOWN)   


led.value(0)

while True:
    if gpio_green.value():  
        led.value(1)    
        
    if gpio_red.value():
        led.value(0)    
        
    time.sleep(0.1)     
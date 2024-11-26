from machine import Pin, ADC
import time

# Use on-board led and temperature sensor
led = Pin("LED", Pin.OUT)
temp_sensor = ADC(4)  # Internal temperature sensor on ADC4

# Blink led to confirm successful flashing
for _ in range(5):
    led(0)
    time.sleep(.1)
    led(1)
    time.sleep(.1)

def read_temperature():
    # Read voltage from temperature sensor
    voltage = temp_sensor.read_u16() * (3.3 / 65535)
    # Calculate temperature using the provided formula
    temperature = 27 - (voltage - 0.706) / 0.001721
    return round(temperature, 1)

# Wait for data from the connection
while True:
    data = input()

    print("Received '" + data + "'.")
    if data == '0':
        print("Turning led off.")
        led(0)
    elif data == '1':
        print("Turning led on.")
        led(1)
    elif data == 't':
        temp = read_temperature()
        print(f"Temperature: {temp}°C")
    else:
        print("Unknown command.")

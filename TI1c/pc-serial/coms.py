import serial
import time

# Configure serial connection (adjust COM port as needed)
ser = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)  # Wait for connection to establish

while True:
    command = input("Enter command (0=LED off, 1=LED on, t=temperature): ")
    
    # Send command to Pico
    ser.write((command + '\n').encode())
    
    # Read response from Pico
    response = ser.readline().decode().strip()
    print(response)
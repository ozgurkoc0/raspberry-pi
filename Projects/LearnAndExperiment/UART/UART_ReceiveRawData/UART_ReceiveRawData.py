import serial
import time

ser = serial.Serial('/dev/ttyS0', baudrate = 115200, timeout = 1)

while True:
    
    data = ser.read();
    print(data)
from __future__ import print_function
import serial
import io
import time

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0, xonxoff=True)

print("Serial open:", ser.isOpen())
send = bytearray.fromhex('55fd')
print(send)
ser.write(send)
while ser.inWaiting() == 0:
    x=2
bytesToRead = ser.inWaiting()
print(bytesToRead)
print(ser.read(bytesToRead))
while ser.inWaiting() == 0:
    x=2
bytesToRead = ser.inWaiting()
print(bytesToRead)
print(ser.read(bytesToRead))
exit = 0
ch1 = 0
ch2 = 0
ch3 = 0
ch4 = 0
ch5 = 0
ch6 = 0
while exit == 0:
    while ser.inWaiting() == 0:
        #do nothing
        x=2
    bytesToRead = ser.inWaiting()
    read = ser.read(bytesToRead)
    for i in read:
        print("{0:9b}".format(i), end = '')
    print("")
print(ser.close())

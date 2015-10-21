from __future__ import print_function
import serial
import io
import time

def main():
    ser = openSerial()
    getChannelPositions(ser)
    print(ser.close())

def openSerial():
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0, xonxoff=True)
    return ser

def getChannelPositions(ser):
    print("Serial open:", ser.isOpen())
    send = bytearray.fromhex('55fd')
    print(send)
    ser.write(send)
    while ser.inWaiting() == 0:
        time.sleep(.007)
    bytesToRead = ser.inWaiting()
    ser.read(bytesToRead)
    while ser.inWaiting() == 0:
        time.sleep(.007)
    bytesToRead = ser.inWaiting()
    ser.read(bytesToRead)
    exit = 0

    # infinite loop
    while exit == 0:
        while ser.inWaiting() == 0:
            time.sleep(.007)
        bytesToRead = ser.inWaiting()

        # Sometimes only 17 bytes are sent with a byte missing from channel 4
        if bytesToRead != 18:
            ser.flushInput()
        else:
            read = ser.read(bytesToRead)
            data = 0
            for i in read:
                data = (data<<8) + i
            channels = []
            while data !=0:
                channels.append(data & 65535)
                data = data >> 16
            channels.reverse()

            print(channels)

if __name__ == "__main__":
    main()

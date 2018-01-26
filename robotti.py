import serial
import time

def main():

    connected = False
    ser = serial.Serial("COM4", 9600)
    if ser:
        connected = True
        ser.write(bytes(b'1'))
    time.sleep(5)
    ser.close()


main()

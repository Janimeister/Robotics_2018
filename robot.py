import serial
import time

def main():
    try:
        ser = serial.Serial("/dev/rfcomm0", 9600)
        while 1:
            ser.write("1".encode())
    except:
        print("Error connecting to serialport. Aborting...")
    
main()

import serial
import time
import neural_network as nn

def main():
    try:
        ser = serial.Serial("COM4", 9600)
    except:
        print("Error connecting to serialport. Aborting...")
    
    
main()

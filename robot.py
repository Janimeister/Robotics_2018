import serial
import time
import neural_network as nn
def main():
    """
    connected = False
    ser = serial.Serial("COM4", 9600)
    if ser:
        connected = True
        while (connected):
            ser.write(b'1')
    ser.close()
    """
    nn.Qlearn_initialize()
    
main()

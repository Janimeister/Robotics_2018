import serial
import neural_network
import time
def main():
    model = neural_network.initialize()
    data = 0
    #Open serial port between Arduino and Raspberry Pi
    ser = serial.Serial("/dev/rfcomm0", 9600)
    while True:
            print("Reading from serial: ")
            try:
                #Read sensor values
                bt_data = (ser.readline().strip())
                bt_data = bt_data.decode("utf-8")
                
                s_list = bt_data.split(',')
                s_list = list(map(int, s_list))
                
                print("Read data is: ", s_list)
                
                #Send the sensor readings to neural network
                state = neural_network.data(s_list)
                time.sleep(1.5)
                
                #Read new sensor values
                bt_data = (ser.readline().strip())
                bt_data = bt_data.decode("utf-8")
                
                s_list = bt_data.split(',')
                s_list = list(map(int, s_list))
                
                #Send the sensor readings to neural network
                state_new = neural_network.data(s_list)
                #Call training function in NN to get next action (direction)
                model, action = neural_network.nn_train_sensor(model, state, state_new)
                time.sleep(0.5)
                print("Action is: " ,action)
                #Send desired action to Arduino
                ser.write(str(action).encode())
                time.sleep(0.5)

            except:
                print("Something was wrong with the data...")

main()

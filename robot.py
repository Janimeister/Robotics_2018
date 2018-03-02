import serial
import neural_network
def main():
    model = neural_network.initialize()
    data = 0
    ser = serial.Serial("/dev/rfcomm0", 9600)
    while True:
            print("Reading from serial: ")
            #try:
            bt_data = (ser.readline().strip())
            bt_data = bt_data.decode("utf-8")
            
            s_list = bt_data.split(',')
            s_list = list(map(int, s_list))
            
            print("Read data is: ", s_list)
            
            #Lisätään lista printtauksen lisäksi neuroverkolle
            
            state = neural_network.data(s_list)
            model, action = neural_network.nn_train_sensor(model, state)
            print("Action is: " ,action)
            ser.write(str(action).encode())
"""
            except:
                print("Something was wrong with the data...")
"""
main()

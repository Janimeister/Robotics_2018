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
            lista = bt_data.split(',')
            print("Read data is: ", lista)
            #Lisätään lista printtauksen lisäksi neuroverkolle
            state = data(lista)
            model, action = neural_network.nn_train_sensor(model, state)
            print("Action before converting: ", action)
            action = str(action)
            print("Action is: " ,action)
            ser.write(action.encode())
"""
            except:
                print("Something was wrong with the data...")
"""
main()

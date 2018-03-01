import serial
import neural_network
def main():
    model = neural_network()
    data = 0
    ser = serial.Serial("/dev/rfcomm0", 9600)
    while True:
	    print("Reading from serial: ")
            try:
                    data = (ser.readline().strip())
                    data = data.decode("utf-8")
                    lista = data.split(',')
                    #Lisätään lista printtauksen lisäksi neuroverkolle
                    state = data(lista)
                    model, action = neural_network.nn_train_sensor(model, state)
                    ser.write(action.encode())

            except:
                    print("Something was wrong with the data...")
                    var2 = input("Haluatko varmasti lopettaa?: ")
                    if var2 == "y": quit()
main()

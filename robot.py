import serial

def main():
	data = 0
	ser = serial.Serial("/dev/rfcomm0", 9600)
	while True:
		print("Reading from serial: ")
		try:
			data = (ser.readline().strip())
			data = data.decode("utf-8")
			lista = data.split(',')
			#Lisätään lista printtauksen lisäksi neuroverkolle
			print(lista)
			#Tietojen perusteella lähetetään vastaus neuroverkolta
			#Tyylillä ser.write("neuroverkonvastaus")
			var = input("Lähetä jotakin arduinolle(1-4): ")
			ser.write(var.encode())
		except:
			print("Something was wrong with the data...")
			var2 = input("Haluatko varmasti lopettaa?: ")
			if var2 == "y": quit()
main()

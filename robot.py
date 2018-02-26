import serial

def main():
	data = 0
	ser = serial.Serial("/dev/rfcomm0", 9600)
	while True:
		print("Reading from serial: ")
		data = (ser.readline().strip())
		data = data.decode("utf-8")
		lista = data.split(',')
		print(lista)

main()

import serial

class keypad:

	kpad = -1
	#BaudRate = 9600
	#keypadLocation = "/dev/ttyUSB0"

	def __init__(self):
		global kpad
		#global keypadLocation
		#global BaudRate
		kpad = serial.Serial("/dev/ttyUSB0",9600)
		
		
	def ReadLine():
		global kpad
		
		while kpad.inWaiting() > 0:
			buff += kpad.read()
			
		return buff
		
	def SendLine(data):
		global kpad
		
		kpad.write(data)

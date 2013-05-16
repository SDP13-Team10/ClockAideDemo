import serial, string


class keypad:

	kpad = -1
	#BaudRate = 9600 keypadLocation = "/dev/ttyUSB0"

	def __init__(self):
		global kpad
		# global keypadLocation global BaudRate
		kpad = serial.Serial("/dev/ttyUSB0",9600)
		
		
	def ReadLine(self):
		global kpad
		#buff = ""
		#while buff.__len__() == 0:
		#	while kpad.inWaiting() > 0:
		#		buff = buff + kpad.read()
			
		#return buff
		return kpad.read()

	def SendLine(self,data):
		global kpad
		
		return kpad.write(data)

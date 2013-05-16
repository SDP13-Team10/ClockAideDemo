import serial, string


class keypad:

	kpad = -1
	#BaudRate = 9600 keypadLocation = "/dev/ttyUSB0"

	def __init__(self):
		global kpad
		# global keypadLocation global BaudRate
		kpad = serial.Serial("/dev/ttyUSB5",9600)
		
		
	def ReadLine(self):
		#global kpad
		#buff = ""
		#temp = ""
		#while buff.__len__() == 0 and kpad.inWaiting() >0:
		#	buff = kpad.read()
		#	temp = temp + buff			
		#	buff = ""
		#return temp
		return kpad.read()

	def SendLine(self,data):
		global kpad
		
		return kpad.write(data)

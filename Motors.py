import serial

class motors:

	motor = -1
	#BaudRate = 9600
	#motorLocation = "/dev/ttyUSB1"

	def __init__(self):
		global motor
		#global BaudRate
		#global motorLocation
		
		motor = serial.Serial("/dev/ttyUSB1",9600)
		
		
	def ReadLine():
		global motor
		
		while motor.inWaiting() > 0:
			buff += motor.read()
			
		return buff
		
	def SendLine(data):
		global motor
		
		motor.write(data)

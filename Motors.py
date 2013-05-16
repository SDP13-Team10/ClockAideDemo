import serial

class motors:

	motor
	BaudRate = 9600
	keypadLocation = "/dev/ttyUSB0"

	def __init__(self):
		global motor
		
		motor = serial.Serial(keypadLocation,BaudRate)
		
		
	def ReadLine():
		global motor
		
		while motor.inWaiting() > 0:
			buff += motor.read()
			
		return buff
		
	def SendLine(data):
		global motor
		
		motor.write(data)
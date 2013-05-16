
import time	# Does not execute this command when launched from terminal
from commands import *
from ClockAideTime import *
from Keypad import *
from Motors import *

keypad = keypad()
motor = motors()

def initialization():
	global mode
	global currentTime
	time.sleep(2)
	#keypad.flush()
	#motor.flush()
	
	currentTime = datetime.datetime.now()
	print(keypad.SendLine(currentTime.strftime("%H, %M, %S, %d, %m, %Y")))
	print(motor.SendLine(currentTime.strftime("%H, %M, %S, %d, %m, %Y")))
	
	time.sleep(2)
	
	return modes[0]
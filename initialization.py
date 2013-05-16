
import time	# Does not execute this command when launched from terminal
from commands import *
from ClockAideTime import *
from Keypad import *
from Motors import *

pad = keypad()
mtr = motors()
mode = -1
currentTime = -1

def initialization():
	global mode
	global currentTime
	time.sleep(2)
	#keypad.flush()
	#motor.flush()
	
	currentTime = datetime.datetime.now()
	pad.SendLine(currentTime.strftime("%H, %M, %S, %d, %m, %Y"))
	#keypad.SendLine("12, 03, 00, 12, 12, 2003")
	mtr.SendLine(currentTime.strftime("%H, %M, %S, %d, %m, %Y"))
	
	time.sleep(2)
	
	return modes[0]

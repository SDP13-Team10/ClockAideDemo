#!/usr/bin/python	
# Normal Mode (Can be launched two ways: python normal.py or ./normal.py with permission)

import time	# Does not execute this command when launched from terminal
#from commands import *
from ClockAideTime import *
import Keypad
import Motors
from commands import *
from SpeakTime import speakTime

keypad = Keypad.keypad()
motor = Motors.motors()



def normal():
	print "in normal"
	lineRead = keypad.ReadLine()
	lineRead = str(lineRead)
	comm = COMMAND[lineRead]
	print "received" 
	print comm
	if comm == "SPEAK_TIME":
		speakTime(nowHour(), nowMinute())
		print(keypad.SendLine(modeLookUp["normal"]))
		#keypad.flushInput()
		comm = ""
		print comm
		print(keypad.SendLine(modeLookUp["normal"]))
		print(motor.SendLine(modeLookUp["normal"]))
		return modes[0]
	elif comm == "WAKE_UP":					## send check ID signal to keypad and motor
		print(keypad.SendLine(modeLookUp["auth"]))
		print(motor.SendLine(modeLookUp["auth"]))
			
		return modes[1]						## return statements???
	else:
		return modes[0]


		


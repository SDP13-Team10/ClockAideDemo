#!/usr/bin/python	
# Normal Mode (Can be launched two ways: python normal.py or ./normal.py with permission)

import time	# Does not execute this command when launched from terminal
from commands import *
from ClockAideTime import *
from Keypad import *
from Motors import *
from ClockAideSpeakTime import *



keypad = keypad()
motor = motors()



def normal():
	print "in normal"
	comm = COMMAND[str(keypad.ReadLine())]		## use different method other than stuff dictionary
	print "received" 
	print comm
	if comm == "SPEAK_TIME":
		speakTime(nowHour(), nowMinute())
		print(keypad.write(modeLookUp["normal"]))
		keypad.flushInput()
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


		


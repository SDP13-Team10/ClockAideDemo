import time	# Does not execute this command when launched from terminal
from commands import *
from ClockAideTime import *
from questionBank import QuestionBank
from keypad import *
from Motors import *
from DB import *

keypad = keypad()
motor = motors()

def auth():

	TeacherID = 01475963
	AdminID = 36957410
	DB clockAideDB = DB("ClockAideDB")
	
	id = keypad.ReadLine()
	clockAideDB.authenticateUser(id)
	if id == TeacherID:
		keypad.SendLine(MODES['4'])
		return [,,modes[4]]								# auth() returns a list of the form [ID, Name, Session - True/False, Mode - Read/Set]
		
	elif id == AdminID:
		keypad.SendLine(MODES['5'])
		return [,,modes[5]]								# auth() returns a list of the form [ID, Name, Session - True/False, Mode - Read/Set]
		
	elif clockAideDB.isUserAuthenticated():
		
		keypad.SendLine(command["good"])			# Sends "Correct" Code to Keypad
		time.sleep(2)
		keypad.SendLine(name)					# Sends Student Name to Keypad
		
		# beginning logging information
		
		return [0,'',modes[int(keypad.ReadLine())]]		# auth() returns a list of the form [ID, Name, Session - True/False, Mode - Read/Set]
	else:
		print(keypad.SendLine(command["wrong"]))		# Sends "Wrong" Code to Keypad
		time.sleep(2)
		return modes[0]	
	

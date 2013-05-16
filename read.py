import time	# Does not execute this command when launched from terminal
from commands import *
from ClockAideTime import *
from questionBank import QuestionBank
from keypad import *
from Motors import *
from DB import *

keypad = keypad()
motor = motors()

qBank = QuestionBank(databaseLocation)
DB clockAideDB = DB("ClockAideDB")

def read(id, sessionActive):
	qBank.generateTime()
	readTime = readModeTime(id)
	numAttempts = 0
	#answerRight = 
	#while sessionActive && answerWrong:
	while (sessionActive && (numAttempts < 3)):
		
		keypad.SendLine(modeLookUp["read"])
		motor.SendLine(modeLookUp["read"])
		time.sleep(2)
		
		motor.SendLine(readTime)		## send time to be displayed to motor
		#randomTime = qBank.getTimeTouple()
		#speakTime(randomTime[0],randomTime[1])
		keypadTime = keypad.ReadLine()			## include some timeout logic

	# Check time entered for correctness and send appropriate signal.
	# Create a readtime function

		if checkReadTime(keypadTime,readTime):
			numAttempts = 0
			
			clockAideDB.addToStudentResponseTable(clockAideDB.getQuestionID(), keypadTime)
			
			print(keypad.SendLine(command["good"]))
			time.sleep(2)
			print(keypad.SendLine(command["more"]))
						
			response = keypad.ReadLine()
			if response == command["ack"]:
				qBank.generateTime()
				readTime = readModeTime(id)
				sessionActive = True
			else:
				keypad.SendLine(modeLookUp["normal"])
				sessionActive = False
				
			#return modes[0]
		else:
			numAttempts++
			
			clockAideDB.addToStudentResponseTable(clockAideDB.getQuestionID(), keypadTime)
			
			print(keypad.SendLine(command["wrong"]))
			time.sleep(2)
			print(keypad.SendLine(command["more"]))
			response = keypad.ReadLine()
			
			if response == command["ack"]:
				sessionActive = True
				
			else:
				keypad.SendLine(modeLookUp["normal"])
				sessionActive = False
				
	return [sessionActive, modes[0]]

def readModeTime(ID):
	
	# Get difficulty level that the student is on
	# return time based on that level
	
	global qBank
	return qBank.getTimeString()
	
def checkReadTime(readTime, sentTime):

	#Remove leading whitespaces:

	readTime = re.sub("^0+","",readTime)
	sentTime = re.sub("^0+","",sentTime)

	#Convert To Integers
	readHour = int(readTime.split(',')[0])
	readMinute = int(readTime.split(',')[1])

	sentHour = int(sentTime.split(',')[0])
	sentMinute = int(sentTime.split(',')[1])

	print "Check readTime entered"
	print "Time received: " + str(readHour) + "," + str(readMinute)
	print "Time sent: " + str(sentHour) + "," + str(sentMinute)
	# compare entered time with time given to student
	# return TRUE or False
	
	if readHour == sentHour and readMinute == sentMinute:
		return True
		
	else: 
		return False
	
	#return True


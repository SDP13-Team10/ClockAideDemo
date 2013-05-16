import string, time, datetime, re

#Return the complete time and date in string format
#Required to initialize the stepper motors
def getDateTimeString():
	currentTime = datetime.datetime.now()
	#print(currentTime.strftime("%I%M"))
	return currentTime.strftime("%H, %M, %S, %d, %m, %Y")

#Returns the hour and minute in string format
def getTimeString():
    currentTime = datetime.datetime.now()
    #print(currentTime.strftime("%I%M"))
    return currentTime.strftime("%H, %M")

def getTimeTuple():
	currentTime = datetime.datetime.now()
	hour = currentTime.strftime("%H")
	minute = currentTime.strftime("%M")
	timeTouple = hour, minute
	return timeTouple
	
def nowHour():
	return datetime.datetime.now().strftime("%I")
	
def nowMinute():
	return datetime.datetime.now().strftime("%M")
	
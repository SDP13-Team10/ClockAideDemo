import sqlite3, uuid, time, string
from datetime import datetime

class DB:
	databaseLocation = ""
	connection = ""
	cursorObj = ""
	userID = -1
	sessionID = -1
	name = ""
	randomHour = -1
	randomMinute = -1
	questionID = -1

	def __init__ (self,pathToDB):
		global databaseLocation
		global connection
		global cursorObj
		global userID
		randomHour = -1

		randomMinute = -1
		databaseLocation = pathToDB
		connection = sqlite3.connect(databaseLocation)
		cursorObj = connection.cursor()

	def printDatabaseLocation(self):
		global databaseLocation
		print databaseLocation

	def authenticateUser(self, uid):
		global userID
		global name
		global cursorObj
		global sessionID
		global connection

		cursorObj.execute('SELECT * FROM students WHERE id=?', uid)
		row = cursorObj.fetchone()

		#Authentication Failure
		if row is None:
			userID = -1
			name = ""

		#Authentication Successful
		if row[0] == uid
			userID = uid
			name = row[1]
			sessionID = uuid.uuid4() #Create a unique session ID
			#Insert authentication information into DB
			cursorObj.execute('INSERT INTO sessionLog (id,sessionStartTime,sessionID) VALUES (?,?,?)', userID, datetime.now(), sessionID)
			connection.commit()

	def isUserAuthenticated():
		if userID == -1
			return false
		else:
			return true

	def endSession():
		global userID
		cursorObj.execute('INSERT INTO sessionLog (sessionEndTime) VALUES (?)', datetime.now())
		userID = -1
		name = ""

	def addToStudentResponseTable(qid,studentResponse):
		global userID
		global cursorObj
		global sessionID
		global connection
		cursorObj.execute('INSERT INTO sessionLog (sid,qid,studentResponse) VALUES (?,?,?)', userID, qid, studentResponse)

		def printDatabaseLocation(self):
		global databaseLocation
		print databaseLocation

	def generateTime(self, difficulty=None):
		global randomHour
		global randomMinute

		if difficulty is None:
			cursorObj.execute('SELECT * FROM questionBank ORDER BY RANDOM() LIMIT 1')
			row = cursorObj.fetchone()
			questionID = row[0]
			randomHour = row[1]
			randomMinute = row[2]

		else:
			d = (difficulty,)
			cursorObj.execute('SELECT * FROM questionBank WHERE difficulty=? ORDER BY RANDOM() LIMIT 1', d)
			row = cursorObj.fetchone()
			questionID = row[0]
			randomHour = row[1]
			randomMinute = row[2]

	def getTimeString(self):
		global randomHour
		global randomMinute
		hour = str(randomHour)
		minute = str(randomMinute)
		if minute == 0 or minute ==5:
			minute = "0" + minute
		return hour + "," + minute

	def getTimeTouple(self):
		global randomHour
		global randomMinute
		timeTouple = randomHour, randomMinute
		return timeTouple
	
	def getQuestionID(self):
		global questionID
		return questionID



import normal, read, set, auth, teacher, admin

def Controller:
	mode = initialization()
	
	userID = 0
	userName = ""
	userSession
	
	while 1:
		if mode == "NORMAL":
			mode = normal()
		
		elif mode == "AUTH":
			userList = auth() # auth() returns a list of the form [ID, Name, Session - True/False, Mode - Read/Set]
			userID = userList[0]
			userName = userList[1]
			userSession = userList[2]
			mode = userList[3]
			
		elif mode == "READ":
			readList = read(userID, userSession)# read(userID, userSession) returns a list of the form [Session, Mode]
			userSession = readList[0]
			if userSession == False:
				userID = 0
				userName = ""				
				mode = readList[1]
				
			else:
				mode = "READ"
		
		elif mode == "SET":
			setList = set(userID, userSession)			# set(userID, userSession) returns a list of the form [Session, Mode]
			userSession = setList[0]
			if userSession == False:
				userID = 0
				userName = ""				
				mode = setList[1]
				
			else:
				mode = "SET"
		
		
		elif mode == "TEACHER":
			mode = teacher()
			
		elif mode == "ADMIN":
			mode = admin()



BaudRate = 9600
keypadLocation = "/dev/ttyUSB0"
motorLocation = "/dev/ttyACM0"
databaseLocation = "/home/pi/ClockAideDatabase/ClockAideDB"

modes =	("NORMAL",  "AUTH",  "READ", "SET", "TEACHER", "ADMIN")

MODES =	{
	'0'  : "NORMAL", \
	'1'  : "AUTH", \
	'2'  : "READ",\
	'3'  : "SET", \
	'4'  : "TEACHER", \
	'5'  : "ADMIN"
	}

COMMAND = {
	'0'  : "GOOD", \
	'1'  : "WRONG", \
	'2'  : "WAKE_UP",\
	'3'  : "GET_TIME", \
	'4'  : "RESET", \
	'5'  : "SPEAK_TIME", \
	'6'  : "MORE", \
	'7'  : "ACK", \
	'8'  : "NAK", \
	'9'  : "DATA"
	}
	
command = {
	"good"			: '0',\
	"wrong"			: '1',\
	"wake_up"		: '2',\
	"get_time"		: '3',\
	"reset"			: '4',\
	"speak_time"	: '5',\
	"more"			: '6',\
	"ack"			: '7',\
	"nak"			: '8',\
	"data"			: '9' 
}

modeLookUp = {
	"normal"	: '0',\
	"auth"		: '1',\
	"read"		: '2',\
	"set"		: '3',\
	"teacher"	: '4',\
	"admin"		: '5'
}




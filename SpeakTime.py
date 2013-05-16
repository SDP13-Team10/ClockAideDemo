import re, os, subprocess

def speakTime(hour,minute):

	hour = str(hour)
	minute = str(minute)

	if minute is not "0":
		minute = re.sub("^0+","",minute)

	hour = re.sub("^0+","",hour)

	#print "Hour Entered " + hour
	#print "Minute Entered" + minute 

	minuteInteger = int(minute)

	hourFile = "~/ClockAideVoiceMap/Hours/"+str(hour)+".wav"
	if minute is "0":
		minuteFile="~/ClockAideVoiceMap/Wildcard/oclock.wav"
	elif minuteInteger <= 9:
		#print "Minute is single digit"
		#print minute
		minuteFile="~/ClockAideVoiceMap/Minutes/O"+str(minute)+".wav"
 	else:
		minuteFile="~/ClockAideVoiceMap/Minutes/"+str(minute)+".wav"

	playVoiceMap = "mplayer %s 1>/dev/null 2>&1 " + hourFile + " " + minuteFile
	#print playVoiceMap
	os.system(playVoiceMap)
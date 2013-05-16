import re, os, subprocess

def speakTime(hour,minute):

	hour = str(hour)
	minute = str(minute)

	if minute is not "0":
		minute = re.sub("^0+","",minute)

	hour = re.sub("^0+","",hour)

	hourFile = "~/ClockAideVoiceMap/Hours/"+str(hour)+".wav"
	if minute is "0":
		minuteFile="~/ClockAideVoiceMap/Wildcard/oclock.wav"
	elif minute is "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
		minuteFile="~/ClockAideVoiceMap/Minutes/O"+str(minute)+".wav"
 	else:
		minuteFile="~/ClockAideVoiceMap/Minutes/"+str(minute)+".wav"

	playVoiceMap = "mplayer %s 1>/dev/null 2>&1 " + hourFile + " " + minuteFile
	os.system(playVoiceMap)
#!/usr/bin/python

# ClockAide System

import time	# Does not execute this command when launched from terminal
import sys
import random

#---------------------------------
#Normal Mode
greeting = "Welcome to ClockAide!"
mode = "Normal Mode"

def normal():
 print greeting
 print mode
 time.ctime()
 clock = time.ctime()
 print clock
 control = int(raw_input("Key pressed: "))
 if control != 0:
  modeSelect()

#----------------------------------
# Mode Selector
greeting = "Welcome to Quiz Mode."
menu = "Would you like to Read the time (1), or Set the time (2)?"
prompt = "User Selection:"
#u_input = input("User Selection: ")
m_read = 1
s_read = 2

def modeSelect():
 print greeting
 print menu
 u_input = int(raw_input("User Selection: ")) #Cast required
# print u_input

 if u_input == 1:
  read()
 elif u_input == 2:
  Set()
#----------------------------------
# Read Mode

def read():
 h = random.randrange(1,12)	
 m = random.randrange(0,59)
 attempt = 0
 correct = 0
 print "*************************"
 print 'Welcome to Read Mode.'
 print "*************************"
 r_prompt = 'What time is it?'

# Move stepper motors here
 print r_prompt
 print h, m	# For debugging purposes only
 u_hr = int(raw_input("Hour: "))
 u_min = int(raw_input("Minute :"))

# Correct Answer ************** #
 if u_hr == h and u_min == m:
  print 'Correct! Good Job!'
  correct += 1
  control = int(raw_input('Try again? 1 Yes 2 No '))
  if control == 1:
   read()
  elif control == 2:
   print 'Thanks for playing. Goodbye!'
   print 'Returning to normal mode...'
   normal()
# Record activity to database

# Wrong Answer **************** #
 else:
  print "*************************"	
  print 'Sorry! That is not the correct time. Try again.'
  while attempt != 3:
  # print 'Wrong answer. Try it again'
   u_hr = int(raw_input("Hour: "))
   u_min = int(raw_input("Minute :"))
   if u_hr == h and u_min == m:
    print 'Correct! Good Job!'
    correct += 1
    control = int(raw_input('Try again? 1 Yes 2 No '))
    if control == 1:
     read()
    elif control == 2:
     print 'Thanks for playing. Goodbye!'
     print 'Returning to normal mode...'
     normal()			# Return to normal mode
   else:
    ++attempt
    print 'Correct answer is...'
    print h, m
    print '*************************'
    read() 
# Record activity to database


def Set():
 h = random.randrange(0,12)	
 m = random.randrange(0,59)

 print "*************************"
 print 'Welcome to Set Mode.'
 print "*************************"

 r_prompt = 'Set the clock to the following time:'
# Display value on LCD screen
 print h , m	
 print r_prompt
 u_hr = int(raw_input("Hour: "))
 u_min = int(raw_input("Minute :"))
 print 'Done'



def main():
 normal()
# modeSelect()

main()

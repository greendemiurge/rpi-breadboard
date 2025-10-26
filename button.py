#!/usr/bin/python3

import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	pressed = GPIO.input(16) == GPIO.LOW
	print('pressed', pressed)
	
	GPIO.output(8, GPIO.HIGH)
	if pressed:
		sleep(.1)
	else:
	  sleep(3)
	GPIO.output(8, GPIO.LOW)
	if pressed:
		sleep(.1)
	else:
		sleep(1)

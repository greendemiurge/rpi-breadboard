#!/usr/bin/python3

import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   

while True:
	GPIO.output(8, GPIO.HIGH)
	sleep(3)
	GPIO.output(8, GPIO.LOW)
	sleep(1)

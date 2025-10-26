#!/usr/bin/python3

import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

red_pin = 8
green_pin = 18

GPIO.setup(green_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(red_pin, GPIO.OUT, initial=GPIO.LOW)   
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	pressed = GPIO.input(16) == GPIO.LOW
	print('pressed', pressed)

	
	if pressed:
		sleep(.1)
		GPIO.output(green_pin, GPIO.LOW)
		sleep(.1)
		GPIO.output(green_pin, GPIO.HIGH)
	else:	
		sleep(.1)
		GPIO.output(red_pin, GPIO.LOW)
		sleep(.1)
		GPIO.output(red_pin, GPIO.HIGH)

#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Rfid:

	reader = SimpleMFRC522()

	try:
		id, text = reader.read()
		num = hex(id)
		print(num.upper())
		#print(text)
	finally:
		GPIO.cleanup()

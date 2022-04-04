import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Rfid:
	@staticmethod
	def readid():
		try:
			reader = SimpleMFRC522()
			id, text = reader.read()
			num = hex(id)
			print(num.upper())
		finally:
			GPIO.cleanup()
	#readid()
	

#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Rfid
    reader = SimpleMFRC522()
	#def read_uid(self):

    try:
        id, text = reader.read()
        print("Hola "+ id)
        #if __name__ == "__main__";
         #   rf = Rfid...()
          #  uid = rf.read_uid()
           # print(uid)

    finally:
        GPIO.cleanup()

from lcd import drivers
from time import sleep
import sys

class Rfid:

	def __init__(self):
		self.display = drivers.Lcd()

	def testLCD(self):
		try:
			self.display.lcd_backlight(1)
			print("Enter sentences that you want to be displayed:\n")
			i = 1
			#1. Llegim i anem escrivint frase per frase
			''' 
			while i <= 4: #entrem fins a 4 frases
				try:
					line = input()
				except EOFError:
					break
				self.display.lcd_display_string(line,i) #les mostrem per pantalla
				i += 1
			'''
			#2. Llegim tot alhora
			userInput = sys.stdin.readlines()
			for i in range(1,min(5, len(userInput) + 1)):
				self.display.lcd_display_string(userInput[i - 1].strip(),i)
			
			sleep(10) #Esperem 10 segons abans de borrar
			#netegem el display abans d'acabar
			self.display.lcd_clear()
			return

		except KeyboardInterrupt:
			#Si algu prem ctrl+c es neteja el display
			self.display.lcd_clear()
			return
			
	def write(self, text):
		try:
			self.display.lcd_clear()
			splitText = text.splitlines()

			for i in range(min(len(splitText), 4)):
				self.display.lcd_display_string(splitText[i],i + 1) #les mostrem per pantalla
			return

		except KeyboardInterrupt:
			#Si algu prem ctrl+c es neteja el display
			self.display.lcd_clear()
			return

if __name__ == "__main__":
	rf = Rfid()
	rf.testLCD()

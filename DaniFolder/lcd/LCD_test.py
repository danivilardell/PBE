import drivers
from time import sleep

class Rfid:

	def __init__(self, display):
		self.display = display

	def testLCD(self):
		try:
			print("Enter sentences that you want to be displayed:\n")
			i = 1
			while i <= 4: #entrem fins a 4 frases
				try:
					line = input()
				except EOFError:
					break
				self.display.lcd_display_string(line,i) #les mostrem per pantalla
				i += 1
			sleep(10) #Esperem 10 segons abans de borrar
			#netegem el display abans d'acabar
			self.display.lcd_clear()
			return

		except KeyboardInterrupt:
			#Si algu prem ctrl+c es neteja el display
			self.display.lcd_clear()
			return

if __name__ == "__main__":
	display = drivers.Lcd()
	rf = Rfid(display)
	rf.testLCD()

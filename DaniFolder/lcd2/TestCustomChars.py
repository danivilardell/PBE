from lcd import drivers

if __name__ == "__main__":
	disp = drivers.Lcd()
	customchars = drivers.CustomCharacters(disp)
	customchars.load_custom_characters_data()
	disp.lcd_display_char(0,1)

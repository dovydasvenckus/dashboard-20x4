from RPLCD.i2c import CharLCD

class Screen:
    lcd = CharLCD('PCF8574', 0x27)
    max_line_length = 20
  
    def write_line(self, line, text):
        self.lcd.cursor_pos = (line, 0)
        self.lcd.write_string(text)

    def clear(self):
        self.lcd.clear()

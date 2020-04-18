from RPLCD.i2c import CharLCD

class Screen:
    lcd = CharLCD('PCF8574', 0x27)
    max_line_count = None
    max_line_length = None
    line_buffer = []
    flushed_lines = []

    def __init__(self, line_count, line_length):
        self.max_line_count = line_count
        self.max_line_length = line_length
        self.line_buffer = [None] * line_count
  
    def write_line(self, line, text):
        if line >= 0 and self.max_line_count > line:
            self.line_buffer[line] = text

    def flush(self):
        if (self.flushed_lines == self.line_buffer):
            return

        self.lcd.clear()
        for index, line in enumerate(self.line_buffer):
            self.__flush_line(index, line)
        self.flushed_lines = self.line_buffer
        self.line_buffer = [None] * self.max_line_count

    def __flush_line(self, index, line):
        if line != None:
            self.lcd.cursor_pos = (index, 0)
            self.lcd.write_string(line)

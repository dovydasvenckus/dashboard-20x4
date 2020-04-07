#!/usr/bin/python

import time
from datetime import date

from screen import Screen
from temperature import get_temperature

screen = Screen()
running = True

seconds_passed = 0
while running:
    screen.clear()
    temperature = get_temperature() + 'C'
    padding = 20 - len(date.today().isoformat()) - len(temperature)

    screen.write_line(0, (date.today().isoformat() + ' ' * padding + temperature))

    screen.write_line(1, '07:30 Breakfast')
    screen.write_line(2, '08:00 Work')
    screen.write_line(3, '17:00 Free time') 
    time.sleep(60 * 30)

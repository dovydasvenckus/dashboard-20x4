#!/usr/bin/python

import time
from datetime import date

from screen import Screen
from temperature import get_temperature

screen = Screen(4, 20)
running = True

seconds_passed = 0
while running:
    temperature = get_temperature() + 'C'
    padding = 20 - len(date.today().isoformat()) - len(temperature)

    screen.write_line(0, (date.today().isoformat() + ' ' * padding + temperature))

    screen.write_line(1, '07:30 Breakfast')
    screen.write_line(2, '08:00 Work')
    screen.write_line(3, '17:00 Free time') 
    screen.flush()
    time.sleep(60 * 30)

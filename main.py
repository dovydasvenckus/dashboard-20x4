#!/usr/bin/python

import time
from datetime import date
from itertools import islice

from screen import Screen
from temperature import get_temperature

screen = Screen(4, 20)
running = True

seconds_passed = 0
while running:
    temperature = get_temperature() + 'C'
    padding = 20 - len(date.today().isoformat()) - len(temperature)

    screen.write_line(0, (date.today().isoformat() + ' ' * padding + temperature))

    with open("agenda.txt", 'r') as input_file:
        lines = islice(input_file, 3)
        for index, line in enumerate(lines):
            screen.write_line(index + 1, line)

    screen.flush()
    time.sleep(60 * 30)

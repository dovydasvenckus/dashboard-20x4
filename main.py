#!/usr/bin/python

import time
from datetime import date
from itertools import islice

from screen import Screen
from temperature import get_temperature

def get_date_temp_formated():
    current_date = date.today().isoformat()
    temperature = (get_temperature() or '--') + 'C'
    padding = 20 - len(current_date) - len(temperature)
    return (current_date + ' ' * padding + temperature)

screen = Screen(4, 20)
running = True

seconds_passed = 0
while running:
    screen.write_line(0, get_date_temp_formated())

    with open("agenda.txt", 'r') as input_file:
        lines = islice(input_file, 3)
        for index, line in enumerate(lines):
            screen.write_line(index + 1, line)

    screen.flush()
    time.sleep(60 * 10)

#!/usr/bin/python

import time
from datetime import date, datetime
from itertools import islice

from agenda import AgendaItem, get_agenda
from screen import Screen
from temperature import get_temperature

def get_date_temp_formated():
    current_date = date.today().isoformat()
    temperature = (get_temperature() or '--') + 'C'
    padding = 20 - len(current_date) - len(temperature)
    return (current_date + ' ' * padding + temperature)

def filter_upcoming_events(agenda_items):
    future_items = []
    current_time = datetime.today()
    last_item = None

    for item in agenda_items:
        if (item.start_date > current_time):
            future_items.append(item)
        else:
            last_item = item

    if (last_item == None):
        return future_items
    else:
        return [last_item] + future_items

screen = Screen(4, 20)
running = True

seconds_passed = 0
while running:
    future_items = filter_upcoming_events(get_agenda())
    screen.write_line(0, get_date_temp_formated())

    upcoming_events = future_items[:3]
    for index, item in enumerate(future_items):
        screen.write_line(index + 1, item.description)

    screen.flush()
    time.sleep(60 * 10)

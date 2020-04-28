#!/usr/bin/python3

import time
from datetime import date, datetime
from tzlocal import get_localzone
from itertools import islice

from agendaItem import AgendaItem
from gCalendar import get_agenda
from screen import Screen
from temperature import get_temperature

def get_date_temp_formated():
    current_date = date.today().isoformat()
    temperature = (get_temperature() or '--') + 'C'
    padding = 20 - len(current_date) - len(temperature)
    return (current_date + ' ' * padding + temperature)

def filter_upcoming_events(agenda_items):
    future_items = []
    current_time = datetime.today().astimezone(get_localzone())
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

def format_agenda_item(item):
    return '{hour}:{minute} {description}'.format(
            hour = format_time(item.start_date.hour), minute=format_time(item.start_date.minute), description=item.description
            )

def format_time(time_unit):
    if (time_unit < 10):
        return '0{time_unit}'.format(time_unit=time_unit)
    return time_unit

def render_events(screen):
    future_events = filter_upcoming_events(get_agenda())
    upcoming_events = future_events[:3]
    if (not upcoming_events):
        screen.write_line(2, '-No upcoming events-')
        return

    for index, item in enumerate(upcoming_events):
        screen.write_line(index + 1, format_agenda_item(item))

screen = Screen(4, 20)
running = True

seconds_passed = 0
while running:
    screen.write_line(0, get_date_temp_formated())

    render_events(screen)

    screen.flush()
    time.sleep(60 * 10)

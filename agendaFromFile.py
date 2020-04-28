from datetime import datetime
from agendaItem import AgendaItem
from tzlocal import get_localzone

def get_agenda():
    current_date = datetime.today()
    agenda_items = []

    agenda = open('agenda.txt', 'r')
    lines = agenda.readlines()
    for line in lines:
        hour_minute = line[0:5].split(':')
        item_date = current_date.replace(
                hour=int(hour_minute[0]),
                minute=int(hour_minute[1]),
                second=0,
                microsecond=0
                ).astimezone(get_localzone())
        agenda_items.append(AgendaItem(item_date, line[6:]))

    return agenda_items

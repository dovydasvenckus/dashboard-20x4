from datetime import datetime

class AgendaItem:
    start_date = None
    description = ''

    def __init__(self, start_date, description):
        self.start_date = start_date
        self.description = description

def get_agenda():
    current_date = datetime.today()
    agenda_items = []

    agenda = open('agenda.txt', 'r')
    lines = agenda.readlines()
    for line in lines:
        hour_minute = line[0:5].split(':')
        item_date = current_date.replace(hour=int(hour_minute[0]), minute=int(hour_minute[1]), second=0, microsecond=0)
        agenda_items.append(AgendaItem(item_date, line))

    return agenda_items

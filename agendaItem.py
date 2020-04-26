class AgendaItem:
    start_date = None
    description = ''

    def __init__(self, start_date, description):
        self.start_date = start_date
        self.description = description

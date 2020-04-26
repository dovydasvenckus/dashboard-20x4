from __future__ import print_function
from datetime import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from agendaItem import AgendaItem

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def format_date(date):
    return date.isoformat() + 'Z'

def get_agenda():
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    current_date = datetime.today()
    tomorrow = current_date.replace(day=current_date.day + 1, hour=0, minute=0, second=0, microsecond=0)
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    events_result = service.events().list(calendarId='primary', 
                                        timeMin=format_date(today), timeMax=format_date(tomorrow),
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    agenda_items = []

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        agenda_items.append(AgendaItem(datetime.fromisoformat(start), event['summary']))

    return agenda_items


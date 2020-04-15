from lxml import html
import requests

url = 'http://www.meteo.lt/lt/miestas?placeCode=Vilnius'

def get_temperature():
    try:
        page = requests.get(url, timeout=10)
        tree = html.fromstring(page.content)
        temperature=int(tree.xpath('//div[@class="weather_info type_1"]//span[@class="temperature"]/text()')[0])

        if temperature > 0:
            return '+' + str(temperature)
        else:
            return temperature
    except requests.exceptions.ConnectionError:
        return None

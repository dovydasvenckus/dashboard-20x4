from lxml import html
import requests

def get_temperature():
    url = 'http://www.meteo.lt/lt/miestas?placeCode=Vilnius'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    return tree.xpath('//div[@class="weather_info type_1"]//span[@class="temperature"]/text()')[0]

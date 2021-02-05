import json
from urllib import request

from config import API_KEY, LANG


class ClimaService:
    def __init__(self):
        self.URL_BASE = f'http://api.openweathermap.org/data/2.5/weather?lang={LANG}&appid={API_KEY}&units=metric'

    def get_by_city(self, city):
        url = self.URL_BASE + f'&q={city}'
        with request.urlopen(url) as api:
            data = json.loads(api.read().decode())
        return data

    def get_by_code(self, code):
        url = self.URL_BASE + f'&id={code}'
        with request.urlopen(url) as api:
            data = json.loads(api.read().decode())
        return data

    def get_by_coord(self, lat, lon):
        url = self.URL_BASE + f"&lat={lat}&lon={lon}"
        with request.urlopen(url) as api:
            data = json.loads(api.read().decode())
        return data

    def get_by_zipcode(self, zipcode, country='br'):
        url = self.URL_BASE + f"&zip={zipcode},{country}"
        with request.urlopen(url) as api:
            data = json.loads(api.read().decode())
        return data

    def get(self, args):
        if 'city' in args:
            city = args.get('city')
            data = self.get_by_city(city)
        elif 'code' in args:
            code = args.get('code')
            data = self.get_by_code(code)
        elif 'zipcode' in args:
            zipcode = args.get('zipcode')
            data = self.get_by_zipcode(zipcode, 'us')
        elif 'lat' in args and 'lon' in args:
            lat = args['lat']
            lon = args['lon']
            data = self.get_by_coord(lat, lon)
        return data

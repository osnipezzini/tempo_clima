import json
from urllib import request

from flask import current_app

from config import API_KEY, LANG, LITERAL_SPACE
from models import Historico


class ClimaService:
    def __init__(self):
        self.URL_BASE = f'http://api.openweathermap.org/data/2.5/weather?lang={LANG}&appid={API_KEY}&units=metric'
        self.search_type = ''
        self.search_term = ''

    def get_by_city(self, city):
        url = self.URL_BASE + f'&q={city.replace(" ", LITERAL_SPACE)}'
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
            self.search_type = 'city'
            self.search_term = city
            data = self.get_by_city(city)
        elif 'code' in args:
            code = args.get('code')
            self.search_type = 'code'
            self.search_term = code
            data = self.get_by_code(code)
        elif 'zipcode' in args:
            zipcode = args.get('zipcode')
            self.search_type = 'zipcode'
            self.search_term = zipcode
            data = self.get_by_zipcode(zipcode, 'us')
        elif 'lat' in args and 'lon' in args:
            lat = args['lat']
            lon = args['lon']
            self.search_type = 'coord'
            self.search_term = f'{lat};{lon}'
            data = self.get_by_coord(lat, lon)
        return data

    def add_history(self):
        history = Historico()
        history.tipo_busca = self.search_type
        history.termo_busca = self.search_term
        current_app.db.session.add(history)
        current_app.db.session.commit()

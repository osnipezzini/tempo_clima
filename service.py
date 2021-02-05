import json
from urllib import request

from config import API_KEY, LANG


class ClimaService:
    def get_by_city(self, query):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={query}&lang={LANG}&appid={API_KEY}'
        with request.urlopen(url) as api:
            data = json.loads(api.read().decode())
        return data

from datetime import datetime

from database import db


class Clima:
    sensacao_termica = 0.0
    umidade = 0
    pressao = 0.0
    temperatura = 0.0
    temperatura_maxima = 0.0
    temperatura_minima = 0.0
    latitude = 0
    longitude = 0
    cidade = ''
    cod_cidade = 0

    def __init__(self, data=None):
        if data is not None:
            self.sensacao_termica = data['main']['feels_like']
            self.temperatura = data['main']['temp']
            self.temperatura_minima = data['main']['temp_min']
            self.temperatura_maxima = data['main']['temp_max']
            self.cidade = data['name']
            self.pressao = data['main']['pressure']
            self.umidade = data['main']['humidity']
            self.latitude = data['coord']['lat']
            self.longitude = data['coord']['lon']
            self.cod_cidade = data['id']
            self.visibilidade = data['visibility']
            self.velocidade_vento = data['wind']['speed']


class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_pesquisa = db.Column(db.DateTime, default=datetime.now())
    termo_busca = db.Column(db.String, default='')
    tipo_busca = db.Column(db.String, default='city')

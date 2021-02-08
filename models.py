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


class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hora = db.Column(db.Time, default=datetime.now())
    termo_busca = db.Column(db.String, default='')
    tipo_busca = db.Column(db.String, default='city')

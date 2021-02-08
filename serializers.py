from flask_marshmallow import Marshmallow

from models import Clima, Historico

ma = Marshmallow()


def init_marshmallow(app):
    ma.init_app(app)


class ClimaSerializer(ma.Schema):
    class Meta:
        model = Clima
        fields = ['sensacao_termica', 'umidade', 'pressao', 'temperatura', 'temperatura_maxima', 'temperatura_minima',
                  'latitude', 'longitude', 'cidade', 'cod_cidade']


class HistoricoSerializer(ma.Schema):
    class Meta:
        model = Historico
        fields = ['hora', 'termo_busca', 'tipo_busca']

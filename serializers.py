from flask_marshmallow import Marshmallow, fields

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
    data_pesquisa = fields.fields.DateTime(format='%d/%m/%y %H:%M:%S')

    class Meta:
        model = Historico
        fields = ['data_pesquisa', 'termo_busca', 'tipo_busca']

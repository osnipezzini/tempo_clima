from flask_marshmallow import Marshmallow

from models import Clima

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class ClimaSerializer(ma.Schema):
    class Meta:
        model = Clima
        fields = ['sensacao_termica', 'umidade', 'pressao', 'temperatura', 'temperatura_maxima', 'temperatura_minima',
                  'latitude', 'longitude', 'cidade', 'cod_cidade']

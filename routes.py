from urllib.error import HTTPError

from flask import request, Blueprint

from models import Clima, Historico
from serializers import ClimaSerializer, HistoricoSerializer
from service import ClimaService
from utils import generate_response

api = Blueprint('api', __name__)


@api.route("/buscar", methods=["GET"])
def buscar_clima():
    service = ClimaService()
    args = request.args
    try:
        data = service.get(args)
        serializer = ClimaSerializer()
        model = Clima()
        model.sensacao_termica = data['main']['feels_like']
        model.temperatura = data['main']['temp']
        model.temperatura_minima = data['main']['temp_min']
        model.temperatura_maxima = data['main']['temp_max']
        model.cidade = data['name']
        model.pressao = data['main']['pressure']
        model.umidade = data['main']['humidity']
        model.latitude = data['coord']['lat']
        model.longitude = data['coord']['lon']
        model.cod_cidade = data['id']
        model.visibilidade = data['visibility']
        model.velocidade_vento = data['wind']['speed']
        retorno = serializer.dump(model)
        service.add_history()
        return generate_response(200, '', 'tempo', retorno)
    except HTTPError as he:
        return generate_response(200, 'Dados não encontrados com o termo digitado')


@api.route("/historico", methods=["GET"])
def historico_busca():
    args = request.args
    if 'city' in args:
        historicos = Historico.query.filter(tipo_busca='city').all()
    elif 'code' in args:
        historicos = Historico.query.filter(tipo_busca='code').all()
    elif 'zipcode' in args:
        historicos = Historico.query.filter(tipo_busca='zipcode').all()
    elif 'coord' in args:
        historicos = Historico.query.filter(tipo_busca='coord').all()
    else:
        historicos = Historico.query.all()

    serializer = HistoricoSerializer(many=True)
    retorno = serializer.dump(historicos)
    return generate_response(200, '', 'historicos', retorno)

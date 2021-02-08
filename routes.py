from urllib.error import HTTPError

from flask import request, Blueprint, render_template

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
        model = Clima(data)
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


@api.route("/historypage", methods=['GET'])
def history():
    historicos = Historico.query.all()
    serializer = HistoricoSerializer(many=True)
    data = serializer.dump(historicos)
    return render_template('history.html', history=data)


@api.route("/", methods=['GET', 'POST'])
def home():
    if request.method.lower() == 'post':
        service = ClimaService()
        serializer = ClimaSerializer()
        typ = request.form.get("search_type")
        if typ == 'coord':
            lat = request.form.get("lat")
            lon = request.form.get("lon")
            data = service.get_by_coord(lat, lon)
        elif typ == 'code':
            code = request.form.get("text")
            data = service.get_by_code(code)
        elif typ == 'zipcode':
            zipcode = request.form.get("text")
            data = service.get_by_zipcode(zipcode)
        else:
            city = request.form.get("text")
            data = service.get_by_city(city)
        if data is not None:
            clima = Clima(data)
            retorno = serializer.dump(clima)
            return render_template('resultado.html', **retorno)
    return render_template('home.html')

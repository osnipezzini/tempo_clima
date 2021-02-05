from urllib.error import HTTPError

from flask import request, Blueprint

from service import ClimaService
from utils import generate_response

api = Blueprint('api', __name__)


@api.route("/buscar", methods=["GET"])
def buscar_clima():
    service = ClimaService()
    args = request.args
    try:
        data = service.get(args)
        return generate_response(200, '', 'tempo', data)
    except HTTPError as he:
        return generate_response(200, 'Dados não encontrados com o termo digitado')


@api.route("/historico", methods=["GET"])
def historico_busca():
    return generate_response(200, '')

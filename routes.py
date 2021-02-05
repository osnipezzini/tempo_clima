from urllib.error import HTTPError

from flask import request, Flask

from service import ClimaService
from utils import generate_response

app = Flask("ClimaTempo", )


@app.route("/buscar", methods=["GET"])
def ola_mundo():
    service = ClimaService()
    args = request.args
    try:
        data = service.get(args)
        return generate_response(200, '', 'tempo', data)
    except HTTPError as he:
        return generate_response(200, 'Dados não encontrados com o termo digitado')

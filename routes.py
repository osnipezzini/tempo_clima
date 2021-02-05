from flask import request, Flask

from service import ClimaService
from utils import generate_response

app = Flask("ClimaTempo",)


@app.route("/buscar", methods=["GET"])
def ola_mundo():
    service = ClimaService()

    if 'city' in request.args:
        data = service.get_by_city(request.args.get('city'))
        return generate_response(200, '', 'tempo', data)

    return generate_response(200, "Ola mundo")

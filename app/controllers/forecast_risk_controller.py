from http import HTTPStatus

from flask import request

from app.decorators.forecast_risk_decorator import request_validator
from app.models import RiskModel
from app.services.forecast_risk_services import get_endangered_cities


@request_validator
def fetch_forecast_risk():

    data = request.get_json()

    endangered_cities = get_endangered_cities(data, RiskModel.PRECIPITATION_LIMIT)

    # TODO add the logic to send an message to the desired users.

    return {"endangered_cities": endangered_cities}, HTTPStatus.OK

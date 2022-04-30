from http import HTTPStatus

from flask import request

from app.exceptions.generic_exc import (
    InvalidKeysError,
    InvalidTypeError,
    MissingKeysError,
)
from app.models import RiskModel
from app.services.forecast_risk_services import get_endangered_cities, request_validator


def fetch_forecast_risk():

    data = request.get_json()

    try:
        request_validator(data)
    except InvalidTypeError as error:
        return error.message, error.status_code
    except MissingKeysError as error:
        return error.message, error.status_code
    except InvalidKeysError as error:
        return error.message, error.status_code

    endangered_cities = get_endangered_cities(data, RiskModel.PRECIPITATION_LIMIT)

    return {"endangered_cities": endangered_cities}, HTTPStatus.OK

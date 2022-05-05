from flask import request

from app.exceptions.generic_exc import (
    InvalidKeysError,
    InvalidTypeError,
    MissingKeysError,
)
from app.services import forecast_risk_services


def request_validator(function):
    def wrapper(*args, **kwargs):

        data = request.get_json()

        try:
            forecast_risk_services.request_validator(data)
        except InvalidTypeError as error:
            return error.message, error.status_code
        except MissingKeysError as error:
            return error.message, error.status_code
        except InvalidKeysError as error:
            return error.message, error.status_code

        return function(*args, **kwargs)

    return wrapper

from http import HTTPStatus

from flask import request
from flask_jwt_extended import jwt_required

from app.exceptions.generic_exc import (
    InvalidKeysError,
    InvalidTypeError,
    MissingKeysError,
    NotFoundError,
)
from app.models.risk_model import RiskModel
from app.services.generic_services import get_user_from_token
from app.services.user_risk_profile_services import (
    select_risk_case,
    validate_keys_and_values,
)


@jwt_required()
def create_user_risk_profile():
    try:
        allowed_keys = list(RiskModel.VALIDATOR.keys())
        data = request.get_json()
        validate_keys_and_values(data, allowed_keys)
        user = get_user_from_token()
        select_risk_case(data, user)
    except MissingKeysError as e:
        return e.message, e.status_code
    except InvalidKeysError as e:
        return e.message, e.status_code
    except InvalidTypeError as e:
        return e.message, e.status_code
    except NotFoundError as e:
        return e.message, e.status_code

    serialized_user = {
        "name": user.name,
        "phone": user.phone,
        "email": user.email,
        "risks": user.risks,
    }

    return serialized_user, HTTPStatus.CREATED

from http import HTTPStatus

from flask import jsonify, request, session
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Session

from app.configs.database import db
from app.exceptions.generic_exc import InvalidKeysError
from app.models.risk_model import RiskModel


@jwt_required()
def create():
    expected_keys = ["title", "description", "text"]

    data = request.get_json()

    invalid_keys = []

    session: Session = db.session

    try:
        for key, _ in data.items():
            if key not in expected_keys:
                invalid_keys.append(key)

        if invalid_keys:
            raise InvalidKeysError(
                expected_keys,
                invalid_keys,
            )

        new_risk = RiskModel(**data)

    except InvalidKeysError as e:
        return e.message, e.status_code

    session.add(new_risk)
    session.commit()

    return jsonify(new_risk), HTTPStatus.CREATED


def retrieve():
    ...

from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.exceptions.generic_exc import (
    InvalidKeysError,
    InvalidTypeError,
    MissingKeysError,
)
from app.models import RiskModel, UserModel


def validate_missing_keys(data: dict, allowed_keys: list):
    missing_keys = [key for key in allowed_keys if key not in data.keys()]

    if missing_keys:
        raise MissingKeysError(allowed_keys, missing_keys)


def validate_invalid_keys(data: dict, allowed_keys: list):
    invalid_keys = [key for key in data.keys() if key not in allowed_keys]

    if invalid_keys:
        raise InvalidKeysError(allowed_keys, invalid_keys)


def validate_wrong_keys(data: dict, allowed_keys: list):
    correct_types = {key: bool.__name__ for key in allowed_keys}
    wrong_types = {}

    for key, value in data.items():
        if not isinstance(value, bool):
            wrong_types[key] = type(value).__name__

    if wrong_types:
        raise InvalidTypeError(correct_types, wrong_types)


def validate_keys_and_values(data: dict, allowed_keys: list):
    validate_missing_keys(data, allowed_keys)
    validate_invalid_keys(data, allowed_keys)
    validate_wrong_keys(data, allowed_keys)


def select_risk_case(data: dict, user: UserModel):
    session: Session = db.session
    selected_case = ""

    for case_key, case_value in RiskModel.CASES.items():
        case_validator = 0
        for key, value in data.items():
            if value == case_value[key]:
                case_validator += 1
            if case_validator == 2:
                selected_case = case_key

    message = RiskModel.VALUES[selected_case]
    risk_query: Query = session.query(RiskModel)

    risk: RiskModel = risk_query.filter_by(title=selected_case).first()

    if not risk:

        risk_data = {"title": selected_case, "text": message}
        risk = RiskModel(**risk_data)

    if user.risks:
        user.risks = []

    risk.users.append(user)
    session.add(risk)
    session.commit()

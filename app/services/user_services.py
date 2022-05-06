from copy import deepcopy

from sqlalchemy.orm import Session

from app.configs.database import db
from app.exceptions.generic_exc import (
    InvalidCredentialsError,
    InvalidKeysError,
    InvalidTypeError,
    MissingKeysError,
    UniqueKeyError,
)
from app.models.user_model import UserModel


def validate_keys_and_values(
    data: dict,
    user: UserModel = {},
    update: bool = False,
    signin: bool = False,
    signup: bool = False,
):

    validator = UserModel.VALIDATOR

    if update:
        validate_keys_and_values_update(data, user, validator)
    elif signup:
        validate_keys_and_values_signup(data, validator)
    elif signin:
        validate_keys_and_values_signin(data, validator)


def validate_keys_and_values_update(data: dict, user: UserModel, validator: dict):

    if data.get("password", None):
        validator = deepcopy(validator)
        validator.update({"old_password": {"type": str}})

    validator_keys = list(validator.keys())

    validate_invalid_keys(data, validator_keys)
    validate_invalid_types(data, validator)
    validate_for_unique(data, validator, user)
    check_for_password(data, user)


def validate_keys_and_values_signup(data: dict, validator: dict):

    validator_keys = list(validator.keys())

    validate_missing_keys(data, validator_keys)
    validate_invalid_keys(data, validator_keys)
    validate_invalid_types(data, validator)
    validate_for_unique(data, validator)


def validate_keys_and_values_signin(data: dict, validator: dict):

    signin_keys = ["email", "password"]
    validator = deepcopy(validator)
    validator = {key: value for key, value in validator.items() if key in signin_keys}

    validator_keys = list(validator.keys())

    validate_missing_keys(data, validator_keys)
    validate_invalid_keys(data, validator_keys)
    validate_invalid_types(data, validator)


def validate_and_setattr(data: dict, user: UserModel, allowed_keys: list):
    invalid_keys = []

    for key, value in data.items():
        if key in allowed_keys:
            setattr(user, key, value)
        else:
            invalid_keys.append(key)

    if invalid_keys:
        raise InvalidKeysError(allowed_keys, invalid_keys)


def validate_invalid_types(data: dict, validator: dict):

    correct_types = {
        key: value.get("type").__name__ for key, value in validator.items()
    }
    wrong_types = {}

    for key, value in data.items():
        if not isinstance(value, str):
            wrong_types[key] = type(value).__name__

    if wrong_types:
        raise InvalidTypeError(correct_types, wrong_types)


def validate_for_unique(data: dict, validator: dict, user: UserModel = {}):

    unique_keys = [
        key for key, value in validator.items() if value.get("unique") == True
    ]

    for key, value in data.items():
        if key in unique_keys:
            session: Session = db.session
            found_user = session.query(UserModel).filter_by(**{key: value}).first()

            if found_user and user is not found_user:
                raise UniqueKeyError(key=key)


def validate_missing_keys(data: dict, validator_keys: list):

    expected_keys = validator_keys

    missing_keys = [key for key in expected_keys if key not in data.keys()]

    if missing_keys:
        raise MissingKeysError(expected_keys, missing_keys)


def validate_invalid_keys(data: dict, validator_keys: list):

    expected_keys = validator_keys

    invalid_keys = [key for key in data.keys() if key not in expected_keys]

    if invalid_keys:
        raise InvalidKeysError(expected_keys, invalid_keys)


def check_for_password(data: dict, user: UserModel):

    password = data.get("password", None)

    if password:

        old_password = data.get("old_password", None)

        if not old_password:
            message = {
                "error": "missing old password value",
                "message": "to update the password, an old_password key is required",
            }
            raise MissingKeysError(message=message)

        is_password_correct = user.verify_password(old_password)

        if not is_password_correct:
            message = {
                "error": "invalid credentials error",
                "message": "old_password did not match",
            }
            raise InvalidCredentialsError(message=message)

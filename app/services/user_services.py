from app.exceptions.generic_exc import InvalidKeysError, InvalidTypeError
from app.models.user_model import UserModel


def validate_and_setattr(data: dict, user: UserModel, allowed_keys: list):
    invalid_keys = []

    for key, value in data.items():
        if key in allowed_keys:
            setattr(user, key, value)
        else:
            invalid_keys.append(key)

    if invalid_keys:
        raise InvalidKeysError(allowed_keys, invalid_keys)


def validate_type(data: dict, allowed_keys: list):
    correct_types = {key: str.__name__ for key in allowed_keys}
    wrong_types = {}

    for key, value in data.items():
        if not isinstance(value, str):
            wrong_types[key] = type(value).__name__

    if wrong_types:
        raise InvalidTypeError(correct_types, wrong_types)


def validate_keys_and_values(data: dict, user: UserModel, allowed_keys: list):
    validate_and_setattr(data, user, allowed_keys)
    validate_type(data, allowed_keys)

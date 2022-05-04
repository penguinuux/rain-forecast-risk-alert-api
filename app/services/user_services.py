from app.exceptions.generic_exc import InvalidKeysError, InvalidTypeError
from app.models.user_model import UserModel


def validate_and_setattr(data: dict, user: UserModel):
    authorized_keys = ["email", "phone", "name", "password"]
    invalid_keys = []

    for key, value in data.items():
        if key in authorized_keys:
            setattr(user, key, value)
        else:
            invalid_keys.append(key)

    if invalid_keys:
        raise InvalidKeysError(authorized_keys, invalid_keys)


def validate_type(data: dict):
    authorized_keys = ["email", "phone", "name", "password"]
    correct_types = {key: str.__name__ for key in authorized_keys}
    wrong_types = {}

    for key, value in data.items():
        if not isinstance(value, str):
            wrong_types[key] = type(value).__name__

    if wrong_types:
        raise InvalidTypeError(correct_types, wrong_types)

from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.exceptions.generic_exc import (
    InvalidKeysError,
    InvalidTypeError,
    MissingKeysError,
)
from app.models.address_model import AddressModel
from app.models.city_model import CityModel
from app.models.state_model import StateModel
from app.models.user_model import UserModel


def get_cities_in_risk(data: dict, precipitation_limit: int):

    risk_situation = [
        forecast
        for forecast in data
        if forecast["precipitation"] >= precipitation_limit
    ]

    return risk_situation


def get_endangered_cities(data: dict, precipitation_limit: int):

    risk_situation = get_cities_in_risk(data, precipitation_limit)

    session: Session = db.session

    endangered_cities = []

    for forecast in risk_situation:
        state_name = forecast.get("state")
        city_name = forecast.get("city")

        users = (
            session.query(UserModel)
            .join(AddressModel)
            .join(CityModel)
            .join(StateModel)
            .filter(StateModel.name == state_name)
            .filter(CityModel.name == city_name)
            .all()
        )

        if users:
            city_info = {
                # TODO check the normalization method that will be added in the database
                # and change it in here
                "city": city_name.title(),
                "state": state_name.title(),
                "users_warned": len(users),
            }

            endangered_cities.append(city_info)

    return endangered_cities


def request_validator(data: list):

    EXPECTED_KEYS_AND_TYPES = {
        "city": [str],
        "state": [str],
        "precipitation": [int, float],
    }

    expected_keys = list(EXPECTED_KEYS_AND_TYPES.keys())

    check_for_request_type(data, list)
    check_for_missing_keys(data, expected_keys)
    check_for_invalid_keys(data, expected_keys)
    check_for_request_inner_types(data, EXPECTED_KEYS_AND_TYPES)


def check_for_request_type(data: list, type):
    """
    This function checks for the main type of the ``data`` request, and compares it to the expected
    ``type``, and if the typing is different, it raises an error specifying the expected and received
    types
    """

    if type(data) is not type:
        expected_type = type.__name__
        received_type = type(data).__name__
        raise InvalidTypeError(expected_type, received_type)


def check_for_missing_keys(data: list, expected_keys: list):
    """
    This function checks for each received keys in the ``data`` and compare with an
    ``expected_keys`` list, if there is any missing key in the data, it raises an error
    with a list of the missing keys
    """

    missing_keys_list = []

    for request in data:
        missing_keys = [key for key in expected_keys if key not in request.keys()]

        if missing_keys:
            request_missing_keys = {"request": request, "missing_keys": missing_keys}
            missing_keys_list.append(request_missing_keys)

    if missing_keys_list:
        raise MissingKeysError(expected_keys, missing_keys_list)


def check_for_invalid_keys(data: list, expected_keys: list):
    """
    This function checks for each received keys in the ``data`` and compare with an
    ``expected_keys`` list, if there is any invalid key in the data, it raises an error
    with a list of the invalid keys
    """

    invalid_keys_list = []

    for request in data:
        invalid_keys = [key for key in request.keys() if key not in expected_keys]

        if invalid_keys:
            request_invalid_keys = {"request": request, "invalid_keys": invalid_keys}
            invalid_keys_list.append(request_invalid_keys)

    if invalid_keys_list:
        raise InvalidKeysError(expected_keys, invalid_keys_list)


def check_for_request_inner_types(data: list, expected_keys_types: dict):
    """
    This function checks for the types of each request in a ``data`` list and compare to the
    ``expected_keys_and_types``, if anything is incorrect, it raises an exception with a list
    of the requests and the invalid types in each request.
    """
    expected_types_message = {
        key: get_correct_type_message(types)
        for key, types in expected_keys_types.items()
    }

    invalid_types_list = []

    for request in data:
        invalid_types = {}

        for key, value in request.items():
            value_type = type(value)

            if value_type not in expected_keys_types[key]:
                invalid_types[key] = value_type.__name__

        if invalid_types:
            request_invalid_types = {"request": request, "invalid_types": invalid_types}
            invalid_types_list.append(request_invalid_types)

    if invalid_types_list:
        raise InvalidTypeError(expected_types_message, invalid_types_list)


def get_correct_type_message(types: list) -> str:
    """
    This function checks a list of ``types``, normalize its values from type values to string
    values, it also checks the length of the list to define a proper message to be displayed.
    """

    normalize_types = [value.__name__ for value in types]

    message = " or ".join(normalize_types)
    if len(normalize_types) > 2:
        message = f"{', '.join(normalize_types[0:-1])} or {normalize_types[-1]}"

    return message

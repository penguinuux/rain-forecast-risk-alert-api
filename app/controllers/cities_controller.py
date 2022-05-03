from http import HTTPStatus

from app.exceptions.state_exc import StateNotFoundError
from app.services.cities_services import get_cities, get_city


def cities():

    cities = get_cities()

    return cities


def city(state):

    try:

        city = get_city(state)

    except StateNotFoundError as err:
        return err.message, HTTPStatus.NOT_FOUND

    return city

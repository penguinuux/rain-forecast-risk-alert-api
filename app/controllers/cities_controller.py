from http import HTTPStatus

from flask import jsonify

from app.exceptions.generic_exc import ObjNotFoundError
from app.services.cities_services import get_cities_from_state, get_states_and_cities


def all_states_and_cities():

    states_and_cities = get_states_and_cities()

    return jsonify(states_and_cities), HTTPStatus.OK


def all_cities_from_state(state):

    try:

        cities_from_state = get_cities_from_state(state) 

    except ObjNotFoundError as err:
        return err.message, err.status_code

    return jsonify(cities_from_state), HTTPStatus.OK

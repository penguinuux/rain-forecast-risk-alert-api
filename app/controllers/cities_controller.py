from http import HTTPStatus

from flask import jsonify

from app.exceptions.state_exc import StateNotFoundError
from app.services.cities_services import (get_cities_from_state,
                                          get_states_and_cities)


def all_states_and_cities():

    states_and_cities = get_states_and_cities()

    return jsonify(states_and_cities), HTTPStatus.OK


def all_cities_from_state(state):

    try:

        cities_from_state = get_cities_from_state(state)

    except StateNotFoundError as err:
        return err.message, HTTPStatus.NOT_FOUND

    return jsonify(cities_from_state), HTTPStatus.OK

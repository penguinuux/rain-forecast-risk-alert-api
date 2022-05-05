from http import HTTPStatus

from flask import jsonify, request

from app.exceptions.city_exc import CityNotFoundError
from app.exceptions.state_exc import StateNotFoundError
from app.services.cities_services import (
    get_cities_from_state,
    get_city,
    get_states_and_cities,
)


def all_states_and_cities():

    try:

        city = request.args.get("city")
        state = request.args.get("state")

        if state:
            cities_from_state = get_cities_from_state(state)
            return jsonify(cities_from_state), HTTPStatus.OK

        if city:

            selected_city = get_city(city)
            return jsonify(selected_city), HTTPStatus.OK
            ...

        states_and_cities = get_states_and_cities()

        return jsonify(states_and_cities), HTTPStatus.OK

    except StateNotFoundError as err:
        return err.message, HTTPStatus.NOT_FOUND
    except CityNotFoundError as err:
        return err.message, HTTPStatus.NOT_FOUND


def all_cities_from_state(state):

    try:

        cities_from_state = get_cities_from_state(state)

    except StateNotFoundError as err:
        return err.message, HTTPStatus.NOT_FOUND

    return jsonify(cities_from_state), HTTPStatus.OK

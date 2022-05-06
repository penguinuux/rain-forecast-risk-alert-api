from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.exceptions.state_exc import StateNotFoundError
from app.models.state_model import StateModel
from app.utils.name_char_normalizer import name_char_normalizer


def get_states_and_cities():
    session: Session = db.session

    base_query: Query = session.query(StateModel).order_by(StateModel.name)

    states = base_query.all()

    serializer = [
        {"state": state.name, "cities": sorted([city.name for city in state.cities])}
        for state in states
        if len(state.cities) > 0
    ]

    return serializer


def get_cities_from_state(name):

    session: Session = db.session

    base_query: Query = session.query(StateModel)

    states = base_query.all()

    state_and_cities = [
        {
            "state": state.name,
            "cities": sorted([cities.name for cities in state.cities]),
        }
        for state in states
        if name_char_normalizer(state.name) == name_char_normalizer(name)
        or name_char_normalizer(state.uf) == name_char_normalizer(name)
    ]

    if not state_and_cities:
        raise StateNotFoundError

    return state_and_cities

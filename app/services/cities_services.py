from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.exceptions.state_exc import StateNotFoundError
from app.models.state_model import StateModel
from app.utils.name_char_normalizer import name_char_normalizer


def get_states_and_cities():
    session: Session = db.session

    base_query: Query = session.query(StateModel)

    states = base_query.all()

    serializer = [{"state": state.name, "cities": state.cities} for state in states]

    return serializer


def get_cities_from_state(state):

    session: Session = db.session

    base_query: Query = session.query(StateModel)

    states = base_query.all()

    city_state = [
        {
            "name": estate.name,
            "cities": sorted([cities.name for cities in estate.cities]),
        }
        for estate in states
        if name_char_normalizer(estate.name) == name_char_normalizer(state)
        or name_char_normalizer(estate.uf) == name_char_normalizer(state)
    ]

    if not city_state:
        raise StateNotFoundError

    return city_state

from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.exceptions.state_exc import StateNotFoundError
from app.models.state_model import StateModel


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


def get_cities_from_state(state):

    session: Session = db.session

    base_query: Query = session.query(StateModel)

    state = base_query.filter_by(name=state).first()

    if not state:
        raise StateNotFoundError

    cities_from_state = {
        "state": state.name,
        "cities": [city.name for city in state.cities],
    }

    return cities_from_state

from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.exceptions.generic_exc import NotFoundError
from app.models.state_model import StateModel


def get_states_and_cities():
    session: Session = db.session

    base_query: Query = session.query(StateModel)

    states = base_query.all()

    serializer = [{"state": state.name, "cities": state.cities} for state in states]

    return serializer


def get_cities_from_state(state):

    session: Session = db.session

    base_query: Query = session.query(StateModel)

    state_from_table = base_query.filter_by(name=state).first()

    if not state_from_table:
        raise NotFoundError(request=state)

    cities_from_state = {
        "state": state_from_table.name,
        "cities": state_from_table.cities,
    }

    return cities_from_state

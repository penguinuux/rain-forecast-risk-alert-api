from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.exceptions.city_exc import CityNotFoundError
from app.exceptions.state_exc import StateNotFoundError
from app.models.city_model import CityModel
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

    state = base_query.filter_by(name=state).first()

    if not state:
        raise StateNotFoundError

    cities_from_state = {"state": state.name, "cities": state.cities}

    return cities_from_state


def get_city(city):
    session: Session = db.session
    base_query: Query = session.query(CityModel)

    selected_city = base_query.filter_by(name=city).first()

    if not selected_city:
        raise CityNotFoundError

    return selected_city

from http import HTTPStatus

from flask import jsonify
from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.exceptions.state_exc import StateNotFoundError
from app.models.state_model import StateModel


def get_cities():
    session: Session = db.session

    base_query: Query = session.query(StateModel)

    states = base_query.all()

    serializer = [{"state": state.name, "cities": state.cities} for state in states]

    return jsonify(serializer), HTTPStatus.OK


def get_city(state):

    session: Session = db.session

    base_query: Query = session.query(StateModel)

    state = base_query.filter_by(name=state).first()

    if not state:
        raise StateNotFoundError

    city = {"state": state.name, "cities": state.cities}

    return jsonify(city), HTTPStatus.OK

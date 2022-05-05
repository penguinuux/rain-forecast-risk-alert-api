from http import HTTPStatus

from flask import jsonify
from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.models.address_model import AddressModel
from app.models.city_model import CityModel
from app.models.message_model import MessageModel
from app.models.state_model import StateModel
from app.models.user_model import UserModel

session: Session = db.session


def query_by_date(date):

    date_query: Query = session.query(MessageModel).filter_by(date=date).first()
    return jsonify(date_query), HTTPStatus.OK


def query_by_city(city):

    if city:
        city_query = (
            session.query(UserModel)
            .join(AddressModel)
            .join(CityModel)
            .filter(CityModel.name == city)
            .all()
        )
        return (
            {
                "city": city,
                "message": [
                    {"user": user.name, "user messages": user.messages}
                    for user in city_query
                ],
            },
            HTTPStatus.OK,
        )


def query_by_state(state):
    if state:
        state_query = (
            session.query(UserModel)
            .join(AddressModel)
            .join(CityModel)
            .join(StateModel)
            .filter(StateModel.name == state)
            .all()
        )

        return (
            {
                "state": state,
                "message": [
                    {"user": user.name, "user messages": user.messages}
                    for user in state_query
                ],
            },
            HTTPStatus.OK,
        )

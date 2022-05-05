from http import HTTPStatus

from flask import jsonify, request
from requests import Session
from sqlalchemy.orm import Session

from app.configs.database import db
from app.models.message_model import MessageModel
from app.services.messages_services import query_by_city, query_by_date, query_by_state


def retrieve():

    data = request.args

    date = data.get("date", default=None)
    city = data.get("city", default=None)
    state = data.get("state", default=None)

    if date:
        return query_by_date(date)

    if city:
        return query_by_city(city)

    if state:
        return query_by_state(state)

    session: Session = db.session
    messages = session.query(MessageModel).all()

    return (
        jsonify(messages),
        HTTPStatus.OK,
    )

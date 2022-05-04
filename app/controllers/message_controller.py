from http import HTTPStatus

from flask import jsonify, request
from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.models.message_model import MessageModel


def retrieve():

    data = request.args

    date = data.get("date", default=None)
    city = data.get("city", default=None)
    state = data.get("state", default=None)

    session: Session = db.session

    if date:
        date_query: Query = session.query(MessageModel).filter_by(date=date).first()
        return jsonify(date_query), HTTPStatus.OK
    # if city:
    #     city_query: Query = session.query(MessageModel).filter_by(city = city).first()
    #     return jsonify(city_query),HTTPStatus.OK
    # if state:
    #     state_query: Query = session.query(MessageModel).filter_by(state = state).first()
    #     return jsonify(state_query),HTTPStatus.OK

    base_query: Query = session.query(MessageModel)

    messages = base_query.all()

    return (
        jsonify(
            [
                {
                    "message id": message.id,
                    "title": message.title,
                    "text": message.text,
                    "date": message.date,
                    "related users": message.users,
                }
                for message in messages
            ]
        ),
        HTTPStatus.OK,
    )

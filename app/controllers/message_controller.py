from http import HTTPStatus

from flask import jsonify
from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.models.message_model import MessageModel


def retrieve():

    session: Session = db.session

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

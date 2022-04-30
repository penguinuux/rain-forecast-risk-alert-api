from http import HTTPStatus

from app.configs.database import db
from app.models.user_model import UserModel
from flask import jsonify
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session


def signup():
    ...
def signin():
    ...
#daqui pra baixo tem q ser autenticado
def retrieve():

    session: Session = db.session
    
    base_query: Query = session.query(UserModel)

    users = base_query.all()

    return jsonify([{
        "name": user.name,
        "email":user.email,
        "phone":user.phone,
        "address":user.address.cep,
        "city":user.address.cities.name,
        "state":user.address.cities.state.name

    } for user in users]), HTTPStatus.OK


def delete():
    ...
def patch():
    ...
from http import HTTPStatus

from app.configs.database import db
from app.models.address_model import AddressModel
from app.models.city_model import CityModel
from app.models.user_model import UserModel
from flask import jsonify, request
from sqlalchemy.orm import Session
from werkzeug.exceptions import NotFound


def signup():
    session: Session = db.session
    data = request.get_json()

    city = data.pop("city")
    cep = data.pop("cep")

    try:

        city_query = session.query(CityModel).filter_by(name=city).first_or_404()
        cep_query = session.query(AddressModel).filter_by(cep=cep).first()

        new_user = UserModel(**data)

        if cep_query:
            new_user.address = cep_query
        else:
            new_cep = AddressModel(cep=cep)
            new_cep.city = city_query
            new_user.address = new_cep

        session.commit()
    except NotFound:
        cities = session.query(CityModel).all()

        return {
            "error": "city out of range",
            "expected": [city.name for city in cities],
            "received": city,
        }, HTTPStatus.BAD_REQUEST

    return (
        jsonify(
            {
                "name": new_user.name,
                "email": new_user.email,
                "phone": new_user.phone,
                "address": new_user.address.cep,
                "city": city_query.name,
                "state": city_query.state.name,
            }
        ),
        HTTPStatus.CREATED,
    )


def signin():
    ...


# authenticated
def retrieve():
    ...


def delete():
    ...


def patch():
    ...

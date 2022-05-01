from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from sqlalchemy.orm import Query, Session

from app.configs.database import db
from app.exceptions.city_exc import CityNotFoundError
from app.models.address_model import AddressModel
from app.models.city_model import CityModel
from app.models.user_model import UserModel


def signup():
    session: Session = db.session
    data = request.get_json()

    city = data.pop("city")
    cep = data.pop("cep")

    try:

        city_query = session.query(CityModel).filter_by(name=city).first()
        cep_query = session.query(AddressModel).filter_by(cep=cep).first()

        if not city_query:
            raise CityNotFoundError

        new_user = UserModel(**data)

        if cep_query:
            new_user.address = cep_query
        else:
            new_cep = AddressModel(cep=cep)
            new_cep.city = city_query
            new_user.address = new_cep

        session.commit()
    except CityNotFoundError:
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
    data = request.get_json()

    user: UserModel = UserModel.query.filter_by(email=data["email"]).first()

    if not user:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND

    if user.verify_password(data["password"]):
        token = create_access_token(user)
        return {"token": token}, HTTPStatus.OK

    else:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def retrieve():

    session: Session = db.session

    base_query: Query = session.query(UserModel)

    users = base_query.all()

    return (
        jsonify(
            [
                {
                    "name": user.name,
                    "email": user.email,
                    "phone": user.phone,
                    "address": user.address.cep,
                    "city": user.address.cities.name,
                    "state": user.address.cities.state.name,
                }
                for user in users
            ]
        ),
        HTTPStatus.OK,
    )


@jwt_required()
def delete():
    ...


@jwt_required()
def patch():
    ...

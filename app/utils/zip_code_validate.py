import requests
from app.models.city_model import CityModel
from app.exceptions.city_exc import (
    CityNotFoundError,
    ZipCodeNotFoundError,
    CityOutOfRangeError,
)
from sqlalchemy.orm import Session
from app.configs.database import db
import json


async def validate_zip_code(zip_code: str):
    """This function validates the received zip code from the request.

    Args:
        zip_code (str): location zip code

    Raises:
        ZipCodeNotFoundError: raises this exception if the zip code are invalid
        CityOutOfRangeError: raises this exception when the city is out of range of the application

    Returns:
        city_query: CityModel instance
    """

    session: Session = db.session

    response = requests.get("https://viacep.com.br/ws/{s}/json/".format(zip_code))
    zip_dict = json.load(response)

    error = zip_dict.get("erro")
    city = zip_dict.get("localidade")
    uf = zip_dict.get("uf")

    if error:
        raise ZipCodeNotFoundError

    city_query = session.query(CityModel).filter_by(name=city).first()

    if not city_query:
        cities = session.query(CityModel).all()
        cities_formated = [{"city": city.name, "uf": city.state.uf} for city in cities]

        raise CityNotFoundError(expected_type=cities_formated, received_type=city)

    if city_query.state.uf != uf:
        raise CityOutOfRangeError(expected_type=cities_formated, received_type=city)

    return city_query

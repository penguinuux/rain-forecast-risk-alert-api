import json

from aiohttp import ClientSession
from sqlalchemy.orm import Session

from app.configs.database import db
from app.exceptions.city_exc import (
    CityOutOfRangeError,
    InvalidZipCodeFormatError,
    ZipCodeNotFoundError,
)
from app.models.city_model import CityModel


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

    async with ClientSession() as client_session:
        async with client_session.get(
            f"https://viacep.com.br/ws/{zip_code}/json/"
        ) as response:
            response = await response.read()

    try:
        zip_dict = json.loads(response.decode("utf-8"))
    except json.JSONDecodeError:
        raise InvalidZipCodeFormatError(zip_code)

    error = zip_dict.get("erro")
    city = zip_dict.get("localidade")
    uf = zip_dict.get("uf")

    if error:
        raise ZipCodeNotFoundError

    city_query = session.query(CityModel).filter_by(name=city).first()

    if not city_query:
        cities = session.query(CityModel).all()
        cities_formatted = [{"city": city.name, "uf": city.state.uf} for city in cities]

        raise CityOutOfRangeError(cities_coverage=cities_formatted, received_city=city)

    if city_query.state.uf != uf:
        raise CityOutOfRangeError(cities_coverage=cities_formatted, received_city=city)

    return city_query

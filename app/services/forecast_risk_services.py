from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.address_model import AddressModel
from app.models.city_model import CityModel
from app.models.state_model import StateModel
from app.models.user_model import UserModel


def get_cities_in_risk(data: dict, precipitation_limit: int):

    risk_situation = [
        forecast
        for forecast in data
        if forecast["precipitation"] >= precipitation_limit
    ]

    return risk_situation


def get_endangered_cities(data: dict, precipitation_limit: int):

    risk_situation = get_cities_in_risk(data, precipitation_limit)

    session: Session = db.session

    endangered_cities = []

    for forecast in risk_situation:

        state_name = forecast.get("state")
        city_name = forecast.get("city")

        users = (
            session.query(UserModel)
            .join(AddressModel)
            .join(CityModel)
            .join(StateModel)
            .filter(StateModel.name == state_name)
            .filter(CityModel.name == city_name)
            .all()
        )

        if users:
            city_info = {
                "city": city_name.title(),
                "state": state_name.title(),
                "users_warned": len(users),
            }

            endangered_cities.append(city_info)

    return endangered_cities

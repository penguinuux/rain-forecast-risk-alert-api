import asyncio
from http import HTTPStatus

from flask import request
from sqlalchemy.orm import Session

from app.configs.database import db
from app.decorators.forecast_risk_decorator import request_validator
from app.models import RiskModel
from app.models.message_model import MessageModel
from app.services.communication_services import sms_send
from app.services.forecast_risk_services import (
    create_message_log,
    get_endangered_cities_and_users,
)
from app.utils.phone_only_numbers_formatter import phone_with_only_numbers


@request_validator
def fetch_forecast_risk():

    data = request.get_json()

    endangered_cities, users = get_endangered_cities_and_users(
        data, RiskModel.PRECIPITATION_LIMIT
    )

    # This logic is to limit the users to only 10 results
    # i think we should delete this to the heroku application
    # and use only real data from there
    # Another suggestion would be to limit the sms function to raise
    # an error when overloading our limit
    users = users[:10]

    for user in users:
        message = user.risks[0].text
        phone = phone_with_only_numbers(user.phone)
        asyncio.run(sms_send(phone, message))

    create_message_log(users)

    return {"endangered_cities": endangered_cities}, HTTPStatus.OK

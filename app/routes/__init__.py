from flask import Blueprint, Flask

from .cities_blueprint import bp as bp_cities
from .forecast_risk_blueprint import bp as bp_forecast_risk
from .message_blueprint import bp_message
from .user_blueprint import bp_users

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")


def init_app(app: Flask):

    bp_api.register_blueprint(bp_message)
    bp_api.register_blueprint(bp_users)
    bp_api.register_blueprint(bp_forecast_risk)
    bp_api.register_blueprint(bp_cities)

    app.register_blueprint(bp_api)

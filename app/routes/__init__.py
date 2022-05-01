from flask import Blueprint, Flask

from .address_blueprint import bp_address
from .message_blueprint import bp_message
from .risk_blueprint import bp_risk
from .user_blueprint import bp_users

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")


def init_app(app: Flask):

    bp_api.register_blueprint(bp_address)
    bp_api.register_blueprint(bp_message)
    bp_api.register_blueprint(bp_risk)
    bp_api.register_blueprint(bp_users)

    app.register_blueprint(bp_api)

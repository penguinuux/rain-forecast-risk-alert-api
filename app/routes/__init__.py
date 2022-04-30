from flask import Blueprint, Flask

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")


def init_app(app: Flask):

    from .address_blueprint import bp_address

    bp_api.register_blueprint(bp_address)

    from .message_blueprint import bp_message

    bp_api.register_blueprint(bp_message)

    from .risk_blueprint import bp_risk

    bp_api.register_blueprint(bp_risk)

    from .user_blueprint import bp_users

    bp_api.register_blueprint(bp_users)

    from .forecast_risk_blueprint import bp as bp_forecast_risk

    bp_api.register_blueprint(bp_forecast_risk)

    app.register_blueprint(bp_api)

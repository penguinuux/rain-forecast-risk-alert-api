from flask import Blueprint, Flask

bp_api = Blueprint("bp_api", __name__)


def init_app(app: Flask):

    app.register_blueprint(bp_api)

from flask import Flask

from .city_and_state_commands import state_and_city_cli


def init_app(app: Flask):
    app.cli.add_command(state_and_city_cli())

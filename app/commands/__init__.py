from flask import Flask

from .populate_db_commands import populate_db_cli


def init_app(app: Flask):
    app.cli.add_command(populate_db_cli())

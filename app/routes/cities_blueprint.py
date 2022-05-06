from flask import Blueprint

from app.controllers import cities_controller

bp = Blueprint("bp_cities", __name__, url_prefix="/cities")

bp.get("")(cities_controller.all_states_and_cities)
bp.get("/from-state/<state>")(cities_controller.all_cities_from_state)

from flask import Blueprint

from app.controllers.cities_controller import cities, city

bp = Blueprint("bp_cities", __name__, url_prefix="/cities")

bp.get("")(cities)
bp.get("/<state>")(city)

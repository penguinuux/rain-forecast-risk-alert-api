from flask import Blueprint

from app.controllers import risk_controller

bp_risk = Blueprint("bp_risk", __name__, url_prefix="/risk")

bp_risk.post("")(risk_controller.create)
bp_risk.get("")(risk_controller.retrieve)

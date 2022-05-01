from flask import Blueprint

from app.controllers import forecast_risk_controller

bp = Blueprint("bp_forecast_risk", __name__, "/forecast-risk")

bp.post("/forecast-risk")(forecast_risk_controller.fetch_forecast_risk)

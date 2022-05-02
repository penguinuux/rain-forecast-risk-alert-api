from flask import Blueprint

from app.controllers import forecast_risk_controller

bp = Blueprint("bp_forecast_risk", __name__, url_prefix="/forecast-risk")

bp.post("")(forecast_risk_controller.fetch_forecast_risk)

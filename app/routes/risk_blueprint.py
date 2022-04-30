from flask import Blueprint
from app.controllers.risk_controller import risks


bp_risk = Blueprint('bp_risk',__name__,url_prefix='/risk')

bp_risk.get('/')(risks)

from flask import Blueprint
from app.controllers.address_controller import address


bp_address = Blueprint('bp_address',__name__,url_prefix='/address')

bp_address.get('/')(address)

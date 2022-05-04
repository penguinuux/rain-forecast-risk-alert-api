from flask import Blueprint

from app.controllers import message_controller

bp_message = Blueprint("bp_message", __name__, url_prefix="/messages")

bp_message.get("")(message_controller.retrieve)

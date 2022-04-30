from flask import Blueprint

from app.controllers.message_controller import messages

bp_message = Blueprint("bp_message", __name__, url_prefix="/messages")

bp_message.get("")(messages)

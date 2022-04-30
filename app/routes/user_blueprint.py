from flask import Blueprint

from app.controllers import user_controller

bp_users = Blueprint("bp_users", __name__, url_prefix="/user")

bp_users.post("/signup")(user_controller.signup)
bp_users.post("/signin")(user_controller.signin)
bp_users.get("/")(user_controller.retrieve)
bp_users.patch("/")(user_controller.patch)
bp_users.delete("/")(user_controller.delete)

from flask import Blueprint
from app.controllers.user_controller import signin,delete_user,get_user,patch_user,signup


bp_users = Blueprint('bp_users',__name__,url_prefix='/user')

bp_users.post('/signup')(signup)
bp_users.post('/signin')(signin)
bp_users.get('/')(get_user)
bp_users.patch('/')(patch_user)
bp_users.delete('/')(delete_user)
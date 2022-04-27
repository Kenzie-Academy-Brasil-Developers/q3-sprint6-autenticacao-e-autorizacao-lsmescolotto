from flask import Blueprint

from app.controllers.user_controller import register_user, update_user, get_users, delete_user, login

bp_user = Blueprint("bp_user", __name__, url_prefix="/api")

bp_user.post("signup")(register_user)
bp_user.post("signin")(login)
bp_user.put("")(update_user)
bp_user.delete("")(delete_user)
bp_user.get("")(get_users)
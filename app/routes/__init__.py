from flask import Flask
from .user_route import bp_user


def init_app(app:Flask):
    app.register_blueprint(bp_user)
from flask import Flask
from environs import Env
from app import routes
from app.configs import database, migration
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)

    env = Env()
    env.read_env()

    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = env("JWT_SECRET_KEY")

    database.init_app(app)
    migration.init_app(app)
    JWTManager(app)
    routes.init_app(app)
    

    return app
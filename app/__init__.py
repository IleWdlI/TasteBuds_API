from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config

api = Api()
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app(config=Config):
    from .resources import initialize_routes

    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    initialize_routes(api)
    jwt.init_app(app)
    api.init_app(app)

    return app

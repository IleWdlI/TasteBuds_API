import werkzeug
from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_admin import Admin
from config import Config

api = Api()
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
admin = Admin()

def create_app(config=Config):
    from .resources import initialize_routes

    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    initialize_routes(api)
    jwt.init_app(app)
    api.init_app(app)
    admin.init_app(app)

    @app.errorhandler(werkzeug.exceptions.BadRequest)
    def handle_validation_error(e):
        return jsonify({'error': e}), 400

    return app

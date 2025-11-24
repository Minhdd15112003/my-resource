from flask import Flask
from flask_marshmallow import Marshmallow

from config import Config
from core.database import connect_db
from .books.controller import books


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    ma = Marshmallow(app)
    connect_db()
    app.register_blueprint(books)
    return app

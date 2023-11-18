from flask_sqlalchemy import SQLAlchemy
from ..utils.config import Config


db = SQLAlchemy()


def init_app(app, database):
    app.config.from_object(Config)
    database.init_app(app)

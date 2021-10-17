"""
Test Umba v0.1
"""

from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from .database import db
from .database.github_users import GithubUsers

def create_app(config):
    """
    Function that create flask application.

    Parameters
    ----------
    config : object
        Object with configuration options

    Returns
    -------
    app : Flask Object
    """
    app = Flask(__name__)

    app.config.from_object(config)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://osvi:123456@127.0.0.1/test_umba"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    migrate = Migrate(directory="database/migrations")
    migrate.init_app(app, db)

    return app

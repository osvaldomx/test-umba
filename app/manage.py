import os

from flask import Flask
from flask_migrate import Migrate

from config import DevelopConfig

from main.database import db

if __name__ == '__main__':
	app = Flask(__name__)
	app.config.from_object(DevelopConfig)

	with app.app_context():
		db.init_app(app)
		db.create_all()

	dir = os.getcwd() + "/main/database/migrations"
	migrate = Migrate(directory=dir)
	migrate.init_app(app, db)
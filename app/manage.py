from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import DevelopConfig

from main.database import db
from main.database.github_users import GithubUsers

if __name__ == '__main__':
	app = Flask(__name__)
	app.config.from_object(DevelopConfig)

	with app.app_context():
		db.init_app(app)
		db.create_all()

	migrate = Migrate(directory="/main/database/migrations")
	migrate.init_app(app, db)
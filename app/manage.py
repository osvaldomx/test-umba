from flask_migrate import Migrate

from config import DevelopConfig

from main import create_app
from main.database import db

if __name__ == '__main__':
	app = create_app(DevelopConfig)
	db.init_app(app)
	migrate = Migrate(directory="database/migrations")
	migrate.init_app(app, db)
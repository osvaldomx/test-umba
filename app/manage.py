from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import DevelopConfig

from main.database import db
from main.database.github_users import GithubUsers


app = Flask(__name__)
app.config.from_object(DevelopConfig)



migrate = Migrate(directory="/main/database/migrations")
migrate.init_app(app, db)
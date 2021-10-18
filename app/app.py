"""
ML Test Umba v0.2
"""
import os
import sys
import csv
import getopt

import sqlite3
from sqlite3 import Error

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

from flask_migrate import Migrate

from config import DevelopConfig

from main.database import db

from main.seed import setup_db
from main.seed import populate_table

from main.database.github_users import GithubUsers

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    """
    Function for page not found
    """
    return render_template("404.html", error=error), 404

@app.route('/')
def index():
    """
    Function for index
    """
    title = "ML Test Umba"

    return render_template("index.html", title=title), 200

@app.route('/setup')
def setup():
    total = request.args.get('total', '150')

    try:
        connection = sqlite3.connect(os.getcwd() + "/main/database/users.db")
    except Error as err:
        raise err

    setup_db(connection)
    populate_table(connection, int(total))

    with open(os.getcwd() + "/main/database/github_users.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            db.session.add(
                GithubUsers(int(row[0]),
                            row[1],
                            row[2],
                            row[3],
                            row[4])
            )
        db.session.commit()

    return redirect(url_for('index'))


@app.route('/users')
@app.route('/users/<int:page>')
def users(page=1):
    title = "GitHub Users"
    per_page = int(request.args.get('pagination', '25'))
    total_records = len(GithubUsers.query.all())
    list_pags = 1

    if total_records > per_page:
        list_pags = int(total_records / per_page)
        if total_records % per_page > 0:
            list_pags += 1

    users_list = GithubUsers.query.paginate(page, per_page, False)

    return render_template("users.html",
                            title=title,
                            users=users_list,
                            pags=list_pags), 200

if __name__ == '__main__':
    app.config.from_object(DevelopConfig)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    app.run()

# CODE TO MIGRATIONS
app.config.from_object(DevelopConfig)
db.init_app(app)
dir = os.getcwd() + "/main/database/migrations"
migrate = Migrate(directory=dir)
migrate.init_app(app, db)

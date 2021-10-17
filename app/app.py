"""
Test Umba v0.1
Script that initialize flask application.
"""
import os
from flask import Flask
from flask import render_template

import sqlite3
from sqlite3 import Error

import getopt
import sys
import csv

from config import DevelopConfig

from main import create_app

from main.seed import setup_db
from main.seed import populate_table

from main.database.github_users import GithubUsers
from main.database import db


app = Flask(__name__)

@app.route('/')
def index():
    """
    Function for index.html
    """
    return render_template("index.html"), 200


if __name__ == '__main__':
    app = create_app(DevelopConfig)
    app.run()

    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'it:', ['init', 'total='])
    except Exception as exc:
        raise exc

    try:
        connection = sqlite3.connect(os.getcwd() + "/main/database/users.db")
    except Error as err:
        raise err

    INIT = False
    TOTAL = 150

    for opt, val in optlist:
        if opt in ['-i', '--init']:
            INIT = True
        elif opt in ['-t', '--total']:
            TOTAL = val

    if INIT:
        setup_db(connection)
        populate_table(connection, TOTAL)

        with app.app_context():
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
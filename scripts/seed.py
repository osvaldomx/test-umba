"""
Stage 1

Create a python shell script called seed.py wiche only responsability will be
to populate and SQLite database, with the information of the GitHub Users API
into a github_users table. The required fields will be:

* id, username, avatar_url, type, URL
"""

import sys
import getopt

import sqlite3
from sqlite3 import Error

import requests

def setup_db(db_file):
    """
    Function to create connection to sqlite databese and create table users.

    Parameters
    ----------
    db_file : str
        Path and name of sqldatabase.

    Raises
    ------
    Exception
        If can't create connection to database.

    Returns
    -------
    conection : Connection Object
    """

    connection = None

    try:
        connection = sqlite3.connect(db_file)
    except Exception as exc:
        raise exc

    create_table = """
                        CREATE TABLE IF NOT EXISTS users (
                            id integer PRIMARY KEY,
                            username text NOT NULL,
                            avatar_url text,
                            type text NOT NULL,
                            url text NOT NULL
                            );
    """

    try:
        cursor = connection.cursor()
        cursor.execute(create_table)
    except Error as err:
        raise err

    return connection

def get_data(list_pages):
    """
    Function to get users from github API.

    Parameters
    ----------
    total_records : int
        Total of records to get from github.
    list_pages : list
        List of limit of records per page.

    Retruns
    -------
    data : list
        List with total of user records.
    """
    data = []
    since = 0

    for page in list_pages:
        json = requests.get("https://api.github.com/users?per_page="\
                                + str(page)\
                                + "&since="\
                                + str(since)).json()
        data.append(json)
        since += json[-1]['id']

    return data


def populate_table(conn, *args):
    """
    Function to populate users table.

    Parameters
    ----------
    conn : Connection Object
        Object to execute queries.
    args : tuple
        Tuple with arguments passed from console.

    Arguments
    ---------
    -t, --total
        Total of records to populate the database. By default 150.
    """

    total = 150

    try:
        optlist, args = getopt.getopt(args[0], 't:', ['total='])

    except getopt.GetoptError as err:
        print(err)
        print(populate_table.__doc__[178:274])
        sys.exit(2)

    for opt, val in optlist:
        if opt in ['-t', '--total']:
            total = int(val)

    per_page = 100
    per_page_list = []

    if total <= per_page:
        per_page_list.append(total)
    else:
        per_page_list = [100] * int(total / per_page)
        if total % per_page > 0:
            per_page_list.append(total % per_page)

    data = get_data(per_page_list)

    insert = "INSERT INTO users VALUES (?,?,?,?,?);"
    cursor = conn.cursor()

    for page in data:
        for element in page:
            user = (element['id'],
                    element['login'],
                    element['avatar_url'],
                    element['type'],
                    element['html_url'])
            cursor.execute(insert, user)

    conn.commit()

    return True


if __name__ == '__main__':
    connection_obj = setup_db("./users.db")
    populate_table(connection_obj, sys.argv[1:])
    connection_obj.close()

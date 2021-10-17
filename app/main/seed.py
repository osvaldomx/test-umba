"""
Test Umba v0.1
"""
from sqlite3 import Error

import csv
import os
import requests

def setup_db(conn):
    """
    Function to create table in database.

    Parameters
    ----------
    conn : object
        Connection Object.

    Raises
    ------
    Error : object
        SQLite Error object

    Returns
    -------
    True : boolean
        True if works.
    """
    create_table = """
                    CREATE TABLE IF NOT EXISTS github_users (
                        id integer PRIMARY KEY,
                        username text NOT NULL,
                        avatar_url text,
                        type text NOT NULL,
                        url text NOT NULL);
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table)
        return True
    except Error as err:
        raise err

def get_data(list_pages):
    """
    Function to get data from GitHub API.

    Parameters
    ----------
    list_pages : list
        List with limit per page.

    Returns
    -------
    data : list
        List with users data.
    """
    data = []
    since = 0

    for page in list_pages:
        json = requests.get("https://api.github.com/users?per_page="\
                                + str(page)\
                                + "&since="\
                                + str(since)).json()
        data.append(json)
        since = json[-1]['id']

    with open(os.getcwd() + "/main/database/github_users.csv", 'w') as file:
        write = csv.writer(file)
        for chunk in data:
            for user in chunk:
                row = [
                        user['id'],
                        user['login'],
                        user['avatar_url'],
                        user['type'],
                        user['html_url']
                ]
                write.writerow(row)

    return data

def populate_table(conn, total=150):
    """
    Function to populate 'github_users' table.

    Parameters
    ----------
    conn : object
        Connection Object
    total : int
        Total of records

    Returns
    -------
    True : boolean
        If works.
    """
    per_page = 100
    per_page_list = []

    if total <= per_page:
        per_page_list.append(per_page)
    else:
        per_page_list = [100] * int(total / per_page)
        if total % per_page > 0:
            per_page_list.append(total % per_page)

    data = get_data(per_page_list)

    insert = "INSERT INTO github_users VALUES (?,?,?,?,?);"
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
    conn.close()

    return True

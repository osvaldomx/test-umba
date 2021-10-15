import sys
import getopt
import requests
import sqlite3

from sqlite3 import Error

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
		print(sqlite3.version)
		print("Connection to databese created...")
	except Exception as e:
		raise e

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
		c = connection.cursor()
		c.execute(create_table)
		print("Database and table 'users' setup up...")
	except Error as e:
		raise e


	return connection

	

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
	args = args[0]

	try:
		optlist, args = getopt.getopt(args, 't:', ['total='])

	except getopt.GetoptError as err:
		print(err)
		print(populate_table.__doc__[178:274])
		sys.exit(2)

	for opt, val in optlist:
		if opt in ['-t', '--total']:
			total = int(val)
			print("The database will populate with {} records".format(total))

	per_page = 100
	per_page_list = []
	since = 0

	if total <= per_page:
		per_page_list.append(total)
	else:
		per_page_list = [100] * int(total / per_page)
		mod = total % per_page
		if mod > 0:
			per_page_list.append(mod)

	data = []

	for page in per_page_list:
		#print(page, since)
		json = requests.get("https://api.github.com/users?per_page="\
								+ str(page)\
								+ "&since="\
								+ str(since)).json()
		data.append(json)
		since += json[-1]['id']

	insert = "INSERT INTO users VALUES (?,?,?,?,?);"
	c = conn.cursor()

	for page in data:
		for element in page:
			user = (element['id'],
					element['login'],
					element['avatar_url'],
					element['type'],
					element['html_url'])
			#print(user)
			c.execute(insert, user)

	conn.commit()

	return True


if __name__ == '__main__':
	conn = setup_db("./users.db")
	populate_table(conn, sys.argv[1:])
	conn.close()
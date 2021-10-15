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
	since = 0
	limit = int(total/per_page) + 1

	#for i in range(limit):
	#	json = requests.get("https://api.github.com/users?per_page="\
	#							+ str(per_page)\
	#							+ "&since="\
	#							+ str(since)).json()
	#	since += 100

	json = [
			{
				"login": "octocat",
			  	"id": 1,
				"node_id": "MDQ6VXNlcjE=",
				"avatar_url": "https://github.com/images/error/octocat_happy.gif",
				"gravatar_id": "",
				"url": "https://api.github.com/users/octocat",
				"html_url": "https://github.com/octocat",
				"followers_url": "https://api.github.com/users/octocat/followers",
				"following_url": "https://api.github.com/users/octocat/following{/other_user}",
				"gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
				"starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
				"subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
				"organizations_url": "https://api.github.com/users/octocat/orgs",
				"repos_url": "https://api.github.com/users/octocat/repos",
				"events_url": "https://api.github.com/users/octocat/events{/privacy}",
				"received_events_url": "https://api.github.com/users/octocat/received_events",
				"type": "User",
				"site_admin": False,
				"name": "monalisa octocat",
				"company": "GitHub",
				"blog": "https://github.com/blog",
				"location": "San Francisco",
				"email": "octocat@github.com",
				"hireable": False,
				"bio": "There once was...",
				"twitter_username": "monatheoctocat",
				"public_repos": 2,
				"public_gists": 1,
				"followers": 20,
				"following": 0,
				"created_at": "2008-01-14T04:33:35Z",
				"updated_at": "2008-01-14T04:33:35Z",
				"private_gists": 81,
				"total_private_repos": 100,
				"owned_private_repos": 100,
				"disk_usage": 10000,
				"collaborators": 8,
				"two_factor_authentication": True,
				"plan": {
					"name": "Medium",
					"space": 400,
					"private_repos": 20,
					"collaborators": 0
				}
			},
			{
				"login": "octocat",
			  	"id": 2,
				"node_id": "MDQ6VXNlcjE=",
				"avatar_url": "https://github.com/images/error/octocat_happy.gif",
				"gravatar_id": "",
				"url": "https://api.github.com/users/octocat",
				"html_url": "https://github.com/octocat",
				"followers_url": "https://api.github.com/users/octocat/followers",
				"following_url": "https://api.github.com/users/octocat/following{/other_user}",
				"gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
				"starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
				"subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
				"organizations_url": "https://api.github.com/users/octocat/orgs",
				"repos_url": "https://api.github.com/users/octocat/repos",
				"events_url": "https://api.github.com/users/octocat/events{/privacy}",
				"received_events_url": "https://api.github.com/users/octocat/received_events",
				"type": "User",
				"site_admin": False,
				"name": "monalisa octocat",
				"company": "GitHub",
				"blog": "https://github.com/blog",
				"location": "San Francisco",
				"email": "octocat@github.com",
				"hireable": False,
				"bio": "There once was...",
				"twitter_username": "monatheoctocat",
				"public_repos": 2,
				"public_gists": 1,
				"followers": 20,
				"following": 0,
				"created_at": "2008-01-14T04:33:35Z",
				"updated_at": "2008-01-14T04:33:35Z",
				"private_gists": 81,
				"total_private_repos": 100,
				"owned_private_repos": 100,
				"disk_usage": 10000,
				"collaborators": 8,
				"two_factor_authentication": True,
				"plan": {
					"name": "Medium",
					"space": 400,
					"private_repos": 20,
					"collaborators": 0
				}
			}
	]

	insert = "INSERT INTO users VALUES (?,?,?,?,?);"
	c = conn.cursor()

	for element in json:
		user = (element['id'],
				element['login'],
				element['avatar_url'],
				element['type'],
				element['html_url'])
		c.execute(insert, user)

	conn.commit()

	return True


if __name__ == '__main__':
	conn = setup_db("./users.db")
	populate_table(conn, sys.argv[1:])
	conn.close()
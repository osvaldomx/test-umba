import unittest
import sqlite3

from seed import setup_db
from seed import populate_table

class TestSeed(unittest.TestCase):

	def test_setup_db(self):
		self.assertIsInstance(setup_db("test.db"), sqlite3.Connection)

	def test_populate_table(self):
		conn = setup_db("test.db")
		assert populate_table(conn, (['x','-t','10'])) == True

if __name__ == '__main__':
	unittest.main()
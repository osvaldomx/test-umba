"""
Tests for seed.py
"""
import unittest
import sqlite3

from seed import setup_db
from seed import get_data
from seed import populate_table

class TestSeed(unittest.TestCase):
    """
    Class for tests
    """
    def test_setup_db(self):
        """
        Test function 'setup_db'
        """
        self.assertIsInstance(setup_db("test.db"), sqlite3.Connection)

    def test_get_data(self):
        """
        Test function 'get_data'
        """
        self.assertIsInstance(get_data([10]), list)

    @staticmethod
    def test_populate_table():
        """
        Test function 'populate_table'
        """
        conn = setup_db("test.db")
        assert populate_table(conn, (['x','-t','10'])) is True

if __name__ == '__main__':
    unittest.main()

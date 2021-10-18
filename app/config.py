import os

class DevelopConfig(object):
	ORIGINS = ['*']
	DEBUG = True
	PORT = 5000
	HOST = '127.0.0.1'
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123456@database:5432/test_umba"
	SQLALCHEMY_TRACK_MODIFICATIONS = False


import os

class DevelopConfig(object):
	ORIGINS = ['*']
	DEBUG = True
	PORT = 5000
	HOST = '0.0.0.0'
	SQLALCHEMY_DATABASE_URI = "postgresql://osvi:123456@127.0.0.1/test_umba"
	SQLALCHEMY_TRACK_MODIFICATIONS = False


from . import db

from marshmallow import Schema
from marshmallow import fields

class GithubUsers(db.Model):
	__tablename__ = 'github_users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), nullable=False)
	avatar_url = db.Column(db.String(500))
	type = db.Column(db.String(20), nullable=False)
	url = db.Column(db.String(500), nullable=False)

	def __init__(self, id, username, avatar_url, type, url):
		self.id = id
		self.username = username
		self.avatar_url = avatar_url
		self.type = type
		self.url = url

class GithubUsersSchema(Schema):
	id = fields.Int()
	username = fields.Str()
	avatar_url = fields.Str()
	type = fields.Str()
	url = fields.Str()
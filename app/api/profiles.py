from flask import Blueprint
from flask import request

from main.database.github_users import GithubUsers
from main.database.github_users import GithubUsersSchema

from utils.responses import response
from utils.responses import bad_request

profile = Blueprint('profiles', __name__)

@profile.route("/profiles")
@profile.route("/profiles/<int:page>")
def profiles(page=1):
	per_page = int(request.args.get('pagination', '25'))
	page = int(request.args.get('page', '1'))
	order = request.args.get('order_by', 'id')
	username = request.args.get('username', None)
	id = int(request.args.get('id', None))

	if order == 'id':
		profiles_obj = GithubUsers.query.order_by(GithubUsers.id).paginate(page, per_page, False)
	elif order == 'type':
		profiles_obj = GithubUsers.query.order_by(GithubUsers.type.asc()).paginate(page, per_page, False)

	if username:
		profiles_obj = GithubUsers.query.filter_by(username=username)
		if profiles_obj:
			return response(GithubUsersSchema(many=True).
							dump(profiles_obj))

	if id:
		profiles_obj = GithubUsers.query.filter_by(id=id)
		if profiles_obj:
			return response(GithubUsersSchema(many=True).
							dump(profiles_obj))


	if profiles_obj:
		return response(GithubUsersSchema(many=True).
							dump(profiles_obj.items))

	return bad_request()


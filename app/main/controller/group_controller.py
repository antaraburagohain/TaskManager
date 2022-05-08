from flask import request
from flask_restx import Resource

from ..util.dto import GroupDto
from ..service.group_Service import save_new_group,add_user,delete_user,get_groups,get_public_id
from ..util.dto import UserDto

api=GroupDto.api
_group = GroupDto.group
_group_user = GroupDto.group_user
_group_list = GroupDto.group_list
@api.route('/new_group')
class createGroup(Resource):
	@api.response(201,'Group successfully created.')
	@api.doc('Create a new group')
	@api.expect(_group,validate=True)
	def post(self):
		data = request.json
		return save_new_group(data=data)


@api.route('/add_new_user')
class Add_user(Resource):
	@api.response(201,'User added successfully.')
	@api.doc('add a user')
	@api.expect(_group_user,validate=True)
	def post(self):
		data = request.json
		return add_user(data)

@api.route('/delete_user')
class Delete_user(Resource):
	@api.response(201,'User deleted successfully.')
	@api.doc('delete a user')
	@api.expect(_group_user,validate=True)
	def post(self):
		data = request.json
		return delete_user(data)

@api.route('/view_groups')
class showGroup(Resource):
	@api.response(201,'Group found.')
	@api.expect(_group_list,validate=True)
	def post(self):
		data = request.json
		public_id = (get_public_id(data['email']))
		return get_groups(public_id)

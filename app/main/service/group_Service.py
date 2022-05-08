import uuid
import datetime

from app.main import db
from app.main.model.group import Group,Group_user
from app.main.model.user import User
def save_new_group(data):
	new_group = Group(
		group_id = str(uuid.uuid4()),
		group_name = data['group_name'],
		group_desc = data['group_desc'],
		admin_id = data['public_id']
		)
	save_changes(new_group)
	group_id = new_group.group_id
	new_group = Group_user(
		group_id = group_id,
		public_id = data['public_id']
		)
	save_changes(new_group)
	response_object ={
	'group_id':group_id,
	'status':'success',
	'message':'Successfully Created.'
	}
	return response_object,201

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def get_public_id(email):
	details = User.query.filter_by(email=email).first()
	return details.public_id

def add_user(data):
	user = User.query.filter_by(email=data['email']).first()
	group = Group.query.filter_by(group_id=data['group_id']).first()
	if user and group:
		group_user = Group_user.query.filter_by(public_id=get_public_id(data['email']),group_id_value = data['group_id']).first()
		if group_user:
			response_object ={
			'status':'success',
			'message':'User already exists.'
			}
			return response_object,201
		else:
			new_group_user = Group_user(
				public_id = get_public_id(data['email']),
				group_id = data['group_id']
				)
			save_changes(new_group_user)
			response_object = {
			'status':'success',
			'message':'User added successfully.'
			}
			return response_object,201
	else:
		response_object = {
		'status':'fail',
		'message':'User not exist'
		}
		return response_object,409

def delete_user(data):
	public_id = get_public_id(data['email'])
	user = Group_user.query.filter_by(public_id = public_id,group_id_value=data['group_id']).first()
	if user:
		db.session.delete(user)
		db.session.commit()
		response_object = {
		'status':'success',
		'message':'User deleted successfully.'
		}
		return response_object,201
	else:
		response_object = {
		'status':'fail',
		'message':'User not exist in group'
		}
		return response_object,409


def get_groups(public_id):
	groups = Group_user.query.filter_by(public_id = public_id).all()
	if groups:
		b=[]
		for i in range(len(groups)):
			a=(groups[i].group_id_value)
			b.append(Group.query.filter_by(group_id=a).first())
		a=[]
		for i in range(len(b)):
			response_object = {
			'group_id':b[i].group_name,
			'group_desc':b[i].group_desc
			}
			a.append(response_object)
		return a,201
	else:
		response_object = {
		'status':'fail',
		'message':'Group not exist'
		}
		return response_object,409
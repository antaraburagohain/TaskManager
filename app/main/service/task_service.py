import uuid
import datetime
from app.main import db
from app.main.model.user import User
from app.main.model.task import Task
def save_new_task(data):
	new_task = Task(
    	userid = str(uuid.uuid4()),
    	public_id = data['public_id'],
    	group_id = data['group_id'],
    	priority = data['priority'],
    	status='open',
    	duedate = datetime.datetime.strptime(data['duedate'],'%d-%m-%Y'),
    	created_date = datetime.datetime.utcnow(),
    	task_Desc = data['task_Desc'],
    	assigned_to = get_email(data['public_id']),
    	created_by = get_email(data['public_id'])
    	)
	save_changes(new_task)
	response_object = {
	'status':'success',
	'message':'Successfully created.'
	}
	return response_object,201

def get_email(public_id):
	user = User.query.filter_by(public_id=public_id).first()
	return user.first_name

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def update_task(data):
	task = Task.query.filter_by(userid=data['userid']).first()
	update_items=''
	if task:
		if data['priority']:
			task.priority=data['priority']
			db.session.commit()
			update_items+='priority'
		if data['status']:
			task.status = get_status(data['status'])
			db.session.commit()
			update_items+=' status'
		if data['duedate']:
			task.duedate = datetime.datetime.strptime(data['duedate'],'%d-%m-%Y')
			db.session.commit()
			update_items+=' duedate'
		if data['assigned_to']:
			task.assigned_to = get_name(data['assigned_to'])
			db.session.commit()
			update_items+=' assigned_to'
		if update_items=='':
			response_object={
			'status':'success',
			'message':'Nothing to update'
			}
			return response_object,201
		update_items+=' got updated.'
		response_object = {
		'status':'success',
		'message':update_items
		}
		return response_object,201



def get_status(status):
	s=''
	if status=='0':
		s='open'
	elif status=='1':
		s='in progress'
	else:
		s='complete'
	return s

def get_name(email):
	user = User.query.filter_by(email=email).first()
	return user.first_name

def get_public_id(email):
	user = User.query.filter_by(email=email).first()
	return user.public_id

def get_task_list(public_id,group_id):
	if group_id!="":
		tasks = Task.query.filter_by(public_id=public_id,group_id_value=group_id).all()
		a=[]
		for i in range(len(tasks)):
			response_object={
			'task_Desc':tasks[i].task_Desc,
			'duedate':str(tasks[i].duedate),
			'status':tasks[i].status,
			'priority':tasks[i].priority_column,
			'created_by':tasks[i].created_by,
			'assigned_to':tasks[i].assigned_to
			}
			a.append(response_object)
		return a,201
	else:
		tasks = Task.query.filter_by(public_id=public_id).all()
		a=[]
		for i in range(len(tasks)):
			response_object={
			'task_Desc':tasks[i].task_Desc,
			'duedate':str(tasks[i].duedate),
			'status':tasks[i].status,
			'priority':tasks[i].priority_column,
			'created_by':tasks[i].created_by,
			'assigned_to':tasks[i].assigned_to
			}
			a.append(response_object)
		return a,201
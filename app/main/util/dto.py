from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first_name'),
        'last_name': fields.String(required=True, description='user last_name'),
        'password': fields.String(required=True, description='user password')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class GroupDto:
    api = Namespace('group',description = 'group related operations')
    group = api.model('group_details',{
        'group_name':fields.String(required=True,description='group name'),
        'group_desc':fields.String(required=True,description='group description'),
        'public_id':fields.String(required=True,description='group created by')
        })
    group_user = api.model('add_user',{
        'email':fields.String(required=True,description='user email'),
        'group_id':fields.String(required=True,description='Group name')
        })
    group_list = api.model('group_list',{
        'email':fields.String(required=True,description=' user public id'),
        })

class TaskDto:
    api = Namespace('task',description = 'task related operations')
    task = api.model('task_details',{
        'public_id':fields.String(required=True,description = 'user public id'),
        'group_id':fields.String(required=True,description='grooup id'),
        'task_Desc':fields.String(required = True,description = 'task description'),
        'priority':fields.String(required = True,description = 'priority value'),
        'duedate':fields.String(required=True,description='task due date')
        })
    update_task = api.model('update_task',{
        'userid':fields.String(required=True,description='task id'),
        'priority':fields.String(required=True,description='priority'),
        'status':fields.String(required=True,description='status'),
        'duedate':fields.String(required=True,description='duedate'),
        'assigned_to':fields.String(required=True,description='assigned_to')
        })
    list_task = api.model('list_task',{
        'email':fields.String(required=True,description='user email'),
        'group_id':fields.String(description='user group id')
        })
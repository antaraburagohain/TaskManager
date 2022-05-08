from .. import db, flask_bcrypt

class Group(db.Model):
	__tablename__= "groups"

	group_id = db.Column(db.String(100),unique=True,nullable=False,primary_key=True)
	group_name = db.Column(db.String(100),nullable=False)
	group_desc=db.Column(db.String(255))
	members_value = db.Column(db.String(1000000))
	admin_id = db.Column(db.String(100))

	@property
	def members(self):
		raise AttributeError('members: write-only field')

	@members.setter
	def members(self,members):
		members_value = group_id

	def __repr__(self):
		return "<User '{}'>".format(self.group_name)




class Group_user(db.Model):
	__tablename__ = "group_user"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	public_id = db.Column(db.String(100))
	group_id_value = db.Column(db.String(100))

	@property
	def group_id(self):
		raise AttributeError('group_id: write-only field')

	@group_id.setter
	def group_id(self,group_id):
		if group_id:
			self.group_id_value = group_id
		else:
			self.group_id_value=None

	def __repr__(self):
		return "<User '{}'>".format(self.public_id)
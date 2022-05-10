from .. import db, flask_bcrypt


class Task(db.Model):

    __tablename__ = "task"
    userid = db.Column(db.String, primary_key=True)
    public_id = db.Column(db.String, nullable=False)
    group_id_value = db.Column(db.String, nullable=True)
    priority_column = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    duedate = db.Column(db.DateTime, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    task_Desc = db.Column(db.String, nullable=False)
    assigned_to = db.Column(db.String, nullable=False)
    created_by = db.Column(db.String, nullable=False)

    @property
    def priority(self):
        raise AttributeError('priority: write-only field')

    @priority.setter
    def priority(self, priority):
        self.priority_column = priority

    @property
    def group_id(self):
        raise AttributeError('group_id: write-only field')

    @group_id.setter
    def group_id(self, group_id):
        if group_id:
            self.group_id_value = group_id
        else:
            self.group_id_value = None

    def __repr__(self):
        return "<User '{}'>".format(self.userid)

from .. import db, flask_bcrypt
import datetime
import jwt
from ..config import key
class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"
    email = db.Column(db.String(255),primary_key=True, unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    public_id = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(50), unique=False,nullable=False)
    last_name = db.Column(db.String(50), unique=False,nullable=False)
    password_hash = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.email)


    @staticmethod
    def encode_auth_token(user_id: int) -> bytes:
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e
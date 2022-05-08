import unittest
import datetime
import uuid
from app.main import db
from app.main.model.user import User
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        user = User(
            public_id=str(uuid.uuid4()),
            email='abc@gmail.com',
            first_name='abc',
            last_name='def',
            password='1234',
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.public_id)

if __name__ == '__main__':
    unittest.main()
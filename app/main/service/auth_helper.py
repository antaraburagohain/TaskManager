from app.main.model.user import User
from flask import make_response


class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.public_id)
                if auth_token:
                    response_object = {
                        'Email': data.get('email'),
                        'Public_Id': user.public_id,
                        'Status': 'Success',
                        'Message': 'Successfully logged in.',
                    }

                    return response_object

            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        print(data)
        if data:
            auth_token = data.split(" ")[1]

        else:
            auth_token = ''
        if auth_token:
            del auth_token
            response_object = {
                'status': 'success',
                'message': 'Successfully logged out'
            }
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

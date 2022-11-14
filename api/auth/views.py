from flask_restx import Namespace, Resource, fields
from flask import request
from ..models.users import User
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus

auth_namespace = Namespace('auth',description="namespace for authentification")


signup_model=auth_namespace.model(
    'SignUp',{
        'id':fields.Integer(),
        'username':fields.String(required=True,description="A username"),
        'email':fields.String(required=True,description="A email"),
        'password':fields.String(required=True,description="A password"),
    }
)


user_model=auth_namespace.model(
    'User',{
        'id':fields.Integer(),
        'username':fields.String(required=True,description="A username"),
        'email':fields.String(required=True,description="A email"),
        'password_hash':fields.String(required=True,description="A password"),
        'is_active':fields.Boolean(description="User is active"),
        'is_staff':fields.Boolean(description="User is staff")
    }
)

@auth_namespace.route('/signup')
class SignUp(Resource):

    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(user_model)
    def post(self):
        """
            Create a new user accout
        """

        data = request.get_json()


        new_user=User(
            username=data.get('username'),
            email=data.get('email'),
            password_hash=generate_password_hash(data.get('password'))            
        )


        new_user.sawe()
        pass

@auth_namespace.route('/login')
class Login(Resource):

    def post(self):
        """
            Create a JWT pair
        """
        pass


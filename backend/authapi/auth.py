from flask import Blueprint
from flask_restplus import Resource, Api, reqparse

auth_bp = Blueprint('auth', __name__)
auth_bp.config = {}

auth_api = Api(auth_bp)
parser = reqparse.RequestParser()

class LoginApi(Resource):

    def post(self):
        print('hello')
        parser.add_argument('email',type=str)
        parser.add_argument('pasword',type=str)
        args = parser.parse_args()
        email = args.get('email',None)
        password = args.get('password',None)

        if not email:
            return {'status': 'success', 'message': 'missing email'}, 200
        if not password:
            return {'status': 'success', 'message': 'missing password'}, 200

    def get(self):
        print('hello')
        parser.add_argument('email',type=str)
        parser.add_argument('pasword',type=str)
        args = parser.parse_args()
        email = args.get('email',None)
        password = args.get('password',None)

        if not email:
            return {'status': 'fail', 'message': 'missing email'}, 400
        if not password:
            return {'status': 'fail', 'message': 'missing password'}, 400





auth_api.add_resource(LoginApi, '/login')
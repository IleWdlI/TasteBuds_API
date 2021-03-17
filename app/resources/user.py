from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource, reqparse
from ..models.user import UserModel
from werkzeug.security import safe_str_cmp

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username', type=str, required=True)
_user_parser.add_argument('password', type=str, required=True)


class User(Resource):
    @staticmethod
    def get(user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            return {'message': 'User not found'}, 404
        return user.json()

    @staticmethod
    def delete(user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            return {'message': 'User not found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}, 200


class UserRegister(Resource):
    @staticmethod
    def post():
        data = _user_parser.parse_args()

        if UserModel.query.filter_by(data['username']).first():
            return {'message': 'A user with that name already exists'}, 400

        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'User created successfully.'}, 201


class UserLogin(Resource):
    @staticmethod
    def post():
        data = _user_parser.parse_args()
        user = UserModel.query.filter_by(data['username']).first()

        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }

        return {'message': 'Invalid credentials'}, 401





import datetime

from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from flask_restful import Resource, reqparse
from ..models.user import UserModel
from werkzeug.security import safe_str_cmp


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('username')
    parser.add_argument('foodie_bio', )
    parser.add_argument('allergy_diet', )
    parser.add_argument('cooking_lvl', type=int)
    parser.add_argument('url', )
    parser.add_argument('facebook', type=bool)
    parser.add_argument('twitter', type=bool)
    parser.add_argument('instagram', type=bool)
    parser.add_argument('avatar', type=bool)

    @staticmethod
    def get(user_id):
        user = UserModel.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.json()

    @staticmethod
    @jwt_required
    def delete(user_id):
        user = UserModel.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}, 200

    @staticmethod
    @jwt_required
    def put(user_id):
        data = User.parser.parse_args()
        user = UserModel.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        user = UserModel(**data)
        user.save_to_db()
        return user.json()


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email", required=True)
    parser.add_argument("password", required=True)

    @staticmethod
    def post():
        data = UserRegister.parser.parse_args()

        if UserModel.query.filter_by(email=data['email']).first():
            return {'message': 'A user with that name already exists'}, 400
        else:
            user = UserModel(email=data['email'])
            user.set_password(data['password'])
            user.save_to_db()
            access_token = create_access_token(identity=user.id, expires_delta=False)
            return {
                'access_token': access_token
            }


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email", required=True)
    parser.add_argument("password", required=True)

    @staticmethod
    def post():
        data = UserLogin.parser.parse_args()
        user = UserModel.query.filter_by(email=data['email']).first()

        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(days=30))
            return {
                'access_token': access_token
            }

        return {'message': 'Invalid credentials'}, 401

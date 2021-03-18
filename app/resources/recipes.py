from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from ..models import RecipeModel


class Recipe(Resource):
    @staticmethod
    @jwt_required
    def get(recipe_id):
        recipe = RecipeModel.query.get(recipe_id)
        return vars(recipe)

    @staticmethod
    @jwt_required
    def put(recipe_id):
        pass

    @staticmethod
    @jwt_required
    def delete(recipe_id):
        recipe = RecipeModel.query.get(recipe_id)
        if recipe:
            recipe.delete_from_db()
            return recipe.json()
        return {'message': 'Not found'}, 404


class CreateRecipe(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('recipe_source', type=str, required=True)
    parser.add_argument('link_to_recipe', type=str, required=True)
    parser.add_argument('other_notes', type=str)
    parser.add_argument('post_type', type=str)
    parser.add_argument('facebook', type=bool)
    parser.add_argument('instagram', type=bool)
    parser.add_argument('twitter', type=bool)

    @staticmethod
    @jwt_required
    def post():
        data = CreateRecipe.parser.parse_args()
        recipe = RecipeModel(**data)

        recipe.save_to_db()
        return recipe.json(), 201


class RecipeList(Resource):
    @staticmethod
    @jwt_required
    def get():
        return {'recipes': [recipe.json() for recipe in RecipeModel.query.all()]}

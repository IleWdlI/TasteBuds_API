from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from ..models import RecipeModel


class Recipe(Resource):
    @staticmethod
    @jwt_required()
    def get(recipe_id):
        recipe = RecipeModel.query.filter_by(recipe_id).first()
        print(recipe.title, recipe.recipe)

        if recipe:
            return recipe.json()

    @staticmethod
    @jwt_required()
    def put(recipe_id):
        pass

    @staticmethod
    @jwt_required()
    def delete(recipe_id):
        recipe = RecipeModel.query.filter_by(id=recipe_id).first()
        if recipe:
            recipe.delete_from_db()
            return recipe.json()
        return {'message': 'Not found'}, 404


class CreateRecipe(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True)
    parser.add_argument('recipe', type=str, required=True)

    @staticmethod
    @jwt_required()
    def post():
        data = CreateRecipe.parser.parse_args()
        recipe = RecipeModel(**data)
        print(recipe.title, recipe.recipe)

        recipe.save_to_db()
        return recipe.json(), 201


class RecipeList(Resource):
    @staticmethod
    @jwt_required
    def get():
        return {'recipes': [recipe.json() for recipe in RecipeModel.query.all()]}

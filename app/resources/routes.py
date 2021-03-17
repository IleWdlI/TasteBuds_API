from .recipes import Recipe, RecipeList, CreateRecipe
from .user import User, UserRegister, UserLogin


def initialize_routes(api):
    api.add_resource(Recipe, '/recipe/<int:recipe_id>')
    api.add_resource(RecipeList, '/recipes')
    api.add_resource(CreateRecipe, '/recipe')

    api.add_resource(User, '/user/<int:user_id>')
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')

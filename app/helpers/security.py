from ..models import RecipeModel, UserModel
import werkzeug


def check_access(user_id, recipe_id, *args):
    current_user = UserModel.query.get(user_id)
    recipe = RecipeModel.query.get(recipe_id)
    if not recipe or recipe.user_id != current_user.id:
        raise werkzeug.exceptions.BadRequest('cant find recipe')
    for arg in args:
        if not arg or arg.project_id != recipe.id:
            raise werkzeug.exceptions.BadRequest('cant find item')
    return current_user, recipe

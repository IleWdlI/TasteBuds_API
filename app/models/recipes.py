from app import db


class RecipeModel(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    recipe = db.Column(db.String)

    def __init__(self, title, recipe):
        self.title = title
        self.recipe = recipe

    def json(self):
        return {'title': self.title, 'recipe': self.recipe}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.remove(self)
        db.session.commit()


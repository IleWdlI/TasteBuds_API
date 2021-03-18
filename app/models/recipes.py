from app import db


class RecipeModel(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_type = db.Column(db.String(100))
    recipe_source = db.Column(db.String(100))
    link_to_recipe = db.Column(db.String(100))
    other_notes = db.Column(db.String(200))
    facebook = db.Column(db.Boolean)
    twitter = db.Column(db.Boolean)
    instagram = db.Column(db.Boolean)

    def json(self):
        print(vars(self))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.remove(self)
        db.session.commit()

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
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    store = db.relationship('UserModel')

    def json(self):
        return {
            "post_type": self.post_type,
            "recipe_source": self.recipe_source,
            "link_to_recipe": self.link_to_recipe,
            "other_notes": self.other_notes,
            "facebook": self.facebook,
            "twitter": self.twitter,
            "instagram": self.instagram,
            "user_id": self.user_id
        }

    def save_to_db(self, post_type=None, recipe_source=None, link_to_recipe=None, other_notes=None, facebook=False,
                   twitter=False, instagram=False):
        self.post_type = post_type
        self.recipe_source = recipe_source
        self.link_to_recipe = link_to_recipe
        self.other_notes = other_notes
        self.facebook = facebook
        self.twitter = twitter
        self.instagram = instagram

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

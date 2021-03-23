from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(256))
    name = db.Column(db.String(100))
    username = db.Column(db.String(100))
    foodie_bio = db.Column(db.String(256))
    allergy_diet = db.Column(db.String(256))
    cooking_lvl = db.Column(db.String(256))
    url = db.Column(db.String(256))
    facebook = db.Column(db.String(100))
    twitter = db.Column(db.String(100))
    instagram = db.Column(db.String(100))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        print(self)
        db.session.remove(self)
        db.session.commit()

    def json(self):
        return {
            'email': self.email,
            'name': self.name,
            'username': self.username,
            'foodie_bio': self.foodie_bio,
            'allergy_diet': self.allergy_diet,
            'cooking_lvl': self.cooking_lvl,
            'url': self.url,
            'facebook': self.facebook,
            'twitter': self.twitter,
            'instagram': self.instagram
        }

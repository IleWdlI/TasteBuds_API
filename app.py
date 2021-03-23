from app import create_app, admin, db
from flask_admin.contrib.sqla import ModelView
from app.models import UserModel

app = create_app()
admin.add_view(ModelView(UserModel, db.session))

if __name__ == '__main__':
    app.run()
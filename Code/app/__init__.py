from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager



db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='abcdef'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from app.routes.home_routes import home
    from app.routes.influencer_login_routes import influencer_login
    from app.routes.sponsor_login_routes import sponsor_login
    from app.routes.admin_login_routes import admin_login
    from app.routes.signup_routes import signup
    from app.routes.logout import logout_me

    app.register_blueprint(home)
    app.register_blueprint(influencer_login)
    app.register_blueprint(sponsor_login)
    app.register_blueprint(admin_login)
    app.register_blueprint(signup)
    app.register_blueprint(logout_me)


    
    from .models import User
    with app.app_context():
        create_database()

    login_manager = LoginManager()
    login_manager.login_view = 'influencer_login.influencer_login_page'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    
    return app



def create_database():
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print('Created Database!')

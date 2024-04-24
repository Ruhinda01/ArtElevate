#!/usr/bin/python3
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "artelevate.db"


def create_app():
    """Creates the application with flask adding CORS and database"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'This is the newest art gallery'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialising the database
    db.init_app(app)

    print("Before")

    # from app.routes.auth import auth
    # app.register_blueprint(auth, url_prefix='/')

    from app.routes.static import static
    from app.routes.auth import auth

    app.register_blueprint(static, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    print("After")

    # Enables cors for all routes to be created
    CORS(app)

    from app.user import User
    from app.artist import Artist
    from app.artwork import Artwork
    from app.artwork_category import ArtworkCategory
    from app.shopping_cart import ShoppingCart
    from app.category import Category
    from app.favorites import Favorites

    #creates database if it does not exist
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    """Creates the database if it does not exist"""
    # ensures i do not overwrite my existing data essential guarding me from data loss
    if not os.path.exists(os.path.join('app', DB_NAME)):
        with app.app_context():
            db.create_all()

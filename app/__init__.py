#!/usr/bin/python3
import os
from flask import Flask, send_file, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager, login_required
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

db = SQLAlchemy()
# DB_NAME = "artelevate.db"
photos = UploadSet('photos', IMAGES)

def create_app():
    """Creates the application with flask adding CORS and database"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artelevate.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOADED_PHOTOS_DEST'] = 'app/uploads'

    # Initialising the database
    db.init_app(app)

    print("Before")

    migrate = Migrate(app, db)

    # from app.routes.auth import auth
    # app.register_blueprint(auth, url_prefix='/')

    from app.routes.static import static
    from app.routes.auth import auth
    from app.routes.artist_profile import artist_profile
    from app.routes.artwork import artwork
    from app.routes.favorites import favorites
    from app.routes.shopping_cart import shopping_cart

    app.register_blueprint(static, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(artist_profile, url_prefix='/') 
    app.register_blueprint(artwork, url_prefix='/')
    app.register_blueprint(favorites, url_prefix='/')
    app.register_blueprint(shopping_cart, url_prefix='/')

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
    from app.forms import ArtistProfileForm
    from app.checkout import Checkout

    #creates database if it does not exist
    create_database(app)

    # configuring photo uploads
    configure_uploads(app, photos)

    @app.route('/uploads/<filename>')
    @login_required
    def serve_file(filename):
        """Serves the uploaded file"""
        print("Serving " + filename)
        # return send_file(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename))
        return send_from_directory('uploads', filename)

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
    with app.app_context():
        db.create_all()

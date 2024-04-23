#!/usr/bin/env python3
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

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

    # Enables cors for all routes to be created
    CORS(app)

    #creates database if it does not exist
    create_database(app)

    return app

def create_database(app):
    """Creates the database if it does not exist"""
    # ensures i do not overwrite my existing data essential guarding me from data loss
    if not os.path.exists(os.path.join('app', DB_NAME)):
        with app.app_context():
            db.create_all()

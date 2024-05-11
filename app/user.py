#!/usr/bin/python3
from . import db
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import Enum


# class UserRole(Enum):
#     """Defines the user roles"""
#     USER = 'user'
#     ARTIST = 'artist'

class User(db.Model, UserMixin):
    """
    This class defines the User table in my database.
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(Enum("user", "artist", name="UserRole"), nullable=False, default="user")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())

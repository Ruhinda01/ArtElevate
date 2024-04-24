#!/usr/bin/python3
import enum
from . import db
from flask_login import UserMixin


class UserRole(enum.Enum):
    """Defines the user roles"""
    USER = 'user'
    ARTIST = 'artist'

class User(db.Model, UserMixin):
    """
    This class defines the User table in my database.
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

#!/usr/bin/env python3
"""Artist class"""
from . import db


class Artist(db.Model):
    """
    Artist model that defines the artist database table
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bio = db.Column(db.Text)
    portfolio_link = db.Column(db.String(255), nullable=False)
    preferred_medium = db.Column(db.String(45), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    user = db.relationship('User', backref=db.backref('artist', uselist=False))

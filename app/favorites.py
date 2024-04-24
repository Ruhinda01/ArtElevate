#!/usr/bin/python3
"""This is the favorites class"""
from . import db


class Favorites(db.Model):
    """
    This favorites class describes the favorites
    database table
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    artwork_id = db.Column(db.Integer, db.ForeignKey('artwork.id'))
    user = db.relationship('User', backref='favorites', lazy=True)
    artwork = db.relationship('Artwork', backref='favorites', lazy=True)

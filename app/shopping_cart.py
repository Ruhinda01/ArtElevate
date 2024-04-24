#!/usr/bin/python3
"""Shopping cart class"""
from . import db


class ShoppingCart(db.Model):
    """
    Shopping cart model database table
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Integer)
    artwork_id = db.Column(db.Integer, db.ForeignKey('artwork.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    artwork = db.relationship('Artwork', backref='shopping_carts')
    user = db.relationship('User', backref='shopping_carts')

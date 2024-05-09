#!/usr/bin/python3
"""Checkout class"""
from . import db


class Checkout(db.Model):
    """
    Checkout model
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='checkout', lazy=True)
    phone_number = db.Column(db.String(45), nullable=False)
    street_address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state_province = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(45), nullable=False)

#!/usr/bin/python3
"""Artwork class"""
from . import db
from datetime import datetime


class Artwork(db.Model):
    """
    Defines artwork database table model
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    medium = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    width = db.Column(db.Numeric(10, 2), nullable=False)
    height = db.Column(db.Numeric(10, 2), nullable=False)
    depth = db.Column(db.Numeric(10, 2), nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    artist = db.relationship('Artist', backref='artworks')

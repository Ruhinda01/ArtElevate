#!/usr/bin/env python3
"""Artwork category class"""
from . import db


class ArtworkCategory(db.Model):
    """
    Contains the category of an artwork.
    """
    artwork_id = db.Column(db.Integer, db.ForeignKey('artwork.id'), primary_key=True, nullable=False)
    artwork = db.relationship('Artwork', backref='categories')
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), primary_key=True, nullable=False)
    category = db.relationship('Category', backref='artworks')

#!/usr/bin/python3
"""Category class"""
from . import db


class Category(db.Model):
    """
    Category model containing name and description
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

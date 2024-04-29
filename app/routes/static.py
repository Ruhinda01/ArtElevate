#!/usr/bin/python3
from flask import Blueprint, render_template
from app.artwork import Artwork
from app.category import Category


static = Blueprint('static', __name__)

@static.route('/')
def home():
    """Home route"""
    artworks = Artwork.query.all()
    categories = Category.query.all()
    return render_template('home.html', artworks=artworks, categories=categories)
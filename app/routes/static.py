#!/usr/bin/python3
from flask import Blueprint, render_template, current_app, redirect, url_for
from app.artwork import Artwork
from app.category import Category
from flask_login import current_user, login_required


static = Blueprint('static', __name__)


# @static.route('/')
# def landing():
#     """Landing route"""
#     return render_template('landing.html')


@static.route('/home')
@login_required
def home():
    """Home route"""
    artworks = Artwork.query.all()
    categories = Category.query.all()
    return render_template('home.html', artworks=artworks, categories=categories, user=current_user)

#!/usr/bin/python3
"""This is the favorites routes"""
from app import db
from app.favorites import Favorites
from app.artwork import Artwork
from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_required, current_user


favorites = Blueprint('favorites', __name__)


@favorites.route('/favorites', methods=['GET', 'POST'])
@login_required
def favorites_page():
    """Gets the user's favorite artworks"""
    artworks = Favorites.query.filter_by(user_id=current_user.id).all()
    return render_template('favorites.html', artworks=artworks, user=current_user)


@favorites.route('/favorites/add/<int:artwork_id>', methods=['GET', 'POST'])
@login_required
def add_favorite(artwork_id):
    """Adds an artwork to the user's favorites"""
    artwork = Artwork.query.filter_by(id=artwork_id).first()
    if artwork:
        fav = Favorites(user_id=current_user.id, artwork_id=artwork_id)
        db.session.add(fav)
        db.session.commit()
        flash('Artwork added to favorites', category='success')
    return redirect(url_for('static.home'))


@favorites.route('/favorites/remove/<int:artwork_id>', methods=['GET', 'POST'])
@login_required
def remove_favorite(artwork_id):
    """Removes an artwork from the user's favorites"""
    fav = Favorites.query.filter_by(user_id=current_user.id, artwork_id=artwork_id).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
        flash('Artwork removed from favorites', category='success')
    return redirect(url_for('static.home'))


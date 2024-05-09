#!/usr/bin/python3
"""This is the artist profile routes"""
import os
import random
from app import db
from datetime import datetime
from flask import render_template, Blueprint, flash, redirect, url_for, request, current_app, send_from_directory
from flask_login import login_required, current_user
from app.forms import ArtistProfileForm
from app.artist import Artist
from app.artwork import Artwork
 

artist_profile = Blueprint('artist_profile', __name__)


@artist_profile.route('/profile')
@login_required
def profile():
    """Gets the artist profile"""
    if current_user.role == 'artist':
        artist = Artist.query.filter_by(user_id=current_user.id).first()
        artworks = Artwork.query.filter_by(artist_id=artist.id).all()
        # for artwork in artworks:
        #     print(artwork.image_url)
        profile_images_dir = os.path.join(current_app.root_path, 'static', 'profile_images')
        profile_images = os.listdir(profile_images_dir)
        if profile_images:
            random_image = random.choice(profile_images)
            avatars_url = url_for('static', filename='profile_images/' + random_image)
            return render_template('artist_profile.html', artist=artist, user=current_user,
                                   artworks=artworks, avatars_url=avatars_url)
        else:
            flash('No profile image found', category='error')
    flash('You are not an artist', category='error')
    return redirect(url_for('static.home'))

@artist_profile.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """Allows only the artist to edit their profile"""
    if current_user.role == 'artist':
        artist = Artist.query.filter_by(user_id=current_user.id).first()
        form = ArtistProfileForm(request.form, obj=artist)
        if request.method == 'POST' and form.validate():
            # updates the artist profile with the information from the form
            form.populate_obj(artist)
            # change the update time
            current_user.updated_at = datetime.utcnow()
            db.session.commit()
            flash('Profile updated successfully!', category='success')
            return redirect(url_for('artist_profile.profile'))
        return render_template('edit_profile.html', form=form, user=current_user)
    flash('You are not an artist', category='error')
    return render_template('home.html', user=current_user)


@artist_profile.route('/profile/<int:artist_id>')
@login_required
def view_profile(artist_id):
    """View artist profile route"""
    artist = Artist.query.get_or_404(artist_id)
    artworks = Artwork.query.filter_by(artist_id=artist.id).all()
    profile_images_dir = os.path.join(current_app.root_path, 'static', 'profile_images')
    profile_images = os.listdir(profile_images_dir)
    if profile_images:
        random_image = random.choice(profile_images)
        avatars_url = url_for('static', filename='profile_images/' + random_image)
    return render_template('view_profile.html', artist=artist, artworks=artworks, avatars_url=avatars_url, user=current_user)

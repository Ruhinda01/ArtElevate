#!/usr/bin/python3
"""This is the artwork routes"""
import os
from app import db
from app import photos
from datetime import datetime
from flask import Blueprint, request, redirect, url_for, flash, render_template, current_app
from flask import send_from_directory
from flask_login import login_required, current_user
from app.forms import ArtworkForm, UpdateArtworkForm
from werkzeug.utils import secure_filename
from app.artwork import Artwork


artwork = Blueprint('artwork', __name__)


# ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']


# def allowed_file(filename):
#     """Checks if the file extension is allowed"""
#     return '.' in filename and \
#         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@artwork.route('/artwork/<int:artwork_id>')
@login_required
def artwork_details(artwork_id):
    """Artwork details route"""
    artwork = Artwork.query.get_or_404(artwork_id)
    return render_template('artwork_details.html', artwork=artwork, user=current_user)

@artwork.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_artwork():
    """Uploading artwork route"""
    form = ArtworkForm()
    file_url = None
    filename = None
    if request.method == 'POST':
            if form.validate_on_submit():
                 created_at = datetime.utcnow()
                 updated_at = created_at
                 artwork = Artwork(title=form.title.data, 
                                   description=form.description.data,
                                   medium=form.medium.data,
                                   price=form.price.data,
                                   width=form.width.data,
                                   height=form.height.data,
                                   depth=form.depth.data, 
                                   unit=form.unit.data,
                                   created_at=created_at,
                                   updated_at=updated_at,
                                   artist_id=current_user.artist.id)
                 if form.photo.data:
                      filename = photos.save(form.photo.data)
                      file_url = url_for('serve_file', filename=filename)
                      artwork.image_url = file_url
                      print(file_url)
                 db.session.add(artwork)
                 db.session.commit()
                 flash('Artwork uploaded successfully', category='success')
                 return redirect(url_for('artist_profile.profile'))
    return render_template('upload_artwork.html', form=form, file_url=file_url,
                           filename=filename, user=current_user)

@artwork.route('/delete/<int:artwork_id>', methods=['GET', 'POST'])
@login_required
def delete_artwork(artwork_id):
    """Delete artwork route"""
    # artwork = Artwork.query.filter_by(id=artwork_id).first()
    artwork = Artwork.query.get_or_404(artwork_id)

    if artwork.image_url:
         filename = os.path.basename(artwork.image_url)
         file_path = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], filename)
         if os.path.exists(file_path):
              os.remove(file_path)
    
    db.session.delete(artwork)
    db.session.commit()
    flash('Artwork deleted successfully', category='success')
    return redirect(url_for('artist_profile.profile'))

@artwork.route('/update/<int:artwork_id>', methods=['GET', 'POST'])
@login_required
def update_artwork(artwork_id):
    """Update artwork route"""
    artwork = Artwork.query.filter_by(id=artwork_id).first_or_404()
    form = UpdateArtworkForm(obj=artwork)
    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(artwork)
        db.session.commit()
        flash('Artwork updated successfully', category='success')
        return redirect(url_for('artist_profile.profile'))
    return render_template('update_artwork.html', form=form,
                           artwork=artwork, user=current_user)


@artwork.errorhandler(404)
def page_not_found(error):
    """Page not found error handler"""
    return "Invalid route", 404


#!/usr/bin/python3
"""This is the forms class"""
import pycountry
from app import photos
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, FileField, SubmitField, DecimalField, SelectField
from wtforms.validators import DataRequired, URL, InputRequired, NumberRange
from flask_wtf.file import FileAllowed, FileRequired


country_choices = [(country.alpha_2, country.name) for country in pycountry.countries]

class ArtistProfileForm(FlaskForm):
    """Artist profile form."""
    bio = TextAreaField('Bio', validators=[InputRequired()])
    portfolio_link = StringField('Portfolio Link', validators=[DataRequired(), URL()])
    preferred_medium = TextAreaField('Preferred Medium', validators=[DataRequired()])


class ArtworkForm(FlaskForm):
    """Artwork form."""
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    medium = StringField('Medium', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)])
    width = DecimalField('Width', validators=[DataRequired(), NumberRange(min=0)])
    height = DecimalField('Height', validators=[DataRequired(), NumberRange(min=0)])
    depth = DecimalField('Depth', validators=[DataRequired(), NumberRange(min=0)])
    unit = StringField('Unit', validators=[DataRequired()])
    photo = FileField(validators=[FileAllowed(photos, 'Images only!'),
                                  FileRequired('File Field should not be empty!')])
    submit = SubmitField('Upload')


class UpdateArtworkForm(FlaskForm):
    """Update artwork form."""
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    medium = StringField('Medium', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)])
    width = DecimalField('Width', validators=[DataRequired(), NumberRange(min=0)])
    height = DecimalField('Height', validators=[DataRequired(), NumberRange(min=0)])
    depth = DecimalField('Depth', validators=[DataRequired(), NumberRange(min=0)])
    unit = StringField('Unit', validators=[DataRequired()])
    submit = SubmitField('Update')


class CheckoutForm(FlaskForm):
    """Checkout form."""
    street_address = StringField('Street Address', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state_province = StringField('State/Province', validators=[DataRequired()])
    country = SelectField('Country', choices=country_choices, validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[DataRequired()])
    submit = SubmitField('Submit')

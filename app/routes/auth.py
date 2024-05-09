#!/usr/bin/python3
"""This is the user authentication routes: login, logout, register"""
import re
from flask import Blueprint, request, flash, redirect, url_for, render_template
from app.user import User
from app.artist import Artist
from app import db
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Logs in a registered user into the application"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # check for user existence in database
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('static.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist', category='error')
    return render_template('login.html', user=current_user)
    # return '<h1>login</h1>'

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Registers new users on to the web application"""
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        role = request.form.get('role')

        print("Role from the form: ", role)

        # Need to check if all fields are filled
        if not all([first_name, last_name, user_name,
                    email, password1, password2, role]):
            flash('All fields are required', category='error')
            return redirect(request.url)
        
        
        # check if the password length is greater than 8 characters
        if len(password1) < 8:
            flash('Password must be at least 8 characters long', category='error')
            return redirect(request.url)
        
        # check if password1 is the same as password2
        if password1 != password2:
            flash('Passwords do not match', category='error')
            return redirect(request.url)
        
        # Hash the password
        hashed_passwd = generate_password_hash(password1)
        
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        # check the email address format
        if not (re.fullmatch(pat, email)):
            flash('Invalid email address', category='error')
            return redirect(request.url)
        
        # Check if the email already exists
        if User.query.filter_by(email=email).first():
            flash('Email already exists', category='error')
            return redirect(request.url)
        
        # check if the username already exists
        if User.query.filter_by(user_name=user_name).first():
            flash('Username already exists', category='error')
            return redirect(request.url)
        
        # try:
        #     user_role = UserRole[role]
        #     print("user_role: ", user_role)
        # except KeyError:
        #     flash('Invalid role selected')
        #     return redirect(request.url)
        
        if role == 'artist':
            bio = request.form.get('bio')
            portfolio_link = request.form.get('portfolio_link')
            preferred_medium = request.form.get('preferred_medium')

            # Need to check if all the fields are filled
            if not all([bio, portfolio_link, preferred_medium]):
                flash('All fields are required')
                return redirect(request.url)
            
            # created_at datetime and updated_at
            created_at = datetime.utcnow()
            updated_at = created_at
            # Create the user
            user = User(first_name=first_name, last_name=last_name,
                        user_name=user_name, email=email,
                        password=hashed_passwd, role='artist',
                        created_at=created_at, updated_at=updated_at)
            # Create the artist
            artist = Artist(bio=bio, portfolio_link=portfolio_link,
                            preferred_medium=preferred_medium, user=user)
            db.session.add(user)
            db.session.add(artist)
        else:
            # created_at datetime and updated_at
            created_at = datetime.utcnow()
            updated_at = created_at
            # Create the user
            user = User(first_name=first_name, last_name=last_name,
                        user_name=user_name, email=email,
                        password=hashed_passwd, role='user',
                        created_at=created_at, updated_at=updated_at)
            db.session.add(user)
        
        # Commit all the changes
        db.session.commit()
        # login the user
        login_user(user, remember=True)
        # Redirect user or artist to the home page
        flash('Account created!', category='success')
        return redirect(url_for('static.home'))
    
    return render_template('register.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    """Logs out the user"""
    logout_user()
    return redirect(url_for('auth.login'))

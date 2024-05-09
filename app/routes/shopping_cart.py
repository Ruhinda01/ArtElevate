#!/usr/bin/python3
"""Shopping cart routes"""
from app import db
from app.shopping_cart import ShoppingCart
from app.artwork import Artwork
from app.checkout import Checkout
from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from app.forms import CheckoutForm


shopping_cart = Blueprint('shopping_cart', __name__)


@shopping_cart.route('/shopping_cart', methods=['GET', 'POST'])
@login_required
def shopping_cart_page():
    """Gets the user's shopping cart"""
    cart_items = ShoppingCart.query.filter_by(user_id=current_user.id).all()
    total_price = sum([cart_item.total_price for cart_item in cart_items])
    return render_template('shopping_cart.html', cart_items=cart_items, total_price=total_price, user=current_user)


@shopping_cart.route('/shopping_cart/add/<int:artwork_id>', methods=['GET', 'POST'])
@login_required
def add_shopping_cart(artwork_id):
    """Adds an artwork to the user's shopping cart"""
    artwork = Artwork.query.filter_by(id=artwork_id).first()
    if artwork:
        # check if item is already in the cart
        existing_cart_item = ShoppingCart.query.filter_by(user_id=current_user.id, artwork_id=artwork_id).first()
        if existing_cart_item:
            # if the artwork already exists in the cart, increment the quantity
            existing_cart_item.quantity += 1
            existing_cart_item.total_price = existing_cart_item.quantity * artwork.price
        else:
            # if the item is not in the cart, add it
            cart = ShoppingCart(user_id=current_user.id, artwork_id=artwork_id, quantity=1)
            cart.total_price = cart.quantity * artwork.price
            db.session.add(cart)
        db.session.commit()
        flash('Artwork added to shopping cart', category='success')
    return redirect(url_for('static.home'))


@shopping_cart.route('/shopping_cart/update_quantity/<int:cart_id>', methods=['GET', 'POST'])
@login_required
def update_quantity(cart_id):
    """Updates the quantity of an artwork in the user's shopping cart"""
    cart = ShoppingCart.query.filter_by(id=cart_id).first()
    new_quantity= int(request.form.get('quantity'))
    if new_quantity > 0:
        cart.quantity = new_quantity
        cart.total_price = new_quantity * cart.artwork.price
        db.session.commit()
        flash('Artwork quantity updated', category='success')
    else:
        db.session.delete(cart)
        db.session.commit()
        flash('Artwork removed from shopping cart', category='success')
    return redirect(url_for('shopping_cart.shopping_cart_page'))

@shopping_cart.route('/shopping_cart/remove/<int:artwork_id>', methods=['GET', 'POST'])
@login_required
def remove_shopping_cart(artwork_id):
    """Removes an artwork from the user's shopping cart"""
    cart = ShoppingCart.query.filter_by(user_id=current_user.id, artwork_id=artwork_id).first()
    if cart:
        db.session.delete(cart)
        db.session.commit()
        flash('Artwork removed from shopping cart', category='success')
    return redirect(url_for('static.home'))


@shopping_cart.route('/shopping_cart/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    """Checks out the user's shopping cart"""
    form = CheckoutForm()
    if request.method == 'POST' and form.validate_on_submit():
        street_address = form.street_address.data
        city = form.city.data
        state_province = form.state_province.data
        country = form.country.data
        phone_number = form.phone_number.data
        postal_code = form.postal_code.data
        checkout = Checkout(user_id=current_user.id, phone_number=phone_number,
                            street_address=street_address, city=city,
                            state_province=state_province, country=country,
                            postal_code=postal_code)
        db.session.add(checkout)
        db.session.commit()
        flash('Checkout information saved successful', category='success')
        return redirect(request.url)
    cart_items = ShoppingCart.query.filter_by(user_id=current_user.id).all()
    total_price = sum([cart_item.total_price for cart_item in cart_items])
    return render_template('checkout.html', form=form, cart_items=cart_items, total_price=total_price, user=current_user)


# @shopping_cart.route('/shopping_cart/payment', methods=['GET', 'POST'])
# @login_required
# def payment():
#     """Processes the payment for the user's shopping cart"""

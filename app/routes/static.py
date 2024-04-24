#!/usr/bin/python3
from flask import Blueprint


static = Blueprint('static', __name__)

@static.route('/')
def home():
    return 'hello'
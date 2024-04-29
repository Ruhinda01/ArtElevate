#!/usr/bin/python3
"""This is the artwork routes"""
from app import db
from flask import Blueprint, request, render_template
from app.artwork import Artwork


artwork = Blueprint('artwork', __name__)



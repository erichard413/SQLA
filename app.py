"""Demo app using SQLAlchemy."""

from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'

with app.app_context():
    db = SQLAlchemy()
    db.app = app
    db.init_app(app)

app.config['SECRET_KEY'] = "chickensareok"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('home.html')


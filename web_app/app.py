
# app.py

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

SECRET_KEY = "TODO: super secret"

def create_app():

    app = Flask(__name__)

    #
    # configuring the database
    #
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///web_app_11.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/mjr/Desktop/web-app-inclass-11/web_app_12.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = SECRET_KEY # allows us to use flash messaging
    db.init_app(app)
    migrate.init_app(app, db)

    #
    # registering routes:
    #
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)

    return app

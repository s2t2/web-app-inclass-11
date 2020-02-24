
# app.py

from flask import Flask, jsonify, render_template, request

from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

def create_app():

    app = Flask(__name__)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)

    return app

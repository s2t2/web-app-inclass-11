from flask import Blueprint, render_template

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)
    return f"TODO GET TWEETS AND INFO FOR {screen_name}"

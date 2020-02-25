from flask import Blueprint, render_template

from web_app.twitter_service import twitter_api

twitter_api_client = twitter_api()

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)
    twitter_user = twitter_api_client.get_user(screen_name)
    return render_template("user.html", user=twitter_user)

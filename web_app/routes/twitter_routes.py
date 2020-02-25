from flask import Blueprint, render_template, jsonify

from web_app.models import db, User, Tweet
from web_app.twitter_service import twitter_api

twitter_api_client = twitter_api()

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users")
@twitter_routes.route("/users.json")
def list_users():
    users=[]
    user_records = User.query.all()
    for user in user_records:
        print(user)
        d = user.__dict__
        del d["_sa_instance_state"]
        users.append(d)
    return jsonify(users)


@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)
    twitter_user = twitter_api_client.get_user(screen_name)

    # find or create database user:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    db.session.add(db_user)
    db.session.commit()

    #breakpoint()

    # todo: store user info in the database
    #statuses = client.user_timeline(screen_name, tweet_mode="extended", count=50, exclude_replies=True, include_rts=False)
    #for status in statuses:
    #    print(status)
    #    print("----")

    return render_template("user.html", user=db_user)

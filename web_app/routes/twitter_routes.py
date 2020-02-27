from flask import Blueprint, render_template, jsonify

from web_app.models import db, User, Tweet, parse_records
from web_app.twitter_service import twitter_api
from web_app.basilica_service import connection as basilica_client

twitter_api_client = twitter_api()

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users")
@twitter_routes.route("/users.json")
def list_users():
    db_users = User.query.all()
    users_response = parse_records(db_users)
    return jsonify(users_response)

@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)

    try:

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

        statuses = twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=100, exclude_replies=True, include_rts=False)
        print("STATUS COUNT:", len(statuses))
        all_tweet_texts = [status.full_text for status in statuses]
        embeddings = list(basilica_client.embed_sentences(all_tweet_texts, model="twitter"))

        # TODO: explore using the zip() function maybe...
        counter = 0
        for status in statuses:
            print(status.full_text)
            print("----")
            #print(dir(status))

            # Find or create database tweet:
            db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
            db_tweet.user_id = status.author.id # or db_user.id
            db_tweet.full_text = status.full_text
            #embedding = basilica_client.embed_sentence(status.full_text, model="twitter") # todo: prefer to make a single request to basilica with all the tweet texts, instead of a request per tweet
            embedding = embeddings[counter]
            print(len(embedding))
            db_tweet.embedding = embedding
            db.session.add(db_tweet)
            counter+=1
        db.session.commit()

        return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets

    except Exception as e:
        print(e)
        return jsonify({"message": "OOPS Something went wrong", "details": str(e)})

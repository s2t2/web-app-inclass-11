
from flask import Blueprint, request, jsonify

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

from web_app.models import User, Tweet

stats_routes = Blueprint("stats_routes", __name__)

@stats_routes.route("/iris")
def iris():
    X, y = load_iris(return_X_y=True)
    classifier = LogisticRegression(
        random_state=0,
        solver="lbfgs",
        multi_class="multinomial"
    ).fit(X, y)

    result = classifier.predict(X[:2, :])
    return str(result)

@stats_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICTING...")
    print("FORM DATA:", dict(request.form))
    #> {'screen_name_a': 'elonmusk', 'screen_name_b': 'chrisalbon', 'tweet_text': 'Example tweet text here'}
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]

    print("FETCHING TWEETS FROM THE DATABASE...")
    # todo: wrap in a try block in case the user's don't exist in the database
    user_a = User.query.filter(User.screen_name == screen_name_a).one()
    user_b = User.query.filter(User.screen_name == screen_name_b).one()
    user_a_tweets = user_a.tweets
    user_b_tweets = user_b.tweets
    #user_a_embeddings = [tweet.embedding for tweet in user_a_tweets]
    #user_b_embeddings = [tweet.embedding for tweet in user_b_tweets]

    embeddings = []
    labels = []
    for tweet in user_a_tweets:
        labels.append(user_a.screen_name)
        embeddings.append(tweet.embedding)

    for tweet in user_b_tweets:
        labels.append(user_b.screen_name)
        embeddings.append(tweet.embedding)

    print("TRAINING THE MODEL...")
    #embeddings = []
    #labels = []
    classifier = LogisticRegression()
    classifier.fit(embeddings, labels)

    breakpoint()

    result_a = classifier.predict([user_a_tweets[0].embedding])
    result_b = classifier.predict([user_b_tweets[0].embedding])


    return jsonify({"message": "RESULTS (TODO)"})

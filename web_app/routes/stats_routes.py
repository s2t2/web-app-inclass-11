
from flask import Blueprint, request, jsonify

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

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
    return jsonify({"message": "RESULTS (TODO)"})

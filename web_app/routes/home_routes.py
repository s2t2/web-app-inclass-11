
from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    #x = 2 + 2
    #return f"Hello World! {x}"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    return "About me"

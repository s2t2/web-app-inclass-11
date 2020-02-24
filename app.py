


# app.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    x = 2 + 2
    return f"Hello World! {x}"

@app.route("/about")
def about():
    return "About me"

@app.route("/books")
@app.route("/books.json")
def list_books():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return jsonify(books)

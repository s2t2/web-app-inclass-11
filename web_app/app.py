
# app.py

from flask import Flask, jsonify, render_template, request

def create_app():

    app = Flask(__name__)

    @app.route("/")
    def index():
        x = 2 + 2
        return f"Hello World! {x}"

    @app.route("/about")
    def about():
        return "About me"

    @app.route("/books.json")
    def list_books():
        books = [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
        return jsonify(books)

    @app.route("/books")
    def list_books_for_humans():
        books = [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
        return render_template("books.html", message="Here's some books", books=books)

    @app.route("/books/new")
    def new_book():
        return render_template("new_book.html")

    @app.route("/books/create", methods=["POST"])
    def create_book():
        print("FORM DATA:", dict(request.form))
        # todo: store in database
        return jsonify({
            "message": "BOOK CREATED OK (TODO)",
            "book": dict(request.form)
        })








    return app

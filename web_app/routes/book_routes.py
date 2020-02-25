
from flask import Blueprint, jsonify, request, render_template, flash, redirect

from web_app.models import db, Book

book_routes = Blueprint("book_routes", __name__)

def get_books_from_db():
    #return [
    #    {"id": 1, "title": "Book 1"},
    #    {"id": 2, "title": "Book 2"},
    #    {"id": 3, "title": "Book 3"},
    #]
    books =[]
    book_records = Book.query.all()
    for b in book_records:
        print(b)
        d = b.__dict__
        del d["_sa_instance_state"]
        books.append(d)
    return books

@book_routes.route("/books.json")
def list_books():
    books = get_books_from_db()
    return jsonify(books)

@book_routes.route("/books")
def list_books_for_humans():
    books = get_books_from_db()
    return render_template("books.html", message="Here's some books", books=books)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))

    new_book = Book(title=request.form["title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()

    #return jsonify({
    #    "message": "BOOK CREATED OK",
    #    "book": dict(request.form)
    #})
    flash(f"Book '{new_book.title}' created successfully!", "success")
    return redirect(f"/books")

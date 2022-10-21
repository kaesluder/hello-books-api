from app.models.books import Book
from flask import Blueprint, jsonify

hello_world_bp = Blueprint("hello_world_bp", __name__)


@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    return "Hello, World!"


@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"],
    }


@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"],
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body


test_books = [
    Book(8, "Die Vol. 4", "A graphic novel"),
    Book(23, "Gender Queer, A Memoir", "A graphic novel"),
    Book(22, "Nona the Ninth", "A SF novel"),
]

books_bp = Blueprint("books_bp", __name__)


@books_bp.route("/books", methods=["GET"])
def test_book_list():
    books_response = [b.to_dict() for b in test_books]
    return jsonify(books_response)

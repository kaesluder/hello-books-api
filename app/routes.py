from app.models.books import Book
from flask import Blueprint, jsonify, abort, make_response

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

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message": f"{book_id} is not valid"}, 400))

    for book in test_books:
        if book.id == book_id:
            return jsonify(book.to_dict())
    abort(make_response({"message": f"{book_id} is not found"}, 404))


@books_bp.route("/books/<book_id>", methods=["GET"])
def single_book_request(book_id):
    result_book = validate_book(book_id)
    return result_book 
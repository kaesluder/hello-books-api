from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request


books_bp = Blueprint("books", __name__, url_prefix="/books")

#refactor to use separate routes for get and post.

@books_bp.route("", methods=["GET"])
def handle_books_get():
    title_query = request.args.get("title")
    if title_query: 
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()

    books_response = []
    for book in books:
        books_response.append(book.to_dict())
    return jsonify(books_response)

@books_bp.route("", methods=["POST"])
def handle_books_post():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} successfully created"), 201)

def validate_model(cls, id):
    try:
        id = int(id)
    except:
        abort(make_response(jsonify({"message":f"book {id} invalid"}), 400))

    record = cls.query.get(id)

    if not record:
        abort(make_response(jsonify({"message":f"book {id} not found"}), 404))

    return record

@books_bp.route("/<book_id>", methods=["GET"])
def handle_single_book(book_id):
    book = validate_model(Book, book_id)
    return book.to_dict()


@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_model(Book, book_id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(jsonify(f"Book #{book.id} successfully updated"))

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_model(Book, book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(jsonify(f"Book #{book.id} successfully deleted"))
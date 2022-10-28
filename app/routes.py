from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response


books_bp = Blueprint("books_bp", __name__)


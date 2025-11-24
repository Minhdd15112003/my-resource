from flask import Blueprint

from app.books.service import insert_book, get_all_books

books = Blueprint("books", __name__, url_prefix="/books")


@books.route("/", methods=['GET'])
def list():
    return get_all_books()


@books.route("/", methods=["POST"])
def insert():
    return insert_book()

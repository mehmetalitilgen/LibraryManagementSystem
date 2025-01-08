from flask import Blueprint, request, jsonify
from services.book_service.services.book_service import get_book, create_book, update_book, delete_book

book_blueprint = Blueprint("book", __name__)


@book_blueprint.route("/book/<int:book_id>", methods=["GET"])
def get_book_endpoint(book_id):
    book = get_book(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404


@book_blueprint.route("/book", methods=["POST"])
def create_book_endpoint():
    data = request.get_json()
    print("data",data)

    if not data:
        return jsonify({"error": "Bad Request", "message": "Request body is missing"}), 400
    book = create_book(data)
    return jsonify(book), 201


@book_blueprint.route("/book/<int:book_id>", methods=["PUT"])
def update_user_endpoint(book_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request", "message": "Request body is missing"}), 400

    updated_book = update_book(book_id, data)
    if updated_book:
        return jsonify(updated_book), 200
    return jsonify({"error": "User not found"}), 404


@book_blueprint.route("/book/<int:book_id>", methods=["DELETE"])
def delete_user_endpoint(book_id):
    if delete_book(book_id):
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "User not found"}), 404

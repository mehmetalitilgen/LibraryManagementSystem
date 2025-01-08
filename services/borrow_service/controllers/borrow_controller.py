from flask import Blueprint, request, jsonify
from services.borrow_service.services.borrow_service import get_borrow_record, create_borrow_record, update_borrow_record, delete_borrow_record

borrow_blueprint = Blueprint("borrow", __name__)

@borrow_blueprint.route("/borrow/<int:borrow_id>", methods=["GET"])
def get_borrow_record_endpoint(borrow_id):
    borrow_record = get_borrow_record(borrow_id)
    if borrow_record:
        return jsonify(borrow_record), 200
    return jsonify({"error": "Borrow record not found"}), 404

@borrow_blueprint.route("/borrow", methods=["POST"])
def create_borrow_record_endpoint():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request", "message": "Request body is missing"}), 400
    borrow_record = create_borrow_record(data)
    return jsonify(borrow_record), 201

@borrow_blueprint.route("/borrow/<int:borrow_id>", methods=["PUT"])
def update_borrow_record_endpoint(borrow_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request", "message": "Request body is missing"}), 400

    updated_borrow_record = update_borrow_record(borrow_id, data)
    if updated_borrow_record:
        return jsonify(updated_borrow_record), 200
    return jsonify({"error": "Borrow record not found"}), 404

@borrow_blueprint.route("/borrow/<int:borrow_id>", methods=["DELETE"])
def delete_borrow_record_endpoint(borrow_id):
    if delete_borrow_record(borrow_id):
        return jsonify({"message": "Borrow record deleted successfully"}), 200
    return jsonify({"error": "Borrow record not found"}), 404

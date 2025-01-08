from flask import Blueprint,request,jsonify
from services.user_service.services.user_service import get_user, create_user , update_user ,delete_user

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/user/<int:user_id>", methods=["GET"])
def get_user_endpoint(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@user_blueprint.route("/user", methods=["POST"])
def create_user_endpoint():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request", "message": "Request body is missing"}), 400
    user = create_user(data)
    return jsonify(user), 201



@user_blueprint.route("/user/<int:user_id>", methods=["PUT"])
def update_user_endpoint(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Bad Request", "message": "Request body is missing"}), 400

    updated_user = update_user(user_id, data)
    if updated_user:
        return jsonify(updated_user), 200
    return jsonify({"error": "User not found"}), 404

@user_blueprint.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user_endpoint(user_id):
    if delete_user(user_id):
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "User not found"}), 404

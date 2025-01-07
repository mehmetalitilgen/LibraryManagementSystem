from flask import Blueprint,request,jsonify
from config import Config


from middlewares.auth import login_user
from middlewares.cache_manager import cache_response
from load_balancer.round_robin import RoundRobinBalancer

gateway = Blueprint("gateway",__name__)

user_service_instances = Config.USER_SERVICE_INSTANCES.split(",")
book_service_instances = Config.BOOK_SERVICE_INSTANCES.split(",")

user_service_balancer = RoundRobinBalancer(user_service_instances)
book_service_balancer = RoundRobinBalancer(book_service_instances)

@gateway.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type", "message": "Content-Type must be application/json"}), 415

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Bad Request", "message": "Invalid JSON format"}), 400

    if not data:
        return jsonify({"error": "Bad Request", "message": "Empty request body"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Bad Request", "message": "Username and password are required"}), 400

    if username == "admin" and password == "password":
        return login_user(username)
    return jsonify({"error": "Invalid credentials"}), 401


@gateway.route("/health-check", methods=["GET"])
def health_check():
    print("mememo")
    return jsonify({"status": "API Gateway is healthy!"}), 200


def register_routes(app):
    app.register_blueprint(gateway)
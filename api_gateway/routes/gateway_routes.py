from flask import Blueprint,request,jsonify
from api_gateway.config import Config
import requests


from api_gateway.middlewares.auth import login_user
from api_gateway.middlewares.cache_manager import cache_response
from api_gateway.load_balancer.round_robin import RoundRobinBalancer

gateway = Blueprint("gateway",__name__)

user_service_instances = Config.USER_SERVICE_INSTANCES.split(",")
book_service_instances = Config.BOOK_SERVICE_INSTANCES.split(",")
borrow_service_instances = Config.BORROW_SERVICE_INSTANCES.split(",")

user_service_balancer = RoundRobinBalancer(user_service_instances)
book_service_balancer = RoundRobinBalancer(book_service_instances)
borrow_service_balancer = RoundRobinBalancer(borrow_service_instances)


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


def forward_request(service_url, endpoint_path):
    """
    Helper function to forward requests to services.
    """
    try:
        full_url = f"{service_url}{endpoint_path}"
        if request.method == "GET":
            response = requests.get(full_url, params=request.args)
        elif request.method == "POST":
            response = requests.post(full_url, json=request.get_json())
        elif request.method == "PUT":
            response = requests.put(full_url, json=request.get_json())
        elif request.method == "DELETE":
            response = requests.delete(full_url)
        else:
            return jsonify({"error": "Method not allowed"}), 405

        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Service Unavailable", "message": str(e)}), 503


@gateway.route("/user-service/<path:endpoint>", methods=["GET", "POST", "PUT", "DELETE"])
def user_service(endpoint):
    service_url = user_service_balancer.get_next_service()
    return forward_request(service_url, f"/api/user/{endpoint}")


@gateway.route("/book-service/<path:endpoint>", methods=["GET", "POST", "PUT", "DELETE"])
def book_service(endpoint):
    service_url = book_service_balancer.get_next_service()
    return forward_request(service_url, f"/api/book/{endpoint}")


@gateway.route("/borrow-service/<path:endpoint>", methods=["GET", "POST", "PUT", "DELETE"])
def borrow_service(endpoint):
    service_url = borrow_service_balancer.get_next_service()
    return forward_request(service_url, f"/api/borrow/{endpoint}")



@gateway.route("/health-check", methods=["GET"])
def health_check():
    return jsonify({"status": "API Gateway is healthy!"}), 200


def register_routes(app):
    app.register_blueprint(gateway)
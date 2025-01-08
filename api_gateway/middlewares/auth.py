from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, verify_jwt_in_request


def login_user(username):
    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    return jsonify(access_token=access_token, refresh_token=refresh_token)

def require_jwt():
    open_routes = ["/login","/health-check"]
    print(request.path,"asdsa")
    if request.path not in open_routes:
        try:
            verify_jwt_in_request()
        except Exception as e:
            return jsonify({"error": "Unauthorized", "message": str(e)}), 401

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from middlewares.auth import require_jwt
from middlewares.logger import log_middleware
from middlewares.rate_limiter import setup_rate_limiter

from routes.gateway_routes import register_routes


app = Flask(__name__)
app.config.from_object("config.Config")

setup_rate_limiter(app)

jwt = JWTManager(app)


@app.before_request
def before_request():
    auth_response = require_jwt()
    if auth_response:
        return auth_response


@app.after_request
def after_request(response):
    return log_middleware(response)

register_routes(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)

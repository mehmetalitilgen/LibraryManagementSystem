import redis
import json
from flask import request, jsonify
from functools import wraps
from config import Config

# Redis connection using config values
redis_client = redis.StrictRedis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=Config.REDIS_DB,
    decode_responses=True
)

def cache_response(timeout=300):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{request.path}"
            cached_response = redis_client.get(key)
            if cached_response:
                return jsonify(json.loads(cached_response))
            response = func(*args, **kwargs)
            redis_client.setex(key, timeout, json.dumps(response.get_json()))
            return response
        return wrapper
    return decorator

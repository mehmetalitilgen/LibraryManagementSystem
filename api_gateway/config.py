import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_jwt_secret")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600))
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB = int(os.getenv("REDIS_DB", 0))
    RATE_LIMIT = os.getenv("RATE_LIMIT", "100 per hour")
    LOAD_BALANCER_TYPE = os.getenv("LOAD_BALANCER_TYPE", "round_robin")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    USER_SERVICE_INSTANCES = os.getenv("USER_SERVICE_INSTANCES", "http://user-service-1:5000,http://user-service-2:5000")
    BOOK_SERVICE_INSTANCES = os.getenv("BOOK_SERVICE_INSTANCES", "http://book-service-1:5000,http://book-service-2:5000")

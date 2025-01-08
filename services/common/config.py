import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy



load_dotenv()

db = SQLAlchemy()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "postgresql://user:password@localhost:5432/library_management_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB = int(os.getenv("REDIS_DB", 0))
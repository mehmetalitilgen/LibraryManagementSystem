from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config
import redis

def setup_rate_limiter(app):
    try:
        limiter = Limiter(
            get_remote_address,
            app=app,
            default_limits=[Config.RATE_LIMIT],
            storage_uri=f"redis://{Config.REDIS_HOST}:{Config.REDIS_PORT}/{Config.REDIS_DB}"
        )
        limiter.init_app(app)
        return limiter
    except redis.ConnectionError:
        app.logger.error("Redis connection failed. Rate limiting disabled.")





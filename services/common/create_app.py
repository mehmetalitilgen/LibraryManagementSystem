from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from services.common.config import db,Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Veritabanı bağlantısını başlat
    db.init_app(app)
    migrate = Migrate(app, db)

    # Hata yakalama middleware
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({"error": "Internal Server Error"}), 500

    # Tüm servis blueprint kayıtları
    from services.user_service.controller.user_controller import user_blueprint
    from services.book_service.controller.book_controller import book_blueprint
    from services.borrow_service.controllers.borrow_controller import borrow_blueprint

    app.register_blueprint(user_blueprint, url_prefix="/api/user")
    app.register_blueprint(book_blueprint, url_prefix="/api/book")
    app.register_blueprint(borrow_blueprint, url_prefix="/api/borrow")

    return app



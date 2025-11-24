from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.configs.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # Tạo ứng dụng Flask
    app = Flask(__name__)

    # Tải cấu hình từ configs.py
    app.config.from_object(Config)

    # Khởi tạo các tiện ích mở rộng
    db.init_app(app)
    migrate.init_app(app, db)
    from app import models

    # Khởi tạo admin
    from app.admin import init_admin
    init_admin(app)
    # Đăng ký blueprint (routes)
    from app.router.index import index
    app.register_blueprint(index)

    return app

from flask.cli import load_dotenv
import os
load_dotenv()
# SECRET_KEY: Dùng để bảo mật các biểu mẫu và session.
# SQLALCHEMY_DATABASE_URI: Đường dẫn đến cơ sở dữ liệu (SQLite ở đây, có thể thay bằng PostgreSQL/MySQL).
# load_dotenv(): Tải các biến môi trường từ file .env.
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or 'mysql://save_brain:minhtit123@192.168.11.76:3306/save_brain'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
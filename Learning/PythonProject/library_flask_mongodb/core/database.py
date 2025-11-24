from mongoengine import connect
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError


def connect_db():
    """Connect to the MongoDB database."""
    try:
        connect(host="mongodb://localhost:27017/library", serverSelectionTimeoutMS=5000)
        print("Successfully connected to the database.")
    except (ConnectionFailure, ServerSelectionTimeoutError) as e:
        print(f"Database connection failed: {e}")
        raise  # raise là để lỗi được xử lý ở nơi gọi hàm

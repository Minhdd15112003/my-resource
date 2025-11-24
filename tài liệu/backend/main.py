from src.socket_io import sio
from flask import Flask

if __name__ == "__main__":
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    sio.init_app(app)
    sio.run(
        app=app,
        host="0.0.0.0",
        port=3000,
        debug=True,
        allow_unsafe_werkzeug=True,
    )
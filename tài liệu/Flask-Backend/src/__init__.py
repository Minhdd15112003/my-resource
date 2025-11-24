import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.json.provider import DefaultJSONProvider
from sqlalchemy import inspect
from flask_cors import CORS
from werkzeug.serving import run_simple
import multiprocessing
from .controller import auth
from flask_restx import Api

DB_NAME = os.path.join(os.getcwd(), 'database.db')
db = SQLAlchemy()

# chỉnh sửa lại cho chạy trên nhiều giao diện mạng
class CustomFlask(Flask):
    def _run_server(self, host, port, debug, options):
        run_simple(host, port, self, use_debugger=debug, use_reloader=False, **options)

    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        if isinstance(host, list) and debug==False:
            processes = []
            for h in host:
                process = multiprocessing.Process(target=self._run_server, args=(h, port, debug, options))
                processes.append(process)
                process.start()
            for process in processes:
                process.join()
        else:
            super().run(host="0.0.0.0", port=port, debug=debug)

# chỉnh sửa lại jsonify return jsonify tự động __table__ thành json
class AlchemyJSONProvider(DefaultJSONProvider):
    def to_dict(self, o):
        if hasattr(o, "__table__"):
            result = {}

            state = inspect(o)

            # Serialize các column đã load
            for attr in state.mapper.column_attrs:
                key = attr.key
                if key not in state.unloaded:  # Field đã load
                    result[key] = getattr(o, key)

            # Serialize các relationship đã load
            for rel in state.mapper.relationships:
                key = rel.key
                if key not in state.unloaded:
                    related_obj = getattr(o, key)
                    if related_obj is not None:
                        if rel.uselist:
                            result[key] = [self.to_dict(i) for i in related_obj]
                        else:
                            result[key] = self.to_dict(related_obj)

            return result
        return o

    def default(self, o):
        if isinstance(o, list):
            return [self.default(item) for item in o]
        if isinstance(o, dict):
            return {k: self.default(v) for k, v in o.items()}
        if hasattr(o, "__table__"):
            return self.to_dict(o)
        return super().default(o)

def create_app():
    app = Flask(__name__)
    app.json = AlchemyJSONProvider(app)
    # app.template_folder = os.path.join(os.getcwd(),"template")
    app.static_folder = os.path.join(os.getcwd(),"public")
    app.config['SECRET_KEY'] = 'test'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from . import webRoutes
    from .controller import clientApi
    from .views import views # static_folder or template_folder ( reactjs build )

    # Gắn namespace vào Flask-RESTX API
    docsApi = Api(app, doc="/docs/api", prefix="/docs",title="API Docs", version="1.0", description="DEV BETA JOIN STOCK COMPANY - devbeta.vn - 0862756099")
    docsApi.add_namespace(clientApi.routes_ns, path='/api/client')

    # đăng kí blueprint vào app
    app.register_blueprint(webRoutes.api, url_prefix='/api')
    app.register_blueprint(auth.routes, url_prefix='/api/auth')
    app.register_blueprint(views, url_prefix='/') 

    CORS(app, 
        supports_credentials=True,
        resources={
            r"/*": {
                "origins": ["http://localhost:5173","https://localhost:5179"]
            }
        },
        methods=["GET","POST","OPTIONS","PATCH","PATH","DELETE"],
        allow_headers=["Content-Type"]
    )

    with app.app_context():
        db.create_all()

    return app


def create_database(app):
    if not os.path.exists(DB_NAME):
        db.create_all(app=app)

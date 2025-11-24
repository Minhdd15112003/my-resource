from flask import Blueprint

from app.router import responses_dp, users_dp, tags_dp, cats_dp

# Một cách tổ chức route theo module, giúp quản lý endpoint trong dự án lớn.
index = Blueprint('index', __name__)

index.register_blueprint(responses_dp)
index.register_blueprint(users_dp)
index.register_blueprint(tags_dp)
index.register_blueprint(cats_dp)

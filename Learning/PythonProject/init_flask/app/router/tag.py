from flask import Blueprint

tags_dp = Blueprint('tag', __name__)


@tags_dp.route('/tag', methods=['GET'])
def find_all():
    return "list tags"


@tags_dp.route('/tag/<int:id>', methods=['GET'])
def find_one(id):
    return "find tags"


@tags_dp.route('/tag', methods=['POST'])
def create():
    return "create tags"


@tags_dp.route('/tag', methods=['PATCH'])
def update():
    return "update tags"


@tags_dp.route('/tag', methods=['DELETE'])
def delete():
    return "delete tags"

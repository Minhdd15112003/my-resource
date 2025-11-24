from flask import Blueprint

users_dp = Blueprint('users', __name__)


@users_dp.route('/users', methods=['GET'])
def find_all():
    return "list users"


@users_dp.route('/users/<int:id>', methods=['GET'])
def find_one(id):
    return "find users"


@users_dp.route('/users', methods=['POST'])
def create():
    return "create users"


@users_dp.route('/users', methods=['PATCH'])
def update():
    return "update users"


@users_dp.route('/users', methods=['DELETE'])
def delete():
    return "delete users"

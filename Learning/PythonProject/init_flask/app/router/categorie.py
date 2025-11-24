from flask import Blueprint

cats_dp = Blueprint('cat', __name__)


@cats_dp.route('/cat', methods=['GET'])
def find_all():
    return "list cats"


@cats_dp.route('/cat/<int:id>', methods=['GET'])
def find_one(id):
    return "find cats"


@cats_dp.route('/cat', methods=['POST'])
def create():
    return "create cats"


@cats_dp.route('/cat', methods=['PATCH'])
def update():
    return "update cats"


@cats_dp.route('/cat', methods=['DELETE'])
def delete():
    return "delete cats"

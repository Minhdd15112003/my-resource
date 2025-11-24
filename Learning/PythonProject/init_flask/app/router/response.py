from flask import Blueprint

responses_dp = Blueprint('responses_dp', __name__)


@responses_dp.route('/responses', methods=['GET'])
def find_all():
    return "list responses"


@responses_dp.route('/responses/<int:id>', methods=['GET'])
def find_one(id):
    return "find responses"


@responses_dp.route('/responses', methods=['POST'])
def create():
    return "create responses"


@responses_dp.route('/responses', methods=['PATCH'])
def update():
    return "update responses"


@responses_dp.route('/responses', methods=['DELETE'])
def delete():
    return "delete responses"

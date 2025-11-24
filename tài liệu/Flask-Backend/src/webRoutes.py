from flask import Blueprint, request, jsonify, make_response
import hashlib
from .controller import network, systemd
# from .utils.files import get_security,get_session_license

api = Blueprint('api', __name__)

@api.before_request
def before_request_func():
    if request.method == "OPTIONS":
        return make_response('', 200)
    session_id = request.cookies.get('session_id')
    # security = hashlib.md5(get_security().text.encode()).hexdigest()
    # if session_id is None or session_id != security:
    #     return jsonify({'error': 'Unauthorized',"login":True}), 500
    # session_license = get_session_license()
    # if session_license is None:
    #     return jsonify({'error': "Lost connection to server","login":True}), 500
    # elif session_license.get("version_update") == True:
    #     return jsonify({"error": session_license.get("version_msg"), "login":True}), 500
    # elif session_license.get("status") != True:
    #     return jsonify({"error": session_license.get("msg"), "login":True}), 500

# Đăng ký Blueprint con vào Blueprint cha
api.register_blueprint(network.routes, url_prefix='/network')
api.register_blueprint(systemd.routes, url_prefix='/system')

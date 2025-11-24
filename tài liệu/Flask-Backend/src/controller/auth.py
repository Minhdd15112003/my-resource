from flask import Blueprint, request, jsonify, make_response
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask import session

routes = Blueprint('auth', __name__)


@routes.post('/signin')
def signin():
    isAuth = {"session_id": "1234"}
    if isinstance(isAuth, tuple):
        return isAuth
    else:
        session_id = isAuth.get("session_id")
        resp = make_response(jsonify({"success":"signin ok","session_id":session_id}))
        resp.set_cookie('session_id', session_id, samesite="Lax", secure=False)
        return resp

from flask import Blueprint, send_from_directory,abort
import os

views = Blueprint('views', __name__)
STATIC_DIR  = os.path.join(os.getcwd(),"public")

@views.route('/')
def serve_react():
    return send_from_directory(STATIC_DIR , 'index.html')

@views.route('/<path:path>')
def serve_file(path):

    if path.startswith('api'):
        return abort(404)
    
    file_path = os.path.join(STATIC_DIR , path)
    if os.path.exists(file_path):
        
        return send_from_directory(STATIC_DIR , path)
    
    return send_from_directory(STATIC_DIR , 'index.html')
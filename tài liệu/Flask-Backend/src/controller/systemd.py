import os
import math
import json
import signal
import subprocess
from flask import Blueprint, jsonify, request
from flask_sock import Sock

routes = Blueprint('systemd', __name__)
sock = Sock(routes)

def format_bytes(bytes):
    if bytes == 0:
        return "0 KB"
    k = 1024
    sizes = ["Bytes", "KB", "MB", "GB", "TB"]
    i = int(math.floor(math.log(bytes, k)))
    i = min(i, 4)  # Giới hạn tối đa là TB
    value = round(bytes / math.pow(k, i), 2)
    return f"{value} {sizes[i]}"

def check_version(version,version_max):
    version = int(version.replace(".",""))
    version_max = int(version_max.replace(".",""))
    if version_max>version:
        return version_max

@routes.get('/reboot')
def reboot_system():
    # subprocess.Popen("sleep 3 && reboot", shell=True)
    return jsonify({"success": "reboot success"}), 200

@sock.route('/update')
def update_system(ws):
    while True:
        data = json.loads(ws.receive())
        action = data.get("action")
        if action=="update":
            isDone = True
            if isDone:
                os.kill(os.getpid(), signal.SIGTERM)
        # ws.send(data)
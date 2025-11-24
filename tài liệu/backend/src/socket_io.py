import os
from .deep_face import detectFace
from flask_socketio import SocketIO

sio = SocketIO(
    cors_allowed_origins="*",
    async_mode="eventlet",
    logger=False,
    engineio_logger=False,
)

@sio.on("face-detect")
def handle_face_detect(data:dict):
    task_id = data.get("task_id")
    image_data = data.get("image_data")

    face_data = detectFace(image_data)
    identity = face_data.get("identity", "")
    face_id = os.path.basename(identity)[:-4]

    sio.emit("face-detect", {"task_id": task_id, "face_id": face_id})

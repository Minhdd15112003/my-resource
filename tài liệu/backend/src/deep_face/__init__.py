from deepface import DeepFace
from .deepEnv import faceImagesDir

def detectFace(image_data):
    try:
        peoples = DeepFace.find(
            img_path = image_data, 
            db_path = faceImagesDir, 
            model_name = "GhostFaceNet",
            detector_backend = "opencv",
            enforce_detection = False,
            anti_spoofing = True,
            align = False,
            silent = True
        )
        if len(peoples) > 0 and not peoples[0].empty:
            return peoples[0].iloc[0].to_dict()
    except Exception as e:
        print(e)
    return {}
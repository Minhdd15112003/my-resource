import os
from pathlib import Path

pathDir = str(Path().absolute())
dataDir = os.path.join(pathDir, "data")
faceImagesDir = os.path.join(dataDir, "faceImages")
modelsDir = os.path.join(dataDir, "models")
os.environ["DEEPFACE_BACKEND"] = 'opencv'
os.environ['DEEPFACE_HOME'] = modelsDir

def data_join_path(path:str):
    return os.path.join(dataDir, path)

def faceImage_path(face_id:str):
    path =  os.path.join(faceImagesDir, f"{face_id}.jpg")
    if os.path.isfile(path):
        return path

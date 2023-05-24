import numpy as np
from . face_detector import FaceDetector


MODEL_PATH = r'../nn_models/Detection/faceboxes_model.pb'
print(MODEL_PATH)
face_detector = FaceDetector(MODEL_PATH, gpu_memory_fraction=0.4, visible_device_list='0')


def pad_faces(frame, tres=0.5):
    face_pad = []

    image_array = np.array(frame)
    width, height, _ = frame.shape
    boxes, scores = face_detector(image_array, score_threshold=tres)

    for b in boxes:
        ymin, xmin, ymax, xmax = b.astype('int')
        face_pad.append((image_array[ymin:ymax, xmin:xmax], (ymin, xmin, ymax, xmax)))

    return max(face_pad, key=lambda x: x[0].shape[0]*x[0].shape[1]) if face_pad else False

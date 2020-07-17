import cv2
import dlib
from imutils import face_utils


face_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_detector = dlib.get_frontal_face_detector()
green = (255, 58, 60)


def find_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_faces = face_detector(gray, 1)  # hog

    for c in detected_faces:
        shape = face_predictor(gray, c)
        shape = face_utils.shape_to_np(shape)
        for (x, y) in shape:
            cv2.circle(frame, (x, y), 3, green, -1)
    return frame





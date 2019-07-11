import numpy as np
import cv2
import imutils
import dlib
from imutils import face_utils


predictor_model = "shape_predictor_68_face_landmarks.dat"
faceCascade = cv2.CascadeClassifier('find-face-haar.xml')
face_detector = dlib.get_frontal_face_detector()

face_predictor = dlib.shape_predictor(predictor_model)

input_photo = 16

blue = (255, 0, 0)
green = (0, 255, 0)

for k in range(1, input_photo):
    img = cv2.imread("train/insult/{}.jpg".format(k))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20)) # haar
    detected_faces = face_detector(gray, 1)  # dlib cascade

    for (x,y,w,h) in faces:  # haar rectangle
        cv2.rectangle(img, (x, y),(x+w,y+h),blue,2)
        # roi_gray = gray[y:y+h, x:x+w]
        # roi_color = img[y:y+h, x:x+w]

    for c in detected_faces:  # dlib rectangle
        (x, y, w, h) = face_utils.rect_to_bb(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), green, 2)

        shape = face_predictor(gray, c)
        shape = face_utils.shape_to_np(shape)
        for (x, y) in shape:  # circles
            cv2.circle(img, (x, y), 1, (0, 0, 255), -1)

    cv2.imwrite("train/insult/result_landmarks/{}.new.jpg".format(k), img)

cv2.destroyAllWindows()

import numpy as np
import cv2
import imutils
import dlib
from imutils import face_utils


predictor_model = "shape_predictor_68_face_landmarks.dat"
face_predictor = dlib.shape_predictor(predictor_model)
faceCascade = cv2.CascadeClassifier('find-face-haar.xml')
face_detector = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture('train/video_test/video_test_input_1.mp4')

img_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

blue = (255, 0, 0)
green = (0, 255, 0)
empty_img_count_haar = 0  # счетчики изображений на корорых не найдено лицо с помощью хаар каскада
empty_img_count_dlib = 0  # счетчики изображений на корорых не найдено лицо с помощью hog градиентов

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))  # haar
    detected_faces = face_detector(gray, 1)  # hog

    for (x, y, w, h) in faces:  # haar rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), blue, 2)
        # roi_gray = gray[y:y+h, x:x+w]
        # roi_color = frame[y:y+h, x:x+w]

    for c in detected_faces:  # rectangle
        (x, y, w, h) = face_utils.rect_to_bb(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), green, 2)

        shape = face_predictor(gray, c)
        shape = face_utils.shape_to_np(shape)
        for (x, y) in shape:  # circles
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

    if len(faces) == 0:
        empty_img_count_haar += 1

    if not detected_faces:
        empty_img_count_dlib += 1

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(str(empty_img_count_haar / img_count * 100) + "% кадров haar не определенно")
print(str(empty_img_count_dlib / img_count * 100) + "% кадров hog не определенно")

cap.release()
cv2.destroyAllWindows()

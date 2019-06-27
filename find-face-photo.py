import numpy as np
import cv2
import imutils
import dlib
from imutils import face_utils



faceCascade = cv2.CascadeClassifier('find-face-haar.xml')
face_detector = dlib.get_frontal_face_detector()


a=0
blue = (255, 0, 0)
green = (0, 255, 0)
while True:
    for k in range(1, 16):
        img = cv2.imread("train/insult/{}.jpg".format(k))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20)) # haar
        detected_faces = face_detector(gray, 1) # dlib cascade

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x, y),(x+w,y+h),blue,2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        for c in detected_faces:
            (x, y, w, h) = face_utils.rect_to_bb(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imwrite("train/insult/result/{}.new.jpg".format(k), img)
        a=a+1

cv2.destroyAllWindows()

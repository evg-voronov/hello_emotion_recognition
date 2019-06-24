import dlib
import cv2 as cv

predictor_model = "shape_predictor_68_face_landmarks.dat"



face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor(predictor_model)

win = dlib.image_window()

image = cv.VideoCapture(0)



while True:
    ret, frame = image.read()
    detected_faces = face_detector(frame, 1)
    print("Found {} faces in the image file".format(len(detected_faces)))
    win.set_image(frame)

    for face_rect in detected_faces:
        win.add_overlay(face_rect)
        pose_landmarks = face_pose_predictor(frame, face_rect)
        win.add_overlay(pose_landmarks)


cv.imshow('Video', frame)

video_capture.release()
cv.destroyAllWindows()

dlib.hit_enter_to_continue()
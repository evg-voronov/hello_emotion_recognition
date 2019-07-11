import cv2
from neural_network import EMR

EMOTIONS = ['angry', 'disgusted', 'fearful', 'happy', 'sad', 'surprised', 'neutral']

cascade_classifier = cv2.CascadeClassifier('find-face-haar.xml')


def format_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade_classifier.detectMultiScale(image, scaleFactor=1.3, minNeighbors=5)
    if not len(faces) > 0:
        return None

    max_area_face = faces[0]

    for face in faces:
        if face[2] * face[3] > max_area_face[2] * max_area_face[3]:
            max_area_face = face
    face = max_area_face
    image = image[face[1]:(face[1] + face[2]), face[0]:(face[0] + face[3])]
    image = cv2.resize(image, (48, 48), interpolation=cv2.INTER_CUBIC) / 255.
    return image


network = EMR()
network.build_network()

font = cv2.FONT_HERSHEY_SIMPLEX

feelings_faces = []
for index, emotion in enumerate(EMOTIONS):
    feelings_faces.append(cv2.imread('./emojis/' + emotion + '.png', -1))


def emotions(image, frame):
    result = network.predict(image)

    if result is not None:
        for index, emotion in enumerate(EMOTIONS):
            cv2.putText(frame, emotion, (10, index * 40 + 40), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 2)
            cv2.putText(frame, str(int(result[0][index]*100))+" %", (180, index * 40 + 40), cv2.FONT_HERSHEY_TRIPLEX,
                        1, (255, 0, 0), 2)
    return frame
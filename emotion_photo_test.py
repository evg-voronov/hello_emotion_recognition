import cv2
from neural_network import EMR

EMOTIONS = ['angry', 'disgusted', 'fearful', 'happy', 'sad', 'surprised', 'neutral']

cascade_classifier = cv2.CascadeClassifier('find-face-haar.xml')

input_photo = 9


def format_image(image):
    if len(image.shape) > 2 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        image = cv2.imdecode(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    faces = cascade_classifier.detectMultiScale(image, scaleFactor=1.3, minNeighbors=5)
    if not len(faces) > 0:
        return None

    max_area_face = faces[0]

    for face in faces:
        if face[2] * face[3] > max_area_face[2] * max_area_face[3]:
            max_area_face = face
    face = max_area_face
    image = image[face[1]:(face[1] + face[2]), face[0]:(face[0] + face[3])]
    try:
        image = cv2.resize(image, (48, 48), interpolation=cv2.INTER_CUBIC) / 255.
    except Exception:
        print("[+] Problem during resize")
        return None
    return image


network = EMR()
network.build_network()

font = cv2.FONT_HERSHEY_SIMPLEX


for k in range(1, input_photo):
    img = cv2.imread("train/surprised/{}.jpg".format(k))
    cv2.imshow("fds", img)
    result = network.predict(format_image(img))

    if result is not None:
        for index, emotion in enumerate(EMOTIONS):
            cv2.putText(img, emotion, (10, index * 40 + 40), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 2)
            cv2.putText(img, str(int(result[0][index]*100))+" %", (180, index * 40 + 40), cv2.FONT_HERSHEY_TRIPLEX, 1,
                        (255, 0, 0), 2)

    cv2.imwrite("train/surprised/{}.new.jpg".format(k), img)

cv2.destroyAllWindows()
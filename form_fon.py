import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QLabel, QVBoxLayout)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap
import cv2
import find_face_video as f
import emotion_video as e


class QtCapture(QWidget):
    global a
    a = 0

    def __init__(self, *args):
        super(QWidget, self).__init__()

        self.cap = cv2.VideoCapture(*args)

        self.video_frame = QLabel()
        lay = QVBoxLayout()
        lay.addWidget(self.video_frame)
        self.setLayout(lay)

    def nextFrameSlot(self):
        ret, frame = self.cap.read()
        if a == 1:
            frame = f.find_face(frame)
        elif a == 2:
            image = e.format_image(frame)
            frame = e.emotions(image, frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.video_frame.setPixmap(pix)

    def start(self):
        global a
        a = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./30)  # задаем fps

    def stop(self):
        self.timer.stop()

    def deleteLater(self):
        self.cap.release()
        super(QWidget, self).deleteLater()

    def key_points(self):
        global a
        a = 1
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./30)  # задаем fps

    def emotion(self):
        global a
        a = 2
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./30)  # задаем fps


class ControlWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.capture = None

        self.start_button = QPushButton('зеркало')
        self.start_button.clicked.connect(self.startCapture)
        self.quit_button = QPushButton('выход')
        self.quit_button.clicked.connect(self.endCapture)

        self.key_points_button = QPushButton('точки')
        self.emotion_button = QPushButton('эмоции')


        self.end_button = QPushButton('пауза')

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.key_points_button)
        vbox.addWidget(self.emotion_button)
        vbox.addWidget(self.quit_button)
        self.setLayout(vbox)
        self.setWindowTitle('управление')
        self.setGeometry(100, 100, 220, 200)
        self.show()


    def startCapture(self):
        if not self.capture:
            self.capture = QtCapture(0)
            self.end_button.clicked.connect(self.capture.stop)
            self.key_points_button.clicked.connect(self.capture.key_points)
            self.emotion_button.clicked.connect(self.capture.emotion)
            # self.capture.setFPS(1)
            self.capture.setParent(self)
            self.capture.setWindowFlags(Qt.Tool)
        self.capture.start()
        self.capture.show()


    def endCapture(self):
        self.capture.deleteLater()
        self.capture = None
        QApplication.quit()


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = ControlWindow()
    sys.exit(app.exec_())
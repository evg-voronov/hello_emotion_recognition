# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PycharmProjects/f/test.ui',
# licensing of 'PycharmProjects/f/test.ui' applies.
#
# Created: Fri Jun 21 16:33:36 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(808, 559)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 180, 421, 171))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: black;\n"
"color: white;\n"
"font-size: 50px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: silver;\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Start", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


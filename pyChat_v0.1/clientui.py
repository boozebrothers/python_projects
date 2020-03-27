# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, QtCore, QtGui


class Ui_Pychat(QtWidgets.QApplication):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Pychat):
        Pychat.setObjectName("Pychat")
        Pychat.resize(387, 468)
        self.centralwidget = QtWidgets.QWidget(Pychat)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 60, 371, 331))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 400, 301, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 400, 61, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 30, 51, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 30, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        Pychat.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Pychat)
        self.statusbar.setObjectName("statusbar")
        Pychat.setStatusBar(self.statusbar)

        self.retranslateUi(Pychat)
        QtCore.QMetaObject.connectSlotsByName(Pychat)

    def retranslateUi(self, Pychat):
        _translate = QtCore.QCoreApplication.translate
        Pychat.setWindowTitle(_translate("Pychat", "Pychat v0.1"))
        self.pushButton.setText(_translate("Pychat", "Send"))
        self.label_2.setText(_translate("Pychat", "username:"))
        self.label_3.setText(_translate("Pychat", "password:"))


app = QtWidgets.QApplication([])
window = Ui_Pychat
window.show()
app.exec_()

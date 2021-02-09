# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MSME_login.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(50, 220, 97, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Login)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 220, 97, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(70, 20, 261, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(45, 80, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(45, 150, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Login)
        self.lineEdit.setGeometry(QtCore.QRect(160, 73, 191, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Login)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 141, 191, 31))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Login", None))
        self.pushButton.setText(_translate("Login", "Login", None))
        self.pushButton_2.setText(_translate("Login", "Cancel", None))
        self.label.setText(_translate("Login", "Welcome to MSME Login", None))
        self.label_2.setText(_translate("Login", "User Name :", None))
        self.label_3.setText(_translate("Login", "Password :", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Login = QtGui.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

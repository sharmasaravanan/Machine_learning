import sys

from PyQt4 import QtCore as qc
from PyQt4 import QtGui as qg


def window():
    d.setObjectName("Login")
    d.resize(400, 300)
    d.setWindowTitle("Login")

    l1 = qg.QLabel(d)
    l1.setGeometry(qc.QRect(70, 20, 261, 21))
    font = qg.QFont()
    font.setUnderline(True)
    font.setBold(True)
    font.setPointSize(14.5)
    l1.setFont(font)
    l1.setText("Welcome to MSME Login")

    l3 = qg.QLabel(d)
    l3.setGeometry(qc.QRect(45, 80, 101, 20))
    font = qg.QFont()
    font.setPointSize(12)
    l3.setFont(font)
    l3.setText("User Name :")

    l4 = qg.QLabel(d)
    l4.setGeometry(qc.QRect(45, 150, 101, 20))
    l4.setFont(font)
    l4.setText("Password :")

    le1.setGeometry(qc.QRect(160, 73, 191, 31))
    le2.setGeometry(qc.QRect(160, 141, 191, 31))
    le2.setMaxLength(8)
    le2.setEchoMode(qg.QLineEdit.Password)

    b1 = qg.QPushButton(d)
    b1.setText("Login")
    b1.clicked.connect(verification)
    b1.setGeometry(qc.QRect(50, 220, 97, 27))
    
    b2=qg.QPushButton(d)
    b2.setText("Cancel")
    b2.clicked.connect(close)
    b2.setGeometry(qc.QRect(240, 220, 97, 27))
    

    d.show()
    sys.exit(app.exec_())


def verification():
    name = le1.text()
    password = le2.text()
    msg = qg.QMessageBox()
    msg.setIcon(qg.QMessageBox.Information)
    msg.setWindowTitle("Login Information")
    if name == "admin" and password == "admin":
        msg.setText("Login Successful")
        msg.exec_()
    else:
        msg.setText("Login Failed")
        msg.buttonClicked.connect(hides)
        msg.exec_()


def hides():
    d.close()


def close():
    sys.exit()


if __name__ == '__main__':
    app = qg.QApplication(sys.argv)
    d = qg.QDialog()
    le1 = qg.QLineEdit(d)
    le2 = qg.QLineEdit(d)
    window()

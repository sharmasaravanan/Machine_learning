from PyQt4 import QtGui as qg
from PyQt4 import QtCore as qc
import sys
import subprocess
import sip
import atexit
import os,csv


def window():
    d.setObjectName("Login")
    d.resize(400, 300)
    d.setWindowTitle("Login")

    l4 = qg.QLabel(d)
    l4.setGeometry(qc.QRect(10, 10, 131, 91))
    pix = qg.QPixmap("logo.jpg")
    l4.setPixmap(pix)

    l5 = qg.QLabel(d)
    l5.setGeometry(qc.QRect(135, 30, 261, 41))
    font = qg.QFont()
    font.setUnderline(True)
    font.setPointSize(14.5)
    l5.setFont(font)
    l5.setText("Welcome to Vignan's CLA-Test")

    l3 = qg.QLabel(d)
    l3.setGeometry(qc.QRect(270, 280, 125, 21))
    font = qg.QFont()
    font.setPointSize(10)
    l3.setFont(font)
    l3.setText("Created by Sharma S")

    l1 = qg.QLabel(d)
    l1.setGeometry(qc.QRect(67, 115, 111, 21))
    font = qg.QFont()
    font.setPointSize(14)
    l1.setFont(font)
    l1.setText("User Name")

    l2 = qg.QLabel(d)
    l2.setGeometry(qc.QRect(70, 165, 111, 21))
    l2.setFont(font)
    l2.setText("Password")

    b1 = qg.QPushButton(d)
    b1.setText("Login")
    b1.clicked.connect(verification)
    b1.setGeometry(qc.QRect(210, 220, 75, 23))

    le1.setGeometry(qc.QRect(190, 110, 171, 31))

    le2.setGeometry(qc.QRect(190, 160, 171, 31))
    le2.setMaxLength(8)
    le2.setEchoMode(qg.QLineEdit.Password)

    d.show()
    sys.exit(app.exec_())


def details():
    d1.setObjectName("details")
    d1.resize(508, 300)
    d1.setWindowTitle("Grade Enter")

    l3 = qg.QLabel(d1)
    l3.setGeometry(qc.QRect(380, 280, 125, 21))
    font = qg.QFont()
    font.setPointSize(10)
    l3.setFont(font)
    l3.setText("Created by Sharma S")

    l1 = qg.QLabel(d1)
    l1.setGeometry(qc.QRect(130, 10, 251, 20))
    l1.setText("Enter Last Experiment Details")
    ft = qg.QFont()
    ft.setPointSize(14)
    ft.setUnderline(True)
    l1.setFont(ft)

    le12.setGeometry(qc.QRect(110, 50, 181, 31))
    l2 = qg.QLabel(d1)
    l2.setGeometry(qc.QRect(11, 54, 91, 21))
    l2.setText("Register No")
    font = qg.QFont()
    font.setPointSize(12)
    l2.setFont(font)

    s1.setGeometry(qc.QRect(420, 50, 61, 31))
    l3 = qg.QLabel(d1)
    l3.setGeometry(qc.QRect(322, 57, 91, 21))
    l3.setText("Experiment")
    l3.setFont(font)

    c1.setGeometry(qc.QRect(140, 140, 91, 31))
    c1.addItem("A")
    c1.addItem("B")
    c1.addItem("C")
    c1.addItem("D")
    c1.addItem("E")
    c1.addItem("ABSENT")
    l4 = qg.QLabel(d1)
    l4.setGeometry(qc.QRect(41, 146, 91, 21))
    l4.setText("Observation")
    l4.setFont(font)

    c2.setGeometry(qc.QRect(350, 140, 91, 31))
    c2.addItem("A")
    c2.addItem("B")
    c2.addItem("C")
    c2.addItem("D")
    c2.addItem("E")
    c2.addItem("ABSENT")
    l5 = qg.QLabel(d1)
    l5.setGeometry(qc.QRect(280, 146, 61, 21))
    l5.setText("Record")
    l5.setFont(font)

    b = qg.QPushButton(d1)
    b.setText("Start")
    b.clicked.connect(opened)
    b.setGeometry(qc.QRect(200, 220, 75, 23))

    d1.show()


def viva():
    v.setObjectName("qustions")
    v.resize(519, 424)
    v.setWindowTitle("Viva")

    l4 = qg.QLabel(v)
    l4.setGeometry(qc.QRect(390, 400, 125, 21))
    font = qg.QFont()
    font.setPointSize(10)
    l4.setFont(font)
    l4.setText("Created by Sharma S")

    l1 = qg.QLabel(v)
    l1.setGeometry(qc.QRect(27, 220, 91, 21))
    l1.setText("Answer")
    font = qg.QFont()
    font.setPointSize(12)
    l1.setFont(font)

    l2 = qg.QLabel(v)
    l2.setGeometry(qc.QRect(23, 70, 91, 21))
    l2.setText("Question")
    l2.setFont(font)

    l3 = qg.QLabel(v)
    l3.setGeometry(qc.QRect(90, 20, 351, 41))
    l3.setText("VIVA-Enter answers for questions below")
    fo = qg.QFont()
    fo.setPointSize(14)
    fo.setUnderline(True)
    l3.setFont(fo)

    te.setGeometry(qc.QRect(20, 260, 481, 101))

    tb.setGeometry(qc.QRect(20, 110, 481, 101))

    b = qg.QPushButton(v)
    b.setText("Next")
    b.clicked.connect(saves)
    b.setGeometry(qc.QRect(160, 370, 75, 23))

    b1 = qg.QPushButton(v)
    b1.setText("Cancel")
    b1.clicked.connect(accept)
    b1.setGeometry(qc.QRect(280, 370, 75, 23))
    qc.QTimer.singleShot(300000, entry)
    v.show()


def entry():
    v.hide()
    d3.setObjectName("Login")
    d3.resize(265, 244)
    d3.setWindowTitle("Viva-Mark")

    l1 = qg.QLabel(d3)
    l1.setGeometry(qc.QRect(30, 20, 211, 41))
    font = qg.QFont()
    font.setUnderline(True)
    font.setPointSize(12.5)
    l1.setFont(font)
    l1.setText("Enter the Grade for CLA-Viva")

    c12.setGeometry(qc.QRect(80, 90, 101, 31))
    c12.addItem("A")
    c12.addItem("B")
    c12.addItem("C")
    c12.addItem("D")
    c12.addItem("E")
    c12.addItem("ABSENT")

    l2 = qg.QLabel(d3)
    l2.setGeometry(qc.QRect(135, 220, 141, 20))
    font = qg.QFont()
    font.setPointSize(10)
    l2.setFont(font)
    l2.setText("Created by Sharma S")

    b1 = qg.QPushButton(d3)
    b1.setText("Submit")
    b1.clicked.connect(saved)
    b1.setGeometry(qc.QRect(100, 160, 75, 23))
    d3.show()


def verification():
    name = le1.text()
    password = le2.text()
    if name == password:
        msg.setText("Login successful")
        msg.exec_()
        details()
    else:
        msg.setText("Login Failed")
        msg.exec_()


def opened():
    # cur_path = os.path.dirname(__file__)
    files = os.path.relpath(".\\grade.csv")
    fe = csv.writer(open(files, "ab+"))
    global num, exp, obs, rec
    num = le12.text()
    exp = s1.value()
    obs = c1.currentText()
    rec = c2.currentText()
    # fe.writerow([num,exp,obs,rec])
    hided()
    viva()


def close():
    sys.exit()


def accept():
    hidee()
    entry()
    # v.close()


def hidee():
    v.hide()


def hided():
    d1.close()


def hides():
    d.close()


def saves():
    i = random.randint(0, 50)
    f = open("question.txt", "r")
    ans = open("answers.txt", "a+")
    a = f.readlines()
    tb.setText(a[i])
    b = te.toPlainText()
    ans.write("\n" + str(a[i]))
    ans.write("\n" + str(b) + "\n")
    te.clear()


def saved():
    files = os.path.relpath(".\\grade.csv")
    fe = csv.writer(open(files, "ab+"))
    grade = c12.currentText()
    fe.writerow([num, exp, obs, rec, grade])
    sys.exit()


if __name__ == '__main__':
    app = qg.QApplication(sys.argv)
    w = qg.QWidget()
    d = qg.QDialog()
    le1 = qg.QLineEdit(d)
    le2 = qg.QLineEdit(d)
    msg = qg.QMessageBox()
    msg.setIcon(qg.QMessageBox.Information)
    msg.setWindowTitle("Login Information")
    msg.buttonClicked.connect(hides)
    d1 = qg.QDialog()
    le12 = qg.QLineEdit(d1)
    s1 = qg.QSpinBox(d1)
    c1 = qg.QComboBox(d1)
    c2 = qg.QComboBox(d1)
    v = qg.QDialog()
    te = qg.QTextEdit(v)
    tb = qg.QTextBrowser(v)
    d3 = qg.QDialog()
    c12 = qg.QComboBox(d3)
    window()
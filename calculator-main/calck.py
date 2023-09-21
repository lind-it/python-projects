from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class CalcUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(423, 553)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 401, 81))
        self.label.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.btn_divide = QtWidgets.QPushButton(Form)
        self.btn_divide.setGeometry(QtCore.QRect(320, 100, 81, 81))
        self.btn_divide.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);\n"
"border-radius: 40px;")
        self.btn_divide.setObjectName("btn_divide")

        self.btn_multiply = QtWidgets.QPushButton(Form)
        self.btn_multiply.setGeometry(QtCore.QRect(320, 190, 81, 81))
        self.btn_multiply.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);\n"
"border-radius: 40px;")
        self.btn_multiply.setObjectName("btn_multiply")

        self.btn_minus = QtWidgets.QPushButton(Form)
        self.btn_minus.setGeometry(QtCore.QRect(320, 280, 81, 81))
        self.btn_minus.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);\n"
"border-radius: 40px;")
        self.btn_minus.setObjectName("btn_minus")

        self.btn_plus = QtWidgets.QPushButton(Form)
        self.btn_plus.setGeometry(QtCore.QRect(320, 370, 81, 81))
        self.btn_plus.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);\n"
"border-radius: 40px;")
        self.btn_plus.setObjectName("btn_plus")

        self.btn_equall = QtWidgets.QPushButton(Form)
        self.btn_equall.setGeometry(QtCore.QRect(320, 460, 81, 81))
        self.btn_equall.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);\n"
"border-radius: 40px;")
        self.btn_equall.setObjectName("btn_equall")

        self.btn_9 = QtWidgets.QPushButton(Form)
        self.btn_9.setGeometry(QtCore.QRect(220, 190, 81, 81))
        self.btn_9.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.btn_9.setObjectName("btn_9")

        self.btn_4 = QtWidgets.QPushButton(Form)
        self.btn_4.setGeometry(QtCore.QRect(220, 280, 81, 81))
        self.btn_4.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.btn_4.setObjectName("btn_4")

        self.btn_point = QtWidgets.QPushButton(Form)
        self.btn_point.setGeometry(QtCore.QRect(220, 460, 81, 81))
        self.btn_point.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.btn_point.setObjectName("btn_point")

        self.btn_3 = QtWidgets.QPushButton(Form)
        self.btn_3.setGeometry(QtCore.QRect(220, 370, 81, 81))
        self.btn_3.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.btn_3.setObjectName("btn_3")

        self.btn_percent = QtWidgets.QPushButton(Form)
        self.btn_percent.setGeometry(QtCore.QRect(220, 100, 81, 81))
        self.btn_percent.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);\n"
"border-radius: 40px;")
        self.btn_percent.setObjectName("btn_percent")

        self.btn_8 = QtWidgets.QPushButton(Form)
        self.btn_8.setGeometry(QtCore.QRect(120, 190, 81, 81))
        self.btn_8.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.btn_8.setObjectName("btn_8")

        self.btn_5 = QtWidgets.QPushButton(Form)
        self.btn_5.setGeometry(QtCore.QRect(120, 280, 81, 81))
        self.btn_5.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.btn_5.setObjectName("btn_5")

        self.btn_0 = QtWidgets.QPushButton(Form)
        self.btn_0.setGeometry(QtCore.QRect(120, 460, 81, 81))
        self.btn_0.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.btn_0.setObjectName("btn_0")

        self.btn_2 = QtWidgets.QPushButton(Form)
        self.btn_2.setGeometry(QtCore.QRect(120, 370, 81, 81))
        self.btn_2.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.btn_2.setObjectName("btn_2")

        self.btn_right = QtWidgets.QPushButton(Form)
        self.btn_right.setGeometry(QtCore.QRect(120, 100, 81, 81))
        self.btn_right.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);\n"
"border-radius: 40px;")
        self.btn_right.setObjectName("btn_right")

        self.btn_7 = QtWidgets.QPushButton(Form)
        self.btn_7.setGeometry(QtCore.QRect(20, 190, 81, 81))
        self.btn_7.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.btn_7.setObjectName("btn_7")

        self.btn_6 = QtWidgets.QPushButton(Form)
        self.btn_6.setGeometry(QtCore.QRect(20, 280, 81, 81))
        self.btn_6.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.btn_6.setObjectName("btn_6")

        self.btn_left = QtWidgets.QPushButton(Form)
        self.btn_left.setGeometry(QtCore.QRect(20, 100, 81, 81))
        self.btn_left.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);\n"
"border-radius: 40px;")
        self.btn_left.setObjectName("btn_left")

        self.btn_1 = QtWidgets.QPushButton(Form)
        self.btn_1.setGeometry(QtCore.QRect(20, 370, 81, 81))
        self.btn_1.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.btn_1.setObjectName("btn_1")

        self.btn_delete = QtWidgets.QPushButton(Form)
        self.btn_delete.setGeometry(QtCore.QRect(20, 460, 81, 81))
        self.btn_delete.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 170, 0);\n"
"border-radius: 40px;")
        self.btn_delete.setObjectName("btn_delete")

        self.setActions()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def setActions(self):
        self.btn_0.clicked.connect(lambda: self.writeNum(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.writeNum(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.writeNum(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.writeNum(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.writeNum(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.writeNum(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.writeNum(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.writeNum(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.writeNum(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.writeNum(self.btn_9.text()))
        self.btn_point.clicked.connect(lambda: self.writeNum(self.btn_point.text()))
        self.btn_plus.clicked.connect(lambda: self.writeNum(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.writeNum(self.btn_minus.text()))
        self.btn_multiply.clicked.connect(lambda: self.writeNum(self.btn_multiply.text()))
        self.btn_divide.clicked.connect(lambda: self.writeNum(self.btn_divide.text()))
        self.btn_percent.clicked.connect(lambda: self.writeNum(self.btn_percent.text()))
        self.btn_left.clicked.connect(lambda: self.writeNum(self.btn_left.text()))
        self.btn_right.clicked.connect(lambda: self.writeNum(self.btn_right.text()))
        self.btn_delete.clicked.connect(self.delete)
        self.btn_equall.clicked.connect(self.solve)

    def writeNum(self, num):
        if self.label.text() == "0":
            self.label.setText("")
        self.label.setText(self.label.text() + num)

    def delete(self):
        self.label.setText("0")

    def solve(self):
        result = eval(self.label.text())
        self.label.setText(str(result))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "0"))
        self.btn_divide.setText(_translate("Form", "/"))
        self.btn_multiply.setText(_translate("Form", "*"))
        self.btn_minus.setText(_translate("Form", "-"))
        self.btn_plus.setText(_translate("Form", "+"))
        self.btn_equall.setText(_translate("Form", "="))
        self.btn_9.setText(_translate("Form", "9"))
        self.btn_4.setText(_translate("Form", "6"))
        self.btn_point.setText(_translate("Form", "."))
        self.btn_3.setText(_translate("Form", "3"))
        self.btn_percent.setText(_translate("Form", "%"))
        self.btn_8.setText(_translate("Form", "8"))
        self.btn_5.setText(_translate("Form", "5"))
        self.btn_0.setText(_translate("Form", "0"))
        self.btn_2.setText(_translate("Form", "2"))
        self.btn_right.setText(_translate("Form", ")"))
        self.btn_7.setText(_translate("Form", "7"))
        self.btn_6.setText(_translate("Form", "4"))
        self.btn_left.setText(_translate("Form", "("))
        self.btn_1.setText(_translate("Form", "1"))
        self.btn_delete.setText(_translate("Form", "C"))


def app():
    applic = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()


    ui = CalcUi()
    ui.setupUi(window)

    window.show()
    sys.exit(applic.exec_())

if __name__ == "__main__":
    app()
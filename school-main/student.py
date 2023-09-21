from PyQt5 import QtCore, QtGui, QtWidgets
from CRUD import CRUD

class Student(QtWidgets.QMainWindow):
    def __init__(self, student_name, login):
        super().__init__()

        self.setObjectName("Form")
        self.resize(261, 222)
        self.setStyleSheet("background-color: rgb(223, 255, 185);")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 10, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText(f"Привет, {student_name}")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        db = CRUD("users")
        # ищем день дежурства ученика
        query = db.Read("users", "dutyDay", f""" (name || ' ' || secondName = '{student_name}'
                                                  OR secondName || ' ' || name = '{student_name}') 
                                                  AND login = '{login}'""")


        self.label_2.setText(query[0][0])

        QtCore.QMetaObject.connectSlotsByName(self)



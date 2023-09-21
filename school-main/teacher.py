from PyQt5 import QtCore, QtGui, QtWidgets
from AutoDestrib import AutoDestrib
from TimeTable import TimeTable
from HandleDestrib import HandleDestrib
from CRUD import CRUD

class Teacher(QtWidgets.QMainWindow):
    def __init__(self, teacher_name):
        super().__init__()

        self.db = CRUD("users")

        self.setObjectName("Form")
        self.resize(650, 518)
        self.setStyleSheet("background-color: rgb(223, 255, 185);")

        self.lbl_greating = QtWidgets.QLabel(self)
        self.lbl_greating.setGeometry(QtCore.QRect(140, 10, 381, 31))
        self.lbl_greating.setObjectName("lbl_greating")
        self.lbl_greating.setText(f"Здравуствуйте, {teacher_name}")

        self.btn_handleDistrib = QtWidgets.QPushButton(self)
        self.btn_handleDistrib.setGeometry(QtCore.QRect(460, 150, 181, 61))
        self.btn_handleDistrib.setObjectName("btn_handleDistrib")

        self.btn_timeTable = QtWidgets.QPushButton(self)
        self.btn_timeTable.setGeometry(QtCore.QRect(460, 220, 181, 61))
        self.btn_timeTable.setObjectName("btn_timeTable")

        self.btn_autoDestrib = QtWidgets.QPushButton(self)
        self.btn_autoDestrib.setGeometry(QtCore.QRect(460, 80, 181, 61))
        self.btn_autoDestrib.setObjectName("btn_autoDestrib")

        self.window = QtWidgets.QGroupBox(self)
        self.window.setGeometry(QtCore.QRect(20, 60, 431, 451))
        self.window.setObjectName("window")

        self.auto_destrib = AutoDestrib()
        self.auto_destrib.setupUi(self.window)

        self.time_table = TimeTable()
        self.time_table.setupUi(self.window)

        self.handle_destrib = HandleDestrib()
        self.handle_destrib.setupUi(self.window)

        self.AutoDestrib()

        self.btn_autoDestrib.clicked.connect(lambda: self.AutoDestrib())
        self.btn_handleDistrib.clicked.connect(lambda: self.HandleDestrib())
        self.btn_timeTable.clicked.connect(lambda: self.ShowTable())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_handleDistrib.setText(_translate("Form", "Распределить в ручную"))
        self.btn_timeTable.setText(_translate("Form", "Посмотреть расписание"))
        self.btn_autoDestrib.setText(_translate("Form", "Автоматическое распределение"))
        self.window.setTitle(_translate("Form", "Автоматическое распределение"))



    def AutoDestrib(self):
        self.time_table.Hide()
        self.handle_destrib.Hide()
        self.auto_destrib.Show()
        self.window.setTitle("Автоматическое распределение")


    def HandleDestrib(self):
        self.time_table.Hide()
        self.auto_destrib.Hide()
        self.handle_destrib.Show()
        self.window.setTitle("Ручное распределение")

    def ShowTable(self):
        self.handle_destrib.Hide()
        self.auto_destrib.Hide()
        self.time_table.Show()
        self.window.setTitle("Расписание")



# def app():
#     import sys
#     applic = QtWidgets.QApplication(sys.argv)
#
#     ui = Teacher("AAAAAAAAAA")
#     ui.show()
#
#     sys.exit(applic.exec_())
#
# if __name__ == "__main__":
#     app()
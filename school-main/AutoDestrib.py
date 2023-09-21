from PyQt5 import QtCore, QtGui, QtWidgets
from CRUD import CRUD
import math

class AutoDestrib(object):
    def setupUi(self, Form):

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 90, 381, 300))
        self.textEdit.setObjectName("textEdit")

        self.btn_distrib = QtWidgets.QPushButton(Form)
        self.btn_distrib.setGeometry(QtCore.QRect(20, 390, 381, 23))
        self.btn_distrib.setObjectName("btn_distrib")

        self.lbl_enter = QtWidgets.QLabel(Form)
        self.lbl_enter.setGeometry(QtCore.QRect(20, 30, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_enter.setFont(font)
        self.lbl_enter.setObjectName("lbl_enter")

        self.btn_distrib.clicked.connect(self.Destrib)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_distrib.setText(_translate("Form", "Распределить"))
        self.lbl_enter.setText(_translate("Form", "Введите имена и фамилии учеников \n(вводите поочередно, через запятую с пробелом):"))

    def Hide(self):
        self.lbl_enter.hide()
        self.btn_distrib.hide()
        self.textEdit.hide()

    def Show(self):
        self.lbl_enter.show()
        self.btn_distrib.show()
        self.textEdit.show()

    def Destrib(self):
        db = CRUD("users")  # экземпляр создается тут чтобы при любом изменении базы данных программа могла рабоать без перезапуска

        students = self.textEdit.toPlainText().split(", ")
        dates = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]

        def arr_split(arr, n):
            for i in range(0, len(arr), n):
                yield arr[i:i + n]

        splitted_students = list(arr_split(students, math.ceil(len(students) / len(dates))))

        for i in range(0, len(splitted_students)):
            for k in range(0, len(splitted_students[i])):
                print(splitted_students[i][k])
                query = db.Read("users", "*", f"""isTeacher = 0
                                                  AND (name || ' ' || secondName = '{splitted_students[i][k]}'
                                                  OR secondName || ' ' || name = '{splitted_students[i][k]}')""")

                # если ученика нет в базе данных, мы добавляем его туда
                if not len(query) > 0:
                    query = db.Insert("users", "name, secondName, isTeacher",
                                      f"'{splitted_students[i][k].split(' ')[0]}', '{splitted_students[i][k].split(' ')[1]}', 0")

                query = db.Update("users", f"dutyDay='{dates[i]}'", f"""isTeacher = 0
                                                                        AND (name || ' ' || secondName = '{splitted_students[i][k]}'
                                                                        OR secondName || ' ' || name = '{splitted_students[i][k]}')""")
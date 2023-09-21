from PyQt5 import QtCore, QtGui, QtWidgets
from CRUD import CRUD
class HandleDestrib(object):
    def setupUi(self, Form):

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 150, 381, 201))
        self.textEdit.setObjectName("textEdit")

        self.lbl_enter = QtWidgets.QLabel(Form)
        self.lbl_enter.setGeometry(QtCore.QRect(20, 100, 381, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_enter.setFont(font)
        self.lbl_enter.setObjectName("lbl_enter")

        self.lbl_day = QtWidgets.QLabel(Form)
        self.lbl_day.setGeometry(QtCore.QRect(20, 70, 221, 21))
        self.lbl_day.setObjectName("lbl_day")

        self.btn_distrib = QtWidgets.QPushButton(Form)
        self.btn_distrib.setGeometry(QtCore.QRect(20, 360, 381, 23))
        self.btn_distrib.setObjectName("btn_distrib")

        self.cmb_day = QtWidgets.QComboBox(Form)
        self.cmb_day.setGeometry(QtCore.QRect(240, 70, 151, 22))
        self.cmb_day.setObjectName("cmb_day")
        self.cmb_day.addItems(["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"])

        self.btn_distrib.clicked.connect(self.Destribution)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_enter.setText(_translate("Form", "Введите имена и фамитлтт учеников \n(вводите поочередно, через запятую с пробелом):"))
        self.lbl_day.setText(_translate("Form", "Выберете день недели"))
        self.btn_distrib.setText(_translate("Form", "Распределить"))

    def Hide(self):
        self.cmb_day.hide()
        self.lbl_day.hide()
        self.btn_distrib.hide()
        self.lbl_enter.hide()
        self.textEdit.hide()

    def Show(self):
        self.cmb_day.show()
        self.btn_distrib.show()
        self.lbl_day.show()
        self.lbl_enter.show()
        self.textEdit.show()

    def Destribution(self):
        db = CRUD("users") # экземпляр создается тут чтобы при любом изменении базы данных программа могла рабоать без перезапуска
        students = self.textEdit.toPlainText().split(", ")
        date = self.cmb_day.currentText()

        for i in range(0, len(students)):
            query = db.Read("users", "*", f"""isTeacher = 0 
                                             AND (name || ' ' || secondName = '{students[i]}' 
                                             OR secondName || ' ' || name = '{students[i]}')""")

            #если ученика нет в базе данных, мы добавляем его туда
            if not len(query) > 0:
                query = db.Insert("users", "name, secondName, isTeacher", f"'{students[i].split(' ')[0]}', '{students[i].split(' ')[1]}', 0")

            query = db.Update("users", f"dutyDay='{date}'", f"""isTeacher = 0 
                                                                   AND (name || ' ' || secondName = '{students[i]}' 
                                                                   OR secondName || ' ' || name = '{students[i]}')""")


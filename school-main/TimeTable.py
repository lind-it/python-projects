from PyQt5 import QtCore, QtGui, QtWidgets
from CRUD import CRUD

class TimeTable(object):
    def setupUi(self, Form):
        self.cmb_day = QtWidgets.QComboBox(Form)
        self.cmb_day.setGeometry(QtCore.QRect(20, 30, 151, 41))
        self.cmb_day.setObjectName("comboBox")
        self.cmb_day.addItems(["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"])

        self.txt_time = QtWidgets.QTextBrowser(Form)
        self.txt_time.setGeometry(QtCore.QRect(20, 70, 401, 371))
        self.txt_time.setObjectName("textBrowser")

        self.cmb_day.currentTextChanged.connect(self.ShowData)
        self.ShowData()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def Hide(self):
        self.cmb_day.hide()
        self.txt_time.hide()

    def Show(self):
        self.cmb_day.show()
        self.txt_time.show()

    def ShowData(self):
        db = CRUD("users") # экземпляр создается тут чтобы при любом изменении базы данных программа могла рабоать без перезапуска

        dutyDay = self.cmb_day.currentText()
        data = db.Read("users", "name ||' '|| secondName as Name", f"isTeacher = 0 AND dutyDay = '{dutyDay}'")
        text = ""

        # это условие нужно, чтобы программа не вылетала, если на выбранный день нету назначенных учеников
        if (len(data) > 0):

            # объединяем данные в одну строку
            text += data[0][0]
            for i in range(1, len(data)):
                for j in range(0, len(data[i])):
                    text += ", "
                    text += data[i][j]

        self.txt_time.setText(text)

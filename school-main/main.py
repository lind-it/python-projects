from PyQt5 import QtCore, QtGui, QtWidgets
from CRUD import CRUD
from teacher import Teacher
from student import Student
import sys

class Ui_Form(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setObjectName("Form")
        self.resize(495, 497)

        self.db = CRUD("users")

        self.menu = QtWidgets.QTabWidget(self)
        self.menu.setGeometry(QtCore.QRect(30, 30, 421, 421))
        self.menu.setObjectName("menu")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.si_btn = QtWidgets.QPushButton(self.tab)
        self.si_btn.setEnabled(True)
        self.si_btn.setGeometry(QtCore.QRect(110, 330, 201, 51))
        self.si_btn.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"border:none;")
        self.si_btn.setObjectName("si_btn")

        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 281))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.si_lbl_login = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.si_lbl_login.setFont(font)
        self.si_lbl_login.setObjectName("si_lbl_login")
        self.verticalLayout.addWidget(self.si_lbl_login)

        self.si_edit_login = QtWidgets.QLineEdit(self.layoutWidget)
        self.si_edit_login.setStyleSheet("")
        self.si_edit_login.setObjectName("si_edit_login")
        self.verticalLayout.addWidget(self.si_edit_login)

        self.si_lbl_pass = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.si_lbl_pass.setFont(font)
        self.si_lbl_pass.setObjectName("si_lbl_pass")
        self.verticalLayout.addWidget(self.si_lbl_pass)

        self.si_edit_pass = QtWidgets.QLineEdit(self.layoutWidget)
        self.si_edit_pass.setObjectName("si_edit_pass")
        self.verticalLayout.addWidget(self.si_edit_pass)

        self.si_lbl_confPass = QtWidgets.QLabel(self.layoutWidget)
        self.si_lbl_confPass.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.si_lbl_confPass.setFont(font)
        self.si_lbl_confPass.setObjectName("si_lbl_confPass")
        self.verticalLayout.addWidget(self.si_lbl_confPass)

        self.si_edit_confPass = QtWidgets.QLineEdit(self.layoutWidget)
        self.si_edit_confPass.setEnabled(True)
        self.si_edit_confPass.setObjectName("si_edit_confPass")
        self.verticalLayout.addWidget(self.si_edit_confPass)

        self.si_lbl_name = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.si_lbl_name.setFont(font)
        self.si_lbl_name.setObjectName("si_lbl_name")
        self.verticalLayout.addWidget(self.si_lbl_name)

        self.si_edit_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.si_edit_name.setObjectName("si_edit_name")
        self.verticalLayout.addWidget(self.si_edit_name)

        self.si_lbl_secondName = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.si_lbl_secondName.setFont(font)
        self.si_lbl_secondName.setObjectName("si_lbl_secondName")
        self.verticalLayout.addWidget(self.si_lbl_secondName)

        self.si_edit_secondName = QtWidgets.QLineEdit(self.layoutWidget)
        self.si_edit_secondName.setObjectName("si_edit_secondName")
        self.verticalLayout.addWidget(self.si_edit_secondName)
        self.si_chek_isTeacher = QtWidgets.QCheckBox(self.layoutWidget)
        self.si_chek_isTeacher.setObjectName("si_chek_isTeacher")
        self.verticalLayout.addWidget(self.si_chek_isTeacher)

        self.si_lbl_error = QtWidgets.QLabel(self.tab)
        self.si_lbl_error.setGeometry(QtCore.QRect(110, 300, 201, 16))
        self.si_lbl_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.si_lbl_error.setText("")
        self.si_lbl_error.setObjectName("si_lbl_error")

        self.menu.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 120, 391, 121))
        self.layoutWidget_2.setObjectName("layoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.log_lbl_login = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log_lbl_login.setFont(font)
        self.log_lbl_login.setObjectName("log_login_label")
        self.verticalLayout_2.addWidget(self.log_lbl_login)

        self.log_edit_login = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.log_edit_login.setStyleSheet("")
        self.log_edit_login.setObjectName("log_login_edit")
        self.verticalLayout_2.addWidget(self.log_edit_login)

        self.log_lbl_password = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log_lbl_password.setFont(font)
        self.log_lbl_password.setObjectName("log_password_label")
        self.verticalLayout_2.addWidget(self.log_lbl_password)

        self.log_edit_password = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.log_edit_password.setText("")
        self.log_edit_password.setObjectName("log_password_edit")
        self.verticalLayout_2.addWidget(self.log_edit_password)

        self.log_btn = QtWidgets.QPushButton(self.tab_2)
        self.log_btn.setEnabled(True)
        self.log_btn.setGeometry(QtCore.QRect(120, 270, 201, 51))
        self.log_btn.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"border:none;")
        self.log_btn.setObjectName("login_btn")

        self.log_lbl_error = QtWidgets.QLabel(self.tab_2)
        self.log_lbl_error.setGeometry(QtCore.QRect(110, 220, 201, 16))
        self.log_lbl_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.log_lbl_error.setText("")
        self.log_lbl_error.setObjectName("log_lbl_error")

        self.menu.addTab(self.tab_2, "")

        self.si_btn.clicked.connect(self.Sign_in)
        self.log_btn.clicked.connect(self.Log_in)

        self.retranslateUi(self)
        self.menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.si_btn.setText(_translate("Form", "Регистрация"))
        self.si_lbl_login.setText(_translate("Form", "Логин:"))
        self.si_edit_login.setPlaceholderText(_translate("Form", "Придумайте свой логин"))
        self.si_lbl_pass.setText(_translate("Form", "Пароль:"))
        self.si_edit_pass.setPlaceholderText(_translate("Form", "Придумайте свой пароль"))
        self.si_lbl_confPass.setText(_translate("Form", "Подтвердите пароль:"))
        self.si_edit_confPass.setPlaceholderText(_translate("Form", "Подтвердите пароль"))
        self.si_lbl_name.setText(_translate("Form", "Имя:"))
        self.si_edit_name.setPlaceholderText(_translate("Form", "Введите свое имя"))
        self.si_lbl_secondName.setText(_translate("Form", "Фамилия:"))
        self.si_edit_secondName.setPlaceholderText(_translate("Form", "Введите сою фамилию"))
        self.si_chek_isTeacher.setText(_translate("Form", "Учитель"))
        self.menu.setTabText(self.menu.indexOf(self.tab), _translate("Form", "Регистрация"))
        self.log_lbl_login.setText(_translate("Form", "Логин:"))
        self.log_edit_login.setPlaceholderText(_translate("Form", "Введите свой логин"))
        self.log_lbl_password.setText(_translate("Form", "Пароль:"))
        self.log_edit_password.setPlaceholderText(_translate("Form", "Введите свой пароль"))
        self.log_btn.setText(_translate("Form", "Войти"))
        self.menu.setTabText(self.menu.indexOf(self.tab_2), _translate("Form", "Вход"))


    def Sign_in(self):
        self.si_lbl_error.setText("")  # очищаем поле error

        login = self.si_edit_login.text()
        password = self.si_edit_pass.text()
        conf_password = self.si_edit_confPass.text()
        name = self.si_edit_name.text()
        second_name = self.si_edit_secondName.text()
        is_teacher = self.si_chek_isTeacher.isChecked()

        if not 3 <= len(login) <= 10:
            self.si_lbl_error.setText("логин не соответствует размеру")
            return 0

        if not 3 <= len(password) <= 10:
            self.si_lbl_error.setText("пароль не соответствует размеру")
            return 0

        if not password == conf_password:
            self.si_lbl_error.setText("пароли не совпадают")
            return 0

        if len(name) < 1:
            self.si_lbl_error.setText("Имя не должно быть пустым")
            return 0

        if len(second_name) < 1:
            self.si_lbl_error.setText("Фамилия не должна быть пустой")
            return 0

        query = self.db.Read("users", "*", f""" name || ' ' || secondName = '{name + " " + second_name}'
                                                OR secondName || ' ' || name = '{second_name + " " + name}'""")

        # если человека не в базе данных, добавляем его туда
        if not len(query) > 0:
            second_query = self.db.Insert("users", "login, password, name, secondName, isTeacher", f"'{login}', '{password}', '{name}', '{second_name}', {is_teacher}")
        # если человек уже находится в базе данных, добавляем туда логин и пароль (относится только к ученикам)
        else:
            second_query = self.db.Update("users", f"login = '{login}', password = '{password}'", f"""isTeacher = 0
                                                     AND (name || ' ' || secondName = '{name + " " + second_name}'
                                                     OR secondName || ' ' || name = '{second_name + " " + name}')""")


        if second_query == 1:
            self.Run(is_teacher, name + " " + second_name)

        elif second_query == 2067:
            self.si_lbl_error.setText("login занят")

        elif query == 0 or second_query == 0:
            self.si_lbl_error.setText("Ошибка базы данных")


    def Log_in(self):
        self.log_lbl_error.setText("")
        login = self.log_edit_login.text()
        password = self.log_edit_password.text()

        result = self.db.Read("users", "name, secondName, isTeacher", f"login='{login}' AND password='{password}'")

        if result == 0:
            self.log_lbl_error.setText("Ошибка базы данных")
            return 0

        if len(result) == 0:
            self.log_lbl_error.setText("пользователь не найден")
        else:
            self.Run(result[0][2], result[0][0] + " " + result[0][1])


    def Run(self, is_teacher, name, login):
        if is_teacher:
            teacher_app = Teacher(name)
            teacher_app.show()
        else:
            student_app = Student(name, login) # логин передается для тоого, чтобы ижбуежать ошибок с одинаковыми фамилиями и имена учеников
            student_app.show()



def app():

    applic = QtWidgets.QApplication(sys.argv)

    ui = Ui_Form()
    ui.show()

    sys.exit(applic.exec_())

if __name__ == "__main__":
    app()
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from CRUD import CRUD

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(563, 486)
        self.menu = QtWidgets.QTabWidget(Form)
        self.menu.setGeometry(QtCore.QRect(70, 50, 421, 321))
        self.menu.setObjectName("menu")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.si_btn = QtWidgets.QPushButton(self.tab)
        self.si_btn.setEnabled(True)
        self.si_btn.setGeometry(QtCore.QRect(110, 240, 201, 51))
        self.si_btn.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"border:none;")
        self.si_btn.setObjectName("si_btn")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 202))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.si_login_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.si_login_label.setFont(font)
        self.si_login_label.setObjectName("si_login_label")
        self.verticalLayout.addWidget(self.si_login_label)
        self.si_login_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.si_login_edit.setStyleSheet("")
        self.si_login_edit.setObjectName("si_login_edit")
        self.verticalLayout.addWidget(self.si_login_edit)
        self.si_password_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.si_password_label.setFont(font)
        self.si_password_label.setObjectName("si_password_label")
        self.verticalLayout.addWidget(self.si_password_label)
        self.si_password_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.si_password_edit.setText("")
        self.si_password_edit.setObjectName("si_password_edit")
        self.verticalLayout.addWidget(self.si_password_edit)
        self.si_conf_pass_label = QtWidgets.QLabel(self.layoutWidget)
        self.si_conf_pass_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.si_conf_pass_label.setFont(font)
        self.si_conf_pass_label.setObjectName("si_conf_pass_label")
        self.verticalLayout.addWidget(self.si_conf_pass_label)
        self.si_conf_pass_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.si_conf_pass_edit.setEnabled(True)
        self.si_conf_pass_edit.setObjectName("si_conf_pass_edit")
        self.verticalLayout.addWidget(self.si_conf_pass_edit)
        self.si_email_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.si_email_label.setFont(font)
        self.si_email_label.setObjectName("si_email_label")
        self.verticalLayout.addWidget(self.si_email_label)
        self.si_email_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.si_email_edit.setObjectName("si_email_edit")
        self.verticalLayout.addWidget(self.si_email_edit)
        self.si_error = QtWidgets.QLabel(self.tab)
        self.si_error.setGeometry(QtCore.QRect(110, 220, 201, 16))
        self.si_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.si_error.setText("")
        self.si_error.setObjectName("si_error")
        self.menu.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 391, 191))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.log_login_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log_login_label.setFont(font)
        self.log_login_label.setObjectName("log_login_label")
        self.verticalLayout_2.addWidget(self.log_login_label)
        self.log_login_edit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.log_login_edit.setStyleSheet("")
        self.log_login_edit.setObjectName("log_login_edit")
        self.verticalLayout_2.addWidget(self.log_login_edit)
        self.log_password_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log_password_label.setFont(font)
        self.log_password_label.setObjectName("log_password_label")
        self.verticalLayout_2.addWidget(self.log_password_label)
        self.log_password_edit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.log_password_edit.setText("")
        self.log_password_edit.setObjectName("log_password_edit")
        self.verticalLayout_2.addWidget(self.log_password_edit)
        self.log_email_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log_email_label.setFont(font)
        self.log_email_label.setObjectName("log_email_label")
        self.verticalLayout_2.addWidget(self.log_email_label)
        self.log_email_edit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.log_email_edit.setObjectName("log_email_edit")
        self.verticalLayout_2.addWidget(self.log_email_edit)
        self.log_btn = QtWidgets.QPushButton(self.tab_2)
        self.log_btn.setEnabled(True)
        self.log_btn.setGeometry(QtCore.QRect(110, 240, 201, 51))
        self.log_btn.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"border:none;")
        self.log_btn.setObjectName("log_btn")
        self.log_error = QtWidgets.QLabel(self.tab_2)
        self.log_error.setGeometry(QtCore.QRect(110, 220, 201, 16))
        self.log_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.log_error.setText("")
        self.log_error.setObjectName("log_error")
        self.menu.addTab(self.tab_2, "")

        self.db = CRUD("sign")
        self.si_btn.clicked.connect(self.SignIn)
        self.log_btn.clicked.connect(self.LogIn)

        self.retranslateUi(Form)
        self.menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.si_btn.setText(_translate("Form", "sign in"))
        self.si_login_label.setText(_translate("Form", "login:"))
        self.si_login_edit.setPlaceholderText(_translate("Form", "enter your login"))
        self.si_password_label.setText(_translate("Form", "password:"))
        self.si_password_edit.setPlaceholderText(_translate("Form", "enter your password"))
        self.si_conf_pass_label.setText(_translate("Form", "confirm password:"))
        self.si_conf_pass_edit.setPlaceholderText(_translate("Form", "confirm your password"))
        self.si_email_label.setText(_translate("Form", "email:"))
        self.si_email_edit.setPlaceholderText(_translate("Form", "enter your email"))
        self.menu.setTabText(self.menu.indexOf(self.tab), _translate("Form", "sign in"))
        self.log_login_label.setText(_translate("Form", "login:"))
        self.log_login_edit.setPlaceholderText(_translate("Form", "enter your login"))
        self.log_password_label.setText(_translate("Form", "password:"))
        self.log_password_edit.setPlaceholderText(_translate("Form", "enter your password"))
        self.log_email_label.setText(_translate("Form", "email:"))
        self.log_email_edit.setPlaceholderText(_translate("Form", "enter your email"))
        self.log_btn.setText(_translate("Form", "log in"))
        self.menu.setTabText(self.menu.indexOf(self.tab_2), _translate("Form", "log in"))


    def SignIn(self):
        self.si_error.setText("")  # очищаем поле error
        login = self.si_login_edit.text()
        password = self.si_password_edit.text()
        conf_password = self.si_conf_pass_edit.text()
        email = self.si_email_edit.text()

        if not 3 <= len(login) <= 10:
            self.si_error.setText("логин не соответствует размеру")
            return 0
        if not 3 <= len(password) <= 10:
            self.si_error.setText("пароль не соответствует размеру")
            return 0
        if not password == conf_password:
            self.si_error.setText("пароли не совпадают")
            return 0
        if not 3 <= len(email) <= 10:
            self.si_error.setText("email не соответствует размеру")
            return 0
        if not "@" in email:
            self.si_error.setText("email должен содержать символ @")
            return 0


        query = self.db.Insert("user", "'login', 'pass', 'email'", f"'{login}', '{password}', '{email}'")
        print(query)

        if query == 1:
            self.Message("Вы успешно зарегестрировались")
        elif query == 2067:
            self.si_error.setText("login занят")
            self.db.Close()
        elif query == 0:
            self.si_error.setText("Ошибка базы данных")
            self.db.Close()

    def LogIn(self):
        self.log_error.setText("")
        login = self.log_login_edit.text()
        password = self.log_password_edit.text()
        email = self.log_email_edit.text()

        result = self.db.Read("user", "*", f"login='{login}' AND pass='{password}' AND email='{email}'")

        if len(result) == 0:
            self.log_error.setText("пользователь не найден")
        else:
            self.Message("Вы вошли")

    def Message(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Успех!")
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

def app():
    applic = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    ui = Ui_Form()
    ui.setupUi(window)

    window.show()
    sys.exit(applic.exec_())

if __name__ == "__main__":
    app()
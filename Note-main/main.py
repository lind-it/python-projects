import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from  note import Note

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(600, 800
                    )
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.btn_addTask = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addTask.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_addTask.setObjectName("btn_addTask")
        self.verticalLayout_2.addWidget(self.btn_addTask)

        self.menu = QtWidgets.QScrollArea(self.centralwidget)
        self.menu.setMinimumSize(QtCore.QSize(100, 50))
        self.menu.setWidgetResizable(True)
        self.menu.setObjectName("menu")

        self.menu_content = QtWidgets.QWidget()
        self.menu_content.setEnabled(True)
        self.menu_content.setGeometry(QtCore.QRect(0, 0, 559, 658))
        self.menu_content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menu_content.setObjectName("menu_content")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.menu_content)
        self.verticalLayout.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.spacerItem)

        self.menu.setWidget(self.menu_content)
        self.verticalLayout_2.addWidget(self.menu)

        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 579, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.btn_addTask.clicked.connect(self.Add_note)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_addTask.setText(_translate("MainWindow", "Добавить задачу"))

    def Add_note(self):
        note = Note()
        self.verticalLayout.insertWidget(0, note)

if __name__ == "__main__":
    applic = QtWidgets.QApplication(sys.argv)

    ui = Ui_MainWindow()
    ui.show()

    sys.exit(applic.exec_())
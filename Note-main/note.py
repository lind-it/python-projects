# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Note(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Note")
        self.setEnabled(True)
        self.resize(485, 150)
        self.setMinimumSize(QtCore.QSize(0, 150))
        self.setMaximumSize(QtCore.QSize(16777215, 150))

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.chek_IsComplited = QtWidgets.QCheckBox(self)
        self.chek_IsComplited.setText("")
        self.chek_IsComplited.setObjectName("chek_IsComplited")
        self.gridLayout.addWidget(self.chek_IsComplited, 0, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(283, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)

        self.btn_noteEdit = QtWidgets.QPushButton(self)
        self.btn_noteEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_noteEdit.setObjectName("btn_noteEdit")
        self.gridLayout.addWidget(self.btn_noteEdit, 0, 2, 1, 1)

        self.btn_noteDelete = QtWidgets.QPushButton(self)
        self.btn_noteDelete.setStyleSheet("background-color: rgb(255, 6, 6);")
        self.btn_noteDelete.setObjectName("btn_noteDelete")
        self.gridLayout.addWidget(self.btn_noteDelete, 0, 3, 1, 1)

        self.txtEd_noteTextEdit = QtWidgets.QTextEdit(self)
        self.txtEd_noteTextEdit.setEnabled(True)
        self.txtEd_noteTextEdit.setMinimumSize(QtCore.QSize(0, 100))
        self.txtEd_noteTextEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtEd_noteTextEdit.setFont(font)
        self.txtEd_noteTextEdit.setStyleSheet("border: none;\n"
"border-bottom: 1px solid;\n"
"")
        self.txtEd_noteTextEdit.setPlaceholderText("Введите текст")
        self.txtEd_noteTextEdit.setObjectName("txt_noteTextEdit")
        self.gridLayout.addWidget(self.txtEd_noteTextEdit, 1, 0, 1, 4)

        self.txt_noteText = QtWidgets.QTextBrowser(self)
        self.txt_noteText.setEnabled(True)
        self.txt_noteText.setMinimumSize(QtCore.QSize(0, 100))
        self.txt_noteText.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_noteText.setFont(font)
        self.txt_noteText.setStyleSheet("border: none;\n"
                                        "border-bottom: 1px solid;\n")
        self.txt_noteText.setObjectName("txt_noteText")
        self.gridLayout.addWidget(self.txt_noteText, 1, 0, 1, 4)
        self.txt_noteText.hide()


        self.isEdit = True
        self.btn_noteDelete.clicked.connect(self.Delete)
        self.btn_noteEdit.clicked.connect(self.Edit)
        self.chek_IsComplited.stateChanged.connect(self.isCompleted)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Note", "Note"))
        self.btn_noteEdit.setText(_translate("Form", "✓"))
        self.btn_noteDelete.setText(_translate("Form", "X"))

    def Delete(self):
        self.hide()

    def Edit(self):
        if self.isEdit:

            self.txt_noteText.setText(self.txtEd_noteTextEdit.toPlainText())

            self.txtEd_noteTextEdit.hide()
            self.txt_noteText.show()

            self.btn_noteEdit.setText("🖊")
            self.isEdit = False

        elif not self.isEdit:

            self.txtEd_noteTextEdit.setText(self.txt_noteText.toPlainText())

            self.txt_noteText.hide()
            self.txtEd_noteTextEdit.show()

            self.btn_noteEdit.setText("✓")
            self.isEdit = True

    def isCompleted(self):
        if self.chek_IsComplited.checkState():

            self.txt_noteText.setText(self.txtEd_noteTextEdit.toPlainText())

            self.txtEd_noteTextEdit.hide()
            self.txt_noteText.show()

            self.txt_noteText.setStyleSheet(self.txt_noteText.styleSheet() + "text-decoration: line-through;") # делаем текст зарекнутым

            self.btn_noteEdit.setText("🖊")
            self.isEdit = False

            self.btn_noteEdit.setEnabled(False) # выключаем кнопку для взаимодействия

        elif not self.chek_IsComplited.checkState():

            self.txt_noteText.setStyleSheet(self.txtEd_noteTextEdit.styleSheet())
            self.btn_noteEdit.setEnabled(True) # включаем кнопку для взаимодействи
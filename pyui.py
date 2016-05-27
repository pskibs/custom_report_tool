# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Report_UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 460)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 420, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 220, 361, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.username_input = QtWidgets.QLineEdit(Dialog)
        self.username_input.setGeometry(QtCore.QRect(20, 100, 113, 20))
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(Dialog)
        self.password_input.setGeometry(QtCore.QRect(20, 139, 113, 21))
        self.password_input.setObjectName("password_input")
        self.sqlserver_input = QtWidgets.QLineEdit(Dialog)
        self.sqlserver_input.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.sqlserver_input.setObjectName("sqlserver_input")
        self.sqlserverlabel = QtWidgets.QLabel(Dialog)
        self.sqlserverlabel.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.sqlserverlabel.setObjectName("sqlserverlabel")
        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(20, 120, 47, 13))
        self.password_label.setObjectName("password_label")
        self.query_label = QtWidgets.QLabel(Dialog)
        self.query_label.setGeometry(QtCore.QRect(20, 190, 47, 20))
        self.query_label.setObjectName("query_label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.sqlserverlabel.setText(_translate("Dialog", "SQL Server"))
        self.username_label.setText(_translate("Dialog", "Username"))
        self.password_label.setText(_translate("Dialog", "Password"))
        self.query_label.setText(_translate("Dialog", "Query"))


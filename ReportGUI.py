# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import pymssql
from PyQt5 import QtCore, QtGui, QtWidgets
import re,decimal
import _mssql as msql
#
global_query = r"""
DECLARE	@return_value int

EXEC	@return_value = [dbo].[ReportAddUpdate]
		@ReportID = NULL,
		@ReportType = 1,
		@ViewName = N'QUERYBUILDER',
		@Name = N'[REPORTNAME]',
		@Description = N'[REPORTDESCRIPTION]',
		@SQLQuery = N'[SQLQUERY]',
		@ColumnList = N'[COLUMNLIST]',
		@FunctionList = NULL,
		@OrderList = NULL,
		@Criteria = NULL,
		@GroupList = NULL,
		@GroupSummaryList = NULL,
		@ColumnVisibility = N'[COLUMNVISIBILITY]'

SELECT	'Return Value' = @return_value
"""

queryrx_str = (r'select\s(.*?)\sfrom')
QRX = re.compile(queryrx_str, re.IGNORECASE)

class Ui_Dialog(object):


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialogue")
        Dialog.resize(400, 460)


        self.sqlserver_input = QtWidgets.QLineEdit(Dialog)
        self.sqlserver_input.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.sqlserver_input.setObjectName("sqlserver_input")

        self.sqlserverlabel = QtWidgets.QLabel(Dialog)
        self.sqlserverlabel.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.sqlserverlabel.setObjectName("sqlserverlabel")

        self.username_input = QtWidgets.QLineEdit(Dialog)
        self.username_input.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.username_input.setObjectName("username_input")

        self.password_input = QtWidgets.QLineEdit(Dialog)
        self.password_input.setGeometry(QtCore.QRect(20, 119, 113, 21))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")

        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.username_label.setObjectName("username_label")

        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.password_label.setObjectName("password_label")

        self.query_label = QtWidgets.QLabel(Dialog)
        self.query_label.setGeometry(QtCore.QRect(20, 190, 47, 20))
        self.query_label.setObjectName("query_label")

        self.secret_pass_label = QtWidgets.QLabel(Dialog)
        self.secret_pass_label.setGeometry(QtCore.QRect(230, 30, 81, 16))
        self.secret_pass_label.setObjectName("secret_pass_label")

        self.secret_pass_input = QtWidgets.QLineEdit(Dialog)
        self.secret_pass_input.setGeometry(QtCore.QRect(230, 50, 131, 20))
        self.secret_pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secret_pass_input.setObjectName("secret_pass_input")


        self.connect_button = QtWidgets.QPushButton(Dialog)
        self.connect_button.setGeometry(QtCore.QRect(20, 160, 75, 23))
        self.connect_button.setObjectName("connect_button")



        self.connection_status = QtWidgets.QLabel(Dialog)
        self.connection_status.setGeometry(QtCore.QRect(130, 160, 71, 16))
        self.connection_status.setObjectName("connection_status")



        self.report_name_label = QtWidgets.QLabel(Dialog)
        self.report_name_label.setGeometry(QtCore.QRect(230, 70, 81, 16))
        self.report_name_label.setObjectName("report_name_label")

        self.report_name_input = QtWidgets.QLineEdit(Dialog)
        self.report_name_input.setGeometry(QtCore.QRect(230, 90, 131, 20))
        self.report_name_input.setText("")
        self.report_name_input.setObjectName("report_name_input")

        self.report_description_labl = QtWidgets.QLabel(Dialog)
        self.report_description_labl.setGeometry(QtCore.QRect(230, 110, 101, 16))
        self.report_description_labl.setObjectName("report_description_labl")

        self.report_description_input = QtWidgets.QLineEdit(Dialog)
        self.report_description_input.setGeometry(QtCore.QRect(230, 129, 131, 21))
        self.report_description_input.setText("")
        self.report_description_input.setObjectName("report_description_input")

        self.report_description_labl = QtWidgets.QLabel(Dialog)
        self.report_description_labl.setGeometry(QtCore.QRect(230, 110, 101, 16))
        self.report_description_labl.setObjectName("report_description_labl")

        self.column_list_input = QtWidgets.QLineEdit(Dialog)
        self.column_list_input.setGeometry(QtCore.QRect(130, 190, 241, 21))
        self.column_list_input.setText("")
        self.column_list_input.setObjectName("column_list_input")

        self.column_list_label = QtWidgets.QLabel(Dialog)
        self.column_list_label.setGeometry(QtCore.QRect(210, 170, 71, 16))
        self.column_list_label.setObjectName("column_list_label")


        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 220, 361, 191))
        self.textEdit.setObjectName("textEdit")





        self.connection = object
        self.cursor = object


        #SUBMIT BUTTON
        self.submit_button = QtWidgets.QPushButton(Dialog)
        self.submit_button.setGeometry(QtCore.QRect(300,415,80,30))
        self.submit_button.setObjectName("submit_button")
        self.submit_button.setText("Submit")
        self.submit_button.setHidden(True)


        #HIDE UI ELEMENTS
        self.report_name_label.setHidden(True)
        self.report_name_input.setHidden(True)

        self.report_description_input.setHidden(True)
        self.report_description_labl.setHidden(True)

        self.column_list_label.setHidden(True)
        self.column_list_input.setHidden(True)


        self.is_connected = False
        self.sql_query_text = object


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def set_not_connected(self):
        self.connection_status.setText('INVALID!')
        self.connection_status.setStyleSheet('color: red')

    def set_success_connected(self):


        if self.secret_pass_input.text() == 'L0sen0rd':
            self.secret_pass_input.setHidden(True)
            self.secret_pass_label.setHidden(True)
            self.connection_status.setText('Connected')
            self.connection_status.setStyleSheet('color: green')
            if self.is_connected == True:
                self.submit_button.setHidden(False)
                # HIDE UI ELEMENTS
                self.report_name_label.setHidden(False)
                self.report_name_input.setHidden(False)

                self.report_description_input.setHidden(False)
                self.report_description_labl.setHidden(False)

                self.column_list_label.setHidden(False)
                self.column_list_input.setHidden(False)
        else:
            mbw = QtWidgets.QMessageBox()
            mbw.setText("Alert Box")
            mbw.setInformativeText("Error! Wrong SnowCode")
            mbw.setWindowTitle("ERROR!")
            mbw.setIcon(QtWidgets.QMessageBox.Critical)
            mbw.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.set_not_connected()
            mbw.exec_()


    def submit_sql(self):

        mb = QtWidgets.QMessageBox()
        try:

            report_str = self.generate_report_with_strings(self.report_name_input.text(),\
                                              self.report_description_input.text(),\
                                              self.textEdit.toPlainText(), self.column_list_input.text())


            res = self.connection.execute_scalar(report_str)
            print(res)

            mb.setText("Alert Box")
            mb.setInformativeText("Successfully Insterted SQL Statement")
            mb.setWindowTitle("Success!")
            mb.setStandardButtons(QtWidgets.QMessageBox.Ok)

            retval = mb.exec_()



        except Exception as e:
            print(e)
            print("ERROR")
            print(self.textEdit.toPlainText())
            mb.setText("Alert Box")
            mb.setInformativeText("Error Inserting SQL")
            mb.setWindowTitle("ERROR!")
            mb.setStandardButtons(QtWidgets.QMessageBox.Ok)

            retval = mb.exec_()



    def connect_curse(self):
        try:
            self.connection = msql.connect(server=self.sqlserver_input.text(),user=self.username_input.text()\
                                          ,password=self.password_input.text(),database='SnowLicenseManager')

            self.is_connected = True
            self.set_success_connected()
        except Exception as e:
            print(e)
            self.set_not_connected()


    def connect_to_sql(self, sqlconnection):
        self.connection_status.setText('Connecting...')
        self.connection_status.setStyleSheet('color: orange')
        self.connect_curse()

    def generate_report_with_strings(self, name, desc, sql_q, col_list):
        dd = sql_q.replace("'","''")
        report_string = global_query.replace('[REPORTNAME]',name)
        report_string = report_string.replace('[REPORTDESCRIPTION]',desc)
        report_string = report_string.replace('[SQLQUERY]',dd)
        report_string = report_string.replace('[COLUMNLIST]',col_list)

        column_visibility = col_list.split(',')



        print('*'*100)

        visibility_numbers = [str(1) for x in column_visibility]
        comma = ","

        column_visibility_replace = comma.join(visibility_numbers)

        report_string = report_string.replace('[COLUMNVISIBILITY]',column_visibility_replace)

        print(report_string)

        print('*' * 100)

        return report_string






    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Custom Report Generator"))
        self.sqlserverlabel.setText(_translate("Dialog", "SQL Server"))
        self.username_label.setText(_translate("Dialog", "Username"))
        self.password_label.setText(_translate("Dialog", "Password"))
        self.query_label.setText(_translate("Dialog", "Query"))
        self.connect_button.setText(_translate("Dialog", "Connect"))
        self.connection_status.setText(_translate("Dialog", "Not Connected"))
        self.report_name_label.setText(_translate("Dialogue","Report Name"))
        self.column_list_label.setText(_translate("Dialogue", "Column List"))
        self.report_description_labl.setText(_translate("Dialog", "Report Description"))
        self.secret_pass_label.setText(_translate("Dialog", "SnowCode"))

        self.connect_button.clicked.connect(self.connect_to_sql)
        self.submit_button.clicked.connect(self.submit_sql)
#


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    sys.exit(app.exec_())


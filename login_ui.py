# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(368, 231)
        Form.setMinimumSize(QtCore.QSize(368, 231))
        Form.setMaximumSize(QtCore.QSize(368, 231))
        self.label_clave = QtWidgets.QLabel(Form)
        self.label_clave.setGeometry(QtCore.QRect(70, 100, 191, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_clave.setFont(font)
        self.label_clave.setObjectName("label_clave")
        self.btn_ingreso = QtWidgets.QPushButton(Form)
        self.btn_ingreso.setGeometry(QtCore.QRect(140, 160, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.btn_ingreso.setFont(font)
        self.btn_ingreso.setObjectName("btn_ingreso")
        self.text_codigo = QtWidgets.QTextEdit(Form)
        self.text_codigo.setGeometry(QtCore.QRect(70, 50, 231, 31))
        self.text_codigo.setObjectName("text_codigo")
        self.label_codigo = QtWidgets.QLabel(Form)
        self.label_codigo.setGeometry(QtCore.QRect(70, 30, 191, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_codigo.setFont(font)
        self.label_codigo.setObjectName("label_codigo")
        self.text_clave = QtWidgets.QTextEdit(Form)
        self.text_clave.setGeometry(QtCore.QRect(70, 120, 231, 31))
        self.text_clave.setObjectName("text_clave")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "login"))
        self.label_clave.setText(_translate("Form", "Clave de Ingreso:"))
        self.btn_ingreso.setText(_translate("Form", "Ingreso"))
        self.label_codigo.setText(_translate("Form", "Codigo de  empleado:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

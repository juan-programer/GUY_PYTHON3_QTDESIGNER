# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(255, 269)
        Form.setMaximumSize(QtCore.QSize(255, 269))
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(10, 220, 90, 21))
        self.checkBox.setObjectName("checkBox")
        self.btn_cancelar = QtWidgets.QPushButton(Form)
        self.btn_cancelar.setGeometry(QtCore.QRect(180, 230, 71, 31))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.label_longitud = QtWidgets.QLabel(Form)
        self.label_longitud.setGeometry(QtCore.QRect(10, 90, 191, 16))
        self.label_longitud.setObjectName("label_longitud")
        self.label_codos = QtWidgets.QLabel(Form)
        self.label_codos.setGeometry(QtCore.QRect(10, 160, 191, 16))
        self.label_codos.setObjectName("label_codos")
        self.text_update_nom_conde = QtWidgets.QTextEdit(Form)
        self.text_update_nom_conde.setGeometry(QtCore.QRect(10, 40, 231, 31))
        self.text_update_nom_conde.setObjectName("text_update_nom_conde")
        self.text_update_cod = QtWidgets.QTextEdit(Form)
        self.text_update_cod.setGeometry(QtCore.QRect(10, 180, 231, 31))
        self.text_update_cod.setObjectName("text_update_cod")
        self.btn_update = QtWidgets.QPushButton(Form)
        self.btn_update.setGeometry(QtCore.QRect(100, 230, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.btn_update.setFont(font)
        self.btn_update.setMouseTracking(False)
        self.btn_update.setStyleSheet("rgba:(255, 255, 0);")
        self.btn_update.setObjectName("btn_update")
        self.label_nom_condesadora = QtWidgets.QLabel(Form)
        self.label_nom_condesadora.setGeometry(QtCore.QRect(10, 20, 191, 16))
        self.label_nom_condesadora.setObjectName("label_nom_condesadora")
        self.text_update_long_conde = QtWidgets.QTextEdit(Form)
        self.text_update_long_conde.setGeometry(QtCore.QRect(10, 110, 231, 31))
        self.text_update_long_conde.setObjectName("text_update_long_conde")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "actulizar datos"))
        self.checkBox.setText(_translate("Form", "confirmar"))
        self.btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.label_longitud.setText(_translate("Form", "Longitud  de la Condensadora:"))
        self.label_codos.setText(_translate("Form", "Codos  de la Condensadora:"))
        self.btn_update.setText(_translate("Form", "Actualizar"))
        self.label_nom_condesadora.setText(_translate("Form", "Nonbre de la Condensadora:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

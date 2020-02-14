# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuyCondesadora.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(503, 365)
        self.label_numero1 = QtWidgets.QLabel(Form)
        self.label_numero1.setGeometry(QtCore.QRect(30, 50, 241, 31))
        self.label_numero1.setObjectName("label_numero1")
        self.label_numero2 = QtWidgets.QLabel(Form)
        self.label_numero2.setGeometry(QtCore.QRect(30, 120, 311, 31))
        self.label_numero2.setObjectName("label_numero2")
        self.label_salida = QtWidgets.QLabel(Form)
        self.label_salida.setGeometry(QtCore.QRect(130, 210, 311, 21))
        self.label_salida.setObjectName("label_salida")
        self.text_numerocodos = QtWidgets.QTextEdit(Form)
        self.text_numerocodos.setGeometry(QtCore.QRect(30, 150, 301, 31))
        self.text_numerocodos.setObjectName("text_numerocodos")
        self.text_longitud = QtWidgets.QTextEdit(Form)
        self.text_longitud.setGeometry(QtCore.QRect(30, 80, 301, 31))
        self.text_longitud.setObjectName("text_longitud")
        self.boton_calcular = QtWidgets.QPushButton(Form)
        self.boton_calcular.setGeometry(QtCore.QRect(30, 200, 81, 41))
        self.boton_calcular.setStyleSheet("")
        self.boton_calcular.setObjectName("boton_calcular")
        self.boton_nuevo = QtWidgets.QPushButton(Form)
        self.boton_nuevo.setGeometry(QtCore.QRect(100, 310, 81, 31))
        self.boton_nuevo.setStyleSheet("")
        self.boton_nuevo.setObjectName("boton_nuevo")
        self.boton_limpiar = QtWidgets.QPushButton(Form)
        self.boton_limpiar.setGeometry(QtCore.QRect(210, 310, 81, 31))
        self.boton_limpiar.setStyleSheet("")
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.boton_salir = QtWidgets.QPushButton(Form)
        self.boton_salir.setGeometry(QtCore.QRect(330, 310, 81, 31))
        self.boton_salir.setStyleSheet("")
        self.boton_salir.setObjectName("boton_salir")

        self.retranslateUi(Form)
        self.boton_salir.clicked.connect(Form.close)
        self.boton_limpiar.clicked.connect(self.label_salida.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CONDESADORA 1.0"))
        self.label_numero1.setText(_translate("Form", "<html><head/><body><p>INGRESE LA LONGITUD DE LA CONDENSADORA:</p></body></html>"))
        self.label_numero2.setText(_translate("Form", "<html><head/><body><p>INGRESE LA CANTIDAD DE CODOS DE LA CONDENSADORA:</p></body></html>"))
        self.label_salida.setText(_translate("Form", "LOS CABALLOS DE POTENCIA SON:"))
        self.boton_calcular.setText(_translate("Form", "CALCULAR"))
        self.boton_nuevo.setText(_translate("Form", "NUEVO "))
        self.boton_limpiar.setText(_translate("Form", "LIMPIAR"))
        self.boton_salir.setText(_translate("Form", "SALIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

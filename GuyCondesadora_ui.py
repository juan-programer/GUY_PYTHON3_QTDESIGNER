# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuyCondesadora.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(641, 430)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(1000, 600))
        Form.setStyleSheet("rgba:(0, 170, 255)")
        self.label_numero1 = QtWidgets.QLabel(Form)
        self.label_numero1.setGeometry(QtCore.QRect(20, 130, 311, 31))
        self.label_numero1.setStyleSheet("rgba:(255, 255, 127)")
        self.label_numero1.setObjectName("label_numero1")
        self.label_numero2 = QtWidgets.QLabel(Form)
        self.label_numero2.setGeometry(QtCore.QRect(20, 190, 331, 31))
        self.label_numero2.setObjectName("label_numero2")
        self.label_salida = QtWidgets.QLabel(Form)
        self.label_salida.setGeometry(QtCore.QRect(20, 350, 371, 21))
        self.label_salida.setStyleSheet("rgba:(0, 170, 255)")
        self.label_salida.setObjectName("label_salida")
        self.text_numerocodos = QtWidgets.QTextEdit(Form)
        self.text_numerocodos.setGeometry(QtCore.QRect(20, 220, 301, 31))
        self.text_numerocodos.setObjectName("text_numerocodos")
        self.text_longitud = QtWidgets.QTextEdit(Form)
        self.text_longitud.setGeometry(QtCore.QRect(20, 160, 301, 31))
        self.text_longitud.setObjectName("text_longitud")
        self.boton_calcular = QtWidgets.QPushButton(Form)
        self.boton_calcular.setGeometry(QtCore.QRect(20, 270, 81, 41))
        self.boton_calcular.setStyleSheet("rgba:(255, 255, 127)")
        self.boton_calcular.setObjectName("boton_calcular")
        self.btn_guardar = QtWidgets.QPushButton(Form)
        self.btn_guardar.setGeometry(QtCore.QRect(120, 270, 81, 41))
        self.btn_guardar.setStyleSheet("")
        self.btn_guardar.setObjectName("btn_guardar")
        self.boton_limpiar = QtWidgets.QPushButton(Form)
        self.boton_limpiar.setGeometry(QtCore.QRect(220, 270, 81, 41))
        self.boton_limpiar.setStyleSheet("")
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.boton_salir = QtWidgets.QPushButton(Form)
        self.boton_salir.setGeometry(QtCore.QRect(280, 380, 81, 41))
        self.boton_salir.setStyleSheet("rgba:(255, 255, 255)")
        self.boton_salir.setObjectName("boton_salir")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 20, 141, 41))
        self.label.setObjectName("label")
        self.btn_editar = QtWidgets.QPushButton(Form)
        self.btn_editar.setGeometry(QtCore.QRect(460, 360, 75, 41))
        self.btn_editar.setObjectName("btn_editar")
        self.condensadores_list = QtWidgets.QListWidget(Form)
        self.condensadores_list.setGeometry(QtCore.QRect(380, 20, 231, 331))
        self.condensadores_list.setObjectName("condensadores_list")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 251, 16))
        self.label_2.setObjectName("label_2")
        self.text_nombre = QtWidgets.QTextEdit(Form)
        self.text_nombre.setGeometry(QtCore.QRect(20, 100, 301, 31))
        self.text_nombre.setObjectName("text_nombre")

        self.retranslateUi(Form)
        self.boton_salir.clicked.connect(Form.close)
        self.boton_limpiar.clicked.connect(self.label_salida.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CONDESOFT 1.0"))
        self.label_numero1.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">INGRESE LA LONGITUD DE LA CONDENSADORA EN </span><span style=\" font-size:8pt; font-weight:600; color:#00aaff;\">(cm)</span><span style=\" font-size:8pt; font-weight:600;\">:</span></p></body></html>"))
        self.label_numero2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">INGRESA LA CANTIDAD DE CODOS DE LA CONDENSADORA:</span></p></body></html>"))
        self.label_salida.setText(_translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:8pt; font-weight:600; color:#000000;\">LOS CABALLOS DE POTENCIA SON:</span></p></body></html>"))
        self.text_longitud.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>"))
        self.boton_calcular.setText(_translate("Form", "CALCULAR"))
        self.btn_guardar.setText(_translate("Form", "GUARDAR"))
        self.boton_limpiar.setText(_translate("Form", "LIMPIAR"))
        self.boton_salir.setText(_translate("Form", "SALIR"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#55aaff;\">CONDESOFT</span></p></body></html>"))
        self.btn_editar.setText(_translate("Form", "Editar"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">ESCRIBA EL NOMBRE DE LA CONDENSADORA:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

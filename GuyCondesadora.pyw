#programa para calcular los caballos de potencia de una condesadora.
#cortecia de Svillsoft Companie Diseñado y Desarrollado para Refrivillalobos S.A

import sys
from GuyCondesadora_ui import *
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QImage, QPalette , QBrush 
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMessageBox
class Ventana_principal(QWidget):
        def __init__(self, parent=None):
                QtWidgets.QWidget.__init__(self, parent)
                self.ui=Ui_Form()
                self.ui.setupUi(self)
                self.ui.boton_calcular.clicked.connect(self.calcular)

                Img = QImage('i1.jpg')
                sImg = Img.scaled(QSize(503,365))
                palete = QPalette()
                palete.setBrush(10, QBrush(sImg))
                self.setPalette(palete)


        def calcular(self):
                try:
                        largo = float(self.ui.text_longitud.toPlainText())
                        numero_codos = int(self.ui.text_numerocodos.toPlainText())
                        resultado = calculo_caballo_de_fuerza().calcular(largo,numero_codos)
                        self.ui.label_salida.setText("LOS CABALLOS EN POTENCIA SON: "+str(resultado))
                except Exception as e:
                        self.ui.text_longitud.setText("")
                        self.ui.text_numerocodos.setText("")
                        self.ui.label_salida.setText("DEBE INGRESAR NUMEROS")
                        #self.ui.boton_calcular.clicked.connect(self.show_dialog)
                        self.abrir_mesaje("! ERROR AL GENERAR EL CALCULO  OK PARA INTERTARLO DE NUEVO¡")


        def abrir_mesaje(self, mensaje):
                QMessageBox.about(self, "!  ERROR ¡", mensaje)
                
class calculo_caballo_de_fuerza():
        def calcular(self, largo, numero_codo):
                op1 = ((largo)*(numero_codo)*(2))
                op2 = (op1 / 15)
                if(largo < .0 or numero_codo < 1):
                        return "! CALCULO FALLIDO ¡"
                elif(largo):
                        return str(op2)

if __name__ == "__main__":
        aplicacion_condesadora = QApplication(sys.argv)
        app = Ventana_principal()
        app.show()
        sys.exit(aplicacion_condesadora.exec_())

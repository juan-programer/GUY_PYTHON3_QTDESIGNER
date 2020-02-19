#programa para calcular los caballos de potencia de una condesadora.
#cortecia de Svillsoft Companie Diseñado y Desarrollado para Refrivillalobos S.A

import sys
from GuyCondesadora_ui import *
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QImage, QPalette , QBrush 
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMessageBox
from condensadoraController import condensadoraController
from models.condensadora import condensadora
class Ventana_principal(QWidget):
        def __init__(self, parent=None):
                QtWidgets.QWidget.__init__(self, parent)
                self.ui=Ui_Form()
                self.ui.setupUi(self)
                self.ui.boton_calcular.clicked.connect(self.calcular)
                self.ui.btn_guardar.clicked.connect(self.guardar)
                self.ui.boton_limpiar.clicked.connect(self.limpiar)
                self.ui.btn_editar.clicked.connect(self.editar)
                self.controlCondensadora = condensadoraController()
                self.llenar_items()
                Img = QImage('i1.jpg')
                sImg = Img.scaled(QSize(503,365))
                palete = QPalette()
                palete.setBrush(10, QBrush(sImg))
                self.setPalette(palete)

        def llenar_items(self):
                self.ui.condensadores_list.clear()
                items = self.controlCondensadora.get_all()
                for row in items:
                        self.ui.condensadores_list.addItem(str(row[1]))

        
        def editar(self):
                print("editando...")
        

        def calcular(self):
                try:
                        self.conde = condensadora()
                        self.conde.set_nombre(str(self.ui.text_nombre.toPlainText()))
                        self.conde.set_longitud(float(self.ui.text_longitud.toPlainText()))
                        self.conde.set_cantidad(int(self.ui.text_numerocodos.toPlainText()))
                        resultado = calculo_caballo_de_fuerza().calcular(self.conde.get_longitud(),self.conde.get_cantidad())                        
                        self.conde.set_resultado(resultado)
                        self.ui.label_salida.setText("LOS CABALLOS EN POTENCIA SON: "+str(resultado))
                        return True
                except Exception as e:
                        print(e)
                        self.ui.text_nombre.setText("")
                        self.ui.text_longitud.setText("")
                        self.ui.text_numerocodos.setText("")
                        self.ui.label_salida.setText("DEBE INGRESAR NUMEROS")
                        #self.ui.boton_calcular.clicked.connect(self.show_dialog)
                        self.abrir_mesaje("! ERROR AL GENERAR EL CALCULO  OK PARA INTERTARLO DE NUEVO¡")

        def guardar(self):
                if(self.calcular()):
                        self.controlCondensadora.insertar(self.conde)
                        self.llenar_items()
                        self.limpiar()

        def abrir_mesaje(self, mensaje):
                QMessageBox.about(self, "!  ERROR ¡", mensaje)

        def limpiar(self):
                self.ui.text_nombre.setText("")
                self.ui.text_longitud.setText("")
                self.ui.text_numerocodos.setText("")
                self.ui.label_salida.setText("LOS CABALLOS EN POTENCIA SON: 0")

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


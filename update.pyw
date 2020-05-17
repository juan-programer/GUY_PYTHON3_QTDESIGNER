import sys
from update_ui import *
from PyQt5.QtWidgets import * 
from PyQt5.QtWidgets import QMessageBox
from condensadoraController import condensadoraController
from models.condensadora import condensadora

class ventana_actualaizar(QWidget):
    def __init__(self,parent=None):
                QtWidgets.QWidget.__init__(self, parent)
                self.ui=Ui_Form()
                self.ui.setupUi(self)
                


if __name__ == "__main__":
        aplicacion_actulizar_datos = QApplication(sys.argv)
        app = ventana_actualaizar()
        app.show()
        sys.exit(aplicacion_actulizar_datos.exec_())

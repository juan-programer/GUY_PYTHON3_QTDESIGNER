import sys
from update_ui import *
from PyQt5.QtWidgets import * 

class ventana_actualaizar(QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # falta llamar ste form des de el panel principal
    

if __name__ == "__main__":
    actualizar_datos = QApplication(sys.argv)
    app_actualizar = ventana_actualaizar()
    app_actualizar.show()
    sys.exit(actualizar_datos.exec_())
    

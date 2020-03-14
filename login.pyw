import sys
from login_ui import *
from PyQt5.QtWidgets import *

class ventana_login(QWidget):
    def __init__(self, parent=None):
            QtWidgets.QWidget.__init__(self, parent)
            self.ui=Ui_Form()
            self.ui.setupUi(self)

            #falta lo mas importante

if __name__ ==  "__main__":
    login_app = QApplication(sys.argv)
    login = ventana_login()
    login.show()
    sys.exit(login_app.exec_())
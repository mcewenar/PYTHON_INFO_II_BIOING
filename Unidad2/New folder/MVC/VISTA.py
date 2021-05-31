from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt5.uic import loadUi

class VentanaLog(QDialog):
    def __init__(self):
        super(VentanaLog,self).__init__()
        loadUi('GUI.ui',self)
        self.setup()

    def setup(self):
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def accept(self):
        p = self.campo_password.text()
        u = self.campo_usuario.text()
        resultado = self.__controlador.validarIngreso(u,p)
        print("Ingesado: "+ u +" - "+ p)
        print(resultado)

    def reject(self):
        p = self.campo_password.setText("")
        u = self.campo_usuario.setText("")

    def closeEvent(self,event):
        print("Esta dentro del close")
        self.close()

    def setControlador(self,c):
        self.__controlador = c

        
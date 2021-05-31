from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox

class VentanaLogin(QDialog): #QDialog es la bandeja principal del Qt designer
    def __init__(self):
        super(VentanaLogin,self).__init__()
        loadUi("botones.ui",self)
        self.setup()


    def setup(self):
        self.buttonBox.accepted.connect(self.accept) #ACEEPT Y REJECT ESTÁN PREDEFINIDOS EN LAS SEÑALES DEL DESIGNER
        self.buttonBox.accepted.connect(self.reject)

    def accept(self): #Para recuperar la 
        #informacion desde la interfaz una vez se presiona el botón aeptar
        login = self.campo_usuario.text() #estos nombres se le dan en el QtDesigner en editor de objeto
        password = self.campo_password.text()
         #.text() es un método que
        #sirve para tomar los datos
        #que se le ingresan al Qline
        resultado = self.__controlador.validarIngreso(login,password)
        print("Ingresado: " + login + " " + password)
        print(resultado)

    def reject(self):
        login = self.campo_password.setText("")
        password = self.campo_usuario.setText("")
    
    def closeEvent(self,event):
        print("Dentro del close")
        self.close()

    def setControlador(self,c): #Para verificar en la base de datos
        self.__controlador = c
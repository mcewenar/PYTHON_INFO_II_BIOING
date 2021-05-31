from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QMessageBox
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
        u = self.campo_usuario.text() #estos nombres se le dan en el QtDesigner en editor de objeto
        p = self.campo_password.text() #.text sirve para guardar los datos
        #ingresados desde el widget principal y los guarda a las variables temporales u,p
         #.text() es un método que
        #sirve para tomar los datos
        #que se le ingresan al Qline
        resultado = self.__controlador.validarIngreso(u,p)
        if resultado:
            texto = "Usuario válido"
        else:
            texto = "Usuario inválido"
        msg = QMessageBox(self) #este qmessage viene referencia con el self
        msg.setIcon(QMessageBox.Information) #Imagen
        msg.setText(texto)
        #msg.setInformativeText("This is additional information")
        #msg.setWindowTitle("MessageBox demo")
        #msg.setDetailedText("The details are as follows:")
        msg.show() #para mostrar la bandeja,
        #print("Ingresado: " + u + " " + p)
        #print(resultado)

    def reject(self):
        u = self.campo_password.setText("")
        p = self.campo_usuario.setText("")
    
    def closeEvent(self,event):
        print("Dentro del close")
        self.close()

    def setControlador(self,c): #Para verificar en la base de datos
        self.__controlador = c
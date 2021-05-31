from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QMessageBox
from PyQt5.uic import loadUi

class Ventana_Menu(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi('ventanaprincipal.ui',self)
        self.setup()

    def setup(self): #los botones de la ventana ppal
        self.bingresarp.clicked.connect(self.ingresarPaciente)
        #self.
    
    def ingresarPaciente(self):
        ventanaingreso = Ventana_Ingreso(self)
        ventanaingreso.setcontrolador(self.__mi_controlador)
        ventanaingreso.show()
        self.hide()

        
    def setcontrolador(self,c):
        self.__mi_controlador = c

class Ventana_Ingreso(QDialog): #lo que ingrese acá tiene que ir a coordinador
    def __init__(self,ppal=None):
        super().__init__(ppal)
        self.__VentanaPpal = ppal #creamos un atributo en el cual el objeto
        loadUi("ingresor.ui", self)
        #self.__mi_VentanaPpal = ppal
        self.setup()

    def setup(self):
        self.ingreboton.accepted.connect(self.ingresarPaciente)
    
    def ingresarPaciente(self):
        n = self.nombre.text()
        c = self.cedula.text()
        resultado = self.__mi_controlador.ingresarPaciente(n,c)
        Vmsj = QMessageBox(self)
        if resultado == True:
            Vmsj.setText("Paciente Ingresado con Éxito")
        else:
            Vmsj.setText("Paciente already exist")
        Vmsj.show()
        self.__VentanaPpal.show()
    def setcontrolador(self,c):
        self.__mi_controlador = c



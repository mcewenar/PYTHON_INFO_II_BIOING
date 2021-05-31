import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QMessageBox,QWidget
from PyQt5.uic import loadUi

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal,self).__init__()
        loadUi('ventanaingreso.ui',self)
        #rutina de configuracion
        self.setup()
    def setup(self):
        #se especifica la señal
        self.boton_ingresar.clicked.connect(self.on_click_ingreso)

    def on_click_ingreso(self):
        print("Dentro del slot")
        #aqui creamos una nuva ventana de ingreso
        #pasando la ventana actual (ventanaprincipal)
        #como argumento
        ventana_ingreso = VentanaIngreso(self)
        ventana_ingreso.show()

class VentanaIngreso(QDialog):
    def __init__(self,ppal=None): #hace referencia de la ventana principal, y el none es para que no genere error
        print("Llamando lasegunda ventana")
        super().__init__(ppal)
        loadUi("datosingreso.ui",self)
        self.setup()
    def setup(self):
        #asignamos las señales a los botones de la caja
        #estos botones están preconfigurados
        self.buttonBox.accepted.connect(self.opcion_aceptar)
    def opcion_aceptar(self):
        print("Dentro de la opción aceptar")
        Vsalida = VentanaSalida(self) #para identificar su propia existencia
        Vsalida.show()
    def opcion_cancelar(self):
        self.__ventanaPadre.show()
        print("Dentro de la opcion cancelar")
#esto va en el controlador
class VentanaSalida(QMainWindow):
    def __init__(self,ppal=None):
        QMainWindow.__init__(self,ppal)
        loadUi("salida3.ui",self)


def main():
    app = QApplication()
    Vppal = VentanaPrincipal()
    Vppal.show()
    sys.exit(app.exec_())
main()
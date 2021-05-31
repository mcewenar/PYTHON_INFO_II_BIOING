from PyQt5 import QtWidgets
import sys


#Herencia
class MiFirstWindow(QtWidgets.QWidget):
    #Constructor
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setup()
    
    #Métodos
    def setup(self):
        self.setGeometry(200,200,400,200)
        self.setWindowTitle("Ventana Principal")

        #Creo un nuevo botón y le asigno una función para el manejo de eventos
        self.nuevo_boton = QtWidgets.QPushButton("Ingresar Paciente",self) #
        self.nuevo_boton.move(20,160)
        #Se especifica la señal de respuesta
        self.nuevo_boton.clicked.connect(self.on_click)

        #etiqueta (el ingresaste)
        self.etiqueta = QtWidgets.QLabel(self)
        self.etiqueta.setText("Ingresaste: ")
        self.etiqueta.move(20,100)
        self.etiqueta.resize(200,40)

        #Boton de cierre
        self.quit_boton = QtWidgets.QPushButton("quit",self)
        self.quit_boton.move(180,160)
        self.quit_boton.clicked.connect(QtWidgets.qApp.quit) #Cierra la ventana


        #entrada de texto
        self.campo_texto = QtWidgets.QLineEdit(self)
        self.campo_texto.move(20,20)
        self.campo_texto.resize(200,40)

        #se muestra la ventana
        self.show()
    def on_click(self):
        #se recupera el texto ingresado por el usuario
        textboxValue = self.campo_texto.text()
        self.etiqueta.setText("Ingresaste: " + textboxValue)
        self.campo_texto.setText("")

    def main():
        app = QtWidgets.QApplication(sys.argv)
        ventana = MiFirstWindow()
        ventana.show()
        sys.exit(app.exec_())
    
    if __name__ == "__main__":
        main()


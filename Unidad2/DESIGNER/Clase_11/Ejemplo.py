#Esto es primordial
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi


class Ventana(QWidget): #Tengo que decir a quién va a heredar
    def __init__(self):
        #super().__init__() ambas opciones son válidas para heredar
        QWidget.__init__(self)
        loadUi("C:\\Users\\dmcew\\proy_programacion\\Info_2\\Interfaces\\DESIGNER\\Clase_11\\ventan.ui",self) #USAR DOBLE SLASH PARA QUE EL CÓDIGO SEA BIEN ESCRITO
        #Aquí va la ruta del archivo 
        #Designer que quiero cargar
def main(): #Esto es protocolario, siempre en def main
    app = QApplication(sys.argv)
    vent = Ventana()
    vent.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


#LOS BOTONES SE CREAN EN EL DESIGNER, PARA EVITAR ESCRIBIR TANTO CÓDIGO
from vista import *
from modelo import *
import sys 
from PyQt5.QtWidgets import QApplication

class coordinador:
    def __init__(self,vista,modelo):
        self.__modelo = modelo
        self.__vista = vista

    def ingresarPaciente(self,n,c):
        return self.__modelo.ingresar_paciente(n,c) 


# Código cliente , main
def main():
    app = QApplication(sys.argv)
    modelo = sistemaBD()
    vista = Ventana_Menu()
    coord = coordinador(vista,modelo)
    vista.setcontrolador(coord)
    vista.show()
    sys.exit(app.exec_())

main()
from vista import * 
from modelo import *
import sys
from PyQt5.QtWidgets import QApplication

# * para importar todas las clases
class coordinador: #aquí se guardan modelo y vista apra que
    #coordinador se pueda comunicar
    def __init__(self,vista,modelo): #no tienen que ser los mismos nombre (vista,modelo)
        self.__modelo = modelo 
        self.__vista = vista
    def ingresarPaciente(self,n,c):
        return self.__modelo.ingresar_paciente(n,c)
    #codigo cliente, main

def main():
    app = QApplication(sys.argv)
    modelo = SistemaBD() #ESTA ES LA CLASE QUE SE HEREDA
    #NO PACIENTE()
    vista = Ventana_Menu()
    coord = coordinador(vista,modelo)
    vista.setcontrolador(coord)
    vista.show()
    sys.exit(app.exec_())

main()
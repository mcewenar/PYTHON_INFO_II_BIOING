from modelo import BaseDatos
from vista import VentanaLogin
import sys
from PyQt5.QtWidgets import QApplication


class Coordinador(object):
    def __init__(self,vista,modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo

    def validarIngreso(self,login,password):
        return self.__mi_modelo.validarUser(login,password)

def main():
    app = QApplication(sys.argv)
    mi_vista = VentanaLogin()
    mi_modelo = BaseDatos()
    mi_coord = Coordinador(mi_vista,mi_modelo)
    mi_vista.setControlador(mi_coord) #El objeto mi vista hace 
    #uso del método de setControlador
    mi_modelo.setLogin("david")
    mi_modelo.setPassword("123")
    mi_vista.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
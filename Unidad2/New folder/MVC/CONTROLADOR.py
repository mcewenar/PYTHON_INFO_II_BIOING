from MODELO import BaseDatos
from VISTA import VentanaLog
import sys
from PyQt5.QtWidgets import QApplication

class Coordinator(object):
    def __init__(self, vista, modelo):
        self.__mi_vista=vista
        self.__mi_modelo=modelo

    def validarIngreso(self,u,p):
        return self.__mi_modelo.validaruser(u,p)

def main():
    app=QApplication(sys.argv)
    mi_vista=VentanaLog()
    mi_modelo=BaseDatos()
    mi_coord= Coordinator(mi_vista,mi_modelo)
    mi_vista.setControlador(mi_coord)
    mi_modelo.setLogin("Yesid")
    mi_modelo.setPassword("1234")
    mi_vista.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
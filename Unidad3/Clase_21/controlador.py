from modelo import Biosenal
from vista import InterfazGrafica
import sys
from PyQt5.QtWidgets import QApplication


class Coordinador(object):
    def __init__(self, vista, biosenal):
        self.__mi_vista = vista
        self.__mi_biosenal = biosenal
        
    def recibirDatosSenal(self,data):
        self.__mi_biosenal.asignarDatos(data)
    def devolverDatosSenal(self, x_min, x_max):
        return self.__mi_biosenal.devolver_segmento(x_min, x_max)
    def escalarSenal(self,x_min,x_max, escala):
        return self.__mi_biosenal.escalar_senal(x_min, x_max, escala)


#codigo cliente
def main():
    app = QApplication(sys.argv)
    mi_vista = InterfazGrafica()
    mi_biosenal = Biosenal()
    mi_controlador = Coordinador(mi_vista, mi_biosenal)
    mi_vista.asignarCoordinador(mi_controlador)
    
    mi_vista.show()
    sys.exit(app.exec_())
main()
        
    


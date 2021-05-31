# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:23:03 2020

@author: dmcew
"""

from modelo import Biosenal
from vista import InterfazGrafico
import sys
from PyQt5.QtWidgets import QApplication

class Coordinador(object):
    #como el coordindor enlaza el modelo con la vista debe
    #tener acceso a objetos de ambas clases
    def __init__(self, vista, biosenal):
        self.__mi_vista = vista
        self.__mi_biosenal = biosenal
    #La idea es que la vista pase los datos que carga de la senal al controlador
    #y con esta se cree el objeto Biosenal que estara en
    def recibirDatosSenal(self,data):
        #Se asignan los datos a la senal
        self.__mi_biosenal.asignarDatos(data)
    def devolverDatosSenal(self, x_min, x_max):
        return self.__mi_biosenal.devolver_segmento(x_min, x_max)
    def escalarSenal(self,x_min,x_max, escala):
        return self.__mi_biosenal.escalar_senal(x_min, x_max, escala)
 
# el main (código cliente) no cambia ya que en esta simplemente se hacen las conexiones que siempre van

def main():
    app = QApplication(sys.argv)
    mi_vista = InterfazGrafico()
    mi_biosenal = Biosenal()
    mi_controlador = Coordinador(mi_vista, mi_biosenal)
    mi_vista.asignarCoordinador(mi_controlador)

    mi_vista.show()
    sys.exit(app.exec_())    
    
if __name__ == "__main__":
    main()    
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:53:45 2020

@author: dmcew
"""
from modelo2 import Senales
from vista2 import InterfazGrafica
import sys
from PyQt5.QtWidgets import QApplication 

class Coordinador():
    def __init__(self, vista, biosenal):
        self.__mi_vista = vista
        self.__mi_biosenal = biosenal
        
    def recibirDatosSenal(self,data):
        self.__mi_biosenal.asignarDatos(data)
    def devolverDatosSenal(self, x_min, x_max):
        return self.__mi_biosenal.devolver_segmento(x_min, x_max)
    def escalarSenal(self,x_min,x_max, escala):
        return self.__mi_biosenal.escalar_senal(x_min, x_max, escala)
    def datos_estadisticos(self,datos):
        return self.__mi_biosenal.datos_estadisticos()
    def datos_senal(self):
        return self.__mi_biosenal.datos_senal()
    def devolver_canal(self, c, xmin, xmax):
        return self.__mi_biosenal.devolver_canal(c,xmin,xmax)
    #def devolver_segmento(self,xmin,xmax):
        #return self.__mi_biosenal.devolver_segmento(xmin,xmax)
#Código cliente
def main():
    app = QApplication(sys.argv)
    mi_vista = InterfazGrafica()
    mi_biosenal = Senales()
    mi_controlador = Coordinador(mi_vista, mi_biosenal)
    mi_vista.asignarCoordinador(mi_controlador)
    
    mi_vista.show()
    sys.exit(app.exec_())

main()
    
    
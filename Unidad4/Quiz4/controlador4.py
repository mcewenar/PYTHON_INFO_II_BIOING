# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:32:30 2021

@author: dmcew
"""

from PyQt5.QtWidgets import QApplication
import sys
from vista4 import VentanaPrincipal
from modelo4 import imagenSis

class Coordinador:
    def __init__(self, vista, imagen):
        self.__mi_vista = vista
        self.__mi_imagen = imagen
    
    def recibirDatosImg(self,img):
        self.__mi_imagen.asignarDatos(img)
        return self.__mi_imagen.verDatos()
    def verImagen(self):
        img = self.__mi_imagen.verDatos()
        return img
    def devolversegmento(self,x1,x2,y1,y2):
        return self.__mi_imagen.devolver_segmento(x1,x2,y1,y2)
        
    def escalarSenal(self,x1,x2,y1,y2, escala):
        return self.__mi_imagen.escalar_imagen(x1,x2,y1,y2, escala)
    
    def normalizar(self,img):
        return self.__mi_imagen.normalizarImg(img)
    #Ver canales
    #def escalarSenales(self,x_min,x_max, escala):
        #return self.__mi_imagen.escalar_senal(x_min, x_max, escala)

#Código cliente

def main():
    app = QApplication(sys.argv)
    mi_vista = VentanaPrincipal()
    mi_imagen = imagenSis()
    mi_controlador = Coordinador(mi_vista, mi_imagen)
    mi_vista.asignarCoordinador(mi_controlador)
    mi_vista.show()
    sys.exit(app.exec_())    
    

main()
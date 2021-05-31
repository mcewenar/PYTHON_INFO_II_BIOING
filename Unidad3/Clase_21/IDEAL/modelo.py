# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:22:13 2020

@author: dmcew
"""

#esta clase tendra toda la logica para manejar la biosenal
class Biosenal:
    #constructor que recibe los datos, si no se entregan por defectos estaran 
    #vacios
    def __init__(self,data = None):
        if data is not None:
            self.asignarDatos(data)
        else:
            self.data = []
            self.canales = 0
            self.puntos = 0
    
    def asignarDatos(self,data):
        self.data = data
        self.canales = data.shape[0]
        self.puntos = data.shape[1]    
    #esta funcion nos permitira movernos en el tiempo xmin y xman
    def devolver_segmento(self, x_min, x_max):
        if x_min >= x_max:
            return None
        return self.data[:,x_min:x_max]
    #esta funcion nos permitira cambiar la amplitud de la senal
    def escalar_senal(self,x_min,x_max, escala):
        #el slicing no genera copia de los datos sino que devuelve un segmento de los originales
        #para no modificar el original se debe hacer una copia
        if x_min >= x_max:
            return None
        copia_data = self.data[:,x_min:x_max].copy()
        return copia_data*escala
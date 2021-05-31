# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:51:32 2020

@author: john.ochoa
"""

#debe ir toda la logica de ejecucion del problema a resolver
import numpy as np

class Biosenal(object):
    def __init__(self):
        self.__data=np.asarray([])
        self.__canales=0
        self.__puntos=0
        
    def asignarDatos(self,data):
        self.__data=data
        self.__canales=data.shape[0]
        self.__puntos=data.shape[1]
    
    #necesitamos hacer operacioes basicas sobre las senal, ampliarla, disminuirla, trasladarla temporalmente etc
    def devolver_segmento(self,x_min,x_max):
        #prevengo errores logicos
        if x_min >= x_max:
            return None
        #cojo los valores que necesito en la biosenal
        return self.__data[:,x_min:x_max]
    
    def devolver_canal(self,canal, x_min, x_max):
        #prevengo errores logicos
        if (x_min >= x_max) and (canal > self.__canales):
            return None
        #cojo los valores que necesito en la biosenal
        return self.__data[canal,x_min:x_max]
    
    def filtrar(self):
        pass
    
    def descomponer(self):
        pass

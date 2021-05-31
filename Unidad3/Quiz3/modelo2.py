# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:53:40 2020

@author: dmcew
"""

import numpy as np;


class Senales():
    def __init__(self,data=None):
        if data is not None:
            self.asignarDatos(data)
        else: 
            self.__data = []
            self.__canales = 0
            self.__puntos = 0
            
    def asignarDatos(self,data):
        self.__data = data
        self.__canales = data.shape[0]
        self.__puntos = data.shape[1]
    
    def devolver_segmento(self, x_min, x_max):
        if x_min >= x_max:
            
            return None
        return self.__data[:,x_min:x_max]
    def devolver_canal(self,canal, x_min, x_max):
        #prevengo errores logicos
        if (x_min >= x_max) and (canal > self.__canales):
            return None
        #cojo los valores que necesito en la biosenal
        return self.__data[canal,x_min:x_max]
    
    def escalar_senal(self,x_min,x_max,escala):
        if x_min >= x_max:
            return None
        copia_data = self.__data[:,x_min:x_max].copy()
        return copia_data*escala
    def datos_estadisticos(self,data):
        desviacion_dato=np.std(self.__data) #el 1 significa las muestras, es decir, promedia de los puntos
        valor_maximo = np.amax(self.__data) #Retorna valor máximo
        valor_minimo = np.amin(self.__data) #retorna valor minimo. Valor mínimo de los canales. Valor máx de las épocas
        promedio_dato= np.mean(self.__data) #Promedio
        mensaje1=("El promedio es: " + str(promedio_dato)+"\n"+"La desviación estandar es: " + str(desviacion_dato.shape) +"/n"+"El valor mínimo es: " + str(valor_minimo.shape)+"\n"+"El valor maximo es: " + str(valor_maximo))
        print("\n"+"La desviación estandar es: " + str(desviacion_dato))
        print("El valor mínimo es: " + str(valor_minimo))#si no usas shape, te muestra los valores y no las dimensiones
        print("El valor máximo es " + str(valor_maximo))
        return mensaje1
    def datos_senal(self,data):
        #canales = data.shape[0] #extraer los canales
        #puntos = data.shape[1] #" " "
        #epocas = data.shape[2]
        #self.cargar_senal2(data)
        mensaje2=("Numero de dimensiones: " + str(self.__data.ndim) + "\n" + "Número de canales: "+str(len(self.data[:])) + "\n" + "Tamanio en memoria (bytes): " + str(self.data.nbytes))
        print("Dimensiones de los datos cargados: " + str(self.__data.shape))
        print("Numero de dimensiones: " + str(self.__data.ndim))
        print("Tamaño (canales*muestras*): " + str(self.__data.size))
        print("Tamanio en memoria (bytes): " + str(self.__data.nbytes))
        print("Número de canales: " +str(len(self.__data[:])))
        
        #print("Número de muestras: " +str(len(data[None,:]))) (NO)
        mensaje2=("numero de canales: " + str(self.__canales))
        print("Numero de épocas: " +str(self.__epocas))
        print("Numero de puntos: " +str(self.__puntos))
        return mensaje2
    





    
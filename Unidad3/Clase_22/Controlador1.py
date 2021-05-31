# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:49:53 2020

@author: john.ochoa
"""

#el controlador enlaza todas las clases: MODELO y VISTA, CONTROLADOR
#necesito importar mi modelo y mi vista
from Modelo import Biosenal
from Vista_Graficacion import VentanaGrafica
#para la ejecucion del programa
import sys
#QApplication controla la ejecución de los programas basados en interfaz
from PyQt5.QtWidgets import QApplication

class Controlador(object):
    #como el coordindor enlaza el modelo con la vista debe
    #tener acceso a objetos de ambas clases
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo
    
    def asignarDatos(self, datos):
        self.__mi_modelo.asignarDatos(datos)
        
    def devolver_segmento(self, xmin, xmax):
        return self.__mi_modelo.devolver_segmento(xmin, xmax)
    
    def devolver_canal(self, c, xmin, xmax ):
        return self.__mi_modelo.devolver_canal(c, xmin, xmax)
    

#Donde esperamos que empiece la ejecucion
def main():
    #siempre uno y solo un QApplication
    app = QApplication(sys.argv)
    #Cuando creo la variable del tipo VentanaLogin creo el objeto que se ejecutara
    mi_vista = VentanaGrafica()
    mi_modelo = Biosenal()
    mi_controlador = Controlador(mi_vista, mi_modelo) #enlaza la vista y el modelo
    #asignarle el controlador a la vista
    mi_vista.asignarControlador(mi_controlador)
    mi_vista.show()#siempre hay que darles a las ventanas el show para que se muestren 
    #le decimos al QApplication que se ejecute
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
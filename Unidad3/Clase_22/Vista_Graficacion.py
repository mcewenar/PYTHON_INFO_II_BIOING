# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:49:03 2020

@author: john.ochoa
"""

#todo lo relacionado con recibir y mostrar informacion al usurio
#Librerias basicas del PyQT
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QIntValidator
# from PyQt5.pyqtgraph import PlotWidget, plot
#encargada de carga lo que hagamos en el Designer
from PyQt5.uic import loadUi

import scipy.io as sio
import numpy as np


#heredamos de la clase que usemos en el designer
class VentanaGrafica(QMainWindow):
    def __init__(self):
        #llamamos al constructor de la clase padre
        super(VentanaGrafica,self).__init__()
        #donde se carga el archivo designer
        loadUi('interfaz_graficacion.ui',self)
        #metodo auxilar configurar lo que queremos que "haga" la interfaz
        self.setup()
    
    def setup(self):
        self.boton_cargar.clicked.connect(self.cargar_senal)
        self.boton_canal.clicked.connect(self.graficar_canal)
        #configuracion para campo numerico
        self.campo_canal.setValidator(QIntValidator(0, 10))
    
    def graficar_canal(self):
        canal = int(self.campo_canal.text())
        datos = self.__mi_controlador.devolver_canal(canal, self.__x_min, self.__x_max)
        self.graficar_senal(datos)
    
    def graficar_senal(self, senal):
        self.campo_graficacion.clear()
        if senal.ndim == 1:
            self.campo_graficacion.plot(senal,pen=('r'))
        else:
            DC = 10
            for canal in range(senal.shape[0]):
                self.campo_graficacion.plot(senal[canal,:] + DC*canal,pen=('r'))
            
    def cargar_senal(self):
        #se abre el cuadro de dialogo para cargar
        #* son archivos .mat
        archivo_cargado, _ = QFileDialog.getOpenFileName(self, "Abrir senal","","Todos los archivos (*)Archivos mat (*.mat)*")
        if archivo_cargado != "":
            print(archivo_cargado)
            #la senal carga exitosamente entonces habilito los botones
            data = sio.loadmat(archivo_cargado)
            data = data["data"]
            #volver continuos los datos
            sensores,puntos,ensayos = data.shape
            senal_continua = np.reshape(data,(sensores,puntos*ensayos),order="F")

            self.__x_min=0
            self.__x_max=2000
            
            #asigno los datos al modelo
            self.__mi_controlador.asignarDatos(senal_continua)
            
            datos = self.__mi_controlador.devolver_segmento(self.__x_min, self.__x_max)

            self.graficar_senal(datos)     
    
    
    def asignarControlador(self,c):
        self.__mi_controlador = c
    
    

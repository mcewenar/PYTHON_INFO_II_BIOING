# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:53:41 2020

@author: dmcew
"""
#IMPORTACIONES CORRESPONDIENTES PARA UTILIZAR TODAS LAS LIBRERÍAS IMPLICADAS

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtGui import QIntValidator
from matplotlib.figure import Figure
from PyQt5.uic import loadUi
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import scipy.io as sio #Cargar archivos .mat
import numpy as np #manipular de forma sencilla los arreglos
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import matplotlib.pyplot as plt;



#gráfico
class MyGraphCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100): #dpi = puntos por pulgada (resolución de imagen)
        self.fig = Figure(figsize=(width,height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        #self.axes = self.fig.add_subplot(112) #falla
        #metodo para crear gráficos
        self.compute_initial_figure()
        
        FigureCanvas.__init__(self,self.fig)
    def graficar_senal(self,datos):
        self.axes.clear()
        for i in range(datos.shape[0]):
            self.axes.plot(datos[i,:] + i*10, label='canal ' + str(i))
    
        self.axes.set_xlabel('Muestras')
        self.axes.set_ylabel('voltaje (uV)')
        self.axes.set_title('Senales Electroencefalograma')
        self.axes.figure.canvas.draw() 
    def compute_initial_figure(self):
        t = arange(0.0,3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.set_title("GRÁFICO PREDETERMINADO")
        self.axes.plot(t,s)
        self.axes.clear()
        
    #def graficar_senal(self,senal):
        #self.axes.clear()
        #self.axes.plot(senal)
        #self.axes.figure.canvas.draw()

        
#La interfaz PYQT5
class InterfazGrafica(QMainWindow):
    def __init__(self):
        super(InterfazGrafica,self).__init__()
        loadUi("menuPrincipal.ui",self)
        self.setup()
        self.show()
        
    def asignarCoordinador(self,coordinador):
        self.__coordinador = coordinador
        
    def setup(self):
        layout = QVBoxLayout()
        self.campo_grafico.setLayout(layout)
        self.sc = MyGraphCanvas(self.campo_grafico, width=5, height=4, dpi=100)
        self.ss = MyGraphCanvas(self.campo_grafico2, width=5, height=4, dpi=100)
        layout.addWidget(self.sc)
        layout.addWidget(self.ss)
        
        self.boton_cargar.clicked.connect(self.cargar_senal)
        self.adelantar.clicked.connect(self.adelantar_senal)
        self.atrasar.clicked.connect(self.atrasar_senal)
        
        
        self.boton_cargar.setEnabled(True)
        self.adelantar.setEnabled(True)
        self.atrasar.setEnabled(True)
        
        
        #2do canvas
        self.boton_cargar2.clicked.connect(self.cargar_senal2)
        self.boton_canal.clicked.connect(self.graficar_canal)
        self.campo_canal.setValidator(QIntValidator(0, 7))
    def graficar_canal(self,datos):
        canal = int(self.campo_canal.text())
        datos = self.__coordinador.devolver_canal(canal, self.__x_min, self.__x_max)
        self.graficar_senal(datos)
        
    ########################################
    def graficar_senal(self, senal):
        self.campo_grafico2.clear()
        if senal.ndim == 1:
            self.campo_grafico2.plot(senal,pen=('r'))
        else:
            DC = 10
            for canal in range(senal.shape[0]):
                self.campo_grafico2.plot(senal[canal,:] + DC*canal,pen=('r'))
                                         
    def cargar_senal2(self):
        archivo_cargado, _ = QFileDialog.getOpenFileName(self,"Abrir Señal", "","Todos los archivos (*);;Archivos mat (*.mat);;Python (*.py)*")
        if archivo_cargado != None:
            print(archivo_cargado)
            
            data = sio.loadmat("C001R_EP_reposo.mat")
            data = data["data"]
            canales = data.shape[0]
            muestras = data.shape[1]
            epocas  = data.shape[2]
            
            senal_continua = np.reshape(data,(canales, muestras*epocas), order= 'F') #Para leer correctamente archivos .mat
            #self.sc.graficar_senal(senal_continua[:,1:2000])
            self.__coordinador.recibirDatosSenal(senal_continua)
            self.__x_min = 0
            self.__x_max = 2000
            
            #self.ss.graficar_senal(self.__coordinador.devolver_canal(self.x_min, self.x_max))
            self.ss.graficar_senal(self.__coordinador.devolverDatosSenal(self.__x_min, self.__x_max))
            self.mensajes_esta()
            self.mensajes_senal()
    def mensajes_esta(self):
        mensaje1 = self.__coordinador.datos_estadisticos()
    
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje1)
        msg.show()

    def mensajes_senal(self):
        mensaje2 = self.__coordinador.datos_senal()
    
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje2)
        msg.show()
            
            
    def cargar_senal(self):
        archivo_cargado, _ = QFileDialog.getOpenFileName(self,"Abrir Señal", "","Todos los archivos (*);;Archivos mat (*.mat);;Python (*.py)*")
        if archivo_cargado != None:
            print(archivo_cargado)
            
            #Cargamos archivo:
            data = sio.loadmat("C001R_EP_reposo.mat") #Diccionarios
            data = data["data"] #acceder Clave Data
            
            
            # hacerlo continuo
            canales = data.shape[0]
            muestras = data.shape[1]
            epocas  = data.shape[2]
            
            senal_continua = np.reshape(data,(canales, muestras*epocas), order= 'F') #Para leer correctamente archivos .mat
            #self.sc.graficar_senal(senal_continua[:,1:2000])
            self.__coordinador.recibirDatosSenal(senal_continua)
            self.x_min = 0
            self.x_max = 2000
            
            self.sc.graficar_senal(self.__coordinador.devolverDatosSenal(self.x_min, self.x_max))
            
            self.adelantar.setEnabled(True)
            self.atrasar.setEnabled(True)
            
            
    
    
    def atrasar_senal(self):
        if self.x_min < 2000:
            return
        self.x_min = self.x_min - 2000
        self.x_max = self.x_max - 2000
        self.sc.graficar_senal(self.__coordinador.devolverDatosSenal(self.x_min, self.x_max))
        
        
        
    def adelantar_senal(self):
        self.x_min = self.x_min + 2000
        self.x_max = self.x_max + 2000
        self.sc.graficar_senal(self.__coordinador.devolverDatosSenal(self.x_min,self.x_max))
    
##############################################################################   ################################

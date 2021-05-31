# Librerias
import os
import sys
#QFileDialog que es una ventana para abrir/guardar archivos
#QVBoxLayout es un organizador de widget en la ventana, este en particular los apila en vertical
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QVBoxLayout, QFileDialog
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
import cv2
from matplotlib.figure import Figure
from numpy import arange, sin, pi
# Contenedor (canvas = lienzo) para graficos de Matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

# clase con el lienzo (canvas) para mostrar en la interfaz los graficos matplotlib
class MyGraphCanvas(FigureCanvas):
    #constructor
    def __init__(self, parent= None,width=5, height=4, dpi=100):
        
        #se crea un objeto figura
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)        
        #se inicializa la clase FigureCanvas con el objeto fig
        FigureCanvas.__init__(self,self.fig)
    
    def graficar_imagen(self, datos):
        #limpiamos el grafico
        self.axes.clear()
        # self.axes.axis("off")# desactiva los ejes 
        # Mostramos la imágen con el metodo de matplolib imshow y le pasamos la imagen 
        self.axes.imshow(datos)
        #ordenamos que dibuje
        self.axes.figure.canvas.draw()

# Interfaz en PYQT
class InterfazGrafico(QMainWindow):
    #condtructor
    def __init__(self):
        #siempre va
        super(InterfazGrafico,self).__init__()
        #se carga el diseño
        loadUi ("anadir_grafico.ui",self)
        #se llama la rutina donde configuramos la interfaz
        self.setup()

    def setup(self):
        self.sc = MyGraphCanvas(self.campo_grafico, width=5, height=4, dpi=100)
        self.layout.addWidget(self.sc)
        self.boton_cargar.clicked.connect(self.cargar_senal)
        self.mostrar.clicked.connect(self.mostrarSeg)
        
    def cargar_senal(self):
        #se abre el cuadro de dialogo para cargar
        archivo_cargado, _ = QFileDialog.getOpenFileName(self, "Cargar Imágen","","Imágenes jpg (*.jpg);;Imágenes png (*.png)")
        if archivo_cargado != '':
            print(archivo_cargado)
            #Leemos la imagen con el etodo de opencv
            dataimg =  cv2.imread(archivo_cargado)
            dataimg = cv2.cvtColor(dataimg, cv2.COLOR_BGR2RGB)
            # sensores, puntos, ensayos = dataimg.shape
            # Evia la matriz de pixeles para guardar en el objeto imagen de modelo       
            #graficamos la imagen            
            self.sc.graficar_imagen(self.__coordinador.recibirDatosImg(dataimg))
            # self.sc.graficar_imagen(dataimg)
                

            

        

    def mostrarSeg(self):
        self.x1 = int(self.x1.text())
        self.x2 = int(self.x2.text())
        self.y1 = int(self.y1.text())
        self.y2 = int(self.y2.text())
        #graficamos la imagen            
        self.sc.graficar_imagen(self.__coordinador.devolver_segmento(self.x1,self.x2,self.y1,self.y2))
        # self.sc.graficar_imagen(dataimg)
             
    


    def asignarCoordinador(self,c):
        self.__coordinador = c

    
# app=QApplication(sys.argv)
# mi_ventana = InterfazGrafico()
# sys.exit(app.exec_()) 
               
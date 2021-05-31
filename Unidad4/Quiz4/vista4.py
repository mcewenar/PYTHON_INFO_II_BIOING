# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:32:21 2021

@author: dmcew
"""
# Librerias
import os
import sys
#QFileDialog que es una ventana para abrir/guardar archivos
#QVBoxLayout es un organizador de widget en la ventana, este en particular los apila en vertical
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QVBoxLayout, QFileDialog,QLayout
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
import cv2
from matplotlib.figure import Figure
from numpy import arange, sin, pi
# Contenedor (canvas = lienzo) para graficos de Matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt


class MyGraphCanvas(FigureCanvas):
    #constructor
    def __init__(self, parent= None,width=5, height=4, dpi=100):
        
        #se crea un objeto figura
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        #self.axes = self.fig.add_subplot(112)       
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
        
    def graficaHis(self,im): 
        img = cv2.imread(im)
        color = ('b','g','r')
        for i, c in enumerate(color):
            hist = cv2.calcHist([img], [i], None, [256], [0, 256])
            self.axes.set_title('Histograma')
            self.axes.set_xlabel("Niveles")
            self.axes.set_ylabel("Densidad")
            self.axes.plot(hist, color = c)
            #self.plot.xlim([0,256])
            self.axes.figure.canvas.draw()
            
    def ecualizarImagen(self,imag):
        i= cv2.imread(imag)
        im = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
        img1=np.uint8(cv2.normalize(im, None, 0, 255, cv2.NORM_MINMAX))
        self.axes.imshow(cv2.equalizeHist(img1),cmap=plt.cm.gray)
        self.axes.figure.canvas.draw()
        
    def ecualizarHisto(self,imgn):
        img = cv2.imread(imgn,cv2.IMREAD_GRAYSCALE)
        img = cv2.equalizeHist(img) 
        #img1=np.uint8(cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX))
        self.axes.imshow(cv2.equalizeHist(img),cmap=plt.cm.gray)
        self.axes.figure.canvas.draw()
        
    def Espacio_Color(self,im):
        img = cv2.imread(im)
        imaHSV=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        self.axes.imshow(imaHSV, vmin=0,vmax=255)
        self.axes.figure.canvas.draw()

        
    def graficar_canal(self,can):
        self.axes.clear()
        self.axes.imshow(can,vmin=0,vmax=255)
        self.axes.figure.canvas.draw()
        
    def graficarSumResDiv(self, imagen):
        self.axes.clear()
        Image = np.clip(imagen, 0, 1)
        self.axes.imshow(Image)
        self.axes.figure.canvas.draw()
        
# Interfaz en PYQT
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        #siempre va
        super(VentanaPrincipal,self).__init__()
        #se carga el diseño
        loadUi ("ventanappal.ui",self)
        #se llama la rutina donde configuramos la interfaz
        self.setup()

    def setup(self):
        
        layout=QVBoxLayout()
        self.campo_grafico.setLayout(layout)
        self.__sc = MyGraphCanvas(self.campo_grafico, width=5, height=4, dpi=100)
        
        self.__ss = MyGraphCanvas(self.campo_grafico, width=5, height=4, dpi=65)
        layout.addWidget(self.__sc)
        
        
        layout.addWidget(self.__ss)
        
        self.cargar_img.clicked.connect(self.cargar_imagen)
        self.visualHisto.clicked.connect(self.campoHistograma)
        self.ecualizarImg.clicked.connect(self.ecualizarImagen)
        self.mostrarS.clicked.connect(self.mostrarSeg)
        self.EspacioColor.clicked.connect(self.Espa_Color)
        self.botonSumar.clicked.connect(self.Sumaimagen)
        self.botonRestar.clicked.connect(self.Restaimagen)
        self.botonMulti.clicked.connect(self.Multiplicarimagen)
        self.botonDividir.clicked.connect(self.Dividirimagen)
        self.botonGraficarCanal.clicked.connect(self.mostrar_canal)
        self.BotonSalir.clicked.connect(self.volver)
        
    def asignarCoordinador(self,c):
        self.__coordinador = c
        
    def cargar_imagen(self):
        #se abre el cuadro de dialogo para cargar
        self.archivo_cargado, _ = QFileDialog.getOpenFileName(self, "Cargar Imagen","","Imágenes jpeg (*.jpeg);;Imágenes png (*.png);;Imágenes jpg (*.jpg)")
        if self.archivo_cargado != '':
            print(self.archivo_cargado)
            #Leemos la imagen con el etodo de opencv
            dataimg =  cv2.imread(self.archivo_cargado)
            dataimg = cv2.cvtColor(dataimg, cv2.COLOR_BGR2RGB)
            #sensores, puntos, ensayos = dataimg.shape
            # Evia la matriz de pixeles para guardar en el objeto imagen de modelo       
            #graficamos la imagen            
            self.__sc.graficar_imagen(self.__coordinador.recibirDatosImg(dataimg))
            #self.sc.graficar_imagen(dataimg)
            print ('filas, columnas y canales: ', dataimg.shape, "respectivamente")
            row,col,ch=np.shape(dataimg)
            mini = np.min(dataimg)
            maxi=np.max(dataimg)
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle('Información:')
            mensaje=("Hay filas " +str(row)+", columnas "+str(col)+" y canales "+str(ch)+ "\n \n Máx: "+str(maxi)+", mínimo "+str(mini))
            msgBox.setText(mensaje)
            msgBox.show()   
        
        else: 
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setWindowTitle('Error')
            mensaje=("No se permite campos vacíos, ni formatos distintos a PNG o JPEG")
            msgBox.setText(mensaje)
            msgBox.show()              
    

    def Graficar_Conteo(self):
        imagen = self.cv_imread(self.archivo_cargado)
        grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)          
        Num_Max = self.verticalSlider.value()
        Num_Min = self.horizontalSlider.value()
        bordes = cv2.Canny(grises, Num_Min, Num_Max)
        ctns, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        print('Número de contornos encontrados: ', len(ctns))   
        a = str(len(ctns))
        
        
        plt.imshow(bordes, cmap='gray')   
        plt.title('\n-\nNúmero de contornos encontrados: '+ a + " \nValores UMBRAL: Mín - "+ str(Num_Min) + " Máx - " + str(Num_Max))        
        plt.show()   

    
    def campoHistograma(self):
        self.__ss.graficaHis(self.archivo_cargado)
        
    def Espa_Color(self):
        self.__sc.Espacio_Color(self.archivo_cargado)
        
    def ecualizarImagen(self):         
       self.__sc.ecualizarImagen(self.archivo_cargado)
       self.__ss.ecualizarHisto(self.archivo_cargado)
       
    def mostrarSeg(self):
        self.x1 = float(self.x1.text())
        self.x2 = float(self.x2.text())
        self.y1 = float(self.y1.text())
        self.y2 = float(self.y2.text())
        #graficamos la imagen            
        self.__sc.graficar_imagen(self.__coordinador.devolversegmento(self.x1,self.x2,self.y1,self.y2))
        
    def Sumaimagen(self):
        I=self.__coordinador.verImagen()
        img=cv2.imread(I)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        Numero=float(self.numero.text())
        img=np.array(img, np.dtype('float64'))
        Ima=self.__coordinador.normalizar(img)
        Imagen=Ima + Numero
        self.__sc.graficarSumResDiv(Imagen)
        
        
    def Restaimagen(self):
        I=self.__coordinador.verImagen()
        img=cv2.imread(I)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        Numero=float(self.numero.text())
        Ima=self.__coordinador.normalizar(img)
        #Ima=img/255
        img=np.array(img, np.dtype('float64'))
        Imagen=Ima-Numero
        self.__sc.graficarSumResDiv(Imagen)    
        
        
    def Multiplicarimagen(self):
        I=self.__coordinador.verImagen()
        img=cv2.imread(I)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        Numero=float(self.numero.text())
        Ima=self.__coordinador.normalizar(img)
        #Ima=img/255
        img=np.array(img, np.dtype('float64'))
        Imagen=Ima*Numero
        self.__sc.graficarSumResDiv(Imagen)
        
        
    def Dividirimagen(self):
        I=self.__coordinador.verImagen()
        img=cv2.imread(I)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        Numero=float(self.numero.text())
        Ima=self.__coordinador.normalizar(img)
        #Ima=img/255
        img=np.array(img, np.dtype('float64'))
        if Numero != 0:
            Imagen=Ima/Numero
            self.__sc.graficarSumResDiv(Imagen)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("ALERTA")
            msg.setText("NO ES POSIBLE LA DIVISÓN POR 0")
            msg.setIcon(QMessageBox.Critical)             
            msg.show()
            
            
            
    def mostrar_canal(self):
        mi_canal=int(self.graficarCanal.text())
        ima=self.__coordinador.verImagen()
        img = cv2.imread(ima)
        ima=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        canalR=np.copy(ima)
        canalR[:,:,1]=0
        canalR[:,:,2]=0
        
        canalG=np.copy(ima)
        canalG[:,:,0]=0
        canalG[:,:,2]=0
        
        canalB=np.copy(ima)
        canalB[:,:,1]=0
        canalB[:,:,0]=0
        if mi_canal==0:
            self.__sc.graficar_canal(canalR)
        elif mi_canal==1:
            self.__sc. graficar_canal(canalG)
        elif mi_canal==2:
            self.__sc. graficar_canal(canalB)
        else:
            Aviso_canal = "Campo fuera del rango. Inténtelo nuevamente" 
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText(Aviso_canal)
            msg.setWindowTitle("ERROR")
            msg.show()
        
    def volver(self):
        self.hide()




    



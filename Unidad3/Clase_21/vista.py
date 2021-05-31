import sys
#QFileDialog que es una ventana para abrir/guardar archivos
#QVBoxLayout es un organizador de widget en la ventana, este en particular los apila en vertical
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from matplotlib.figure import Figure
from numpy import arange, sin, pi
# Contenedor (canvas = lienzo) para graficos de Matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import scipy.io as sio
import numpy as np


class MyGraphCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        
        self.compute_initial_figure()
        
        FigureCanvas.__init__(self,self.fig)
    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t,s)
        
    #crear niuevo metodo, graficar señal
    def graficar_senal(self,senal):
        #se limpia los ejes del gráfico
        self.axes.clear()
        #ingresamos el nuevo gráfico iterando entre canales y dejando espacio entreellos 
        for c in range(datos.shape[0]):
            self.axes.plot(datos[c,:]+c*10)
            
            self.axes.set_xlabel("MNuestras")
            self.axes.set_ylabel("voltaje (uV)")
            #dibuje
            self.axes.figure.canvas.draw()
            
        
        
        
        
        #se grafica la señal
        #self.axes.plot(senal)
        #se actualiza el gráfico
        #self.axes.figure.canvas.draw()
class InterfazGrafica(QMainWindow):
    def __init__(self):
        super(InterfazGrafica,self).__init__()
        loadUi('mainmenu.ui',self)
        self.setup()
        self.show()
    def setup(self):
        #layout = QVBoxLayout()
        #self.campo_grafico.setLayout(layout)
        self.sc = MyGraphCanvas(self.campo_grafico, width=5, height=4, dpi=100)
        self.layout.addWidget(self.sc) #De esta manera interactúa con el designer
        self.boton_cargar.clicked.connect(self.cargar_senal)
        #self.boton_adelante.clicked.connect(self.adelantar_senal)
        #self.boton_atras.clicked.connect(self.atrasar_senal)
        
        #se deshabilitan los botnes de manejo de la senal
        #self.boton_adelante.setEnabled(False)
        #self.boton_atras.setEnabled(False)
        #self.boton_aumentar.setEnabled(False)
        #self.boton_disminuir.setEnabled(False)
        
        
        #self.boton_cargar.clicked.connect(self.cargar_senal)
    def asignarCoordinador(self,c):
        self.__coordinador = c
    def cargar_senal(self):
        archivo_cargado, _ = QFileDialog.getOpenFileName(self,"Abrir señal", "","Archivos mat (*.mat);;Todos los archivos (*)")
        if archivo_cargado != None:
            print(archivo_cargado)
            
        #carga el archivo:
            #Volverlo continuo 3d a 2d 
            data = sio.loadmat(archivo_cargado) #Diccionario
            data = data["data"]
            sensores, puntos, ensayos = data.shape
            senal_continua = np.reshape(data,(sensores,puntos*ensayos),order="F")
            self.sc.graficar_senal(senal_continua[:,:4000])
            
       #misma forma de hacer una señal continua
        #sensores = data.shape[0]
        #puntos = data.shape[1]
        #epocas = data.shape[2]
        
        
        #senal_continua = np.reshape(data,(sensores,puntos*epocas),order = "F")
#app=QApplication(sys.argv)
#mi_ventana = InterfazGrafica()
#sys.exit(app.exec_())
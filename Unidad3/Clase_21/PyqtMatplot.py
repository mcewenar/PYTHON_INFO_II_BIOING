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

# clase con el lienzo (canvas) para mostrar en la interfaz los graficos matplotlib
class MyGraphCanvas(FigureCanvas):
    #constructor
    def __init__(self, parent= None,width=5, height=4, dpi=100):
        
        #se crea un objeto figura
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        
        #llamo al metodo para crear el primer grafico
        self.compute_initial_figure()
        
        #se inicializa la clase FigureCanvas con el objeto fig
        FigureCanvas.__init__(self,self.fig)
    #que esta solo grafica el seno    
    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t,s)

    def graficar_senal(self, datos):
        #limpiamos el grafico
        self.axes.clear()
        #ingresamos el nuevo grafico iterando entre canales y dejando espacio entre ellos
        for c in range(datos.shape[0]):
            self.axes.plot(datos[c,:] + c*10)
        
        self.axes.set_xlabel('Muestras')
        self.axes.set_ylabel('Voltaje (uV)')
        self.axes.set_title('Señales EEG')
        #ordenamos que dibuje
        self.axes.figure.canvas.draw()

# Interfaz en PYQT
class InterfazGrafico(QMainWindow):
    #condtructor
    def __init__(self):
        #siempre va
        super(InterfazGrafico,self).__init__()
        #se carga el diseño
        loadUi ('anadir_grafico.ui',self)
        #se llama la rutina donde configuramos la interfaz
        self.setup()
        #se muestra la interfaz
        self.show()

    def setup(self):
        #los layout permiten organizar widgets en un contenedor
        #esta clase permite añadir widget uno encima del otro (vertical)
        # layout = QVBoxLayout()
        #se añade el organizador al campo grafico
        # self.campo_grafico.setLayout(layout)
        #se crea una clase para manejo de graficos
        self.sc = MyGraphCanvas(self.campo_grafico, width=5, height=4, dpi=100)
        #se añade el campo de graficos
        self.layout.addWidget(self.sc)

          #se organizan las señales 
        self.boton_cargar.clicked.connect(self.cargar_senal)
        self.boton_adelante.clicked.connect(self.adelantar_senal)
        self.boton_atras.clicked.connect(self.atrasar_senal)
        
        #se deshabilitan los botonoes de manejo de la senal
        self.boton_adelante.setEnabled(False)
        self.boton_atras.setEnabled(False)
        # self.boton_aumentar.setEnabled(False)
        # self.boton_disminuir.setEnabled(False)
        

    def asignarCoordinador(self,c):
        self.__coordinador = c
    def cargar_senal(self):
        #se abre el cuadro de dialogo para cargar
        archivo_cargado, _ = QFileDialog.getOpenFileName(self, "Abrir señal","","Todos los archivos (*);;Archivos mat (*.mat);;Python (*.py)")
        if archivo_cargado != '':
            print(archivo_cargado)
            
            #Cargamos los datos
            data = sio.loadmat(archivo_cargado) # Diccionario
            data = data["data"]
            sensores, puntos, ensayos = data.shape
            senal_continua = np.reshape(data,(sensores,puntos*ensayos),order = 'F')
            self.__coordinador.recibirDatosSenal(senal_continua)
            # self.mi_biosenal = Biosenal(senal_continua)
            self.x_min = 0
            self.x_max = 2000
        
            #graficamos
            # self.sc.graficar_senal(self.mi_biosenal.devolver_segmento(self.x_min, self.x_max))
            self.sc.graficar_senal(self.__coordinador.devolverDatosSenal(self.x_min, self.x_max))
        
            #se habilitan los botonoes de manejo de la senal
            self.boton_adelante.setEnabled(True)
            self.boton_atras.setEnabled(True)
            # self.boton_aumentar.setEnabled(True)
            # self.boton_disminuir.setEnabled(True)

    def atrasar_senal(self):
        #no me puedo atrasar si estoy en menos del rango
        if self.x_min < 2000:
            return
        
        self.x_min = self.x_min - 2000
        self.x_max = self.x_max - 2000
        
        #graficamos
        # self.sc.graficar_senal(self.mi_biosenal.devolver_segmento(self.x_min, self.x_max)) # Sin pasar por controlador 
        self.sc.graficar_senal(self.__coordinador.devolverDatosSenal(self.x_min, self.x_max))

    def adelantar_senal(self):
        self.x_min = self.x_min + 2000
        self.x_max = self.x_max + 2000
        
        #graficamos
        # self.sc.graficar_senal(self.mi_biosenal.devolver_segmento(self.x_min, self.x_max))
        self.sc.graficar_senal(self.__coordinador.devolverDatosSenal(self.x_min, self.x_max))

    
# app=QApplication(sys.argv)
# mi_ventana = InterfazGrafico()
# sys.exit(app.exec_())
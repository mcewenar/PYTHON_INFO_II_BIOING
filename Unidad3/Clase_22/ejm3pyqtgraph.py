from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import numpy as np
from random import randint

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.x = np.arange(360)  # 100 time points
        self.y = np.sin(np.radians(self.x))  # 100 time points
        # self.y = np.random.randint(,100)  # 100 data points

        self.graphWidget.setBackground('y')
        
        # pen = pg.mkPen(color=(255, 0, 190))
        pen = pg.mkPen(color=(255,0,0), width=10,style = QtCore.Qt.DashDotLine)
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)
        # Iniciamos temporizador 
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        # Señal timeout, slot update_plot_data
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        self.x=np.append(self.x,self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first 
        self.y=np.append(self.y,np.sin(np.radians(self.x[-1] + 1)))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.
        # self.graphWidget.repaint()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())


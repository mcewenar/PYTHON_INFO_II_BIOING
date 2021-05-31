# La graficación se da redibujando el plot lo que lo hace mas lento 
import sys
import random
import matplotlib
import numpy as np
# matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        # n_data = 360
        # self.xdata = list(range(n_data))
        # self.ydata = [random.randint(0, 10) for i in range(n_data)]
        self.xdata = np.arange(360)  # 100 time points
        self.ydata = np.sin(np.radians(self.xdata))  # 100 time points
        self.update_plot()

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.xdata = self.xdata[1:]  # Remove the first y element.
        self.xdata= np.append(self.xdata,self.xdata[-1] + 1) 
        self.ydata = self.ydata[1:] 
        self.ydata = np.append(self.ydata,np.sin(np.radians(self.xdata[-1] + 1)))
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()



def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()


if __name__ == "__main__":
    main()
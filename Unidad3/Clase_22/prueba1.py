import pyqtgraph as pg
import numpy as np
from PyQt5.QtWidgets import QApplication
import sys

x = np.arange(1000)
y = np.random.normal(3,2.5,size=(3,1000))


app = QApplication(sys.argv)
plotWidget = pg.plot(title="Curve")
for i in range(3):
    plotWidget.plot(x,y[i],pen=(i,3))
#plotWidget.plot(x)
sys.exit(app.exec_())




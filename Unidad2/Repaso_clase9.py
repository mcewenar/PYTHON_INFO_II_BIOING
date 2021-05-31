import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QTextDocumentFragment;

def main():
    app = QtWidgets.QApplication(sys.argv); 
    #La clase QApplication maneja el 
    #flujo principal del programa y
    #las características principales
    
    w = QtWidgets.QWidget();
    w.setGeometry(100,100,200,50);
    w.setWindowTitle("Ventana principal")

    b = QtWidgets.QLabel(w);
    b.setText("Ponte en 4");
    b.move(50,20);

    w.show()
    sys.exit(app.exec_());

main()
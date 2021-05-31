import sys 
from PyQt5 import QtWidgets;

def main():
    #Manejo del flujo principal, con los eventos e interacciones
    app = QtWidgets.QApplication(sys.argv); #Instanciar un objeto app
    #Ventana
    w = QtWidgets.QWidget();
    w.setGeometry(100,100,200,50); #(x,y,ancho,alto)
    w.setWindowTitle("PyQt")


    #Etiqueta
    b = QtWidgets.QLabel();
    boton1 = QtWidgets.QPushButton(w); #Crear botón
    boton1.move(100,100) #Mover botón
    b.setText("Hola Mundo!");
    b.move(50,20); #coordenadas 50 en x, 20 en y
    
    #Cuando se tiene la ventana construída se muestra. Para poder mostrar
    w.show()

    #se comienza el lazo de ejecución
    sys.exit(app.exec_()); #para finaizar correctamente

if __name__ == "__main__":
    main();

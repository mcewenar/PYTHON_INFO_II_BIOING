from modelo import imagen
from vista import InterfazGrafico
import sys
from PyQt5.QtWidgets import QApplication

class Coordinador(object):
    #como el coordindor enlaza el modelo con la vista debe
    #tener acceso a objetos de ambas clases
    def __init__(self, vista, imagen):
        self.__mi_vista = vista
        self.__mi_imagen = imagen
    #La idea es que la vista pase los datos que carga de la senal al controlador
    #y con esta se cree el objeto Biosenal que estara en
    def recibirDatosImg(self,img):
        #Se asignan los datos a la senal
        self.__mi_imagen.asignarDatos(img)
        return self.__mi_imagen.verDatos()

    def devolver_segmento(self, x1,x2,y1,y2):
        return self.__mi_imagen.devolver_segmento(x1,x2,y1,y2)
        
    def escalarSenal(self,x1,x2,y1,y2, escala):
        return self.__mi_imagen.escalar_senal(x1,x2,y1,y2, escala)
 
# el main (código cliente) no cambia ya que en esta simplemente se hacen las conexiones que siempre van

def main():
    app = QApplication(sys.argv)
    mi_vista = InterfazGrafico()
    mi_imagen = imagen()
    mi_controlador = Coordinador(mi_vista, mi_imagen)
    mi_vista.asignarCoordinador(mi_controlador)
    mi_vista.show()
    sys.exit(app.exec_())    
    
if __name__ == "__main__":
    main()   
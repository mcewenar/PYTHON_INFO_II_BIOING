import cv2
import numpy as np

#esta clase tendra toda la logica para manejar la biosenal
class imagen:
    def __init__(self):
        self.img = []
        self.canalesRGB = 0
        self.columnas = 0
        self.filas  = 0
    
    def asignarDatos(self,img):
        self.img = img
        self.filas = img.shape[0]    
        self.columnas = img.shape[1]    
        self.canalesRGB = img.shape[2]

    def verDatos(self):
        return self.img
    
    # Funcion segmentar imagen
    def devolver_segmento(self, x1,x2,y1,y2):
        if x1 >= x2 and y1 >= y2:
            return None
        return self.img[y1:y2,x1:x2,:]
    
    def escalar_imagen(self, x1,x2,y1,y2,c,escala):
            #el slicing no genera copia de los datos sino que devuelve un segmento de los originales
        #para no modificar el original se debe hacer una copia
        if x1 >= x2 and y1 >= y2 and 0>c>3:
            return None
        copia_img = self.img[y1:y2,x1:x2,c].copy()
        return copia_img*escala
    
    def normalizar(self):
        self.img.asdtype(np.float) 
        return self.img/(np.max(self.img))

    def sumar_escalar(self, img1,escala):
        return img1+escala


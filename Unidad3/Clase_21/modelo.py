class Biosenal(object):
    def __init__(self,data = None):
        if data is not None:
            self.asignarDatos(data)
        else:
            self.data = []
            self.canales = 0
            self.puntos = 0
    def asignarDatos(self,data):
        self.data = data
        self.canales = data.shape[0]
        self.puntos = data.shape[1]
    def devolver_segmento(self, x_min, x_max):
        if x_min >= x_max:
            return None
        return self.data[:,x_min,x_max]
    def escalar_senal(self,x_min,x_max,escala):
        
        if x_min >= x_max:
            return None
        copia_data = self.data[:,x_min:x_max].copy()
        return copia_data*escala
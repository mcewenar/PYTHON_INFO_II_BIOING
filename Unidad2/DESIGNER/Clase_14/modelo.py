class Paciente:
    def __init__(self):
        self.__nombre=""
        self.__cedula=""
    def setnombre(self,n):
        self.__nombre = n
    def setcedula(self,c):
        self.__cedula = c


class SistemaBD:
    def __init__(self):
        self.__BDpac= {}
    def ingresar_paciente(self,n,c):
        self.validarPaciente()
        pac = Paciente()
        pac.setnombre(n) #hacemos las asignaciones
        pac.setcedula(c)
        self.__BDpac[c]= pac #Ingresar a la BD, lo de corchetes 
        #es la clave
        #después del =, el objeto paciente (pac) recién inresado
        return True
    def validarPaciente(self):

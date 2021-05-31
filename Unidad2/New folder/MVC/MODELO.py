class BaseDatos():
    def __init__(self):
        self.__login=''
        self.__password=''

    def setLogin(self,l):
        self.__login=l

    def setPassword(self,p):
        self.__password=p

    def validaruser(self,l,p):
        return(self.__login==l)and(self.__password==p)
        
import datetime

class Medicamento(object):
    def __init__(self):
        self.__nombre = ""
        self.__dosis = 0
        
    def verNombre(self):
        return self.__nombre
    def verDosis(self):
        return self.__dosis
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarDosis(self,d):
        self.__dosis = d

#%%        
class Mascota(object):
    def __init__(self):
        self.__nombre = ""
        #NUMERO DE HISTORIA CLINICA
        self.__nhc = 0 
        self.__tipo = "" 
        self.__peso = 0
        self.__fecha_ingreso = ""
        #UNA MASCOTA TIENE MULTIPLES MEDICAMENTOS
        self.__lista_medicamentos = []

    def verNombre(self):
        return self.__nombre
    def asignarNombre(self,n):
        self.__nombre = n

    def verNHC(self):
        return self.__nhc
    def asignarNHC(self,n):
        self.__nhc = n
    #%%    
    def verTipo(self):
        return self.__tipo
    def asignarTipo(self,n):
        self.__tipo = n
    
    def verPeso(self):
        return self.__peso
    def asignarPeso(self,n):
        self.__peso = n

    def verFecha_Ingreso(self):
        return self.__fecha_ingreso
    def asignarFecha_Ingreso(self,n):
        self.__fecha_ingreso = n
    
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n
        
    #metodo sugerido en la clase
    def agregarMedicamento(self,m):
        self.__lista_medicamentos.append(m)
#%%     
class Sistema(object):
    def __init__(self):
        #tenemos una lista de mascotas y cada mascota tiene una lista de 
        #medicamentos
        self.__lista_mascotas = []
    #creamos un metodo para saber si hay capacidad
    def hayCapacidad(self):
        if len(self.__lista_mascotas) > 10:
            return False
        else:
            return True
    
    def verificarMascota(self,nhc):
        encontrado = False
        for m in self.__lista_mascotas:
            if nhc == m.verNHC():
                encontrado = True
                break
        return encontrado
    #%%
    def ingresarMascota(self,m):
        #como todo se verifica desde el menu aca NO tengo que volver a verificar
        self.__lista_mascotas.append(m)
    
    #a partir del nhc me devuelve la posicion de la mascota en la lista
    #si la mascota no existe devuelve el valor -1
    def verPosicionMascota(self,nhc):
        #esta variable posicion la usaremos para seguir las posiciones que hemos ido buscando
        posicion = 0
        #tenemos que recorrer todos los elementos buscando la posicion que tenga ese nhc
        for m in self.__lista_mascotas:
            if nhc == m.verNHC():
                #cuando encuentro la mascota devuelvo la posicion en que la encontre
                return posicion
            posicion = posicion + 1
        #si despues de recorrer todo el for no encontramos la mascota devolvemos -1
        return -1
         
    #a partir del nhc me devuelve la mascota en la lista
    #si la mascota no existe devuelve el valor None
    def verMascota(self,nhc):
        #tenemos que recorrer todos los elementos buscando la posicion que tenga ese nhc
        for m in self.__lista_mascotas:
            if nhc == m.verNHC():
                #cuando encuentro la mascota la devuelvo 
                return m
        #si despues de recorrer todo el for no encontramos la mascota devolvemos -1
        return None
    #%%    
    def verFecha_Ingreso(self,nhc):
        #verifico si existe
        existe = self.verificarMascota(nhc)
        if existe == True:
            #necesito la mascota que tiene el nhc dado para recuperar su fecha de ingreso
            #necesito el objeto mascota que tiene el nhc dado
            m = self.verMascota(nhc)
            return m.verFecha_Ingreso()
        else:
            return "La mascota no está en el sistema"
    
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas)
    
    def eliminarMascota(self,nhc):
        m = self.verMascota(nhc)
        if m == None:
            return "La historia clínica no está en el sistema ..."
        else:
            self.__lista_mascotas.remove(m)
            return "mascota eliminada del sistema ..."
        

#vamos probando funcion por funcion
def Menu():
    sistema = Sistema()
    while True:
        opcion = int(input("Ingrese 1 para Ingresar nueva mascota \n 2 para salir \n 3 ver Fecha \n 4 ver Numero mascotas \n 5 ver medicamentos "))
        if opcion == 2:
            print("Hasta luego ...")
            break
        elif opcion == 6:
            #1 solicito el numero de historia clinica para el cual quiero ver la fecha
            nhc = int(input("Ingrese Historia Clinica de la mascota: "))
            #2 llamo al metodo eliminar mascota e imprimo el resultado
            print(sistema.eliminarMascota())
        elif opcion == 5:
            #1 solicito el numero de historia clinica para el cual quiero ver la fecha
            nhc = int(input("Ingrese Historia Clinica de la mascota: "))
            #2 busco la mascota con la historia clinica
            m = sistema.verMascota(nhc)
            if m == None:
                print("La mascota no está registrada en el sistema")
            else:
                #si la mascota existe imprimo medicamento por medicamento en la lista
                medicamentos = m.verLista_Medicamentos()
                print("La mascota esta consumiendo: ")
                for med in medicamentos:
                    print("medicamento: " + med.verNombre() + " dosis: " + str(med.verDosis()) + "\n")
        elif opcion == 4:
            print("En el sistema hay " + str(sistema.verNumeroMascotas()) + " mascotas")
        elif opcion == 3:
            #1 solicito el numero de historia clinica para el cual quiero ver la fecha
            nhc = int(input("Ingrese Historia Clinica de la mascota: "))
            fecha = sistema.verFecha_Ingreso(nhc)
            print("La mascota con historia clinica: " + str(nhc) + " tienen fecha: " + fecha)
        #%%
        elif opcion == 1:
            #1. pregunto si hay capacidad
            if sistema.hayCapacidad() == False:
                print("El sistema esta lleno ...")
                continue
            
            #2. pregunto si existe la mascota
            continuar = True
            while continuar == True:
                nhc = int(input("Ingrese Historia Clinica de la mascota: "))
                if sistema.verificarMascota(nhc) == True:
                    print("Ya hay una mascota con esa historia clinica: ")
                else:
                    #si no hay una mascota con esa historia clinica continuo solicitando los datos
                    continuar = False
            #3. solicito los datos restantes
            n = input("Ingrese Nombre de la mascota: ")
            t = input("Ingrese el tipo de la mascota: ")
            p = int(input("Ingrese el peso de la mascota: "))
            d = int(input("Ingrese el la fecha, ingrese dia"))
            m = int(input("Ingrese el la fecha, ingrese mes"))
            a = int(input("Ingrese el la fecha, ingrese año"))
            f = datetime.datetime(a,m,d)
            # print(f.strftime("%x"))

            #4. organizar los medicamentos
            cantidad = int(input("Cuantos medicamentos tiene la mascota?: "))
            medicamentos = []
            for c in range(0,cantidad):
                nm = input("Ingrese el nombre del medicamento: ")
                d = int(input("Ingrese la dosis: "))
                medicamento = Medicamento()
                medicamento.asignarDosis(d)
                medicamento.asignarNombre(nm)
                medicamentos.append(medicamento)
            #5. creamos la mascota
            mascota = Mascota()
            mascota.asignarFecha_Ingreso(f.strftime("%x"))
            mascota.asignarLista_Medicamentos(medicamentos)
            mascota.asignarNHC(nhc)
            mascota.asignarPeso(p)
            mascota.asignarTipo(t)
            mascota.asignarNombre(n)
            #6. la anadimos al sistema
            sistema.ingresarMascota(mascota)
            print("Mascota ingresada")


Menu()
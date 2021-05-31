#TIC TAC TOE, ENTREGABLE 1
#Integrantes: Fabianna Julio, David Mceven
#4. Entregable

#Dibujamos el tablero:

#Creamos una clase llama Tablero, donde irán todos los elementos a ingresar:
from os import system, name
class Tablero:
    def __init__(self):#Constructor
        self.lista = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "," "]
        #Creamos un atributo en forma de lista,
         #para guardar los valores ingresados [1],[2],[3], [4]...
         #No usamos el [0] para que el jugador no se enrede
        
    def pantalla(self):#Lo que se muestra
        print(" {}  |  {}  | {}  ".format(self.lista[1],self.lista[2],self.lista[3]))#Usamos métodos format (w3school)
        print("-----------------")#Línea que separa cada fila, para darle forma
        print(" {}  |  {}  | {}  ".format(self.lista[4],self.lista[5],self.lista[6]))
        print("-----------------")
        print(" {}  |  {}  | {}  ".format(self.lista[7],self.lista[8],self.lista[9]))
        
    def seleccion(self, celda, Jugador):
        
        if self.lista[celda] == " ":
            self.lista[celda] = Jugador
        else: 
            print("Has ingresado una opción inválida,preciona 10 para intentarlo de nuevo")
            
    def ganador(self, Jugador):
        if self.lista[1] == Jugador and self.lista[2] == Jugador and self.lista[3] == Jugador:
            return True
        if self.lista[4] == Jugador and self.lista[5] == Jugador and self.lista[6] == Jugador:
            return True
        if self.lista[7] == Jugador and self.lista[8] == Jugador and self.lista[9] == Jugador:
            return True
        if self.lista[1] == Jugador and self.lista[4] == Jugador and self.lista[7] == Jugador:
            return True
        if self.lista[2] == Jugador and self.lista[5] == Jugador and self.lista[8] == Jugador:
            return True
        if self.lista[3] == Jugador and self.lista[6] == Jugador and self.lista[9] == Jugador:
            return True
        if self.lista[1] == Jugador and self.lista[5] == Jugador and self.lista[9] == Jugador:
            return True
        if self.lista[3] == Jugador and self.lista[5] == Jugador and self.lista[7] == Jugador:
            return True
        return False
    def empate(self):
            celdas_usadas = 0;
            for celd in self.lista:
                if celd != " ":
                    celdas_usadas += 1 
            if celdas_usadas == 9:
                return True
            else:
                return False

    def limpiar(self):
        self.lista = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
def Reiniciar_juego():
    #Método que limpia la terminal
    if name == "nt":
        _ = system("cls")
    table.pantalla()
    
table= Tablero()#Instanciamos objeto tablero para usar sus métodos
table.pantalla()
def main():
    while True:
        #inicio_tic()
        Reiniciar_juego()
        elecx = int(input("\n Jugador 1, Elija la opción del 1-9"))
        table.seleccion(elecx, "X")
        #Reiniciar_juego()
        
        if table.ganador("X") == True:
            print("\n Jugador X gana")
            jugar = int(input("¿Quieres jugar de nuevo? elige 1 \n De lo contrario presione cualquier tecla"))
            if jugar == 1:
                table.limpiar()
                Reiniciar_juego()
            else:
                print("Gracias por jugar")
                break
        if table.empate() == True:
            print("\n Empate")
            jugar = int(input("¿Quieres jugar de nuevo? elige 1 \n De lo contrario presione cualquier tecla"))
            if jugar == 1:
                table.limpiar()
                Reiniciar_juego()
            else:
                ("Gracias por jugar")
                break
            #obtener O
        eleco = int(input("\nJugador 2 , Elija opción del 1-9"))
        table.seleccion(eleco, "O")
        #Reiniciar_juego()
        if table.ganador("O") == True:
            print("\n Jugador 2 gana")
            jugar = int(input("¿Quieres jugar de nuevo? elige 1. \n de lo contrario presione cualquier tecla"))
            if jugar == 1:
                table.limpiar()
                Reiniciar_juego()
            else:
                print("Gracias por jugar")
                break
print("Bienvenido al triki :V")
main()

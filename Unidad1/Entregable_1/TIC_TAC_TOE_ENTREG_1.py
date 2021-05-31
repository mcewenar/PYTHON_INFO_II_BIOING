#TIC TAC TOE, ENTREGABLE 1
#4. Entregable

#Realice un algoritmo en Python, utilizando POO, que simule el juego del Tic Tac Toe. Para hacerlo tenga en cuenta lo siguiente:


    #4.1. El usuario podrá realizar sus movimientos con las teclas Q, W, E, A, S, D, Z, X y C o con las teclas de los números
    #7, 8, 9, 4, 5, 3, 2 y 1. Cada tecla representará una posición en la matriz. Encuentre una manera para lograr esto. 
    #Por ejemplo, cuando el usuario presione la letra Q el algoritmo debe identificar que en la posición 0,0 debe escribir 
    #una “X” o un “O”, según sea el caso.

    #4.2. El 3 en línea debe ser jugado por 2 usuarios, es decir, las decisiones de los movimientos serán realizadas por personas, no por el
    #algoritmo. Sugerencia: cree para cada jugador un objeto de la misma clase. De esta manera aprovecha la reutilización de código de POO.

    #4.3. Encuentre una forma para que el algoritmo realice un mapeo de la matriz y encuentre si hay algún ganador o no, que permita continuar 
    #en el juego.

#Dibujamos el tablero:

#Creamos una clase llama Tablero, donde irán todos los elementos a ingresar:
from os import system, name
class Tablero:
    def __init__(self): #Constructor
        self.celda = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "] 
        #Creamos un atributo en forma de lista,
         #para guardar los valores ingresados [1],[2],[3], [4]...
         #No usamos el [0] para que el jugador no se enrede

    def display(self): #Lo que se muestra
        print(" {}  |  {}  | {}  ".format(self.celda[1],self.celda[2],self.celda[3])) #Usamos métodos format (w3school)
        print("-----------------") #Línea que separa cada fila, para darle forma
        print(" {}  |  {}  | {}  ".format(self.celda[4],self.celda[5],self.celda[6]))
        print("-----------------")
        print(" {}  |  {}  | {}  ".format(self.celda[7],self.celda[8],self.celda[9]))
        
        

    def act_celda(self, celdanum, player):
        if self.celda[celdanum] == " ":
            self.celda[celdanum] = player;
        else: 
            print("Elige otra casilla");
    def ganador(self, player):
        if self.celda[1] == player and self.celda[2] == player and self.celda[3] == player:
            return True;
        if self.celda[4] == player and self.celda[5] == player and self.celda[6] == player:
            return True;
        if self.celda[7] == player and self.celda[8] == player and self.celda[9] == player:
            return True;
        if self.celda[1] == player and self.celda[4] == player and self.celda[7] == player:
            return True;
        if self.celda[2] == player and self.celda[5] == player and self.celda[8] == player:
            return True;
        if self.celda[3] == player and self.celda[6] == player and self.celda[9] == player:
            return True;
        if self.celda[1] == player and self.celda[5] == player and self.celda[9] == player:
            return True;
        if self.celda[3] == player and self.celda[5] == player and self.celda[7] == player:
            return True;
        
        return False;
    def empate(self):
        celdas_usadas = 0;
        for celd in self.celda:
            if celd != " ":
                celdas_usadas += 1 #recorre toda la lista para verficiar que todas estén llenas
        if celdas_usadas == 9:
            return True;
        else:
            return False;
    def reset_tablero(self):
        self.celda = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


table= Tablero() #Instanciamos objeto tablero para usar sus métodos
table.display()

#def inicio_tic():
    #print("Bienvenido a 3 in Line")

def Reiniciar_juego():
    #Método que limpia la terminal
    if name == "nt":
        _ = system("cls")

    table.display()

def main():
    while True:
        #inicio_tic()
        Reiniciar_juego()
    #Obtener x
        elecx = int(input("\n Jugador X, Elija la opción del 1-9"))
    #Agregamos tablero
        table.act_celda(elecx, "X")

        Reiniciar_juego();

        if table.ganador("X") == True:
            print("\n Jugador X gana")
            jugar_dnuevo = int(input("quieres jugar de nuevo, elige 1. \n 2, si no"))
            if jugar_dnuevo == 1:
                table.reset_tablero()
                Reiniciar_juego()
            elif jugar_dnuevo == 2:
                print("Bye, bye")
                break;
        if table.empate() == True:
            print("\n Empate")
            jugar_dnuevo = int(input("quieres jugar de nuevo, elige 1. \n 2, si no"))
            if jugar_dnuevo == 1:
                table.reset_tablero()
                Reiniciar_juego()
            elif jugar_dnuevo == 2:
                print("Bye, bye")
                break;


    #obtener O
        eleco = int(input("\nJugador O, Elija opción del 1-9"))

        table.act_celda(eleco, "O")
        Reiniciar_juego()

        if table.ganador("O") == True:
            print("\n Jugador O gana")
            jugar_dnuevo = int(input("quieres jugar de nuevo, elige 1. \n 2, si no"))
            if jugar_dnuevo == 1:
                table.reset_tablero()
                Reiniciar_juego()
            elif jugar_dnuevo == 2:
                print("Bye, bye")
                break;
    

main()



from os import system, name
class Tablero:
    def __init__(self):
        self.lista = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "] 
        
    def pantalla(self):
        print(" {}  |  {}  | {}  ".format(self.lista[1],self.lista[2],self.lista[3]))
        print("-----------------")
        print(" {}  |  {}  | {}  ".format(self.lista[4],self.lista[5],self.lista[6]))
        print("-----------------")
        print(" {}  |  {}  | {}  ".format(self.lista[7],self.lista[8],self.lista[9]))
        
    def seleccion(self, celda, Jugador):
        if self.lista[celda] == " ":
            self.lista[celda] = Jugador
        else: 
            print("Elige otra casilla")
            return Jugador
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
    if name == "nt":
        _ = system("cls")
    table.pantalla()
    
table= Tablero()
table.pantalla()
def main():
    while True:
        Reiniciar_juego()
        elecx = int(input("\n Jugador 1, Elija la opción del 1-9"))
        table.seleccion(elecx, "X")
        Reiniciar_juego()
        if table.ganador("X") == True:
            print("\n Jugador X gana")
            jugar = int(input("¿Quieres jugar de nuevo? elige 1. \n 2, si no"))
            if jugar == 1:
                table.limpiar()
                Reiniciar_juego()
            elif jugar== 2:
                print("Gracias por jugar")
                break
            else:
                print("ingrese opción valida")
                return jugar
        if table.empate() == True:
            print("\n Empate")
            jugar = int(input("¿Quieres jugar de nuevo? elige 1. \n 2, si no"))
            if jugar == 1:
                table.limpiar()
                Reiniciar_juego()
            elif jugar== 2:
                print("Gracias por jugar")
                break
            else:
                print("ingrese opción valida")
                return jugar

        eleco = int(input("\nJugador 2 , Elija opción del 1-9"))
        table.seleccion(eleco, "O")
        Reiniciar_juego()

        if table.ganador("O") == True:
            print("\n Jugador 2 gana")
            jugar = int(input("¿Quieres jugar de nuevo? elige 1. \n 2, si no"))
            if jugar == 1:
                table.limpiar()
                Reiniciar_juego()
            elif jugar == 2:
                print("Gracias por jugar")
                break
            else:
                print("ingrese opción valida")
                return jugar
print("Bienvenido al triki :V")
main()

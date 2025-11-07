def mostrar_tablero(tablero):
    for i in range(0, 9, 3):
        print(f"{tablero[i]} | {tablero[i+1]} | {tablero[i+2]}")
        if i < 6:
            print("--+---+--")
    print("\n")

def verificar_ganador(tablero, jugador):
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    
    for combo in combinaciones:
        if all(tablero[i] == jugador for i in combo):
            return True
    return False

def jugar_gato():  
    print("Bienvenido al juego del Gato")
    
    tablero = [" " for _ in range(9)]
    jugador = "X"
    ganador = False
    
    for turno in range(9):
        mostrar_tablero(tablero)
        
        while True:
            try:
                casilla = int(input(f"Jugador {jugador}, elige una casilla (1-9): ")) - 1
                
                if 0 <= casilla <= 8 and tablero[casilla] == " ":
                    break 
                else:
                    print("Casilla inválida. Elige un número del 1 al 9 y que esté vacía")
            except ValueError:
                print("Entrada inválida. Por favor, introduce un número entero")
                
        tablero[casilla] = jugador
        
        if verificar_ganador(tablero, jugador):
            ganador = True
            mostrar_tablero(tablero)
            print(f"Jugador {jugador} gana")
            break
        
        jugador = "O" if jugador == "X" else "X"

    if not ganador:
        mostrar_tablero(tablero)
        print("Empate")

if __name__ == "__main__":
    jugar_gato() 
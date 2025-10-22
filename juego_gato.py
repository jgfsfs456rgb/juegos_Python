tablero = [" " for _ in range(9)]

def mostrar_tablero():
    print("\n")
    for i in range(0, 9, 3):
        print(f"{tablero[i]} | {tablero[i+1]} | {tablero[i+2]}")
        if i < 6:
            print("--+---+--")
    print("\n")

def verificar_ganador(jugador):
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combo in combinaciones:
        if all(tablero[i] == jugador for i in combo):
            return True
    return False

def jugar():
    jugador = "X"
    for turno in range(9):
        mostrar_tablero()
        casilla = int(input(f"Jugador {jugador}, elige una casilla (1-9): ")) - 1
        if casilla < 0 or casilla > 8 or tablero[casilla] != " ":
            print("Casilla inválida. Intenta de nuevo.")
            continue
        tablero[casilla] = jugador
        if verificar_ganador(jugador):
            mostrar_tablero()
            print(f"¡Jugador {jugador} gana!")
            return
        jugador = "O" if jugador == "X" else "X"
    mostrar_tablero()
    print("¡Empate!")

print("Bienvenido al juego de Gato y Ratón (Tic Tac Toe)")
jugar()



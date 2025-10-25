print("Bienvenido al juego de Gato y Ratón (Tic Tac Toe)")
tablero = [" " for _ in range(9)]
combinaciones = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  
    [0, 3, 6], [1, 4, 7], [2, 5, 8],   
    [0, 4, 8], [2, 4, 6]               
]

jugador = "X"
for turno in range(9):
    print("\n")
    for i in range(0, 9, 3):
        print(f"{tablero[i]} | {tablero[i+1]} | {tablero[i+2]}")
        if i < 6:
            print("--+---+--")
    print("\n")
    casilla = int(input(f"Jugador {jugador}, elige una casilla (1-9): ")) - 1
    if casilla < 0 or casilla > 8 or tablero[casilla] != " ":
        print("Casilla inválida. Intenta de nuevo.")
        continue
    tablero[casilla] = jugador
    ganador = False
    for combo in combinaciones:
        if all(tablero[i] == jugador for i in combo):
            ganador = True
            break
    if ganador:
        print("\n")
        for i in range(0, 9, 3):
            print(f"{tablero[i]} | {tablero[i+1]} | {tablero[i+2]}")
            if i < 6:
                print("--+---+--")
        print("\n")
        print(f"¡Jugador {jugador} gana!")
        break
    jugador = "O" if jugador == "X" else "X"
if not ganador:
    print("\n")
    for i in range(0, 9, 3):
        print(f"{tablero[i]} | {tablero[i+1]} | {tablero[i+2]}")
        if i < 6:
            print("--+---+--")
    print("\n")
    print("¡Empate!")



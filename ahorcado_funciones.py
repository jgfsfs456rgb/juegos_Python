import random

def seleccionar_palabra(lista_palabras):
    return random.choice(lista_palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
  
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra
        else:
            tablero += "_"
    return tablero

def jugar_ahorcado():
    palabras = ["telefono", "calculadora", "gato", "ingeniero", "software", "computacion"]
    palabra_secreta = seleccionar_palabra(palabras)
    letras_adivinadas = []
    intentos = 3

    print("Bienvenido al juego del ahorcado. Tienes 3 vidas")
    print("Empezamos")

    while intentos > 0:
        tablero = mostrar_tablero(palabra_secreta, letras_adivinadas)
        print("\nPalabra:", tablero)

        if tablero == palabra_secreta:
            print(f"\n¡Felicidades! Has acertado la palabra:{palabra_secreta}")
            break

        letra_ingresada = input("Introduce una letra: ").lower()

        if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
            print("Por favor, introduce una única letra válida.")
            continue
            
        if letra_ingresada in letras_adivinadas:
            print("Ya probaste esa letra, intenta con otra.")
            continue
        
        if letra_ingresada in palabra_secreta:
            letras_adivinadas.append(letra_ingresada)
            print("¡Acierto!")

        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intento(s).")
            letras_adivinadas.append(letra_ingresada) 
            
    if intentos == 0:
        print(f"\nHas perdido. La palabra era:{palabra_secreta}")
   
jugar_ahorcado()

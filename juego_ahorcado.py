import random
print("Bienvenido al juego del ahorcado. Tienes 3 vidas.")
print("Empezamos")
palabras = ["telefono", "calculadora", "gato", "ingeniero", "software", "computacion"]
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
intentos = 3
while intentos > 0:
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra
        else:
            tablero += "_"
    print("Palabra:", tablero)
    letra_ingresada = input("Introduce una letra: ").lower()
    if letra_ingresada in letras_adivinadas:
        print("Ya probaste esa letra, intenta con otra.")
        continue
    if letra_ingresada in palabra_secreta:
        letras_adivinadas.append(letra_ingresada)
        todas_adivinadas = True
        for letra in palabra_secreta:
            if letra not in letras_adivinadas:
                todas_adivinadas = False
                break
        if todas_adivinadas:
            print("¡Felicidades! Has acertado la palabra:", palabra_secreta)
            break
    else:
        intentos -= 1
        print(f"Letra incorrecta. Te quedan {intentos} intento(s).")
if intentos == 0:
    print(f"Has perdido. La palabra era: {palabra_secreta}")

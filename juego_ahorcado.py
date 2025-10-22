import random

print("Bienvenido al juego del ahorcado tienes 3 vidas")
print("Empezamos")
def obtener_palabra_aleatoria():
    palabras = ["telefono", "calculadora", "gato", "ingeniero", "software", "computacion"]
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero+="_"
    print(tablero)
        
def jugar():
    palabra_secreta=obtener_palabra_aleatoria()
    letras_adivinadas=[]
    intentos=3

    while intentos>0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra=input("introduce una letra:").lower()

        if letra in letras_adivinadas:
            print("Ya probaste esa letra ingresa otra")
            continue
        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            if set(letras_adivinadas)==set(palabra_secreta):
             print("Haz acertado la palabra")
             break
        else:
            intentos-=1
            print(f"Letra incorrecta te quedan {intentos}")
    if intentos==0:
        print(f"perdiste la palabra era {palabra_secreta}")

jugar()
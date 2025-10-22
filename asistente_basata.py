#import random #Nos va a importar TODA la librería
from random import choice
from time import sleep
from os import system

#Lista de las categorías que debemos adivinar en el juego
categorias = {}
letras = "abcdefghijklmnopqrstuvwxyz"
puntosTotales = 0
contadorRondas = 0

print("\n---¡Bienvenido al asistente del juego Basta!---")
print("Configura las categorías de tu juego Basta\n")
contadorCategoria = 0
while True:
    contadorCategoria += 1
    categoria = input("Ingresa categoría (deja vació para salir): ")
    if categoria == "":
        break
    categorias[contadorCategoria] = categoria.capitalize()

sleep(2)
system("clear")

"""
        1. Elegir la letra para jugar
        2. Mostrar categorías
        3. Preguntar los valores de las categorías
        4. Preguntar puntos
        5. Sumar puntos a Totales
        6. Preguntar si quiere seguir jugando
"""
while True:
    contadorRondas += 1
    #Elegir una letra random del abecedario
    letra = choice(letras)
    letras = letras.replace(letra,"")
    print(f"\n¡Comienza la ronda {contadorRondas}, con la letra: {letra.upper()}!")
    valoresCategorias = categorias.values()
    print("Categorías: ", ", ".join(map(str, valoresCategorias)))

    print("Pensando...")
    sleep(3)

    palabras = {} #Diccionario para almacenar las palabras que ingrese el usuario por categoría
    """for categoria in categorias:
        palabra = input(f"\nCon la letra {letra.upper()}, introduce {categoria}: ")
        palabras[categoria] = palabra
    """
    while True:
        for llave, valor in categorias.items():
            print(f"{llave}. {valor.capitalize()}")
        categoriaSeleccionada = input("\nSelecciona categoria (-1 para salir): ")

        if categoriaSeleccionada == "-1" or categoriaSeleccionada.isalpha():
            break
        if categoriaSeleccionada == "":
            continue
        else:
            categoriaSeleccionada = int(categoriaSeleccionada)
            palabra = input(f"\n{categorias[categoriaSeleccionada]} con la letra {letra.upper()}: ")
            palabras[categorias[categoriaSeleccionada]] = palabra.capitalize()

    print("\n--Tus entradas fueron--")
    for categoria, palabra in palabras.items():
        print(f"{categoria} --> {palabra.capitalize()}")

    sleep(3)
    print("\n--Ingresa tus puntos por categoría--")
    puntosRonda = 0
    for llave, categoria in categorias.items():
        puntosCategoria = input(f"Puntos obtenidos en {categoria}: ")
        if puntosCategoria == "":
            puntosCategoria = 0
        elif puntosCategoria.isnumeric():
            puntosRonda += int(puntosCategoria)
        else:
            puntosCategoria = 0

    print(f"\nPuntos Ronda: {puntosRonda}")
    puntosTotales += puntosRonda

    sleep(5)
    system("clear") #Windows system(cls)

    continuar = input("\n¿Quieres seguir jugando? (s/n)")
    if continuar.lower() != "s":
        break

print("\nPuntos Totales: ", puntosTotales)
print("¡Adiós!")

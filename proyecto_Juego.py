import tkinter as tk
from tkinter import messagebox
import json 
import os
from datetime import datetime

# VARIABLES GLOBALES Y CONSTANTES (¡Todo lo importante va aquí!) 

ARCHIVO_GUARDAR = "datos_de_juego.json"  # Aquí guardamos los récords, ¡pa' que no se pierdan!

# Las 8 formas de ganar, ¡la lógica es la que rifa!
FORMAS_DE_GANAR = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

# Variables del estado del juego (cosas que cambian)
mi_tablero = [""] * 9
jugador_activo = "X"
partida_terminada = False
botones_tablero = []

# Variables de la interfaz (para que Tkinter jale)
ventana_principal = None
label_info_turno = None
marcador_victorias = {"X": 0, "O": 0} # Contador de puntos


#  SECCIÓN DE PERSISTENCIA (Para que el profe vea que guardamos datos)

def guardar_record(quien_gano: str):
    """
    Guarda el resultado de la partida en el archivo JSON. 
    ¡Para tener historial y presumir quién es el mejor!

    Args:
        quien_gano (str): El ganador de la partida ("X", "O" o "Empate").
    """
    
    # Armamos el paquetito de datos para guardar
    datos_de_esta_partida = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ganador": quien_gano,
        "tablero_final": "".join(mi_tablero) # Lo guardamos como una cadena simple, ¡fácil!
    }

    # Intentamos cargar lo que ya había
    historial_cargado = []
    if os.path.exists(ARCHIVO_GUARDAR):
        try:
            with open(ARCHIVO_GUARDAR, 'r') as f:
                historial_cargado = json.load(f)
        except:
            # Si el archivo está roto o vacío, ¡ni modo! Empezamos de cero.
            historial_cargado = [] 

    # Agregamos la nueva partida al final y guardamos de nuevo
    historial_cargado.append(datos_de_esta_partida)
    with open(ARCHIVO_GUARDAR, 'w') as f:
        json.dump(historial_cargado, f, indent=4) # El indent=4 es para que se vea bonito

def cargar_records_y_ver():
    """
    Carga todos los resultados y muestra las estadísticas en una ventana.
    Ideal para ver cuántas veces has ganado.
    """
    try:
        with open(ARCHIVO_GUARDAR, 'r') as f:
            historial = json.load(f)
    except:
        messagebox.showinfo("Historial", "Aún no hay partidas guardadas, ponte a jugar")
        return

    # Contamos quién ha ganado en todo el historial
    victorias_x = sum(1 for p in historial if p['ganador'] == 'X')
    victorias_o = sum(1 for p in historial if p['ganador'] == 'O')
    empates_totales = sum(1 for p in historial if p['ganador'] == 'Empate')
    
    total_de_juegos = len(historial)
    
    # Preparamos el mensaje para el cuadro emergente
    mensaje = f"Récords Generales\n"
    mensaje += f"Partidas Jugadas: {total_de_juegos}\n"
    mensaje += f"Victorias de X: {victorias_x}\n"
    mensaje += f"Victorias de O: {victorias_o}\n"
    mensaje += f"Empates: {empates_totales}\n\n"
    mensaje += f"Marcador Actual:\n"
    mensaje += f"  X: {marcador_victorias['X']} | O: {marcador_victorias['O']}"

    messagebox.showinfo("Estadísticas", mensaje)

#  SECCIÓN DE LÓGICA DEL JUEGO (Lo que hace que funcione)

def checar_si_hay_ganador() -> bool:
    """
    Verifica si el jugador que está jugando ahora completó una línea.

    Returns:
        bool: True si ya ganó, False si aún sigue la pelea.
    """
    for combo in FORMAS_DE_GANAR:
        # Checa si las 3 casillas tienen la marca del jugador_activo
        if mi_tablero[combo[0]] == jugador_activo and \
           mi_tablero[combo[1]] == jugador_activo and \
           mi_tablero[combo[2]] == jugador_activo:
            return True
    return False

def resetear_juego():
    """
    Deja las variables listas para empezar otra partida.
    """
    global mi_tablero, jugador_activo, partida_terminada
    
    mi_tablero = [""] * 9 # Tablero de nuevo en blanco
    jugador_activo = "X" # Siempre empieza la X, es la regla
    partida_terminada = False
    
    label_info_turno.config(text=f"Turno de: {jugador_activo}")
    for boton in botones_tablero:
        boton.config(text="") # Limpiamos los botones

def manejar_clic(indice_casilla: int):
    """
    Se ejecuta cada vez que alguien hace clic en una casilla del tablero.
    Aquí pasa toda la magia (la lógica del turno).

    Args:
        indice_casilla (int): El número de casilla presionado (de 0 a 8).
    """
    global mi_tablero, jugador_activo, partida_terminada
    
    # Manejo de errores (básico, ¡pero funcional!)
    if partida_terminada:
        messagebox.showwarning("Aviso", "Ya estuvo Dale a Reiniciar.")
        return
    if mi_tablero[indice_casilla] != "":
        messagebox.showwarning("Aviso", "No se vale Esa ya está ocupada.")
        return

    # 1. Marcamos y actualizamos la interfaz
    mi_tablero[indice_casilla] = jugador_activo
    botones_tablero[indice_casilla].config(text=jugador_activo)

    # 2. ¿Ganó? 
    if checar_si_hay_ganador():
        partida_terminada = True
        marcador_victorias[jugador_activo] += 1 # Le sumamos el punto
        label_info_turno.config(text=f"siuuu Ganó {jugador_activo}")
        guardar_record(jugador_activo) # Guardamos el récord
        messagebox.showinfo("Eres mi hijo", f"¡{jugador_activo} se llevó la ronda!")
        
    # 3. ¿Empate? (Checamos si no quedan espacios vacíos)
    elif "" not in mi_tablero:
        partida_terminada = True
        label_info_turno.config(text="EMPATE")
        guardar_record("Empate")
        messagebox.showinfo("Empate", "Qué aburrido Nadie ganó.")
        
    # 4. Si no, cambiamos de turno
    else:
        # Esto alterna rápido entre X y O
        jugador_activo = "O" if jugador_activo == "X" else "X" 
        label_info_turno.config(text=f"Turno de: {jugador_activo}")

# SECCIÓN DE LA INTERFAZ (Tkinter) Y ARRANQUE

def armar_la_interfaz():
    """
    Define y coloca todos los botones, etiquetas y frames en la ventana.
    """
    global ventana_principal, label_info_turno
    
    ventana_principal.title("Proyecto Gato - El Crack")
    
    # La etiqueta que dice quién va o quién ganó
    label_info_turno = tk.Label(ventana_principal, text=f"Turno de: {jugador_activo}", font=('Arial', 18, 'bold'))
    label_info_turno.pack(pady=10)

    # Creamos un frame para el tablero para que se vea ordenado
    frame_tablero = tk.Frame(ventana_principal)
    frame_tablero.pack()

    # Bucle para crear los 9 botones del gato
    for i in range(9):
        fila = i // 3
        columna = i % 3

        # El 'command' llama a manejar_clic con el índice de este botón
        boton = tk.Button(frame_tablero, text="", font=('Arial', 26),
                          width=4, height=2,
                          command=lambda i=i: manejar_clic(i))
        
        boton.grid(row=fila, column=columna, padx=5, pady=5)
        botones_tablero.append(boton) # Los guardamos para poder editarlos después
        
    # Botones de control extra
    frame_control = tk.Frame(ventana_principal)
    frame_control.pack(pady=15)
    
    # Botón Reiniciar
    tk.Button(frame_control, text="¡Otra Ronda!", command=resetear_juego).pack(side=tk.LEFT, padx=10)
    # Botón de Persistencia
    tk.Button(frame_control, text="Ver Récords", command=cargar_records_y_ver).pack(side=tk.LEFT, padx=10)

def iniciar_proyecto():
    """
    Función principal (main). Es el punto de inicio.
    """
    global ventana_principal
    
    ventana_principal = tk.Tk()
    
    armar_la_interfaz()
    resetear_juego() # Aseguramos que empiece bien
    
    # ¡A correr! (Esto mantiene la ventana abierta)
    ventana_principal.mainloop()

if __name__ == "__main__":
    iniciar_proyecto()
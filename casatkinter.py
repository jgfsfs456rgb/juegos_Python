import tkinter as tk

def casa(canvas):
    canvas.create_rectangle(0, 0, 400, 250, fill="#ADD8E6", outline="#ADD8E6") 
    canvas.create_oval(320, 40, 390, 110, fill="#FFD700", outline="#FFD700") 
    canvas.create_rectangle(0, 250, 400, 400, fill="#556B2F", outline="#556B2F") 

    x_origen_casa = 120
    y_base_casa = 320
    ancho_casa = 160
    alto_casa = 130
    
    canvas.create_rectangle(
        x_origen_casa, y_base_casa - alto_casa,
        x_origen_casa + ancho_casa, y_base_casa,
        fill="#D3D3D3", 
        outline="black"
    )

    puntos_tejado = [
        x_origen_casa + ancho_casa / 2, y_base_casa - alto_casa - 80, 
        x_origen_casa - 10, y_base_casa - alto_casa, 
        x_origen_casa + ancho_casa + 10, y_base_casa - alto_casa 
    ]
    canvas.create_polygon(
        puntos_tejado,
        fill="#B22222", 
        outline="black"
    )

    ancho_puerta = 50
    alto_puerta = 90
    x_puerta = x_origen_casa + (ancho_casa / 2) - (ancho_puerta / 2)
    canvas.create_rectangle(
        x_puerta, y_base_casa - alto_puerta,
        x_puerta + ancho_puerta, y_base_casa,
        fill="#A0522D", 
        outline="black"
    )

    ancho_ventana = 40
    alto_ventana = 40
    x_ventana1 = x_origen_casa + 20
    y_ventana1 = y_base_casa - alto_casa + 30
    canvas.create_rectangle(
        x_ventana1, y_ventana1,
        x_ventana1 + ancho_ventana, y_ventana1 + alto_ventana,
        fill="#4682B4", 
        outline="black"
    )

    x_ventana2 = x_origen_casa + ancho_casa - ancho_ventana - 20
    canvas.create_rectangle(
        x_ventana2, y_ventana1, 
        x_ventana2 + ancho_ventana, y_ventana1 + alto_ventana,
        fill="#4682B4", 
        outline="black"
    )

root = tk.Tk()
root.title("Casita con Cielo Despejado") 
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()
casa(canvas) 

root.mainloop()

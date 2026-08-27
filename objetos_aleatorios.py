from tkinter import *
import random

#---------------------
# Variables globales
#----------------------
BASE = 460
ALTURA = 220

#--------------------
# Ventana principal
#-------------------

ventana_principal = Tk()
ventana_principal.title("Grafucas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="#747580")

#--------------------------
# Frame de graficacion
#-------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="#E19E71", width=480, height=240)
frame_graficacion.place(x=10, y=10)

#----------------------------------
# Lienzo de graficasion
#---------------------------------
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="#B7E9BF")
c.place(x=10, y=10)

#--------------------------------
# dibujar n objetos de tamaño y objetos aleatorios
#----------------------------------
# lineas rectas
for i in range(50):
    # punto inicialde la linea
    x1 = random.randint(10, int(BASE//2))
    y1 = random.randint(10, ALTURA)
    # punto final de la linea
    X2 = random.randint(10, int(BASE/2))
    Y2 = random.randint(10, ALTURA)

    # generar un color aleatorio
    color = "#"

    for caracter in range(6):
        color = color + random.choice("0123456789ABCDEF")
    # Dibujar la linea
    linea = c.create_line(x1, y1, X2, Y2, fill=color, width=2)

# circulos de tamaño 20x20
for i in range(50):
    # punto inicial de la linea
    x1 = random.randint( int(BASE/2), BASE-20)
    y1 = random.randint(0, ALTURA-20)
    # punto final de la linea
    X2 = x1 + 20
    Y2 = y1 + 20

    # generar un color aleatorio
    color = "#"

    for caracter in range(6):
        color = color + random.choice("0123456789ABCDEF")
    # Dibujar la linea
    circulo = c.create_oval(x1, y1, X2, Y2, fill=color, width=2)    


#----------------------------------
# frame de cpontroles   
#---------------------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="#E19E71", width=480, height=230)
frame_controles.place(x=10, y=260)                                          





#------------------------
# Desplegar ventana principal
#--------------------------
ventana_principal.mainloop()
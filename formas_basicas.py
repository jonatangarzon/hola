from tkinter import *

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

#------------------------------
# Lineas rectas
#-------------------------------
linea_1 = c.create_line(BASE/2, ALTURA/2, BASE, 0, fill="#A794B6", width=2)
linea_2 = c.create_line(0,0,BASE/2, ALTURA/2, fill="#FFA700", width=2)
linea_3 = c.create_line(0,ALTURA,BASE/2, ALTURA/2, fill="#9095CA", width=2)
linea_4 = c.create_line(BASE,ALTURA, BASE/2, ALTURA/2, fill="#B7B3A7", width=2)

#-------------------------------
# Texto
#------------------------------
texto_1 = c.create_text(BASE/3,ALTURA/4, anchor="center", text="Jonatan Garzon",
font=("Arial", 25, "bold"), fill="blue", activefill="black")

#----------------------------
# Rectangulos
#----------------------------
rectangulo_1 = c.create_rectangle(BASE/2, ALTURA/2, BASE,ALTURA, fill="pink", 
outline="#8684C1")

#----------------------------
# poligonos
#----------------------------
poligono_1 = c.create_polygon(0,0, BASE/2, ALTURA/2, 0, ALTURA, fill="red", outline="red")

#----------------------------
# Círculos
#----------------------------
cirvulo_1 = c.create_oval(BASE/2 - 50, ALTURA/2 - 50, BASE/2 + 50, ALTURA/2 + 50, fill="#6ABABF", outline="green")

#----------------------------
# Círculos
#----------------------------
cirvulo_2 = c.create_oval(BASE/2 - 50, ALTURA/2 - 50, BASE/2 + 150, ALTURA/2 + 150, fill="#6ABABF", outline="green")


#----------------------------
# Arcos
#----------------------------
arco_1 = c.create_arc(BASE/2 - 30, ALTURA/2 - 30, BASE/2 + 30, ALTURA/2 + 30, start=30, extent=300, fill="#FFFF50")


#------------------------
# Desplegar ventana principal
#--------------------------
ventana_principal.mainloop()
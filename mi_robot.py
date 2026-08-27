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
ventana_principal.title("robot V 2.0")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x700")
ventana_principal.config(bg="#747580")

#--------------------------
# Frame de graficacion
#-------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="#E19E71", width=480, height=680)
frame_graficacion.place(x=10, y=10)

#----------------------------------
# creación canvas
#---------------------------------
c = Canvas(frame_graficacion, width=460, height=660)
c.config(bg="#B7E9BF")
c.place(x=10, y=10)



#------------------------------
# Lineas rectas
#-------------------------------
linea_1 = c.create_line(BASE/2- 130, ALTURA/2+ 500, BASE/2+ 0, 330, fill="gray", width=12)
linea_2 = c.create_line(BASE/2, ALTURA/2+ 240, BASE/2, ALTURA/2- 0, fill="gray" , width=12)
linea_3 = c.create_line(BASE/2+ 130, ALTURA/2+ 500, BASE/2+ 0, 330, fill="gray", width=12)
linea_4 = c.create_line(BASE- 100, ALTURA- 0, BASE/2+ 0, 110, fill="gray", width=12)
linea_5 = c.create_line(BASE- 375, ALTURA- 0, BASE/2+ 0, 110, fill="gray", width=12)
linea_6= c.create_line(BASE/2- 130, ALTURA/2+ 500, BASE/2+ 0, 330, fill="gray", width=60)
linea_7 = c.create_line(BASE/2, ALTURA/2+ 240, BASE/2, ALTURA/2- 0, fill="gray" , width=60)
linea_8 = c.create_line(BASE/2+ 130, ALTURA/2+ 500, BASE/2+ 0, 330, fill="gray", width=60) 
linea_9 = c.create_line(BASE- 100, ALTURA- 0, BASE/2+ 0, 110, fill="gray", width=60)
linea_10 = c.create_line(BASE- 375, ALTURA- 0, BASE/2+ 0, 110, fill="gray", width=60)

#-----------------------------
#triangulos
#-----------------------------
triangulo_1 = c.create_polygon(BASE/2- 130, ALTURA/2+ 500, BASE/2+ 0, 330, BASE/2+ 130, ALTURA/2+ 500, fill="gray", outline="green")
triangulo_2 = c.create_polygon(BASE- 100, ALTURA- 0, BASE/2+ 0, 110, BASE- 375, ALTURA- 0, fill="gray", outline="green")

#------------------------------
# Rectángulos
#------------------------------
rectangulo_1 = c.create_rectangle(BASE/2- 130, ALTURA/2+ 500, BASE/2+ 130, ALTURA/2+ 500, fill="gray", outline="green")
rectangulo_2 = c.create_rectangle(BASE- 100, ALTURA- 0, BASE- 375, ALTURA- 0, fill="gray", outline="green")

#-----------------------------
# Círculos
#-----------------------------  
circulo_1 = c.create_oval(BASE- 270, ALTURA/2- 90, BASE/2+ 50, ALTURA/2 + 10, fill="orange", outline="green")

#-----------------------------
#CARA DEL ROBOT
#-----------------------------
cara_1 = c.create_oval(BASE- 270, ALTURA/2- 90, BASE/2+ 50, ALTURA/2 + 10, fill="orange", outline="green")
ojo_1 = c.create_oval(BASE- 250, ALTURA/2- 70, BASE- 200, ALTURA/2- 20, fill="white", outline="BLACK", width=19)

# texto
texto = c.create_text(BASE/2, ALTURA/2 -90, anchor="center", text="TERRENEITOR", font=("courier", "30", "bold"), fill="blue", activefill="red")
texto = c.create_text(BASE/2, ALTURA/2 + 520, anchor="center", text="JONATAN", font=("courier", "30", "bold"), fill="blue", activefill="red")
texto = c.create_text(BASE/2, ALTURA/2 -90, anchor="center", text="TERRENEITOR", font=("courier", "30", "bold"), fill="blue", activefill="red")
texto = c.create_text(BASE/2, ALTURA/2 + 100, anchor="center", text="🥵​🥵​🥵​", font=("courier", "15", "bold"), fill="blue", activefill="red")

#------------------------
# Desplegar ventana principal
#--------------------------
ventana_principal.mainloop()
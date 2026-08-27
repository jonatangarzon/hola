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



#------------------------
# Desplegar ventana principal
#--------------------------
ventana_principal.mainloop()
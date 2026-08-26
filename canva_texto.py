from tkinter import *

# variables globales
BASE = 460
ALTURA = 380

# ventana principal
ventana_principal = Tk()
ventana_principal.title("Graficas 2D - Texto")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="green")

# frame de graficación
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480, height=400)
frame_graficacion.pack(fill=BOTH, padx=10, pady=10)

# creación canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.place(x=10, y=10)

# texto
texto = c.create_text(BASE/2, ALTURA/2, anchor="center", text="Sistemas Guanentá", font=("Arial", "30", "bold"), fill="blue", activefill="red")

ventana_principal.mainloop()
# frame de graficación

from tkinter import *
import tkinter
from tkinter import messagebox
ventana = tkinter.Tk()  # Aqui se crea la ventana principal
ventana.geometry("950x550")#es para el tamaño de la ventana
ventana.title("Lavalimpia-Inicio de sesión") #Es para el titulo de la ventana
ventana.configure(bg="#188999") #Color del fondo de la ventana
ventana.resizable(False,False) # se desactiva el cambio de tamaño de la ventana


def salirApp():
    valor=messagebox.askokcancel(" Cerrar sesión","Estas segurisimo de querer salir?")
    if valor==True:
        ventana.destroy()

boton_cerrar = Button(ventana,text=" Cerrar sesión  ", command=salirApp, bg= "red", fg="white") #Boton para cerrar la ventana emergente
boton_cerrar.place(x=820,y=20)    #se ubica el boton



boton1= Button(ventana, text="Buscador de pedidios",font=("arial",18))
boton1.configure(bg="blue",fg="#ffffff")
boton1.place(x=200,y=200)



boton2= Button(ventana, text="Datos y estadísticas",font=("arial",18))
boton2.configure(bg="blue",fg="#ffffff")
boton2.place(x=500,y=200)


ventana.mainloop()
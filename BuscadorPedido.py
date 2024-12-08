from tkinter import *
import tkinter

ventana = tkinter.Tk()  # Aqui se crea la ventana principal
ventana.geometry("950x550")#es para el tamaño de la ventana
ventana.title("Lavalimpia-Inicio de sesión") #Es para el titulo de la ventana
ventana.configure(bg="#188999") #Color del fondo de la ventana
ventana.resizable(False,False) # se desactiva el cambio de tamaño de la ventana


ticket=Label(ventana,text="N°de ticket:",font=("arial",18), bg="#188999")
ticket.place(x=50,y=100, height=30)

ticket1=Entry(ventana)
ticket1.place(x=190,y=100, width=70, height=30)

ticket=Label(ventana,text="ID usuario:",font=("arial",18), bg="#188999")
ticket.place(x=270,y=100, height=30)

ticket1=Entry(ventana)
ticket1.place(x=400,y=100, width=70, height=30)


Boton=Button(ventana, text="Buscar",font=("arial",14))
Boton.place(x=600,y=100,width=100)


Nticket=Label(ventana, text="N°Ticket",font=("arial",12), bg="#188999",bd=2, relief="solid", fg="black")
Nticket.place(x=90,y=200,width=140,height=30)


SalidaTicket=Label(ventana,bd=2, relief="solid", fg="black")
SalidaTicket.place(x=90,y=230,width=140,height=30)



Id=Label(ventana, text="ID usuario",font=("arial",12), bg="#188999",bd=2, relief="solid", fg="black")
Id.place(x=230,y=200,width=140,height=30)

SalidaId=Label(ventana,bd=2, relief="solid", fg="black")
SalidaId.place(x=230,y=230,width=140,height=30)


Fecha=Label(ventana, text="Fecha",font=("arial",12), bg="#188999",bd=2, relief="solid", fg="black")
Fecha.place(x=360,y=200,width=140,height=30)

SalidaFecha=Label(ventana,bd=2, relief="solid", fg="black")
SalidaFecha.place(x=360,y=230,width=140,height=30)


Estado=Label(ventana, text="Estado",font=("arial",12), bg="#188999",bd=2, relief="solid", fg="black")
Estado.place(x=500,y=200,width=140,height=30)

SalidaEstado=Label(ventana,bd=2, relief="solid", fg="black")
SalidaEstado.place(x=500,y=230,width=140,height=30)


















ventana.mainloop()
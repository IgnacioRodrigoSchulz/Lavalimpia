import tkinter
 
def creador_de_pedidos():
    ventana_operador = tkinter.Tk()
    ventana_operador.geometry("950x550")
    ventana_operador.title("Lavalimpia")
    ventana_operador.configure(bg="#188999")
    ventana_operador.resizable(False,False)
    ventana_operador.iconbitmap("fondoL.ico")

    etiqueta001= tkinter.Label(ventana_operador,text="Creador de pedidos", font= ("Britannic Bold",28))
    etiqueta001.configure(bg="#188999")
    etiqueta001.place(x=40,y=30) 

    boton_salir =tkinter.Button(ventana_operador, text="Cerrar sesión",font=("Arial", 10), cursor="hand2")
    boton_salir.configure(bg="#e31414",fg="#ffffff")
    boton_salir.place(x=840,y=8,width=100, height=25) 

    etiqueta003 = tkinter.Label(ventana_operador, text= "Usuario",font=("Arial", 12))
    etiqueta003.configure(bg="#188999",fg="#ffffff")
    etiqueta003.place(x=120,y=120) 

    Texto_nro_ticket = tkinter.Entry(ventana_operador) 
    Texto_nro_ticket.place(x=120,y=150, width=280, height=30)

    etiqueta004 = tkinter.Label(ventana_operador, text= "Dirección",font=("Arial", 12))
    etiqueta004.configure(bg="#188999",fg="#ffffff")
    etiqueta004.place(x=120,y=190) 

    Texto_nro_ticket = tkinter.Entry(ventana_operador) 
    Texto_nro_ticket.place(x=120,y=220, width=280, height=30)

    etiqueta005 = tkinter.Label(ventana_operador, text= "Tarifa",font=("Arial", 12))
    etiqueta005.configure(bg="#188999",fg="#ffffff")
    etiqueta005.place(x=120,y=260) 

    Texto_nro_ticket = tkinter.Entry(ventana_operador) 
    Texto_nro_ticket.place(x=120,y=290, width=280, height=30)

    boton_info = tkinter.Button(ventana_operador, text="Crear pedido",font=("Arial", 20))
    boton_info.configure(bg="#2a3ab6",fg="#ffffff")
    boton_info.place(x=360,y=410,width=260, height=40) 

    ventana_operador.mainloop()

creador_de_pedidos()
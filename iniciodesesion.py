import tkinter as tk

imagenes=[]

def inicio_de_sesion():
    ventana_usuario = tk.Tk()
    ventana_usuario.geometry("950x550")
    ventana_usuario.title("Lavalimpia")
    ventana_usuario.configure(bg="#188999")
    ventana_usuario.resizable(False,False)
    ventana_usuario.iconbitmap("fondoL.ico")

    etiqueta01= tk.Label(ventana_usuario,text="Información de pedido", font= ("Britannic Bold",28))
    etiqueta01.configure(bg="#188999")
    etiqueta01.place(x=40,y=30)

    foto_logo2= tk.PhotoImage(file="Logo2.png")
    imagenes.append(foto_logo2)
    logo2=tk.Label(ventana_usuario,image=foto_logo2,bd=0)
    logo2.place(x=55,y=240)

    boton_salir =tk.Button(ventana_usuario, text="Cerrar sesión",font=("Arial", 10), cursor="hand2")
    boton_salir.configure(bg="#e31414",fg="#ffffff")
    boton_salir.place(x=840,y=8,width=100, height=25) 

    etiqueta02 = tk.Label(ventana_usuario, text= "Mis pedidos",font=("Arial", 18))
    etiqueta02.configure(bg="#ffffff")
    etiqueta02.place(x=420,y=180,width=250, height=30) 

    etiqueta03 = tk.Label(ventana_usuario, text= "N° de ticket",font=("Arial", 12))
    etiqueta03.configure(bg="#188999")
    etiqueta03.place(x=420,y=220) 

    Texto_nro_ticket = tk.Entry(ventana_usuario) 
    Texto_nro_ticket.place(x=420,y=245, width=250, height=30)

    etiqueta04 = tk.Label(ventana_usuario, text= "N° de ticket",font=("Arial", 12))
    etiqueta04.configure(bg="#188999")
    etiqueta04.place(x=420,y=280) 

    Texto_nro_ticket = tk.Entry(ventana_usuario) 
    Texto_nro_ticket.place(x=420,y=310, width=250, height=30)

    boton_info = tk.Button(ventana_usuario, text="Información del pedido",font=("Arial", 20))
    boton_info.configure(bg="#2a3ab6",fg="#ffffff")
    boton_info.place(x=400,y=370,width=300, height=40) 

    ventana_usuario.mainloop()

inicio_de_sesion()
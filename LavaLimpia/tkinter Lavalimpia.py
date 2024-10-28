import tkinter #sirve para importar tkinter

ventana = tkinter.Tk()  #sirve para crear una ventana
ventana.geometry("950x500")#es para el tamaño de la ventana
ventana.title("Lavalimpia") #Es para el titulo
ventana.configure(bg="#3f88c5")
ventana.resizable(False,False)

etiqueta1 = tkinter.Label(ventana, text="Inicio de sesión", font=("Arial", 20))  #es una etiqueta y el tamaño de fuente
etiqueta1.configure(bg="#3f88c5")
etiqueta1.place(x=450, y=100) 

foto_logo= tkinter.PhotoImage(file="logoLavaLimpia.png")
logo=tkinter.Label(ventana, image=foto_logo)
logo.place(x=50,y =100)

etiqueta2 = tkinter.Label(ventana, text= "Ingrese usuario o E-mail",font=("Arial", 15))#es una etiqueta
etiqueta2.configure(bg="#3f88c5")
etiqueta2.place(x=450,y=150) 

Texto = tkinter.Entry(ventana)
Texto.place(x=450,y=200, width=250, height=30)

etiqueta3 = tkinter.Label(ventana, text= "Ingrese contraseña:",font=("Arial", 15))#es una etiquueta
etiqueta3.configure(bg="#3f88c5")
etiqueta3.place(x=450,y=250,)

Texto = tkinter.Entry(ventana)
Texto.place(x=450,y=300,width=250, height=30)

boton1 =tkinter.Button(ventana, text="Iniciar sesion",font=("Arial", 20))  # es una boton 
boton1.place(x=450,y=350,width=250, height=30) 

etiqueta = tkinter.Label(ventana, text= "¿Olvido su  contraseña o Usuario?",font=("Arial", 10))
etiqueta.configure(bg="#3f88c5")
etiqueta.place(x=450,y=420)

boton2 = tkinter.Button(ventana, text="Crear cuenta de usuario",font=("Arial", 15))   
boton2.place(x=450,y=450)

ventana.iconbitmap("fondoL.ico") #es el icono 


ventana.mainloop() #sirve para el registro del programa


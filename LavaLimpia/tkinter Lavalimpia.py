import tkinter #sirve para importar tkinter

imagenes=[]

ventana = tkinter.Tk()  #sirve para crear una ventana
ventana.geometry("950x550")#es para el tamaño de la ventana
ventana.title("Lavalimpia") #Es para el titulo
ventana.configure(bg="#188999")
ventana.resizable(False,False)

etiqueta1 = tkinter.Label(ventana, text="Inicio de sesión", font=("Britannic Bold", 20))  #es una etiqueta y el tamaño de fuente
etiqueta1.configure(bg="#188999")
etiqueta1.place(x=380, y=165) 

foto_logo1= tkinter.PhotoImage(file="logoLavaLimpia.png")
logo=tkinter.Label(ventana, image=foto_logo1,bd=0)
logo.place(x=0,y =0)
logo.lower()


foto_logo2= tkinter.PhotoImage(file="Logo2.png")
logo2=tkinter.Label(ventana,image=foto_logo2,bd=0)
logo2.place(x=65,y=280)
logo2.lower()

etiqueta2 = tkinter.Label(ventana, text= "Ingrese usuario o E-mail",font=("Arial", 15))#es una etiqueta
etiqueta2.configure(bg="#188999")
etiqueta2.place(x=380,y=220) 
etiqueta2.lower()

TextoIngreso = tkinter.Entry(ventana)
TextoIngreso.place(x=380,y=245, width=250, height=30)

etiqueta3 = tkinter.Label(ventana, text= "Ingrese contraseña:",font=("Arial", 15))#es una etiqueta
etiqueta3.configure(bg="#188999")
etiqueta3.place(x=380,y=275)

Texto = tkinter.Entry(ventana,show="*")
Texto.place(x=380,y=300,width=250, height=30)

boton1 =tkinter.Button(ventana, text="Iniciar sesion",font=("Arial", 20))  # es un boton 
boton1.place(x=380,y=350,width=250, height=30) 

def recuperacion():
    ventana.destroy()
    ventaRecu=tkinter.Tk()
    ventaRecu.geometry("950x550")#es para el tamaño de la ventana
    ventaRecu.title("Lavalimpia-Recuperacion contraseña") #Es para el titulo
    ventaRecu.configure(bg="#188999")
    ventaRecu.resizable(False,False)

    foto_logo1= tkinter.PhotoImage(file="logoLavaLimpia.png")
    imagenes.append(foto_logo1)
    logo=tkinter.Label(ventaRecu, image=foto_logo1,bd=0)
    logo.place(x=0,y =0)
    logo.lower()

    foto_logo2= tkinter.PhotoImage(file="Logo2.png")
    imagenes.append(foto_logo2)
    logo2=tkinter.Label(ventaRecu,image=foto_logo2,bd=0)
    logo2.place(x=65,y=280)
    logo2.lower()


    etiqRecu = tkinter.Label(ventaRecu, text= "Ingrese su usuario o su E-mail:",font=("Arial", 12))#es una etiqueta
    etiqRecu.configure(bg="#188999")
    etiqRecu.place(x=280,y=165) 

    textRecu = tkinter.Entry(ventaRecu)
    textRecu.place(x=280,y=190, width=250, height=30)

    def envioCo():
        ventaRecu.destroy()
        ventaRecu2=tkinter.Tk()  
        ventaRecu2.geometry("950x550")#es para el tamaño de la ventana
        ventaRecu2.title("Lavalimpia-Recuperacion contraseña") #Es para el titulo
        ventaRecu2.configure(bg="#188999")
        ventaRecu2.resizable(False,False)
        
        foto_logo1= tkinter.PhotoImage(file="logoLavaLimpia.png")
        imagenes.append(foto_logo1)
        logo=tkinter.Label(ventaRecu2, image=foto_logo1,bd=0)
        logo.place(x=0,y =0)
        logo.lower()

        foto_logo2= tkinter.PhotoImage(file="Logo2.png")
        imagenes.append(foto_logo2)
        logo2=tkinter.Label(ventaRecu2,image=foto_logo2,bd=0)
        logo2.place(x=65,y=280)
        logo2.lower()

        
        etiqRecu2 = tkinter.Label(ventaRecu2, text= "Ingrese el código:",font=("Arial", 12))#es una etiqueta
        etiqRecu2.configure(bg="#188999")
        etiqRecu2.place(x=280,y=165) 

        textRecu2 = tkinter.Entry(ventaRecu2)
        textRecu2.place(x=280,y=190, width=250, height=30)
    
        def nuevaC():
                ventaRecu2.destroy()
                ventaRecu3=tkinter.Tk()  
                ventaRecu3.geometry("950x550")#es para el tamaño de la ventana
                ventaRecu3.title("Lavalimpia-Recuperacion contraseña") #Es para el titulo
                ventaRecu3.configure(bg="#188999")
                ventaRecu3.resizable(False,False)

                foto_logo1= tkinter.PhotoImage(file="logoLavaLimpia.png")
                imagenes.append(foto_logo1)
                logo=tkinter.Label(ventaRecu3, image=foto_logo1,bd=0)
                logo.place(x=0,y =0)
                logo.lower()

                foto_logo2= tkinter.PhotoImage(file="Logo2.png")
                imagenes.append(foto_logo2)
                logo2=tkinter.Label(ventaRecu3,image=foto_logo2,bd=0)
                logo2.place(x=65,y=280)
                logo2.lower()


                etiqRecu3_1 = tkinter.Label(ventaRecu3, text= "Ingrese el código:",font=("Arial", 12))#es una etiqueta
                etiqRecu3_1.configure(bg="#188999")
                etiqRecu3_1.place(x=280,y=165) 

                textRecu3_1 = tkinter.Entry(ventaRecu3)
                textRecu3_1.place(x=280,y=190, width=250, height=30)

                etiqRecu3_2 = tkinter.Label(ventaRecu3, text= "Ingrese el código:",font=("Arial", 12))#es una etiqueta
                etiqRecu3_2.configure(bg="#188999")
                etiqRecu3_2.place(x=280,y=225) 

                textRecu3_2 = tkinter.Entry(ventaRecu3)
                textRecu3_2.place(x=280,y=250, width=250, height=30)
    
                botonRecu3 =tkinter.Button(ventaRecu3, text="Cambiar contraseña",font=("Arial", 18))  # es un boton 
                botonRecu3.place(x=545,y=250,width=250, height=30)
    
        botonRecu2 =tkinter.Button(ventaRecu2, text="Enviar código ",font=("Arial", 20),command=nuevaC)  # es un boton 
        botonRecu2.place(x=545,y=190,width=250, height=30)
     

    botonRecu =tkinter.Button(ventaRecu, text="Enviar código ",font=("Arial", 20),command=envioCo)  # es un boton 
    botonRecu.place(x=545,y=190,width=250, height=30) 
    ventaRecu.mainloop()

OlvidoContraseña = tkinter.Button(ventana, text= "¿Olvido su  contraseña?",font=("Arial", 10),bd=0,cursor="hand2",command=recuperacion)
OlvidoContraseña.configure(bg="#188999")
OlvidoContraseña.place(x=380,y=420)

def registro():
    ventana.destroy()
    ventRegistro=tkinter.Tk()
    ventRegistro.geometry("950x550")#es para el tamaño de la ventana
    ventRegistro.title("Lavalimpia-Registro") #Es para el titulo
    ventRegistro.configure(bg="#188999")
    ventRegistro.resizable(False,False)
    
    foto_logo1= tkinter.PhotoImage(file="logoLavaLimpia.png")
    logo=tkinter.Label(ventRegistro, image=foto_logo1,bd=0)
    logo.place(x=0,y =0)
    logo.lower()
    
    foto_logo2= tkinter.PhotoImage(file="Logo2.png")
    logo2=tkinter.Label(ventRegistro,image=foto_logo2,bd=0)
    logo2.place(x=65,y=280)
    logo2.lower()

    
    etiq1 = tkinter.Label(ventRegistro, text= "Nuevo nombre de usuario: ",font=("Arial", 12))#es una etiqueta
    etiq1.configure(bg="#188999")
    etiq1.place(x=380,y=165) 

    Text = tkinter.Entry(ventRegistro)
    Text.place(x=380,y=190, width=250, height=30)

    etiq2 = tkinter.Label(ventRegistro, text= "Ingrese E-mail: ",font=("Arial", 12))#es una etiqueta
    etiq2.configure(bg="#188999")
    etiq2.place(x=380,y=220)

    Text2 = tkinter.Entry(ventRegistro)
    Text2.place(x=380,y=245, width=250, height=30)

    etiq3 = tkinter.Label(ventRegistro, text= "Ingrese contraseña: ",font=("Arial", 12))#es una etiqueta
    etiq3.configure(bg="#188999")
    etiq3.place(x=380,y=275)

    Text3 = tkinter.Entry(ventRegistro,show="*")
    Text3.place(x=380,y=300, width=250, height=30)

    etiq4 = tkinter.Label(ventRegistro, text= "Confirme su contraseña: ",font=("Arial", 12))#es una etiqueta
    etiq4.configure(bg="#188999")
    etiq4.place(x=380,y=330)

    Text4 = tkinter.Entry(ventRegistro,show="*")
    Text4.place(x=380,y=355, width=250, height=30)

    registro =tkinter.Button(ventRegistro, text="Crear cuenta",font=("Arial", 20))  # es un boton 
    registro.place(x=380,y=410,width=250, height=30) 

    ventRegistro.mainloop()

boton2 = tkinter.Button(ventana, text="Crear cuenta de usuario",font=("Arial", 15),cursor="hand2",command=registro)   
boton2.place(x=380,y=450)

ventana.iconbitmap("fondoL.ico") #es el icono 

ventana.mainloop() #sirve para el registro del programa


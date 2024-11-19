import tkinter #sirve para importar tkinter para poder  crear interfaces gráficas 
from tkinter import messagebox
imagenes=[] #aquí se almacenan las imagenes de fondo

ventana = None
ventaRecu = None
ventaRecu2 = None
ventaRecu3 = None

def guardarDatos(usuario, correo, contrasena, confirmar_contrasena):
    if not usuario or not correo or not contrasena or not confirmar_contrasena: 
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.") 
        return 
    if contrasena != contrasena: 
        messagebox.showerror("Error", "Las contraseñas no coinciden.") 
    messagebox.showinfo("Éxito", "Datos registrados correctamente.") # Aquí puedes llamar a otra función o realizar otra acción  


def ventanaPrincipal():
    global ventana
    ventana = tkinter.Tk()  # Aqui se crea la ventana principal
    ventana.geometry("950x550")#es para el tamaño de la ventana
    ventana.title("Lavalimpia-Inicio de sesión") #Es para el titulo de la ventana
    ventana.configure(bg="#188999") #Color del fondo de la ventana
    ventana.resizable(False,False) # se desactiva el cambio de tamaño de la ventana

    etiqueta1 = tkinter.Label(ventana, text="Inicio de sesión", font=("Britannic Bold", 20))  #es una etiqueta de inisio de sesión  y el tamaño de fuente
    etiqueta1.configure(bg="#188999")
    etiqueta1.place(x=380, y=165) # ubica la etiqueta en la ventana

    foto_logo1= tkinter.PhotoImage(file="logoLavaLimpia.png") #importa la imagen desde la carpeta 
    imagenes.append(foto_logo1)
    logo=tkinter.Label(ventana, image=foto_logo1,bd=0) # aqui se pone la imagen en la ventana y el bd le quita el borde a la imagen 
    logo.place(x=0,y =0)

    foto_logo2= tkinter.PhotoImage(file="Logo2.png")
    imagenes.append(foto_logo2)
    logo2=tkinter.Label(ventana,image=foto_logo2,bd=0)
    logo2.place(x=65,y=280)

    etiqueta2 = tkinter.Label(ventana, text= "Ingrese usuario o E-mail",font=("Arial", 15))#es una etiqueta
    etiqueta2.configure(bg="#188999")
    etiqueta2.place(x=380,y=220) 

    TextoIngreso = tkinter.Entry(ventana) # campo donde se ingresa el usuario o gmail
    TextoIngreso.place(x=380,y=245, width=250, height=30)

    etiqueta3 = tkinter.Label(ventana, text= "Ingrese contraseña:",font=("Arial", 15))#es una etiqueta
    etiqueta3.configure(bg="#188999")
    etiqueta3.place(x=380,y=275)

    Texto = tkinter.Entry(ventana,show="*") #campo donde se pone la contraseña, el show reemplaza pero no cambia la letra, mostrando los * 
    Texto.place(x=380,y=300,width=250, height=30)

    boton1 =tkinter.Button(ventana, text="Iniciar sesión",font=("Arial", 20))  # es un boton, donde se inicia sesión 
    boton1.place(x=380,y=350,width=250, height=30) 

    OlvidoContraseña = tkinter.Button(ventana, text= "¿Olvidó su contraseña?",font=("Arial", 10),bd=0,cursor="hand2",command=recuperacion) #boton que llama a la función con la variable command   
    OlvidoContraseña.configure(bg="#188999")
    OlvidoContraseña.place(x=380,y=420)

    boton2 = tkinter.Button(ventana, text="Crear cuenta de usuario",font=("Arial", 15),cursor="hand2",command=registro) #boton que llama a la funcion registro, con la variable command  
    boton2.place(x=380,y=450)

    ventana.iconbitmap("fondoL.ico") #es el icono 

    ventana.mainloop() #sirve para el registro del programa

def recuperacion():
    global ventana, ventaRecu
    if ventana:
        ventana.destroy()  # Destruye la ventana principal 
    ventaRecu=tkinter.Tk() #se abre otra ventana 
    ventaRecu.geometry("950x550")#es para el tamaño de la ventana
    ventaRecu.title("Lavalimpia-Recuperación contraseña") #Es para el titulo
    ventaRecu.configure(bg="#188999")
    ventaRecu.resizable(False,False)

    foto_logo1= tkinter.PhotoImage(file="logoLavaLimpia.png")
    imagenes.append(foto_logo1)
    logo=tkinter.Label(ventaRecu, image=foto_logo1,bd=0)
    logo.place(x=0,y =0)
    

    foto_logo2= tkinter.PhotoImage(file="Logo2.png")
    imagenes.append(foto_logo2)
    logo2=tkinter.Label(ventaRecu,image=foto_logo2,bd=0)
    logo2.place(x=65,y=280)

    etiqRecu = tkinter.Label(ventaRecu, text= "Ingrese su usuario o su E-mail:",font=("Arial", 12))
    etiqRecu.configure(bg="#188999")
    etiqRecu.place(x=280,y=165) 

    textRecu = tkinter.Entry(ventaRecu)
    textRecu.place(x=280,y=190, width=250, height=30)

    botonRecu =tkinter.Button(ventaRecu, text="Enviar código ",font=("Arial", 20),command=envioCo)  # es un boton 
    botonRecu.place(x=545,y=190,width=250, height=30) 
    ventaRecu.iconbitmap("fondoL.ico")
    ventaRecu.mainloop()

def envioCo():
    global ventaRecu, ventaRecu2
    if ventaRecu:
        ventaRecu.destroy()     
        ventaRecu2=tkinter.Tk()  
        ventaRecu2.geometry("950x550")
        ventaRecu2.title("Lavalimpia-Recuperacion contraseña") 
        ventaRecu2.configure(bg="#188999")
        ventaRecu2.resizable(False,False)
        
        foto_logo1= tkinter.PhotoImage(file="logoLavaLimpia.png")
        imagenes.append(foto_logo1)
        logo=tkinter.Label(ventaRecu2, image=foto_logo1,bd=0)
        logo.place(x=0,y =0)
        
        foto_logo2= tkinter.PhotoImage(file="Logo2.png")
        imagenes.append(foto_logo2)
        logo2=tkinter.Label(ventaRecu2,image=foto_logo2,bd=0)
        logo2.place(x=65,y=280)
                
        etiqRecu2 = tkinter.Label(ventaRecu2, text= "Ingrese el código:",font=("Arial", 12))
        etiqRecu2.configure(bg="#188999")
        etiqRecu2.place(x=280,y=165) 

        textRecu2 = tkinter.Entry(ventaRecu2)
        textRecu2.place(x=280,y=190, width=250, height=30)
        
        botonRecu2 =tkinter.Button(ventaRecu2, text="Ingresar código",font=("Arial", 20),command=nuevaC)
        botonRecu2.place(x=545,y=190,width=250, height=30)
        
        ventaRecu2.iconbitmap("fondoL.ico")
        ventaRecu2.mainloop()

def nuevaC():
    global ventaRecu2, ventaRecu3
    if ventaRecu2:
        ventaRecu2.destroy()      
    ventaRecu3=tkinter.Tk()  
    ventaRecu3.geometry("950x550")
    ventaRecu3.title("Lavalimpia-Recuperación contraseña") 
    ventaRecu3.configure(bg="#188999")
    ventaRecu3.resizable(False,False)

    foto_logo1= tkinter.PhotoImage(file="logoLavaLimpia.png")
    imagenes.append(foto_logo1)
    logo=tkinter.Label(ventaRecu3, image=foto_logo1,bd=0)
    logo.place(x=0,y =0)
                
    foto_logo2= tkinter.PhotoImage(file="Logo2.png")
    imagenes.append(foto_logo2)
    logo2=tkinter.Label(ventaRecu3,image=foto_logo2,bd=0)
    logo2.place(x=65,y=280)
                
    etiqRecu3_1 = tkinter.Label(ventaRecu3, text= "Ingrese su nueva contraseña:",font=("Arial", 12))
    etiqRecu3_1.configure(bg="#188999")
    etiqRecu3_1.place(x=280,y=165) 

    textRecu3_1 = tkinter.Entry(ventaRecu3)
    textRecu3_1.place(x=280,y=190, width=250, height=30)

    etiqRecu3_2 = tkinter.Label(ventaRecu3, text= "Confirme su nueva contraseña:",font=("Arial", 12))
    etiqRecu3_2.configure(bg="#188999")
    etiqRecu3_2.place(x=280,y=225) 

    textRecu3_2 = tkinter.Entry(ventaRecu3)
    textRecu3_2.place(x=280,y=250, width=250, height=30)
    
    botonRecu3 =tkinter.Button(ventaRecu3, text="Cambiar contraseña",font=("Arial", 18))  
    botonRecu3.place(x=545,y=250,width=250, height=30)
    
    ventaRecu3.iconbitmap("fondoL.ico")
    ventaRecu3.mainloop()

def registro():
    global ventana
    ventana.destroy()
    ventRegistro=tkinter.Tk()
    ventRegistro.geometry("950x550")#es para el tamaño de la ventana
    ventRegistro.title("Lavalimpia-Registro") #Es para el titulo
    ventRegistro.configure(bg="#188999")
    ventRegistro.resizable(False,False)
    
    foto_logo1= tkinter.PhotoImage(file="logoLavaLimpia.png")
    imagenes.append(foto_logo1)
    logo=tkinter.Label(ventRegistro, image=foto_logo1,bd=0)
    logo.place(x=0,y =0)
    
    
    foto_logo2= tkinter.PhotoImage(file="Logo2.png")
    imagenes.append(foto_logo2)
    logo2=tkinter.Label(ventRegistro,image=foto_logo2,bd=0)
    logo2.place(x=65,y=280)
        
    etiq1 = tkinter.Label(ventRegistro, text= "Nuevo nombre de usuario: ",font=("Arial", 12))#es una etiqueta
    etiq1.configure(bg="#188999")
    etiq1.place(x=380,y=165) 

    Text1 = tkinter.Entry(ventRegistro)
    Text1.place(x=380,y=190, width=250, height=30)

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

    registro =tkinter.Button(ventRegistro, text="Crear cuenta",font=("Arial", 20),command=lambda: guardarDatos(Text1.get(), Text2.get(), Text3.get(),Text4.get()))  # es un boton 
    
    registro.place(x=380,y=410,width=250, height=30) 

    ventRegistro.iconbitmap("fondoL.ico")
     
    ventRegistro.mainloop()

ventanaPrincipal()

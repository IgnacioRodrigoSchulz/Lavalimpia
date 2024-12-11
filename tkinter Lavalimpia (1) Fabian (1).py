import tkinter #sirve para importar tkinter para poder  crear interfaces gráficas 
from tkinter import *
from tkinter.scrolledtext import ScrolledText
imagenes=[] #aquí se almacenan las imagenes de fondo

ventana = None
ventaRecu = None
ventaRecu2 = None
ventaRecu3 = None

ventana = tkinter.Tk()  # Aqui se crea la ventana principal
ventana.geometry("950x550")#es para el tamaño de la ventana
ventana.title("Lavalimpia-Inicio de sesión") #Es para el titulo de la ventana
ventana.configure(bg="#188999") #Color del fondo de la ventana
ventana.resizable(False,False) # se desactiva el cambio de tamaño de la ventana



etiqueta1 = tkinter.Label(ventana, text="Inicio de sesión", font=("Britannic Bold", 20))  #es una etiqueta de inisio de sesión  y el tamaño de fuente
etiqueta1.configure(bg="#188999")
etiqueta1.place(x=380, y=165) # ubica la etiqueta en la ventana 

foto_logo1= tkinter.PhotoImage(file="logoLavaLimpia.png") #importa la imagen desde la carpeta 
logo=tkinter.Label(ventana, image=foto_logo1,bd=0) # aqui se pone la imagen en la ventana y el bd le quita el borde a la imagen 
logo.place(x=0,y =0)

foto_logo2= tkinter.PhotoImage(file="Logo2.png")
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

def recuperacion():
    global ventana, ventaRecu
    if ventana:
        ventana.destroy()  # Destruye la ventana principal 
    ventaRecu=tkinter.Tk() #se abre otra ventana 
    ventaRecu.geometry("950x550")#es para el tamaño de la ventana
    ventaRecu.title("Lavalimpia-Recuperación contraseña") #Es para el titulo
    ventaRecu.configure(bg="#188999")
    ventaRecu.resizable(False,False)

    foto_logo1= tkinter.PhotoImage(file="POO/newLavalimpia/logoLavaLimpia.png")
    imagenes.append(foto_logo1)
    logo=tkinter.Label(ventaRecu, image=foto_logo1,bd=0)
    logo.place(x=0,y =0)
    

    foto_logo2= tkinter.PhotoImage(file="POO/newLavalimpia/Logo2.png")
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
    ventaRecu.iconbitmap("POO/newLavalimpia/fondoL.ico")
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
        
        foto_logo1= tkinter.PhotoImage(file="POO/newLavalimpia/logoLavaLimpia.png")
        imagenes.append(foto_logo1)
        logo=tkinter.Label(ventaRecu2, image=foto_logo1,bd=0)
        logo.place(x=0,y =0)
        
        foto_logo2= tkinter.PhotoImage(file="POO/newLavalimpia/Logo2.png")
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
        
        ventaRecu2.iconbitmap("POO/newLavalimpia/fondoL.ico")
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

    foto_logo1= tkinter.PhotoImage(file="POO/newLavalimpia/logoLavaLimpia.png")
    imagenes.append(foto_logo1)
    logo=tkinter.Label(ventaRecu3, image=foto_logo1,bd=0)
    logo.place(x=0,y =0)
                
    foto_logo2= tkinter.PhotoImage(file="POO/newLavalimpia/Logo2.png")
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
    
    ventaRecu3.iconbitmap("POO/newLavalimpia/fondoL.ico")
    ventaRecu3.mainloop()

OlvidoContraseña = tkinter.Button(ventana, text= "¿Olvidó su contraseña?",font=("Arial", 10),bd=0,cursor="hand2",command=recuperacion) #boton que llama a la función con la variable command   
OlvidoContraseña.configure(bg="#188999")
OlvidoContraseña.place(x=380,y=420)

def mostrar_ter(ventRegistro):  #Función que muestra los terminos y condiciones, es una ventana emergente
    ventana_terminos= Toplevel(ventRegistro)   #Toplevel crea una ventana emergente
    ventana_terminos.title("Terminos y condiciones")  #Es el titulo de la nueva ventana
    ventana_terminos.geometry("600x400")    #Tamaño de ventana emergente
    
     
    #Texto
    terminos="""Leer los términos y condiciones cuidadosamente   

    1.Lavamos por carga de ropa o media carga de ropa. La carga, o media carga, está determinada por el volumen de la ropa y no por su peso.


    2.El servicio de lavandería es personalizado, es decir, la carga de ropa se lava de manera individual en una máquina lavadora para luego ser traspasada a una máquina secadora, no mezclados con ropa de otros clientes en ninguna parte del proceso.


    3.Se asume que todas las prendas recibidas son aptas para el lavado y secado a máquina.


    4.No se responde por pérdida de objetos de valor dejados en las prendas


    5.LavaLimpia no separa prendas de una carga para lavarlas de manera independiente, por ejemplo, ropa blanca. Si el cliente desea lavar prendas aparte por un criterio de éste, entonces el mismo cliente debe formar otra carga, o media carga, con esas prendas a la cual se le aplicará el cobro correspondiente a esa nueva carga o media carga.


    6.La entrega de las prendas se realizará en el domicilio de entrega designado. De tal forma, el prestador no asume responsabilidad alguna por cuando la entrega del producto o servicio no llegue a realizarse como consecuencia de que los datos facilitados por el usuario sean falsos, inexactos o incompletos o cuando la entrega no pueda efectuarse por causas ajenas a nuestro servicio de entregas, como lo es la ausencia del destinatario. Sin perjuicio de lo anterior, el prestador deberá adoptar las medidas exigidas a un comerciante diligente para que la entrega pueda efectuarse en el tiempo acordado, y de no ser así, lo antes posible, a satisfacción del remitente como del destinatario, por lo que no podrá imputarse responsabilidad alguna en contra del prestador.


    7.El usuario se compromete a no realizar ningún uso indebido de la presente página web, como es la introducción intencionada de virus, troyanos, gusanos o cualesquiera programas o software dañino y perjudicial para el sistema de Tu Lavandería, así como intentos de accesos no autorizados al servidor, equipos, dispositivos y bases de datos de Tu Lavandería. El incumplimiento de esta estipulación podrá llevar aparejada la declaración de infracciones penales tipificadas por la legislación vigente en la materia.


    8.El presente contrato tiene por objeto regular la relación contractual nacida entre el prestador y el usuario en el momento en que éste acepta, durante el proceso de contratación online. La relación contractual conlleva la entrega, a cambio de un precio determinado y públicamente expuesto a través del sitio web, de un producto o servicio concreto.


    9.El único método de pago del servicio es en efectivo.


    10.No nos hacemos cargo del daño causado en la ropa si ha olvidado algo en los bolsillos como esmalte de uñas, chicle o un bolígrafo.


    11.No nos hacemos responsables de los daños que pueda sufrir la ropa que no sea apta para este proceso estándar de lavado.


    12.Los clientes deben vaciar los bolsillos de sus prendas y quitar cualquier tipo de accesorio que sea independiente de las mismas.


    13.No lavamos ropa para mascotas.


    14.Haremos todo lo posible para evitar dañar su ropa. Desafortunadamente, hay limitaciones en lo que podemos hacer. No siempre es posible inspeccionar todas las prendas en busca de daños o su estado previo al recibirlas.


    15.La lavandería se compromete a proteger la información personal del cliente y a utilizarla exclusivamente para fines administrativos relacionados con la prestación del servicio. En ningún caso se compartirán estos datos con terceros sin el consentimiento del cliente

    16.Nuestra lavandería cumple con todas las normas de higiene y seguridad establecidas por las autoridades locales. Las instalaciones se mantienen limpias y se toman todas las precauciones necesarias para asegurar que las prendas se manejen en condiciones higiénicas y seguras.


    17.La lavandería no será responsable de demoras, daños o pérdidas causadas por circunstancias fuera de su control, como desastres naturales, pandemias, incendios, huelgas o cualquier otro evento de fuerza mayor


    18.Si el cliente observa cualquier daño o irregularidad en sus prendas después de recibir el servicio, puede enviar un correo en el apartado de contactos para solucionar el problema.


    """
    texto_terminos = ScrolledText(ventana_terminos,wrap=WORD,width=60, height=15, font=("Arial",12))  #el wrap=Word, hace que se ajuste el texto sin cortarlo en el widget
    texto_terminos.insert(INSERT, terminos)  #Se insertan los terminos en el widget
    texto_terminos.configure(state="disabled")  #Hace que sea solo modo lectura
    texto_terminos.place(x=10,y=10) #Ubica el widget
    


    boton_cerrar = Button(ventana_terminos,text="Cerrar", command=ventana_terminos.destroy) #Boton para cerrar la ventana emergente
    boton_cerrar.place(x=200,y=320)    #se ubica el boton

def verificacion(event,ventRegistro):      #Funcion que se llama cuando se hace click en la etiqueta
    mostrar_ter(ventRegistro)     #Llama a la función que muestra los terminos

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
    
    
    foto_logo2= tkinter.PhotoImage(file="Logo2.png")
    logo2=tkinter.Label(ventRegistro,image=foto_logo2,bd=0)
    logo2.place(x=65,y=280)
        
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
    
    
    etiq5 = tkinter.Label(ventRegistro, text="Acepto los terminos y condiciones",font=("Arial", 10), fg="Blue", cursor="hand2") #el cursor cambia al estar en la etiqueta
    etiq5.configure(bg="#188999")
    etiq5.place(x=405,y=405)
    etiq5.bind("<Button-1>", lambda event:verificacion(event,ventRegistro))  #hace que la etiqueta5 sea un "boton" y a la vez se vincule a la función verificacion
    #bind vincula un evento con una función
    
    Terminos=Checkbutton(ventRegistro,)
    Terminos.configure(bg="#188999")
    Terminos.place(x=380,y=403)

    registro =tkinter.Button(ventRegistro, text="Crear cuenta",font=("Arial", 20))  # es un boton 
    registro.place(x=380,y=440,width=250, height=30) 

    ventRegistro.iconbitmap("fondoL.ico")
     
    ventRegistro.mainloop()

boton2 = tkinter.Button(ventana, text="Crear cuenta de usuario",font=("Arial", 15),cursor="hand2",command=registro) #boton que llama a la funcion registro, con la variable command  
boton2.place(x=380,y=450)

ventana.iconbitmap("fondoL.ico") #es el icono 

ventana.mainloop() #sirve para el registro del programa

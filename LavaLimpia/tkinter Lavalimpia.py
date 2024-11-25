import tkinter as tk #sirve para importar tkinter para poder  crear interfaces gráficas 
from tkinter import messagebox
imagenes=[] 

ventana = None
ventaRecu = None
ventaRecu2 = None
ventRegistro= None
ventana_usuario=None

# Función para configurar la ventana principal
def configurar_ventana(ventana, titulo, ancho=950, alto=550, color_fondo="#188999", icono=None, redimensionable=(False, False)):
    ventana.geometry(f"{ancho}x{alto}")
    ventana.title(titulo)
    ventana.configure(bg=color_fondo)
    ventana.resizable(*redimensionable)
    if icono:
        ventana.iconbitmap(icono)
     
# Función para agregar logos
def agregar_logo(ventana, archivo, x, y):
    imagen = tk.PhotoImage(file=archivo)
    logo = tk.Label(ventana, image=imagen, bd=0)
    logo.image = imagen  # Necesario para mantener la referencia a la imagen
    logo.place(x=x, y=y)

# Función para crear etiquetas
def crear_etiqueta(ventana, texto, fuente, tamano, x, y, **kwargs):
    etiqueta = tk.Label(ventana, text=texto, font=(fuente, tamano), **kwargs)
    width = kwargs.get('width', None)
    height = kwargs.get('height', None)
    
    if width and height:
        etiqueta.place(x=x, y=y, width=width, height=height)
    else:
        etiqueta.place(x=x, y=y)
    

def crear_entry(ventana,x,y,width,height,mostrar=None):
    entrada=tk.Entry(ventana,show=mostrar) if mostrar else tk.Entry(ventana)
    entrada.place(x=x,y=y,width=width,height=height)
    return entrada

def crear_boton(ventana, text, font, x, y, command=None, **kwargs):
    boton = tk.Button(ventana, text=text, font=font, command=command, **kwargs)
    width = kwargs.get('width', None)
    height = kwargs.get('height', None)
    
    if width and height:
        boton.place(x=x, y=y, width=width, height=height)
    else:
        boton.place(x=x, y=y)
        
    return boton
       
def guardarDatos(usuario, correo, contrasena, confirmar_contrasena):
    if not usuario or not correo or not contrasena or not confirmar_contrasena: 
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.") 
        return 
    if contrasena != confirmar_contrasena: 
        messagebox.showerror("Error", "Las contraseñas no coinciden.") 
    messagebox.showinfo("Éxito", "Datos registrados correctamente.")
    
    ventRegistro.destroy()
    ventanaPrincipal()
    
def inicio_de_sesion():
    ventana_usuario = tk.Tk()
    configurar_ventana(ventana_usuario,titulo="Lavalimpia-Usuario",ancho=950, alto=550, color_fondo="#188999", icono=None, redimensionable=(False, False))
    
    etiqueta01=crear_etiqueta(ventana_usuario,texto="Información de pedido",fuente="Britannic Bold",tamano=28,x=40,y=30,bg="#188999")
    
    agregar_logo(ventana_usuario, "Logo2.png", x=65, y=280)
    
    boton_salir=crear_boton(ventana_usuario,text="Cerrar sesión",font=("Arial", 10),x=840,y=8,command=lambda:cambiarVentana(ventana_usuario,ventanaPrincipal),width=100, height=25,bg="#e31414",fg="#ffffff",cursor="hand2") 

    etiqueta02 =crear_etiqueta(ventana_usuario,texto="Mis pedidos",fuente="Arial",tamano=18,x=420,y=180,width=250, height=30,bg="#ffffff")
 
    etiqueta03=crear_etiqueta(ventana_usuario,texto="N° de ticket",fuente="Arial",tamano=12,x=420,y=220,bg="#188999") 

    Texto_nro_ticket=crear_entry(ventana_usuario,x=420,y=245,width=250, height=30)
    
    etiqueta04=crear_etiqueta(ventana_usuario,texto="N° de ticket",fuente="Arial",tamano=12,x=420,y=280,bg="#188999")
 
    Texto_nro_ticket=crear_entry(ventana_usuario,x=420,y=310, width=250, height=30)
   
    boton_info=crear_boton(ventana_usuario,text="Información del pedido",font=("Arial", 20),x=400,y=370,width=300, height=40,bg="#2a3ab6",fg="#ffffff")
 
    ventana_usuario.mainloop()
    
def cambiarVentana(actual,nuevaVentana):
    if actual:
        actual.destroy()
    nuevaVentana()

def ventanaPrincipal():
    global ventana
    ventana = tk.Tk()
    configurar_ventana(ventana,titulo="Lavalimpia-Inicio de sesión",ancho=950, alto=550,color_fondo="#188999",icono="fondoL.ico",redimensionable=(False, False))

    agregar_logo(ventana, "logoLavaLimpia.png", x=0, y=0)
    agregar_logo(ventana, "Logo2.png", x=65, y=280)

    crear_etiqueta(ventana, "Inicio de sesión", "Britannic Bold", 20, x=380, y=165,bg="#188999")
    crear_etiqueta(ventana, "Ingrese usuario o e-mail", "Arial", 15, x=380, y=220,bg="#188999")
    crear_etiqueta(ventana, "Ingrese contraseña:", "Arial", 15, x=380, y=275,bg="#188999")

    texto_ingreso =crear_entry(ventana,x=380, y=245, width=250, height=30)
    texto_contrasena =crear_entry(ventana,x=380, y=300, width=250, height=30,mostrar="*")

    boton1=crear_boton(ventana,text="Iniciar sesión",font=("Arial", 20),x=380, y=350, width=250, height=30,command=lambda: validar_credenciales(texto_ingreso.get(), texto_contrasena.get()))

    boton_olvido=crear_boton(ventana,text="¿Olvidó su contraseña?", font=("Arial", 10),x=380, y=420,command=lambda: cambiarVentana(ventana,envioCo),bd=0, cursor="hand2",bg="#188999")

    boton_registro =crear_boton(ventana,text="Crear cuenta de usuario",font=("Arial", 15),x=380, y=450,command=registro,cursor="hand2")

    ventana.mainloop()

def validar_credenciales(usuario, contrasena):
    if not usuario or not contrasena:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
        return
    if usuario == "Pancracio" and contrasena == "1234":  # Ejemplo de validación
        messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
        cambiarVentana(ventana,inicio_de_sesion)
    else:
        messagebox.showerror("Error", "Credenciales incorrectas. Intente nuevamente.")


def envioCo():
    global ventaRecu
    ventaRecu = tk.Tk()
    configurar_ventana(ventaRecu, titulo="Lavalimpia-Recuperacion contraseña", ancho=950, alto=550, color_fondo="#188999", icono="fondoL.ico", redimensionable=(False, False))  
   
    agregar_logo(ventaRecu,archivo="logoLavaLimpia.png",x=0,y =0)   
    agregar_logo(ventaRecu,archivo="Logo2.png",x=65,y=165)      
    
    etiqueta1=crear_etiqueta(ventaRecu,texto="Ingrese el código",fuente="Arial",tamano=12,x=280,y=165,bg="#188999")          

    Entry1=crear_entry(ventaRecu,x=280,y=190, width=250, height=30)

    boton1=crear_boton(ventaRecu,text="Ingresar código",font=("Arial",20),x=545,y=190,command=lambda:cambiarVentana(ventaRecu,nuevaC),width=250, height=30)    
            
    ventaRecu.iconbitmap("fondoL.ico")
    ventaRecu.mainloop()

def nuevaC():
    global ventaRecu2
    ventaRecu2=tk.Tk()  
    configurar_ventana(ventaRecu2,titulo="Lavalimpia-Recuperación contraseña",ancho=950, alto=550, color_fondo="#188999", icono="fondoL.ico", redimensionable=(False, False))     

    agregar_logo(ventaRecu2,archivo="logoLavaLimpia.png",x=0,y =0)   
    agregar_logo(ventaRecu2,archivo="Logo2.png",x=65,y=165)
    
    etiqueta1=crear_etiqueta(ventaRecu2,texto="Ingrese su nueva contraseña:",fuente="Arial",tamano=12,x=280,y=165,bg="#188999")            
 
    entry1=crear_entry(ventaRecu2,x=280,y=190, width=250, height=30)

    etiqueta2=crear_etiqueta(ventaRecu2,texto="Confirme su nueva contraseña: ",fuente="Arial",tamano=12,x=280,y=225,bg="#188999")
    etiqRecu3_2 = tk.Label(ventaRecu2, text= "Confirme su nueva contraseña:",font=("Arial", 12))

    entry2=crear_entry(ventaRecu2,x=280,y=250, width=250, height=30)
    
    boton=crear_boton(ventaRecu2,text="Cambiar contraseña",font=("Arial",18),x=545,y=250,width=250, height=30) 
        
    ventaRecu2.iconbitmap("fondoL.ico")
    ventaRecu2.mainloop()


def registro():
    global ventana,ventRegistro
    ventana.destroy()
    ventRegistro=tk.Tk()
    configurar_ventana(ventRegistro,titulo="Lavalimpia-Inicio de sesión",ancho=950, alto=550,color_fondo="#188999",icono="fondoL.ico",redimensionable=(False, False))
        
    agregar_logo(ventRegistro, "logoLavaLimpia.png", x=0, y=0)
    agregar_logo(ventRegistro, "Logo2.png", x=65, y=280)
    
    crear_etiqueta(ventRegistro,texto="Nuevo nombre de usuario: ",fuente="Arial", tamano=12,x=380,y=165,bg="#188999")
    crear_etiqueta(ventRegistro,texto="Ingrese e-mail:",fuente="Arial", tamano=12,x=380,y=220,bg="#188999")
    crear_etiqueta(ventRegistro,texto="Ingrese contraseña:",fuente="Arial", tamano=12,x=380,y=275,bg="#188999")
    crear_etiqueta(ventRegistro,texto="Confirme su contraseña:",fuente="Arial", tamano=12,x=380,y=330,bg="#188999")
    
    Text1=crear_entry(ventRegistro,x=380,y=190, width=250, height=30)
    Text2=crear_entry(ventRegistro,x=380,y=245, width=250, height=30)
    Text3=crear_entry(ventRegistro,x=380,y=300, width=250, height=30,mostrar="*")
    Text4=crear_entry(ventRegistro,x=380,y=355, width=250, height=30,mostrar="*")
 
    registro_boton = crear_boton(ventRegistro,text="Crear cuenta",font=("Arial", 20),x=380,y=410,width=250, height=30,command=lambda: guardarDatos(Text1.get(), Text2.get(), Text3.get(),Text4.get()))
  
    ventRegistro.iconbitmap("fondoL.ico")
     
    ventRegistro.mainloop()

ventanaPrincipal()

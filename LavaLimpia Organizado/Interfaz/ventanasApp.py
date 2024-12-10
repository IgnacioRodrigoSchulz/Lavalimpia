from creacionVent import creacion_ventana 
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import funciones
 
 
     
class ventanaPrincipal(creacion_ventana): #esta clase es la tiene una herencia con cracion_ventana.
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Inicio de sesión", icono="recursosImagenes/fondoL.ico") #con super.() se puede acceder a los métodos de la clase padre desde una subclase (ventanaPrincipal)
        self.interfaz() 
        
    def VentEmergente(self):
        self.crear_ventana_emergente("hola","Como estan muchachos")
    
    def interfaz(self): #método donde se construye la interfaz o elementos gráficos de la ventana 
        self.agregar_logo("recursosImagenes/logoLavaLimpia.png",x=0,y=0)
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        
        self.crear_etiqueta("Inicio de sesión", "Britannic Bold", 20, x=380, y=165,bg="#188999")
        self.crear_etiqueta("Ingrese usuario o e-mail", "Arial", 15, x=380, y=220,bg="#188999")
        self.crear_etiqueta("Ingrese contraseña:", "Arial", 15, x=380, y=275,bg="#188999")
        
        texto_ingreso =self.crear_entry(x=380, y=245, width=250, height=30) #texto ingreso usuario/e-mail
        texto_contrasena =self.crear_entry(x=380, y=300, width=250, height=30,mostrar="*") #texto ingreso contraseña
        
        boton1=self.crear_boton(text="Iniciar sesión",font=("Arial", 20),x=380, y=350, width=250, height=30,command=lambda: self.validar_credenciales(texto_ingreso.get(), texto_contrasena.get())) #boton de iniciar sesión dónde se llama a un método donde se validan los datos ingresados.
        boton_olvido=self.crear_boton(text="¿Olvidó su contraseña?", font=("Arial", 10),x=380, y=420,command=lambda: self.cambiarVentana(VentanaIngreseEmail),bd=0, cursor="hand2",bg="#188999")
        boton_registro =self.crear_boton(text="Crear cuenta de usuario",font=("Arial", 15),x=380, y=450,command=lambda:self.cambiarVentana(ventanaRegistro),cursor="hand2") #boton que sirve para ir a la ventanad de registro
        
    def validar_credenciales(self, identificador, contrasena):
        if not identificador or not contrasena:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

            # Diccionario con credenciales. Cada entrada tiene correo y usuario como posibles identificadores.
        credenciales = {
            "gerente": {"correo": "gerente@lavalimpia.com", "contrasena": "admin123", "ventana": ventana_gerente},
            "Pancracio": {"correo": "pancracio@gmail.com", "contrasena": "1234", "ventana": ventana_usuario},
            "operador": {"correo": "operador@lavalimpia.com", "contrasena": "operador123", "ventana": ventana_operador},
            "recaudador": {"correo": "recaudador@lavalimpia.com", "contrasena": "recaudador123", "ventana": ventana_EmpleadoRecaudador}
            }

            # Verificar si el identificador coincide con un usuario o correo
        for usuario, datos in credenciales.items(): #.items sirve para recorrer el diccionario y así poder acceder a los datos
            if identificador == usuario or identificador == datos["correo"]: # datos[] comprueba si es correspondiente a lo guardado en el diccionario
                # Si el identificador coincide, validamos la contraseña
                if datos["contrasena"] == contrasena:
                    messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
                    self.cambiarVentana(datos["ventana"])
                    return
                else:
                    messagebox.showerror("Error", "Contraseña incorrecta. Intente nuevamente.")
                    return
        messagebox.showerror("Error", "Usuario no encontrado. Intente nuevamente.")


            
class ventana_usuario(creacion_ventana): #ventan que se muestra  tras iniciar sesión
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Usuario", icono="recursosImagenes/fondoL.ico")
        self.interfaz()
        
    def interfaz(self):
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        self.crear_etiqueta("Información de pedido",fuente="Britannic Bold",tamano=28,x=40,y=30,bg="#188999")
        boton_salir=self.crear_boton("Cerrar sesión",font=("Arial", 10),x=840,y=8,command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25,bg="#e31414",fg="#ffffff",cursor="hand2")
    
        frame_tabla=ttk.Frame(self.ventana) #se crea un contenedor frame para posicionar la tabla
        frame_tabla.place(x=280, y=150, width=550, height=150)
        columnas = ["N° de ticket", "Nombre","Fecha", "Prenda", "Estado"]
        datos = [
            (1, "Pancracio" ,"10-12-2024","Polera", "Pendiente"),
            ]
        
        self.crear_tabla( #agrega kla tabla con los datos existentes
            parent=frame_tabla,
            columnas=columnas,
            datos=datos,
            ancho_columnas=[],
            expandir=True
        )

class ventana_gerente(creacion_ventana):
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Gerente", icono="recursosImagenes/fondoL.ico")
        self.interfaz()
    
    def interfaz(self):
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        self.crear_boton(text=" Cerrar sesión  ",font=("Arial", 10),x=840,y=8, command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25, bg= "red", fg="white")
        self.crear_boton(text="Buscador de pedidos",font=("Arial",18),x=200,y=200,bg="blue",fg="#ffffff")
        self.crear_boton(text="Datos y estadísticas",font=("Arial",18),x=500,y=200,bg="blue",fg="#ffffff")

class ventana_operador(creacion_ventana):
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Operador",icono="recursosImagenes/fondoL.ico")
        self.interfaz()
    
    def interfaz(self):
        self.crear_boton(text=" Cerrar sesión  ",font=("Arial", 10),x=840,y=8, command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25, bg= "red", fg="white")
        self.crear_etiqueta(texto="Creador de pedidos", fuente= ("Britannic Bold"),tamano=28,x=40,y=30,bg="#188999")
        self.crear_etiqueta(texto="Usuario",fuente=("Arial"),tamano=12,x=120,y=120,bg="#188999",fg="#ffffff")
        self.crear_entry(x=120,y=150, width=280, height=30)
        self.crear_etiqueta(texto= "Dirección",fuente=("Arial"),tamano=12,x=120,y=190,bg="#188999",fg="#ffffff")
        self.crear_entry(x=120,y=220, width=280, height=30)
        self.crear_etiqueta(texto= "Tarifa",fuente=("Arial"),tamano=12,x=120,y=260,bg="#188999",fg="#ffffff")
        self.crear_entry(x=120,y=290, width=280, height=30)
        self.crear_boton(text="Crear pedido",font=("Arial", 20),x=360,y=410,command=None,width=260, height=40,bg="#2a3ab6",fg="#ffffff")

class  ventana_EmpleadoRecaudador(creacion_ventana):
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Recaudador",icono="recursosImagenes/fondoL.ico")
        self.interfaz()
    
    def interfaz(self):
        self.agregar_logo("recursosImagenes/logoLavaLimpia.png",x=0,y=0)
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        self.crear_etiqueta(texto="Total a pagar:", fuente=("Arial"),tamano=22,x=380, y=165,bg="#188999",fg="White")
        self.crear_entry(x=380, y=245, width=250, height=30)
        self.crear_boton(text="Confirmar pago",font=("Arial",12),x=380, y=350,width=200, height=50)
        self.crear_boton(text=" Cerrar sesión  ",font=("Arial", 10),x=840,y=8, command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25, bg= "red", fg="white")
        
class ventanaRegistro(creacion_ventana): # ventana para registrar a los nuevos usuarios 
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Registro", icono="recursosImagenes/fondoL.ico")
        self.interfaz()
    
    def interfaz(self):
        self.agregar_logo("recursosImagenes/logoLavaLimpia.png", 0, 0)
        self.agregar_logo("recursosImagenes/Logo2.png", 65, 280)
        
        boton_salir=self.crear_boton("Volver al inicio",font=("Arial", 10),x=840,y=8,command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25,bd=0, cursor="hand2",bg="#188999")

        
        self.crear_etiqueta("Nuevo nombre de usuario:", "Arial", 12, 380, 165, bg="#188999")
        self.crear_etiqueta("Ingrese e-mail:", "Arial", 12, 380, 220, bg="#188999")
        self.crear_etiqueta("Ingrese contraseña:", "Arial", 12, 380, 275, bg="#188999")
        self.crear_etiqueta("Confirme su contraseña:", "Arial", 12, 380, 330, bg="#188999")
        
        usuario=self.crear_entry(x=380,y=190, width=250, height=30)
        correo=self.crear_entry(x=380,y=245, width=250, height=30)
        contrasena=self.crear_entry(x=380,y=300, width=250, height=30,mostrar="*")
        confirmar_contrasena=self.crear_entry(x=380,y=355, width=250, height=30,mostrar="*")
        
        boton_crear_cuenta=self.crear_boton("Crear cuenta",font=("Arial", 20),x=380,y=410,width=250, height=30,command=lambda: self.guardarDatos(usuario.get(), correo.get(), contrasena.get(),confirmar_contrasena.get())) #boton para crear la cuenta y que llama al método guardarDatos, pasando los datos ingresados como parámetros
    
    def guardarDatos(self,usuario,correo,contrasena,confirmar_contrasena): #valida los datos ingresados y los guarda si son válidos
     if not usuario or not correo or not contrasena or not confirmar_contrasena:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
        return  # Termina la ejecución si hay campos vacíos

    # Validar usuario, correo y contraseña
     try: # se llama a funciones externas para validar los datos.
        usuarioValido = funciones.verificarUsuario(usuario)
        correoValido = funciones.verificarCorreo(correo)
        contrasenaValida = funciones.verificarContrasena(contrasena, confirmar_contrasena)
     except ValueError as e:  # Si las funciones lanza un error se manejan de la siguiente forma
        messagebox.showerror("Error de Validación", str(e))
        return

    # Proceder si todo es válido
     if usuarioValido and correoValido and contrasenaValida:
        messagebox.showinfo("Éxito", "Datos registrados correctamente.")
        self.cambiarVentana(ventanaPrincipal)

class VentanaIngreseEmail(creacion_ventana):
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Recuperación contraseña", icono="recursosImagenes/fondoL.ico")
        self.crear_interfaz()

    def crear_interfaz(self):
        boton_salir=self.crear_boton("Volver al inicio",font=("Arial", 10),x=840,y=8,command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25,bd=0, cursor="hand2",bg="#188999")

        self.agregar_logo("recursosImagenes/logoLavaLimpia.png", 0, 0)
        self.agregar_logo("recursosImagenes/Logo2.png", 65, 280)
        self.crear_etiqueta("Ingrese su email", "Arial", 12, 280, 165, bg="#188999")
        codigo = self.crear_entry(280, 190, 250, 30)
        self.crear_boton("Siguiente", font=("Arial", 18), x=545, y=190, width=250, height=30,command=lambda: self.cambiarVentana(VentanaIngresoCodigo))
    
class VentanaIngresoCodigo(creacion_ventana):
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Recuperación contraseña", icono="recursosImagenes/fondoL.ico")
        self.crear_interfaz()

    def crear_interfaz(self):
        boton_salir=self.crear_boton("Volver al inicio",font=("Arial", 10),x=840,y=8,command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25,bd=0, cursor="hand2",bg="#188999")

        self.agregar_logo("recursosImagenes/logoLavaLimpia.png", 0, 0)
        self.agregar_logo("recursosImagenes/Logo2.png", 65, 280)
        self.crear_etiqueta("Ingrese el código", "Arial", 12, 280, 165, bg="#188999")
        codigo = self.crear_entry(280, 190, 250, 30)
        self.crear_boton("Siguiente", font=("Arial", 18), x=545, y=190, width=250, height=30,command=lambda: self.cambiarVentana(VentanaNuevaContrasena))

class VentanaNuevaContrasena(creacion_ventana):
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Cambiar contraseña", icono="recursosImagenes/fondoL.ico")
        self.crear_interfaz()

    def crear_interfaz(self):
        boton_salir=self.crear_boton("Volver al inicio",font=("Arial", 10),x=840,y=8,command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25,bd=0, cursor="hand2",bg="#188999")

        self.agregar_logo("recursosImagenes/logoLavaLimpia.png", 0, 0)
        self.agregar_logo("recursosImagenes/Logo2.png", 65, 280)
        self.crear_etiqueta("Ingrese su nueva contraseña:", "Arial", 12, 280, 165, bg="#188999")
        nueva_contrasena = self.crear_entry(280, 190, 250, 30, mostrar="*")
        self.crear_etiqueta("Confirme su nueva contraseña:", "Arial", 12, 280, 225, bg="#188999")
        confirmar_contrasena = self.crear_entry(280, 250, 250, 30, mostrar="*")
        self.crear_boton("Cambiar contraseña", font=("Arial", 18), x=545, y=250, width=250, height=30)
        
print("Hola mundo")

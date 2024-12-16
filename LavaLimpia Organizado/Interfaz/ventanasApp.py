from Interfaz.creacionVent import creacion_ventana 
import tkinter as tk
from tkinter import messagebox,ttk
from Interfaz import funciones
import json
import random,smtplib,string

      
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
        
    def validar_credenciales(self, usuario, contrasena):
        archivo="nuevos_usuarios.json"
        
        try:
            with open(archivo, "r") as file:
                usuarios=json.load(file)
        except(FileNotFoundError,json.JSONDecodeError):
            messagebox.showerror("Error","No hay ususarios registrasdos")
            return False
        
        usuarioEncontrado=False
        for user in usuarios:
            for tipoUsuario,nombreUsuario in user.items():
                if tipoUsuario in ["correo ","contrasena"]:
                    continue
                if (nombreUsuario==usuario or user["correo"]==usuario) and user["contrasena"]==contrasena:
                    usuarioEncontrado=True
                    messagebox.showinfo("Bienvenido",f"{nombreUsuario}!")
                    
                    
                    if tipoUsuario=="gerente":
                        self.cambiarVentana(ventana_gerente)
                    elif tipoUsuario=="operador":
                        self.cambiarVentana(ventana_operador)
                    elif tipoUsuario=="recaudador":
                        self.cambiarVentana(ventana_EmpleadoRecaudador)
                    elif tipoUsuario=="usuario":
                        self.cambiarVentana(ventana_usuario)
                    else:
                        messagebox.showerror("Error","Tipo de usuario desconocido")
                    return True
        if not usuarioEncontrado:
            messagebox.showerror("Error","El ususario o contraseña son incorrectos")        
        return False
            
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
        self.crear_boton(text="Buscador de pedidos",font=("Arial",18),x=150,y=200,width=300,height=50,bg="blue",fg="#ffffff")
        self.crear_boton(text="Buscador de usuarios",font=("Arial",18),x=150,y=300,width=300,height=50,bg="blue",fg="#ffffff")
        self.crear_boton(text="Datos y estadísticas",font=("Arial",18),x=500,y=200,width=300,height=50,bg="blue",fg="#ffffff")
        self.crear_boton(text="Crear pedido",font=("Arial",18),x=500,y=300,width=300,height=50,bg="blue",fg="#ffffff")

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
        self.acepto_terminos = tk.BooleanVar(value=False)
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
        
        check_frame = tk.Frame(self.ventana, bg="#188999")
        check_frame.place(x=380, y=385)

        check_btn = tk.Checkbutton(check_frame,variable=self.acepto_terminos,onvalue=True, offvalue=False,bg="#188999")
        check_btn.pack(side="left")

        terminos_label = tk.Label(
            check_frame,
            text="Aceptar los términos y condiciones",
            fg="blue",
            bg="#188999",
            font=("Arial", 10, "underline"),
            cursor="hand2"
        )
        terminos_label.pack(side="left")
        terminos_label.bind("<Button-1>", lambda e: self.mostrar_terminos())
        
        boton_crear_cuenta=self.crear_boton("Crear cuenta",font=("Arial", 20),x=380,y=410,width=250, height=30,command=lambda: self.guardarDatos(usuario.get(), correo.get(), contrasena.get(),confirmar_contrasena.get())) #boton para crear la cuenta y que llama al método guardarDatos, pasando los datos ingresados como parámetros
    
    def guardarDatos(self,usuario,correo,contrasena,confirmar_contrasena): #valida los datos ingresados y los guarda si son válidos
        if not self.acepto_terminos.get():
            messagebox.showwarning("Advertencia", "Debe aceptar los términos y condiciones para continuar")
            return
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
            nuevo_usuario={
                "usuario":usuario,
                "correo":correo,
                "contrasena":contrasena
            }
            self.guardar_json(nuevo_usuario)
            
            messagebox.showinfo("Éxito","Sus datos estan registrados en el sistema")
            self.cambiarVentana(ventanaPrincipal)
    
    def guardar_json(self,nuevo_usuario):
        archivo = "nuevos_usuarios.json"  # Archivo donde se guardan los datos
        try:
            # Leer usuarios existentes
            with open(archivo, "r") as file:
                usuarios = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            usuarios = []  # Si no existe el archivo, crear uno nuevo

        # Agregar el nuevo usuario
        usuarios.append(nuevo_usuario)

        # Guardar la lista actualizada de usuarios en el archivo
        with open(archivo, "w") as file:
            json.dump(usuarios, file, indent=4)
            
    def mostrar_terminos(self):
        """Muestra los términos y condiciones en una ventana emergente."""
        terminos = (
            "Leer los términos y condiciones cuidadosamente:\n\n"
            "1. Lavamos por carga de ropa o media carga de ropa. La carga, o media carga, está determinada por el volumen de la ropa y no por su peso.\n\n"
            "2. El servicio de lavandería es personalizado, es decir, la carga de ropa se lava de manera individual en una máquina lavadora para luego ser traspasada a una máquina secadora, no mezclados con ropa de otros clientes en ninguna parte del proceso.\n\n"
            "3. Se asume que todas las prendas recibidas son aptas para el lavado y secado a máquina.\n\n"
            "4. No se responde por pérdida de objetos de valor dejados en las prendas.\n\n"
            "5. LavaLimpia no separa prendas de una carga para lavarlas de manera independiente, por ejemplo, ropa blanca. Si el cliente desea lavar prendas aparte por un criterio de éste, entonces el mismo cliente debe formar otra carga, o media carga, con esas prendas a la cual se le aplicará el cobro correspondiente a esa nueva carga o media carga.\n\n"
            "6. La entrega de las prendas se realizará en el domicilio de entrega designado. De tal forma, el prestador no asume responsabilidad alguna por cuando la entrega del producto o servicio no llegue a realizarse como consecuencia de que los datos facilitados por el usuario sean falsos, inexactos o incompletos o cuando la entrega no pueda efectuarse por causas ajenas a nuestro servicio de entregas, como lo es la ausencia del destinatario. Sin perjuicio de lo anterior, el prestador deberá adoptar las medidas exigidas a un comerciante diligente para que la entrega pueda efectuarse en el tiempo acordado, y de no ser así, lo antes posible, a satisfacción del remitente como del destinatario, por lo que no podrá imputarse responsabilidad alguna en contra del prestador.\n\n"
            "7. El usuario se compromete a no realizar ningún uso indebido de la presente página web, como es la introducción intencionada de virus, troyanos, gusanos o cualesquiera programas o software dañino y perjudicial para el sistema de Tu Lavandería, así como intentos de accesos no autorizados al servidor, equipos, dispositivos y bases de datos de Tu Lavandería. El incumplimiento de esta estipulación podrá llevar aparejada la declaración de infracciones penales tipificadas por la legislación vigente en la materia.\n\n"
            "8.El presente contrato tiene por objeto regular la relación contractual nacida entre el prestador y el usuario en el momento en que éste acepta, durante el proceso de contratación online. La relación contractual conlleva la entrega, a cambio de un precio determinado y públicamente expuesto a través del sitio web, de un producto o servicio concreto.\n\n"
            "9.El único método de pago del servicio es en efectivo.\n\n"
            "10.No nos hacemos cargo del daño causado en la ropa si ha olvidado algo en los bolsillos como esmalte de uñas, chicle o un bolígrafo.\n\n"
            "11.No nos hacemos responsables de los daños que pueda sufrir la ropa que no sea apta para este proceso estándar de lavado.\n\n"
            "12.Los clientes deben vaciar los bolsillos de sus prendas y quitar cualquier tipo de accesorio que sea independiente de las mismas.\n\n"
            "13.No lavamos ropa para mascotas.\n\n"
            "14.Haremos todo lo posible para evitar dañar su ropa. Desafortunadamente, hay limitaciones en lo que podemos hacer. No siempre es posible inspeccionar todas las prendas en busca de daños o su estado previo al recibirlas.\n\n"
            "15.La lavandería se compromete a proteger la información personal del cliente y a utilizarla exclusivamente para fines administrativos relacionados con la prestación del servicio. En ningún caso se compartirán estos datos con terceros sin el consentimiento del cliente.\n\n"
            "16.Nuestra lavandería cumple con todas las normas de higiene y seguridad establecidas por las autoridades locales. Las instalaciones se mantienen limpias y se toman todas las precauciones necesarias para asegurar que las prendas se manejen en condiciones higiénicas y seguras.\n\n"
            "17.La lavandería no será responsable de demoras, daños o pérdidas causadas por circunstancias fuera de su control, como desastres naturales, pandemias, incendios, huelgas o cualquier otro evento de fuerza mayor.\n\n"
            "18.Si el cliente observa cualquier daño o irregularidad en sus prendas después de recibir el servicio, puede enviar un correo en el apartado de contactos para solucionar el problema.\n\n"

            "\nAl aceptar estos términos, garantizas cumplir con las normas establecidas."
        )
        self.crear_ventana_emergente(
            titulo="términos y condiciones",
            mensaje=terminos,
            ancho=600,
            alto=400,
            color_fondo="#ffffff"
                )
        
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
    """""""""    
    def generar_codigo(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    
    def enviar_correo(self):
        try:
            with open('nuevos_usuarios.json','r') as file:
                data=json.load(file)
                destinatario=data['correo']
        except Exception as e:
            messagebox.showerror("Error",f"no se pudo leer el archivo json:{e}")
            return
        
        remitente=
        try:
            with smtplib.SMTP('smtp.gmail.com',587) as server:
                server.starttls()
                server.login(remitente,contrasena)
        """""""""""""""
    
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

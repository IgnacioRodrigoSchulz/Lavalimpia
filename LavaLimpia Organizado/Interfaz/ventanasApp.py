from Interfaz.creacionVent import creacion_ventana 
import tkinter as tk
from tkinter import messagebox
from Interfaz import funciones
import json,random,string
from datetime import datetime,timedelta

#ventana inicial de inicio se sesión y creacion de cuenta
class ventanaPrincipal(creacion_ventana):
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Inicio de sesión", icono="recursosImagenes/fondoL.ico")
        self.usuario_actual = None  # Usuario autenticado
        self.interfaz()

    def interfaz(self):
        self.agregar_logo("recursosImagenes/logoLavaLimpia.png", x=0, y=0)
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)

        self.crear_etiqueta("Inicio de sesión", "Britannic Bold", 20, x=380, y=165, bg="#188999")
        self.crear_etiqueta("Ingrese usuario o e-mail", "Arial", 15, x=380, y=220, bg="#188999")
        self.crear_etiqueta("Ingrese contraseña:", "Arial", 15, x=380, y=275, bg="#188999")

        texto_ingreso = self.crear_entry(x=380, y=245, width=250, height=30)  # Usuario o email
        texto_contrasena = self.crear_entry(x=380, y=300, width=250, height=30, mostrar="*")  # Contraseña

        # Botón iniciar sesión
        self.crear_boton(
            text="Iniciar sesión",
            font=("Arial", 20),
            x=380,
            y=350,
            width=250,
            height=30,
            command=lambda: self.validar_credenciales(texto_ingreso.get().strip(), texto_contrasena.get().strip())
        )

        # Botón registro
        self.crear_boton(
            text="Crear cuenta de usuario",
            font=("Arial", 15),
            x=380,
            y=450,
            command=lambda: self.cambiarVentana(ventanaRegistro),  # Suponiendo que la ventanaRegistro está implementada
            cursor="hand2"
        )

    def validar_credenciales(self, usuario, contrasena):
        archivo_usuarios = "nuevos_usuarios.json"

        if not usuario or not contrasena:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return False

        try:
            with open(archivo_usuarios, "r") as file:
                usuarios = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo de usuarios no fue encontrado.")
            return False
        except json.JSONDecodeError:
            messagebox.showerror("Error", "El archivo de usuarios tiene un formato incorrecto.")
            return False

        for user in usuarios:
            # Comprobar si es usuario regular o un tipo especial (gerente, operador, etc.)
            tipo_usuario = next((key for key in user if key not in ["correo", "contrasena"]), None)

            if (
                (user.get(tipo_usuario) == usuario or user.get("correo") == usuario)
                and user.get("contrasena") == contrasena
            ):
                self.usuario_actual = user
                messagebox.showinfo("Bienvenido", f"¡Hola, {user[tipo_usuario]}!")
                
                if tipo_usuario == "usuario":
                    self.cambiarVentana(lambda usuario_actual: ventana_usuario(usuario_actual))
                elif tipo_usuario == "gerente":
                    self.cambiarVentana(lambda usuario_actual:ventana_gerente(usuario_actual))  # Asumiendo que esta clase está implementada
                elif tipo_usuario == "operador":
                    self.cambiarVentana(lambda usuario_actual:ventana_operador(usuario_actual))
                elif tipo_usuario == "recaudador":
                    self.cambiarVentana(lambda usuario_actual:ventana_EmpleadoRecaudador(usuario_actual))
                else:
                    messagebox.showerror("Error", "Tipo de usuario desconocido.")
                return True

        messagebox.showerror("Error", "El usuario o la contraseña son incorrectos.")
        return False

#ventana de usuario especificado en la ventana inicial
class ventana_usuario(creacion_ventana):  # Ventana para usuarios regulares
    def __init__(self, usuario):
        super().__init__(titulo="Lavalimpia-Usuario", icono="recursosImagenes/fondoL.ico")
        self.usuario = usuario  # Usuario autenticado
        self.pedidos_usuario = []
        self.interfaz()

    def interfaz(self):
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        self.crear_etiqueta(f"¡Bienvenido, {self.usuario['usuario']}!",fuente="Britannic Bold",tamano=28,x=40,y=30,bg="#188999")

        # Botón para cerrar sesión
        self.crear_boton("Cerrar sesión", font=("Arial", 10),x=840,y=8,command=lambda: self.cambiarVentana(ventanaPrincipal),width=100, height=25, bg="#e31414", fg="#ffffff", cursor="hand2")

        # Botón para cargar pedidos
        self.crear_etiqueta("Para ver tus códigos únicos asociados a tu cuenta cliquea aquí:",fuente="Arial",tamano=15,x=40,y=100,bg="#188999")
        self.boton_pedidos = self.crear_boton(text="Códigos",font=("Arial", 18),x=40,y=150,command=self.cargar_pedidos,width=100,height=25)
        
        self.crear_etiqueta("Para saber el estado de su pedido cliquea Aquí he ingrese el código único de su pedido:",fuente="Arial",tamano=15,x=40,y=200,bg="#188999")
        self.botonEstado=self.crear_boton(text="Estado",font=("Arial",18),x=40,y=250,command=self.ver_estado_pedido,width=100,height=25)
    
    def cargar_pedidos(self):
        """
        Busca y muestra los pedidos asociados al usuario actual.
        """
        archivo_pedidos = "pedidos.json"

        try:
            # Leer el archivo JSON
            with open(archivo_pedidos, 'r', encoding='utf-8') as file:
                datos = json.load(file)

            # Filtrar los pedidos del usuario actual
            self.pedidos_usuario = next((user["pedidos"] for user in datos if user.get("usuario") == self.usuario["usuario"]),[])

            if self.pedidos_usuario:
                
                    self.ventanaE_InfoCodUnico(titulo=f"Pedido del usuario",pedidos=self.pedidos_usuario,ancho=850,alto=350,color_fondo="#e6f7ff")
            else:
                messagebox.showinfo("Pedidos del usurio","No tienes pedidos registrados.")

        except FileNotFoundError:
            messagebox.showerror("Error", f"El archivo {archivo_pedidos} no fue encontrado.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "no existe código único, debe realizar un pedido")
    
    def ver_estado_pedido(self):
        """
        Abre una ventana para ingresar el código único y mostrar detalles del pedido.
        """
        ventana_estado = tk.Toplevel(self.ventana)
        ventana_estado.title("Estado del Pedido")
        ventana_estado.geometry("400x300")
        ventana_estado.transient(self.ventana)
        ventana_estado.grab_set()

        tk.Label(ventana_estado, text="Ingrese el código único del pedido:", font=("Arial", 12)).pack(pady=10)
        entry_codigo = tk.Entry(ventana_estado, font=("Arial", 12))
        entry_codigo.pack(pady=5)

        # Etiquetas para mostrar información del pedido
        label_estado = tk.Label(ventana_estado, text="Estado: ", font=("Arial", 10))
        label_estado.pack(pady=5)
        label_fecha_entrega = tk.Label(ventana_estado, text="Fecha de Entrega: ", font=("Arial", 10))
        label_fecha_entrega.pack(pady=5)
        label_direccion = tk.Label(ventana_estado, text="Dirección: ", font=("Arial", 10))
        label_direccion.pack(pady=5)
        label_tarifa = tk.Label(ventana_estado, text="Tarifa: ", font=("Arial", 10))
        label_tarifa.pack(pady=5)

        def buscar_estado():
            codigo = entry_codigo.get()
            pedido = next((p for p in self.pedidos_usuario if p.get('Código único') == codigo), None)
            if pedido:
                label_estado.config(text=f"Estado: {pedido.get('Estado', 'Desconocido')}")
                label_fecha_entrega.config(text=f"Fecha de Entrega: {pedido.get('Fecha entrega', 'Desconocida')}")
                label_direccion.config(text=f"Dirección: {pedido.get('Dirección', 'Desconocida')}")
                label_tarifa.config(text=f"Tarifa: {pedido.get('Tarifa pedido', 'Desconocida')} CLP")
            else:
                label_estado.config(text="Código no encontrado")
                label_fecha_entrega.config(text="")
                label_direccion.config(text="")
                label_tarifa.config(text="")

        tk.Button(ventana_estado, text="Buscar", command=buscar_estado).pack(pady=10)
#Terminada pero con posibles modificaciones.

#Esta es la ventana de registro, la cual sirve para cear cuentas en LavaLimpia
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
#cierre de esta ventana.

#En proceso
#Esta es la ventana del gerente.
class ventana_gerente(creacion_ventana):
    def __init__(self,usuario_actual):
        super().__init__(titulo="Lavalimpia-Gerente", icono="recursosImagenes/fondoL.ico")
        self.interfaz()
        self.usuario_actual=usuario_actual
    
    def interfaz(self):
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        self.crear_boton(text=" Cerrar sesión  ",font=("Arial", 10),x=840,y=8, command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25, bg= "red", fg="white")
        self.crear_boton(text="Buscador de pedidos",font=("Arial",18),x=150,y=200,width=300,height=50,bg="blue",fg="#ffffff")
        self.crear_boton(text="Buscador de usuarios",font=("Arial",18),x=150,y=300,width=300,height=50,bg="blue",fg="#ffffff")
        self.crear_boton(text="Datos y estadísticas",font=("Arial",18),x=500,y=200,width=300,height=50,bg="blue",fg="#ffffff")
        self.crear_boton(text="Crear pedido",font=("Arial",18),x=500,y=300,width=300,height=50,bg="blue",fg="#ffffff")
#cierre de esa ventana.

###medianamente listo
#ventana del operador #terminado medianamente Hay que corregir cosas básicas
class ventana_operador(creacion_ventana):
    def __init__(self,usuario_actual):
        super().__init__(titulo="Lavalimpia-Operador",icono="recursosImagenes/fondoL.ico")
        self.interfaz()
        self.usuario_actual = usuario_actual
    def interfaz(self):
        self.agregar_logo("recursosImagenes/logoLavaLimpia.png",x=0,y=0)
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        self.crear_boton(text=" Cerrar sesión  ",font=("Arial", 10),x=840,y=8, command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25, bg= "red", fg="white")
        
        self.crear_boton(text="Ingresar pedido",font=("Arial",20),x=150,y=250,command=lambda:self.cambiarVentana(IngresoPedido_operador),width=260, height=40)
        self.crear_boton(text="Consultar pedido",font=("Arial",20),x=450,y=250,command=lambda:self.cambiarVentana(ConsultaPedido_operador),width=260, height=40)
        
class IngresoPedido_operador(creacion_ventana):
    def __init__(self,usuario_actual):
        super().__init__(titulo="Lavalimpia-Operador (Ingreso de pedido)", icono="recursosImagenes/fondoL.ico")
        self.interfaz()
        self.usuario_actual = usuario_actual
    def interfaz(self):
        self.crear_etiqueta(texto="Creador de pedidos", fuente=("Britannic Bold"), tamano=28, x=40, y=30, bg="#188999")
        self.crear_boton("Volver",font=("Arial", 10),x=840,y=8,command=lambda:self.cambiarVentana(ventana_operador),width=100, height=25,bd=0, cursor="hand2",bg="white")
        self.crear_etiqueta(texto="Usuario", fuente=("Arial"), tamano=12, x=120, y=120, bg="#188999", fg="#ffffff")
        self.entry_usuario = self.crear_entry(x=120, y=150, width=280, height=30)
        
        self.crear_etiqueta(texto="Dirección", fuente=("Arial"), tamano=12, x=120, y=190, bg="#188999", fg="#ffffff")
        self.entry_direccion = self.crear_entry(x=120, y=220, width=280, height=30)
        
        self.crear_etiqueta(texto="Tarifa", fuente=("Arial"), tamano=12, x=120, y=260, bg="#188999", fg="#ffffff")
        self.entry_tarifa = self.crear_entry(x=120, y=290, width=280, height=30)
        
        
        self.crear_boton(
            text="Crear pedido",
            font=("Arial", 20),
            x=360, y=410,
            command=self.guardar_pedido,
            width=260, height=40
        )
        
    def guardar_pedido(self):
        # Obtener la fecha y hora actual
        fecha_actual = datetime.now()
        fecha_creacion = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
    
        # Calcular la fecha de entrega sumando 2 días
        fecha_entrega = (fecha_actual + timedelta(days=2)).strftime("%d-%m-%Y")
    
        # Obtener los datos de los campos de entrada
        usuario = self.entry_usuario.get().strip()
        direccion = self.entry_direccion.get().strip()
        tarifa = self.entry_tarifa.get().strip()

        # Validaciones
        if not usuario:
            messagebox.showwarning("Campo vacío", "El campo 'Usuario' no puede estar vacío.")
            return
        if not direccion:
            messagebox.showwarning("Campo vacío", "El campo 'Dirección' no puede estar vacío.")
            return
        if not tarifa:
            messagebox.showwarning("Campo vacío", "El campo 'Tarifa' no puede estar vacío.")
            return

        # Validar que la tarifa sea numérica
        try:
            tarifa_float = float(tarifa)
            if tarifa_float<=0:
                messagebox.showwarning("Valor inválido","La tarifa debe ser un valor numérico positivo.")
                return
        except ValueError:
            messagebox.showwarning("Formato incorrecto","La tarifa debe ser un valor numérico válido.")
            return

        try:
            with open("nuevos_usuarios.json", "r", encoding="utf-8") as archivo_usuarios:
                usuarios = json.load(archivo_usuarios)
        except (FileNotFoundError, json.JSONDecodeError):
                messagebox.showerror("Error", "No se encontró el archivo de usuarios o está vacío.")
                return
        
        # Comprobar si el usuario existe en la lista
        usuario_existente = any(u.get("usuario") == usuario for u in usuarios)
        if not usuario_existente:
            messagebox.showwarning("Usuario no encontrado", "El usuario ingresado no está registrado.")
            return
        
        codigo_unico = self.generar_CodigoUnico()
        estado_inicial="Recepcionado"
        # Crear un diccionario con los datos
        datos_pedido = {
            "Fecha creación": fecha_creacion,
            "Fecha entrega": fecha_entrega,
            "Usuario": usuario,
            "Dirección": direccion,
            "Tarifa pedido": tarifa_float,
            "Código único": codigo_unico,
            "Estado":estado_inicial
            }

        # Leer el contenido existente del archivo JSON si existe
        try:
            with open("pedidos.json", "r", encoding="utf-8") as archivo_pedidos:
                pedidos = json.load(archivo_pedidos)
        except (FileNotFoundError, json.JSONDecodeError):
            # Si el archivo no existe o está vacío, inicializar una lista
            pedidos = []

        for entrada in pedidos:
            if entrada["usuario"]==usuario:
                entrada["pedidos"].append(datos_pedido)
                break
        else:
            # Agregar el nuevo pedido a la lista
            pedidos.append({
                "usuario":usuario,
                "pedidos":[datos_pedido]
            })
        # Escribir los datos actualizados en el archivo JSON
        with open("pedidos.json", "w", encoding="utf-8") as archivo:
            json.dump(pedidos, archivo, indent=4, ensure_ascii=False)

        messagebox.showinfo("Éxito", "Pedido guardado exitosamente.")

        # Limpiar los campos después de guardar
        self.entry_usuario.delete(0, "end")
        self.entry_direccion.delete(0, "end")
        self.entry_tarifa.delete(0, "end")
        
    def generar_CodigoUnico(self):
        # Leer los códigos únicos existentes del archivo JSON
        try:
            with open("pedidos.json", "r", encoding="utf-8") as archivo:
                pedidos = json.load(archivo)
                codigos_existentes = {
                    pedido["Código único"] 
                    for usuario in pedidos
                    for pedido in usuario.get("pedidos",[])
                    }
        except (FileNotFoundError, json.JSONDecodeError):
            # Si el archivo no existe o está vacío, inicializar un conjunto vacío
            codigos_existentes = set()

        # Generar un código único que no se encuentre en los códigos existentes
        while True:
            caracteres = string.ascii_letters + string.digits
            codigo_unico = ''.join(random.choices(caracteres, k=8))
            if codigo_unico not in codigos_existentes:
                return codigo_unico
                
class ConsultaPedido_operador(creacion_ventana):
    def __init__(self,usuario_actual):
        super().__init__(titulo="Lavalimpia-Recaudador (Ingreso de pedido)", icono="recursosImagenes/fondoL.ico")
        self.interfaz()
        self.usuario_actual = usuario_actual
    def interfaz(self):
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        # Etiqueta principal
        self.crear_etiqueta(texto="Consulta de Pedidos por código único", fuente=("Britannic Bold"), tamano=20, x=40, y=30, bg="#188999")
        self.crear_boton("Volver", font=("Arial", 10), x=840, y=8, command=lambda: self.cambiarVentana(ventana_operador), width=100, height=25, bd=0, cursor="hand2", bg="white")

        # Etiqueta y entrada para el nombre del usuario
        self.crear_etiqueta(texto="Código único:", fuente=("Arial"), tamano=12, x=40, y=100, bg="#188999")
        self.entry_usuario = self.crear_entry(x=200, y=100, width=250, height=30)

        # Botón para buscar pedidos
        self.crear_boton(text="Buscar Pedidos", font=("Arial", 14), x=470, y=100,
                         command=lambda: self.buscar_pedidos(self.entry_usuario.get()), width=150, height=30)

    def buscar_pedidos(self, codigo_unico):
        """
        Busca pedidos en un archivo JSON según el usuario proporcionado.

        :param usuario: Nombre del usuario a buscar.
        """
        archivo_json = "pedidos.json"
        #campo = "Código único"
        valor = codigo_unico.strip()  # Eliminar espacios en blanco innecesarios

        try:
            # Leer el archivo JSON
            with open(archivo_json, 'r', encoding='utf-8') as file:
                datos = json.load(file)

            # Filtrar los pedidos que coinciden con el usuario
            pedido_encontrado=None
            for usuario in datos:
                for pedido in usuario.get("pedidos",[]):
                    if pedido.get("Código único")==valor:
                        pedido_encontrado=pedido
                        break
                if pedido_encontrado:
                    break


            if pedido_encontrado:
                self.ventanaE_InfoPedidoOperador(titulo="Información pedido",ruta_json="pedidos.json",codigo_filtro=valor)
            else:
                messagebox.showinfo("Sin resultados", f"No se encontraron pedidos para el usuario '{codigo_unico}'.")

        except FileNotFoundError:
            messagebox.showerror("Error", f"El archivo {archivo_json} no fue encontrado.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", f"El archivo {archivo_json} no contiene un formato JSON válido.")
#Hasta aquí llega la interfaz del operador

#Todavia no se empieza.
#Ventana del empleado recaudador.
class  ventana_EmpleadoRecaudador(creacion_ventana):
    def __init__(self,usuario_actual):
        super().__init__(titulo="Lavalimpia-Recaudador",icono="recursosImagenes/fondoL.ico")
        self.usuario_actual=usuario_actual
        self.interfaz()
        
    
    def interfaz(self):
        self.agregar_logo("recursosImagenes/logoLavaLimpia.png",x=0,y=0)
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        self.crear_etiqueta(texto="Total a pagar:", fuente=("Arial"),tamano=22,x=380, y=165,bg="#188999",fg="White")
        self.crear_entry(x=380, y=245, width=250, height=30)
        self.crear_boton(text="Confirmar pago",font=("Arial",12),x=380, y=350,width=200, height=50)
        self.crear_boton(text=" Cerrar sesión  ",font=("Arial", 10),x=840,y=8, command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25, bg= "red", fg="white")
#cierre de la ventana recaudador.        

print("Hola mundo")

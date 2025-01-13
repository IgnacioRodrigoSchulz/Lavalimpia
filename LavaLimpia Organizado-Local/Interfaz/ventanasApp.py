from Interfaz.creacionVent import creacion_ventana # Importa la clase base `creacion_ventana` que se usará para crear la interfaz.
import tkinter as tk # Importa la biblioteca de Python para crear interfaces gráficas.
from tkinter import messagebox,ttk,scrolledtext,Menu  # Importa componentes específicos de Tkinter para cuadros de diálogo, menús, etc.
from Interfaz import funciones # Importa funciones adicionales de un módulo personalizado.
import json,random,string # Importa bibliotecas estándar de Python para trabajar con JSON, generar valores aleatorios y cadenas.
from datetime import datetime,timedelta # Importa clases para trabajar con fechas y horas.
import pyperclip # Permite copiar y pegar texto en el portapapeles.
from tkinter import * # Importa todos los componentes de Tkinter.
'''
###Funcionalidades###
1.Cambiar de ventana entre las distintas interfaces.
2.Validar credenciales de usuario (inicio de sesión).
3.Crear una cuenta de usuario.
4.Cerrar sesión del usuario.
5.Crear un pedido.
6.Consultar pedidos asociados al usuario.
7.Consultar el estado de un pedido.
8.Mostrar y aceptar términos y condiciones.
9.Copiar texto (como códigos únicos) al portapapeles.
10.Generar códigos únicos para usuarios y pedidos.
11.Cargar datos desde un archivo JSON (usuarios y pedidos).
12.Guardar datos en un archivo JSON (usuarios y pedidos).
13.Filtrar y buscar usuarios en la interfaz del gerente.
14.Filtrar y buscar pedidos en la interfaz del gerente.
15.Modificar el estado de un pedido en la interfaz del gerente.
16.Mostrar estadísticas diarias (como cuentas creadas y dinero proyectado).
17.Procesar pagos de pedidos en la interfaz del recaudador.
18.Mostrar detalles de un pedido para su pago.
19.Ver estadísticas en tablas.
20.Pegar texto desde el portapapeles.
21.Configurar menús contextuales para acciones rápidas (como copiar).
22.Mostrar mensajes de éxito, error o advertencia al usuario.
23.Validar datos ingresados por el usuario, como tarifas, contraseñas, y nombres.
24.Crear ventanas emergentes para consultar detalles específicos.
25.Mostrar tablas con filtros.
'''
#1) Aquí empieza la ventana principal
class ventanaPrincipal(creacion_ventana): # Clase que representa la ventana principal, heredando de `creacion_ventana`.
    def __init__(self): # Constructor de la clase.
        super().__init__(titulo="Lavalimpia-Inicio de sesión", icono="recursosImagenes/fondoL.ico")
        ## Atributo encapsulado para almacenar al usuario autenticado.# Inicializa la ventana principal con un título y un ícono.
        self.usuario_actual = None  # Variable para almacenar el usuario autenticado.# Inicialización de una instancia de usuario actual como None.
        self.interfaz() # Llama al método que define los elementos de la interfaz gráfica.

    def interfaz(self): # Método que configura la interfaz de usuario.
        self.agregar_logo("recursosImagenes/logoLavaLimpia.png", x=0, y=0)
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        # Agrega etiquetas con texto descriptivo.
        self.crear_etiqueta("Inicio de sesión", "Britannic Bold", 20, x=380, y=165, bg="#188999")
        self.crear_etiqueta("Ingrese usuario o e-mail", "Arial", 15, x=380, y=220, bg="#188999")
        self.crear_etiqueta("Ingrese contraseña:", "Arial", 15, x=380, y=275, bg="#188999")
        # Crea campos de entrada para el usuario y la contraseña.
        texto_ingreso = self.crear_entry(x=380, y=245, width=250, height=30)  # Usuario o email# Instancia de un campo de entrada para el usuario o correo.
        texto_contrasena = self.crear_entry(x=380, y=300, width=250, height=30, mostrar="*")  # Contraseña # Instancia de un campo de entrada para la contraseña.

        # Botón iniciar sesión
        self.crear_boton(
            text="Iniciar sesión", # Texto del botón.
            font=("Arial", 20),# Fuente y tamaño del texto.
            x=380,
            y=350,
            width=250,# Ancho del botón.
            height=30,# Altura del botón.
            command=lambda: self.validar_credenciales(texto_ingreso.get().strip(), texto_contrasena.get().strip()) ## Llama al método `validar_credenciales` al hacer clic, pasando los valores ingresados.
        )

        # Crea un botón para registrar un nuevo usuario.
        self.crear_boton(
            text="Crear cuenta de usuario",
            font=("Arial", 15),
            x=380,
            y=450,
            command=lambda: self.cambiarVentana(ventanaRegistro),  # Llama al método `cambiarVentana` para cambiar a la ventana de registro.
            cursor="hand2" # Cambia el cursor al pasar sobre el botón.
        )
    # Método para validar las credenciales ingresadas por el usuario.
    def validar_credenciales(self, usuario, contrasena):
        """
        Método que valida las credenciales del usuario y asigna la instancia del usuario actual.
        Este método aplica encapsulamiento al manejar internamente la autenticación.
        """
        archivo_usuarios = "usuariostest.json" # Archivo JSON donde se almacenan los datos de usuarios.
        # Verifica si los campos están vacíos.
        if not usuario or not contrasena:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return False

        try:
            # Intenta abrir y cargar el archivo de usuarios.
            with open(archivo_usuarios, "r") as file:
                usuarios = json.load(file)  # Carga el contenido del archivo JSON en un diccionario.
        except FileNotFoundError:# Si el archivo no existe.
            messagebox.showerror("Error", "El archivo de usuarios no fue encontrado.")
            return False
        except json.JSONDecodeError: # Si el archivo tiene un formato inválido.
            messagebox.showerror("Error", "El archivo de usuarios tiene un formato incorrecto.")
            return False
        # Recorre la lista de usuarios para validar las credenciales.
        for user in usuarios:
            # Comprueba si el usuario coincide por nombre o correo, y si la contraseña es correcta.
            if (user["nombre"] == usuario or user["correo"] == usuario) and user["contrasena"] == contrasena:
                self.usuario_actual = user  # Almacena al usuario autenticado. # Se instancia el usuario actual con la información del usuario autenticado.
                tipo_usuario = user["tipoUsuario"] # Obtiene el tipo de usuario.
                messagebox.showinfo("Bienvenido", f"¡Hola, {user['nombre']}! Has ingresado como {tipo_usuario}.")

                # Redirigir según el tipo de usuario
                if tipo_usuario == "cliente":
                    self.cambiarVentana(ventana_usuario,self.usuario_actual)
                elif tipo_usuario == "gerente":
                    self.cambiarVentana(ventana_gerente,self.usuario_actual)
                elif tipo_usuario == "operador":
                    self.cambiarVentana(ventana_operador, self.usuario_actual)
                elif tipo_usuario=="recaudador":
                    self.cambiarVentana(ventana_EmpleadoRecaudador,self.usuario_actual)
                else:
                    messagebox.showerror("Error", "Tipo de usuario desconocido.")
                return True
        # Si no se encuentra una coincidencia, muestra un mensaje de error.
        messagebox.showerror("Error", "El usuario o la contraseña son incorrectos.")
        return False
#Aquí termina la ventana principal.

#2)Aquí empieca la ventana del usuario.
class ventana_usuario(creacion_ventana):  # Clase que representa la ventana para usuarios 
    def __init__(self, usuario):
        super().__init__(titulo="Lavalimpia-Usuario", icono="recursosImagenes/fondoL.ico") # Constructor de la clase. Llama al constructor de la clase base `creacion_ventana`.
        self.usuario = usuario  # Usuario autenticado,# Almacena los datos del usuario autenticado.
        self.pedidos_usuario = [] # Lista para almacenar los pedidos del usuario actual.
        self.archivo_pedidos = "pedidostest.json"  # Nombre del archivo que contiene los pedidos.
        self.ventanaPedidos = None # Variable para la ventana secundaria que muestra los pedidos.
        self.interfaz() # Llama al método que configura la interfaz de usuario.

    def interfaz(self):
        # Configura la interfaz gráfica de la ventana.
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        self.crear_etiqueta(f"¡Bienvenido, {self.usuario['nombre']}!", fuente="Britannic Bold", tamano=28, x=40, y=30, bg="#188999") # Muestra un saludo personalizado al usuario.

        # Botón para cerrar sesión
        self.crear_boton("Cerrar sesión", font=("Arial", 10), x=840, y=8,
                         command=lambda: self.cambiarVentana(ventanaPrincipal), width=100, height=25, bg="#e31414", fg="#ffffff", cursor="hand2")

        # Botón para cargar pedidos
        self.crear_etiqueta("Para ver tus códigos únicos asociados a tus pedidos cliquea aquí:", fuente="Arial", tamano=15, x=40, y=100, bg="#188999")
        self.boton_pedidos = self.crear_boton(text="Códigos", font=("Arial", 18), x=40, y=150, command=self.cargar_pedidos, width=100, height=25) # Llama al método para cargar pedidos.

        # Botón para ver estado del pedido
        self.crear_etiqueta("Para saber el estado de su pedido cliquea Aquí he ingrese el código único de su pedido:", fuente="Arial", tamano=15, x=40, y=200, bg="#188999")
        self.botonEstado = self.crear_boton(text="Estado", font=("Arial", 18), x=40, y=250, command=self.ver_estado_pedido, width=100, height=25) # Llama al método para verificar el estado del pedido.

    def cargar_pedidos(self, mostrar_ventana=True):
        """
        Busca y muestra los pedidos asociados al usuario actual en una tabla interactiva.
        """
        try:
            # Leer el archivo JSON
            with open(self.archivo_pedidos, 'r', encoding='utf-8') as file: # Carga los datos del archivo JSON.
                datos_pedidos = json.load(file)

            # Filtra los pedidos que pertenecen al usuario actual.
            self.pedidos_usuario = [pedido for pedido in datos_pedidos if pedido["usuario"] == self.usuario["codigoUnico"]]

            if self.pedidos_usuario:
                if mostrar_ventana:
                    self.mostrar_tabla_pedidos() # Muestra los pedidos en una tabla.
            else:
                messagebox.showinfo("Pedidos del usuario", "No tienes pedidos registrados.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"El archivo {self.archivo_pedidos} no fue encontrado.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "El archivo de pedidos tiene un formato incorrecto.")

    def mostrar_tabla_pedidos(self):
        """
        Muestra los pedidos en una tabla interactiva con opción de copiar.
        """
        if self.ventanaPedidos is not None and self.ventanaPedidos.winfo_exists():
            return # Evita abrir múltiples ventanas.
        # Crea una ventana secundaria para mostrar los pedidos.
        self.ventanaPedidos = Toplevel(self.ventana)
        self.ventanaPedidos.title("Código único de sus pedidos")
        self.ventanaPedidos.geometry("850x300")
        self.ventanaPedidos.resizable(False,False)
        # Configura la tabla interactiva.
        columnas = ("codigo", "estado", "fecha")
        tabla = ttk.Treeview(self.ventanaPedidos, columns=columnas, show="headings", height=10)
        tabla.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Define los encabezados de la tabla.
        tabla.heading("codigo", text="Código Único")
        tabla.heading("estado", text="Estado")
        tabla.heading("fecha", text="Fecha Plazo")

        # Llena la tabla con los datos de los pedidos del usuario.
        for pedido in self.pedidos_usuario:
            tabla.insert("", "end", values=(pedido["codigoUnico"], pedido.get("estadoActual", "Desconocido"), pedido.get("fechaPlazo", "Desconocida")))

        # Función para copiar el código único al portapapeles.
        def copiar_codigo():
            try:
                item_seleccionado = tabla.selection()[0]
                codigo_unico = tabla.item(item_seleccionado, "values")[0]
                pyperclip.copy(codigo_unico)
                messagebox.showinfo("Copiar Código", f"Código único '{codigo_unico}' copiado al portapapeles.")
            except IndexError:
                messagebox.showerror("Error", "No se ha seleccionado ningún código para copiar.")

        # Botón para copiar el código único.
        boton_copiar = Button(self.ventanaPedidos, text="Copiar Código", command=copiar_codigo)
        boton_copiar.pack(pady=5)

        # Menú contextual para copiar el código único.
        menu = Menu(self.ventanaPedidos, tearoff=0)
        menu.add_command(label="Copiar Código", command=copiar_codigo)

        def mostrar_menu(event):
            menu.post(event.x_root, event.y_root)

        tabla.bind("<Button-3>", mostrar_menu) # Vincula el menú al clic derecho.

    def ver_estado_pedido(self):
        """
        Abre una ventana para ingresar el código único y mostrar detalles del pedido.
        """
        # Asegurarse de que los pedidos del usuario están cargados
        if not self.pedidos_usuario:
            self.cargar_pedidos(mostrar_ventana=False)
            if not self.pedidos_usuario:
                #messagebox.showinfo("Estado del Pedido", "No tienes pedidos registrados para mostrar.")
                return
            
        # Crea una ventana emergente para consultar el estado del pedido.
        ventana_estado = Toplevel(self.ventana)
        ventana_estado.title("Estado del pedido")
        ventana_estado.geometry("400x280")
        ventana_estado.resizable(False,False)
        ventana_estado.transient(self.ventana)
        ventana_estado.grab_set()

        # Configura el diseño de la ventana emergente.
        ventana_estado.columnconfigure(0, weight=1)

        # Etiqueta para el código único
        Label(ventana_estado, text="Ingrese el código único del pedido:", font=("Arial", 12), anchor="w").grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        # Frame para agrupar el Entry y el botón de pegar
        frame_entry = Frame(ventana_estado)
        frame_entry.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        # Crea un contenedor (Frame) para organizar el campo de entrada (Entry) y el botón de pegar de forma horizontal.

        # Campo de entrada
        entry_codigo = Entry(frame_entry, font=("Arial", 12), width=25)
        entry_codigo.pack(side=LEFT, padx=(0, 5))  # Deja un espacio mínimo entre el Entry y el botón
        # Agrega un campo de texto donde el usuario puede ingresar manualmente el código único.
        # Se posiciona a la izquierda dentro del Frame, dejando un pequeño espacio a la derecha.

       # Botón para pegar código desde el portapapeles
        def pegar_codigo():
            codigo_clipboard = pyperclip.paste().strip() # Obtiene el texto del portapapeles.
            if not codigo_clipboard:
                # Muestra una advertencia si el portapapeles está vacío.
                messagebox.showwarning("Advertencia", "El portapapeles está vacío. No se puede pegar un código.")
                return
            entry_codigo.delete(0, END) # Limpia el campo de entrada.
            entry_codigo.insert(0, codigo_clipboard) # Inserta el contenido del portapapeles.


        Button(frame_entry, text="Pegar", font=("Arial", 10), command=pegar_codigo).pack(side=LEFT) # Agrega un botón que llama a la función `pegar_codigo` para pegar el texto del portapapeles en el campo de entrada.

        # Etiquetas para mostrar información del pedido
        label_estado = Label(ventana_estado, text="Estado: ", font=("Arial", 10), anchor="w")
        label_estado.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        label_fecha_entrega = Label(ventana_estado, text="Fecha de Entrega: ", font=("Arial", 10), anchor="w")
        label_fecha_entrega.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        label_direccion = Label(ventana_estado, text="Dirección: ", font=("Arial", 10), anchor="w")
        label_direccion.grid(row=4, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        label_tarifa = Label(ventana_estado, text="Tarifa: ", font=("Arial", 10), anchor="w")
        label_tarifa.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        # Botón para buscar el estado del pedido
        def buscar_estado():
            """
            Busca el estado del pedido basado en el código único ingresado.
            Actualiza las etiquetas con la información del pedido si se encuentra.
            """
            codigo = entry_codigo.get().strip() # Obtiene el código ingresado por el usuario.
            pedido = next((p for p in self.pedidos_usuario if p.get("codigoUnico") == codigo), None)
             # Busca el pedido en la lista de pedidos del usuario.

            if pedido:
                # Si el pedido existe, actualiza las etiquetas con la información correspondiente.
                label_estado.config(text=f"Estado: {pedido.get('estadoActual', 'Desconocido')}")
                label_fecha_entrega.config(text=f"Fecha de Plazo: {pedido.get('fechaPlazo', 'Desconocida')}")
                label_direccion.config(text=f"Dirección: {pedido.get('direccion', 'Desconocida')}")
                label_tarifa.config(text=f"Tarifa: {pedido.get('tarifa', 'Desconocida')} CLP")
            else:
                # Si no se encuentra el pedido, muestra un mensaje de error y limpia las etiquetas.
                label_estado.config(text="Código no encontrado")
                label_fecha_entrega.config(text="")
                label_direccion.config(text="")
                label_tarifa.config(text="")

        Button(ventana_estado, text="Buscar", command=buscar_estado).grid(row=6, column=0, columnspan=2, pady=10)
        # Agrega un botón que ejecuta la función `buscar_estado` para buscar el pedido y actualizar las etiquetas.       
#Aquí termina la ventana del usuario.

#3) Esta es la ventana de registro
class ventanaRegistro(creacion_ventana):# Clase para la ventana de registro de nuevos usuarios
    def __init__(self):
        # Inicializa la ventana con un título e icono específicos
        super().__init__(titulo="Lavalimpia-Registro", icono="recursosImagenes/fondoL.ico")
        self.interfaz()
    
    def interfaz(self):
        self.acepto_terminos = tk.BooleanVar(value=False) # Variable para verificar si se aceptaron los términos y condiciones
        self.agregar_logo("recursosImagenes/logoLavaLimpia.png", 0, 0)
        self.agregar_logo("recursosImagenes/Logo2.png", 65, 280)
        
        boton_salir=self.crear_boton("Volver al inicio",font=("Arial", 10),x=840,y=8,command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25,bd=0, cursor="hand2",bg="#188999")

        # Etiquetas para los campos de registro
        self.crear_etiqueta("Nuevo nombre de usuario:", "Arial", 12, 380, 165, bg="#188999")
        self.crear_etiqueta("Ingrese e-mail:", "Arial", 12, 380, 220, bg="#188999")
        self.crear_etiqueta("Ingrese contraseña:", "Arial", 12, 380, 275, bg="#188999")
        self.crear_etiqueta("Confirme su contraseña:", "Arial", 12, 380, 330, bg="#188999")
        # Campos de entrada para el registro
        usuario=self.crear_entry(x=380,y=190, width=250, height=30)
        correo=self.crear_entry(x=380,y=245, width=250, height=30)
        contrasena=self.crear_entry(x=380,y=300, width=250, height=30,mostrar="*")
        confirmar_contrasena=self.crear_entry(x=380,y=355, width=250, height=30,mostrar="*")
        # Frame para la casilla de términos y condiciones
        check_frame = tk.Frame(self.ventana, bg="#188999")
        check_frame.place(x=380, y=385)
        # Casilla para aceptar términos y condiciones
        check_btn = tk.Checkbutton(check_frame,variable=self.acepto_terminos,onvalue=True, offvalue=False,bg="#188999")
        check_btn.pack(side="left")
        # Etiqueta vinculada a los términos y condiciones
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
        """
        Valida los datos ingresados por el usuario y los guarda si son válidos.
        """
        if not self.acepto_terminos.get():
            # Verifica si se aceptaron los términos y condiciones
            messagebox.showwarning("Advertencia", "Debe aceptar los términos y condiciones para continuar")
            return
        if not usuario or not correo or not contrasena or not confirmar_contrasena:
            # Verifica que todos los campos estén completos
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return  # Termina la ejecución si hay campos vacíos
        
        # Validar usuario, correo y contraseña
        try: # se llama a funciones externas para validar los datos.
            usuarioValido = funciones.verificarUsuario(usuario) # Valida el nombre de usuario
            correoValido = funciones.verificarCorreo(correo) # Valida el correo electrónico
            contrasenaValida = funciones.verificarContrasena(contrasena, confirmar_contrasena) # Valida la contraseña
        except ValueError as e:  # Si las funciones lanza un error se manejan de la siguiente forma
            # Manejo de errores de validación
            messagebox.showerror("Error de Validación", str(e))
            return
        # Si los datos son válidos, procede a guardarlos
        if usuarioValido and correoValido and contrasenaValida:
            nuevo_usuario = {
                "nombre": usuario,
                "contrasena": contrasena,
                "correo": correo,
                "pedidos": [],
                "tipoUsuario": "cliente",  # Tipo de usuario predeterminado
                "fechaCreacion": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "codigoUnico": self.generar_codigo_unico()
            }
            guardado=self.guardar_json(nuevo_usuario) # Guarda el usuario en un archivo JSON
            if guardado:
                messagebox.showinfo("Éxito","Sus datos estan registrados en el sistema")
                self.cambiarVentana(ventanaPrincipal) # Regresa a la ventana principal
            else:
                messagebox.showerror("Error", "El correo ya está registrado.")
    def guardar_json(self, nuevo_usuario):
        """
        Guarda los datos del nuevo usuario en un archivo JSON.
        """
        archivo = "usuariostest.json"  # Archivo donde se guardan los datos
        try:
            # Leer usuarios existentes
            with open(archivo, "r") as file:
                usuarios = json.load(file) # Lee los usuarios existentes
        except (FileNotFoundError, json.JSONDecodeError):
            usuarios = []   #Si no existe el archivo, inicializa una lista vacía

        # Verifica si el correo ya está registrado
        for usuario in usuarios:
            if usuario["correo"] == nuevo_usuario["correo"]:
                return False  # Retorna False si el correo está duplicado

        usuarios.append(nuevo_usuario) # Agrega el nuevo usuario
    
        # Guardar los datos actualizados
        with open(archivo, "w") as file:
            json.dump(usuarios, file, indent=4)
    
        return True  # Indica que se guardó correctamente
    
    def generar_codigo_unico(self):
        archivo = "usuariostest.json"
        try:
            with open(archivo, "r") as file:
                usuarios = json.load(file)
            return str(len(usuarios)) # El código único es el número total de usuarios
        except (FileNotFoundError, json.JSONDecodeError):
            return "0"  # Si no hay usuarios, el código único es "0"
        
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
#Aquí termina la ventana de registro

#4) Aquí empieza la ventana del gerente
class ventana_gerente(creacion_ventana):
    """
    Clase para la ventana principal de un gerente en la aplicación.
    Permite al gerente gestionar pedidos, usuarios y visualizar estadísticas.
    Hereda de creacion_ventana.
    """
    def __init__(self, usuario):
        super().__init__(titulo="Lavalimpia-Gerente", icono="recursosImagenes/fondoL.ico")
        self.usuario = usuario
        self.archivo_pedidos = "pedidostest.json"
        self.archivo_usuarios = "usuariostest.json"
        self.interfaz()

    def interfaz(self):
        self.crear_etiqueta(
            f"¡Bienvenido, {self.usuario['nombre']}!", # Muestra un mensaje de bienvenida personalizado para el gerente
            fuente="Britannic Bold", 
            tamano=28, 
            x=40, y=30, 
            bg="#188999"
        )
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        # Botones de funcionalidad
        self.crear_boton( 
            text="Cerrar sesión",
            font=("Arial", 10),
            x=840, y=8,
            command=lambda: self.cambiarVentana(ventanaPrincipal),
            width=100, height=25, bg="red", fg="white"
        )
        self.crear_boton(
            text="Buscador de pedidos",
            font=("Arial", 18),
            x=150, y=200,
            command=lambda: self.cambiarVentana(BuscarPedidosGerente, self.usuario),
            width=300, height=50
        )
        self.crear_boton(
            text="Buscador de usuarios",
            font=("Arial", 18),
            x=150, y=300,
            command=lambda: self.cambiarVentana(BuscarUsuariosGerente, self.usuario),
            width=300, height=50
        )
        self.crear_boton(
            text="Datos y estadísticas",
            font=("Arial", 18),
            x=500, y=200,
            command=self.mostrarEstadisticas,
            width=300, height=50
        )
        self.crear_boton(
            text="Crear pedido",
            font=("Arial", 18),
            x=500, y=300,
            command=lambda: self.cambiarVentana(IngresoPedido_gerente, self.usuario),
            width=300, height=50
        )

    def mostrarEstadisticas(self):
        """
        Muestra una ventana emergente con estadísticas diarias de la lavandería.
        Permite al gerente visualizar datos como cuentas creadas, dinero proyectado y pedidos realizados.

        Incluye una tabla interactiva y filtros para buscar estadísticas específicas.
        """
        # Configuración de la ventana emergente
        ventana_emergente = tk.Toplevel(self.ventana)
        ventana_emergente.title("Estadísticas Diarias de la Lavandería")

        frame = ttk.Frame(ventana_emergente, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E)) #tk.W y tk.E representan las direcciones Oeste (West) y Este (East), respectivamente. Al combinarlos, estás diciendo que el widget debe estirarse horizontalmente para llenar toda la anchura de la celda en la que está colocado.
        # Entrada para buscar por fecha
        ttk.Label(frame, text="Buscar por Fecha (YYYY-MM-DD):").grid(row=0, column=0, sticky=tk.W)
        entrada_fecha = ttk.Entry(frame)
        entrada_fecha.grid(row=0, column=1, sticky=(tk.W, tk.E))

        # Tabla con barra de desplazamiento# Tabla para mostrar datos
        tabla_frame = ttk.Frame(frame)
        tabla_frame.grid(row=1, column=0, columnspan=5, sticky=(tk.W, tk.E))

        tabla = ttk.Treeview(tabla_frame, columns=("Fecha", "Dinero Proyectado", "Cuentas Creadas", "Pedidos Realizados", "Pedidos Pagados"), show='headings', height=10)
        for col in ("Fecha", "Dinero Proyectado", "Cuentas Creadas", "Pedidos Realizados", "Pedidos Pagados"):
            tabla.heading(col, text=col)
        # Barra de desplazamiento para la tabla
        barra_desplazamiento = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
        tabla.configure(yscroll=barra_desplazamiento.set)
        tabla.grid(row=0, column=0, sticky=(tk.W, tk.E))
        barra_desplazamiento.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Función para cargar datos
        def cargar_datos():
            """
            Carga los datos de usuarios y pedidos desde archivos JSON.

            Returns:
                tuple: Dos listas, una con los usuarios y otra con los pedidos.
            """
            try:
                with open(self.archivo_usuarios, 'r') as f:
                    usuarios = json.load(f)
                with open(self.archivo_pedidos, 'r') as f:
                    pedidos = json.load(f)
                return usuarios, pedidos
            except (FileNotFoundError, json.JSONDecodeError) as e:
                messagebox.showerror("Error", f"Error al cargar los datos: {e}")
                return [], []

        # Función para generar estadísticas
        def generar_datos_estadisticas():
            """
            Genera estadísticas diarias con base en los datos de usuarios y pedidos.

            Returns:
                dict: Diccionario con las estadísticas organizadas por fecha.
            """
            usuarios, pedidos = cargar_datos()
            datos = {}
            # Procesa usuarios
            for usuario in usuarios:
                fecha = usuario.get('fechaCreacion', '').split(" ")[0]
                if fecha:
                    datos.setdefault(fecha, {'dinero_proyectado': 0, 'cuentas': 0, 'pedidos': 0, 'pagados': 0})
                    datos[fecha]['cuentas'] += 1
            # Procesa pedidos
            for pedido in pedidos:
                fecha = pedido.get('fechaCreacion', '').split(" ")[0]
                if fecha:
                    datos.setdefault(fecha, {'dinero_proyectado': 0, 'cuentas': 0, 'pedidos': 0, 'pagados': 0})
                    datos[fecha]['dinero_proyectado'] += pedido.get('tarifa', 0)
                    datos[fecha]['pedidos'] += 1
                    if pedido.get('estadoActual') == "Entregado":
                        datos[fecha]['pagados'] += pedido.get('tarifa', 0)
            return datos

        # Función para cargar datos en la tabla
        def cargar_datos_tabla():
            """
            Carga las estadísticas en la tabla de la ventana emergente.
            """
            datos = generar_datos_estadisticas()
            tabla.delete(*tabla.get_children())# Limpia la tabla antes de cargar nuevos datos
            for fecha, valores in sorted(datos.items()):# Ordena y carga las estadísticas en la tabla
                tabla.insert("", "end", values=(fecha, f"${valores['dinero_proyectado']}", valores['cuentas'], valores['pedidos'], f"${valores['pagados']}"))

        # Refrescar tabla periódicamente
        def refrescar_tabla():
            """
            Actualiza los datos de la tabla llamando a cargar_datos_tabla.
            """
            cargar_datos_tabla()

        # Filtrar tabla por fecha
        def filtrar_por_fecha():
            """
            Filtra los datos en la tabla según la fecha ingresada por el usuario.
            Solo muestra las filas que coinciden con la fecha proporcionada.
            """
            fecha = entrada_fecha.get()
            for item in tabla.get_children():
                valores = tabla.item(item, "values")
                if valores[0] != fecha: # Si la fecha no coincide, oculta la fila
                    tabla.detach(item)
        # Botones para aplicar el filtro y refrescar los datos
        ttk.Button(frame, text="Aplicar Filtro", command=filtrar_por_fecha).grid(row=0, column=2, sticky=tk.W)
        ttk.Button(frame, text="Refrescar", command=refrescar_tabla).grid(row=0, column=3, sticky=tk.W)

        # Gestión de actualizaciones periódicas
        temporizador_id = None # Variable para almacenar el ID del temporizador


        def actualizar_periodicamente():
            """
            Refresca los datos de la tabla cada 30 segundos automáticamente.
            """
            nonlocal temporizador_id
            refrescar_tabla()  # Llama a refrescar_tabla para actualizar los datos
            temporizador_id = ventana_emergente.after(30000, actualizar_periodicamente) # Repite después de 30s

        def al_cerrar():
            """
            Cancela el temporizador al cerrar la ventana emergente.
            Esto asegura que no queden procesos en segundo plano.
            """
            if temporizador_id is not None: # Si hay un temporizador activo, lo cancela
                ventana_emergente.after_cancel(temporizador_id)
            ventana_emergente.destroy() # Cierra la ventana
        # Configuración del cierre y carga inicial de dato
        ventana_emergente.protocol("WM_DELETE_WINDOW", al_cerrar) # Llama a al_cerrar al cerrar la ventana
        cargar_datos_tabla()  # Carga inicial de los datos en la tabla
        actualizar_periodicamente() # Inicia el refresco automático

class IngresoPedido_gerente(creacion_ventana):
    def __init__(self, usuario):
        if not usuario:
            raise ValueError("El usuario no puede ser None")
        super().__init__(titulo="Lavalimpia-Gerente (Ingreso de pedido)", icono="recursosImagenes/fondoL.ico")
        self.interfaz()
        self.archivo_pedidos = "pedidostest.json"
        self.archivo_usuarios = "usuariostest.json"
        self.usuario = usuario
    def interfaz(self):
        self.crear_etiqueta(texto="Creador de pedidos", fuente=("Britannic Bold"), tamano=28, x=40, y=30, bg="#188999")
        self.crear_boton("Volver", font=("Arial", 10), x=840, y=8, command=self.volver, width=100, height=25, bd=0, cursor="hand2", bg="white")

        self.crear_etiqueta(texto="Nombre del usuario", fuente=("Arial"), tamano=12, x=120, y=120, bg="#188999", fg="#ffffff")
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
    def volver(self):
        # Al hacer clic en Volver, se pasa el usuario correctamente a la ventana_operador
        self.cambiarVentana(ventana_gerente, self.usuario)
    def guardar_pedido(self):
        # Obtener la fecha y hora actual
        fecha_actual = datetime.now()
        fecha_creacion = fecha_actual.strftime("%Y-%m-%d %H:%M")

        # Calcular la fecha de entrega sumando 2 días
        fecha_entrega = (fecha_actual + timedelta(days=2)).strftime("%Y-%m-%d %H:%M")

        # Obtener los datos de los campos de entrada
        nombre_usuario = self.entry_usuario.get().strip()
        direccion = self.entry_direccion.get().strip()
        tarifa = self.entry_tarifa.get().strip()

        # Validaciones
        if not nombre_usuario:
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
            if tarifa_float <= 0:
                messagebox.showwarning("Valor inválido", "La tarifa debe ser un valor numérico positivo.")
                return
        except ValueError:
            messagebox.showwarning("Formato incorrecto", "La tarifa debe ser un valor numérico válido.")
            return

        # Leer archivo de usuarios
        try:
            with open(self.archivo_usuarios, "r", encoding="utf-8") as archivo_usuarios:
                usuarios = json.load(archivo_usuarios)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "No se encontró el archivo de usuarios o está vacío.")
            return

        # Comprobar si el código único del usuario existe
        usuario_existente = next((u for u in usuarios if u.get("nombre") == nombre_usuario), None)
        if not usuario_existente:
            messagebox.showwarning("Usuario no encontrado", "El código único ingresado no corresponde a ningún usuario registrado.")
            return
        # Obtener el ID del usuario
        id_usuario = usuario_existente.get("codigoUnico")
        # Generar un código único para el pedido
        codigo_unico_pedido = self.generar_CodigoUnico()

        # Crear un diccionario con los datos
        datos_pedido = {
        "codigoUnico": codigo_unico_pedido,
        "direccion": direccion,
        "usuario": id_usuario,  # ID del usuario
        "usuario_nombre": nombre_usuario,  # Nombre del usuario
        "tarifa": tarifa_float,
        "fechaCreacion": fecha_creacion,
        "estadoActual": "Recepcionado",
        "estadoHistorial": [
            [fecha_creacion, "Recepcionado", codigo_unico_pedido]
        ],
        "fechaPlazo": fecha_entrega
    }

        # Leer archivo de pedidos
        try:
            with open(self.archivo_pedidos, "r", encoding="utf-8") as archivo_pedidos:
                pedidos = json.load(archivo_pedidos)
        except (FileNotFoundError, json.JSONDecodeError):
            pedidos = []

        # Añadir el nuevo pedido
        pedidos.append(datos_pedido)

        # Guardar el archivo de pedidos actualizado
        with open(self.archivo_pedidos, "w", encoding="utf-8") as archivo_pedidos:
            json.dump(pedidos, archivo_pedidos, indent=4, ensure_ascii=False)

        # Actualizar el archivo de usuarios
        usuario_existente.setdefault("pedidos", []).append(codigo_unico_pedido)
        with open(self.archivo_usuarios, "w", encoding="utf-8") as archivo_usuarios:
            json.dump(usuarios, archivo_usuarios, indent=4, ensure_ascii=False)

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Pedido guardado exitosamente.")

        # Limpiar los campos después de guardar
        self.entry_usuario.delete(0, "end")
        self.entry_direccion.delete(0, "end")
        self.entry_tarifa.delete(0, "end")

    def generar_CodigoUnico(self):
        """
        Genera un código único alfanumérico de 8 caracteres que no se repite entre los pedidos existentes.

        Este método asegura que cada código generado sea único al verificarlo contra los códigos 
        ya registrados en un archivo JSON. Si el archivo no existe o tiene un formato inválido, 
        se asume que no hay códigos existentes.

        :return: Un código único de 8 caracteres.
        """
        try:
            # Intenta abrir el archivo de pedidos y cargar los códigos existentes
            with open(self.archivo_pedidos, "r", encoding="utf-8") as archivo_pedidos:
                pedidos = json.load(archivo_pedidos)
                # Extrae los códigos únicos existentes en un conjunto para una búsqueda eficiente
                codigos_existentes = {pedido["codigoUnico"] for pedido in pedidos}
        except (FileNotFoundError, json.JSONDecodeError):
            # Si el archivo no existe o tiene errores de formato, inicializa un conjunto vacío
            codigos_existentes = set()
        # Genera códigos hasta encontrar uno que no esté en el conjunto de códigos existentes
        while True:
            # Genera un código aleatorio de 8 caracteres alfanuméricos
            codigo_unico = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            # Verifica si el código es único
            if codigo_unico not in codigos_existentes:
                return codigo_unico
 
class BuscarPedidosGerente(creacion_ventana): # Clase para la interfaz de búsqueda y gestión de pedidos por parte del gerente.
    def __init__(self, usuario):
        # Constructor de la clase.
        super().__init__(titulo="Lavalimpia-Gerente (Ingreso de pedido)", icono="recursosImagenes/fondoL.ico")
        self.usuario = usuario # Usuario actual.
        self.pedidos = [] # Lista de pedidos cargados desde el archivo.
        self.usuarios = {} # Diccionario de usuarios cargados desde el archivo.
        self.interfaz() # Cambia a la ventana del gerente.

    def volver(self):
        self.cambiarVentana(ventana_gerente, self.usuario)

    def interfaz(self):
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        self.crear_etiqueta(
            texto="Consulta de Pedidos por código único o usuario",
            fuente=("Britannic Bold"), tamano=20, x=40, y=30, bg="#188999"
        )
        self.crear_boton("Volver", font=("Arial", 10), x=840, y=8, command=self.volver, width=100, height=25, bd=0, cursor="hand2", bg="white")
        # Marco para los filtros de búsqueda.
        frame_filtros = tk.Frame(self.ventana, bg="#188999")
        frame_filtros.place(x=10, y=60, width=880, height=50)
        # Filtros de búsqueda.
        tk.Label(frame_filtros, text="Código único:", font=("Arial", 12), bg="#188999", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_codigo = tk.Entry(frame_filtros)
        self.entry_codigo.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_filtros, text="ID del Usuario:", font=("Arial", 12), bg="#188999", fg="white").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.entry_usuario = tk.Entry(frame_filtros)
        self.entry_usuario.grid(row=0, column=3, padx=5, pady=5)
        # Botón para aplicar el filtro de búsqueda.
        tk.Button(frame_filtros, text="Buscar", command=self.filtrar_pedidos, bg="blue", fg="white", font=("Arial", 12)).grid(row=0, column=4, padx=10, pady=5)

        # Configuración de la tabla para mostrar pedidos.
        self.tree = ttk.Treeview(self.ventana, columns=("fechaCreacion", "fechaPlazo", "usuario", "direccion", "tarifa", "codigoUnico", "estadoActual"), show="headings")
        self.tree.place(x=10, y=120, width=880, height=400)
        # Barra de desplazamiento para la tabla.
        scrollbar_vertical = ttk.Scrollbar(self.ventana, orient="vertical", command=self.tree.yview)
        scrollbar_vertical.place(x=890, y=120, height=400)
        self.tree.configure(yscrollcommand=scrollbar_vertical.set)
        # Configuración de las columnas.
        self.tree.heading("fechaCreacion", text="Fecha Creación")
        self.tree.heading("fechaPlazo", text="Fecha Plazo")
        self.tree.heading("usuario", text="ID usuario")
        self.tree.heading("direccion", text="Dirección")
        self.tree.heading("tarifa", text="Tarifa Pedido")
        self.tree.heading("codigoUnico", text="Código Único")
        self.tree.heading("estadoActual", text="Estado Actual")

        for col in ("fechaCreacion", "fechaPlazo", "usuario", "direccion", "tarifa", "codigoUnico", "estadoActual"):
            self.tree.column(col, width=120, anchor=tk.W)
        # Eventos en la tabla.
        self.tree.bind("<Double-1>", self.modificar_estado) # Doble clic para modificar el estado.
        self.tree.bind("<Button-3>", self.copiar_codigo) # Clic derecho para copiar el código único.
        # Carga inicial de datos.
        self.cargar_usuarios()
        self.cargar_pedidos()

    def copiar_codigo(self, event):
        # Copia el código único seleccionado al portapapeles.
        item = self.tree.identify_row(event.y)
        if item:
            valores = self.tree.item(item, "values")
            codigo_unico = valores[5]  # La columna del código único
            self.ventana.clipboard_clear()
            self.ventana.clipboard_append(codigo_unico)
            self.ventana.update()
            messagebox.showinfo("Copiar Código", f"Código único '{codigo_unico}' copiado al portapapeles.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un código único válido.")

    def modificar_estado(self, event):
        # Abre una ventana para modificar el estado del pedido seleccionado.
        item = self.tree.selection()
        if not item:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un pedido para modificar el estado.")
            return

        item = item[0]
        valores = self.tree.item(item, "values")
        estado_actual = valores[6]
        codigo = valores[5]

        ventana_estado = tk.Toplevel(self.ventana)
        ventana_estado.title("Modificar Estado")
        ventana_estado.geometry("300x200")
        ventana_estado.transient(self.ventana)
        ventana_estado.grab_set()

        tk.Label(ventana_estado, text="Estado actual:", font=("Arial", 12)).pack(pady=10)
        tk.Label(ventana_estado, text=estado_actual, font=("Arial", 10, "bold")).pack(pady=5)
        tk.Label(ventana_estado, text="Seleccionar nuevo estado:", font=("Arial", 12)).pack(pady=10)

        estados_posibles = ["Recepcionado", "Procesado", "En despacho", "Listo para el retiro"]
        combo_estado = ttk.Combobox(ventana_estado, values=estados_posibles, state="readonly")
        combo_estado.pack(pady=5)
        combo_estado.set(estado_actual)

        def guardar_estado():
            nuevo_estado = combo_estado.get()
            if not nuevo_estado:
                messagebox.showerror("Error", "Debes seleccionar un estado.")
                return

            self.tree.set(item, column="estadoActual", value=nuevo_estado)

            for pedido in self.pedidos:
                if pedido["codigoUnico"] == codigo:
                    pedido["estadoActual"] = nuevo_estado
                    pedido["estadoHistorial"].append([str(datetime.now()), nuevo_estado, codigo])
                    break

            self.guardar_cambios()
            ventana_estado.destroy()

        tk.Button(ventana_estado, text="Guardar", command=guardar_estado, bg="blue", fg="white").pack(pady=20)

    def guardar_cambios(self):
        # Guarda los cambios realizados en los pedidos.
        archivo_json = "pedidostest.json"
        try:
            with open(archivo_json, "w", encoding="utf-8") as file:
                json.dump(self.pedidos, file, indent=4, ensure_ascii=False)
            messagebox.showinfo("Éxito", "Los cambios se han guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los cambios: {e}")

    def cargar_usuarios(self):
        # Carga los usuarios desde un archivo JSON.
        archivo_usuarios = "usuariostest.json"
        try:
            with open(archivo_usuarios, "r", encoding="utf-8") as file:
                datos_usuarios = json.load(file)
                self.usuarios = {usuario["codigoUnico"]: usuario["nombre"] for usuario in datos_usuarios}
        except FileNotFoundError:
            messagebox.showerror("Error", f"El archivo {archivo_usuarios} no fue encontrado")
        except json.JSONDecodeError:
            messagebox.showerror("Error", f"El archivo {archivo_usuarios} no contiene un formato JSON válido.")

    def cargar_pedidos(self):
        # Carga los pedidos desde un archivo JSON.
        archivo_json = "pedidostest.json"
        try:
            with open(archivo_json, "r", encoding="utf-8") as file:
                self.pedidos = json.load(file)
                for pedido in self.pedidos:
                    usuario_id = str(pedido.get("usuario", ""))
                    pedido["usuario_nombre"] = self.usuarios.get(usuario_id, "Desconocido")
                self.actualizarTabla(self.pedidos)
        except FileNotFoundError:
            messagebox.showerror("Error", f"El archivo {archivo_json} no fue encontrado")
        except json.JSONDecodeError:
            messagebox.showerror("Error", f"El archivo {archivo_json} no contiene un formato JSON válido.")

    def actualizarTabla(self, pedidos):
        # Actualiza la tabla con los pedidos.
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar los nuevos pedidos con el nombre de usuario en la tabla
        for pedido in pedidos:
            self.tree.insert("", tk.END, values=(
                pedido["fechaCreacion"], 
                pedido["fechaPlazo"], 
                pedido["usuario"],  # Aquí ya se asigna el nombre del usuario
                pedido["direccion"], 
                pedido["tarifa"], 
                pedido["codigoUnico"], 
                pedido["estadoActual"]
            ))

    def filtrar_pedidos(self):
        # Filtra los pedidos según el código único o ID de usuario.
        codigo_filtro = self.entry_codigo.get().strip().lower()
        usuario_filtro = self.entry_usuario.get().strip().lower()

        pedidos_filtrados = [
            pedido for pedido in self.pedidos
            if (not codigo_filtro or codigo_filtro in pedido["codigoUnico"].lower()) and
               (not usuario_filtro or usuario_filtro in pedido["usuario"].lower())
        ]
        self.actualizarTabla(pedidos_filtrados)

class BuscarUsuariosGerente(creacion_ventana):
    """
    Ventana para que el gerente pueda buscar usuarios registrados en la plataforma.
    Permite filtrar usuarios por nombre, correo y tipo de cuenta.
    """
    def __init__(self, usuario):
        super().__init__(titulo="Lavalimpia-Gerente (Búsqueda de Usuarios)", icono="recursosImagenes/fondoL.ico")
        self.usuario = usuario
        self.usuarios = []  # Lista para almacenar los usuarios cargados
        self.interfaz()

    def volver(self):
        self.cambiarVentana(ventana_gerente, self.usuario)

    def interfaz(self):
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        self.crear_etiqueta(
            texto="Consulta de Usuarios por Nombre, Correo o Tipo de Cuenta",
            fuente=("Britannic Bold"), tamano=20, x=40, y=30, bg="#188999"
        )
        self.crear_boton("Volver", font=("Arial", 10), x=840, y=8, command=self.volver, width=100, height=25, bd=0, cursor="hand2", bg="white")
        # Marco para los filtros de búsqueda
        frame_filtros = tk.Frame(self.ventana, bg="#188999")
        frame_filtros.place(x=10, y=60, width=880, height=50)
        # Campos para filtrar por nombre, correo y tipo de cuenta
        tk.Label(frame_filtros, text="Nombre:", font=("Arial", 12), bg="#188999", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nombre = tk.Entry(frame_filtros)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_filtros, text="Correo:", font=("Arial", 12), bg="#188999", fg="white").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.entry_correo = tk.Entry(frame_filtros)
        self.entry_correo.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_filtros, text="Tipo de Cuenta:", font=("Arial", 12), bg="#188999", fg="white").grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)
        
        # Cambio a un Combobox con opciones de tipo de cuenta
        self.entry_tipo_cuenta = ttk.Combobox(frame_filtros, values=["", "cliente", "operador", "recaudador", "gerente"], state="readonly")
        self.entry_tipo_cuenta.grid(row=0, column=5, padx=5, pady=5)
        # Botón para ejecutar la búsqueda
        tk.Button(frame_filtros, text="Buscar", command=self.filtrar_usuarios, bg="blue", fg="white", font=("Arial", 12)).grid(row=0, column=6, padx=10, pady=5)

        # Tabla para mostrar usuarios
        self.tree = ttk.Treeview(self.ventana, columns=("nombre", "correo", "tipoUsuario", "fechaCreacion", "codigoUnico"), show="headings")
        self.tree.place(x=10, y=120, width=880, height=400)
        scrollbar_vertical = ttk.Scrollbar(self.ventana, orient="vertical", command=self.tree.yview)
        scrollbar_vertical.place(x=890, y=120, height=400)
        self.tree.configure(yscrollcommand=scrollbar_vertical.set)

        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("correo", text="Correo")
        self.tree.heading("tipoUsuario", text="Tipo de Usuario")
        self.tree.heading("fechaCreacion", text="Fecha de Creación")
        self.tree.heading("codigoUnico", text="ID")

        for col in ("nombre", "correo", "tipoUsuario", "fechaCreacion", "codigoUnico"):
            self.tree.column(col, width=160, anchor=tk.W)
        # Vincula el clic derecho para copiar el código único
        self.tree.bind("<Button-3>", self.copiar_codigo)
        # Carga inicial de los usuarios
        self.cargar_usuarios()
        
    def copiar_codigo(self, event):
        """
        Copia el código único del usuario seleccionado al portapapeles.
        """
        item = self.tree.identify_row(event.y)
        if item:
            valores = self.tree.item(item, "values")
            codigo_unico = valores[4]  # La columna del código único
            self.ventana.clipboard_clear()
            self.ventana.clipboard_append(codigo_unico)
            self.ventana.update()
            messagebox.showinfo("Copiar Código", f"Código único '{codigo_unico}' copiado al portapapeles.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un código único válido.")

    def cargar_usuarios(self):
        """
        Carga los usuarios desde el archivo JSON y los muestra en la tabla.
        """
        archivo_usuarios = "usuariostest.json"
        try:
            with open(archivo_usuarios, "r", encoding="utf-8") as file:
                self.usuarios = json.load(file)
            self.actualizarTabla(self.usuarios)
        except FileNotFoundError:
            messagebox.showerror("Error", f"El archivo {archivo_usuarios} no fue encontrado")
        except json.JSONDecodeError:
            messagebox.showerror("Error", f"El archivo {archivo_usuarios} no contiene un formato JSON válido.")

    def actualizarTabla(self, usuarios):
        """
        Actualiza los datos mostrados en la tabla.
        """
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Limpia las filas actuales
        for usuario in usuarios:
            # Inserta los nuevos datos
            self.tree.insert("", tk.END, values=(
                usuario["nombre"],
                usuario["correo"],
                usuario["tipoUsuario"],
                usuario["fechaCreacion"],
                usuario["codigoUnico"]
            ))

    def filtrar_usuarios(self):
        """
        Filtra los usuarios según los valores ingresados en los campos de búsqueda.
        """
        nombre_filtro = self.entry_nombre.get().strip().lower() #.strip(): Elimina cualquier espacio en blanco al principio y al final de la cadena obtenida. y lower convierte todo a minúsculas
        correo_filtro = self.entry_correo.get().strip().lower()
        tipo_cuenta_filtro = self.entry_tipo_cuenta.get().strip().lower()
        # Aplica los filtros
        usuarios_filtrados = [
            usuario for usuario in self.usuarios
            if (not nombre_filtro or nombre_filtro in usuario["nombre"].lower()) and
               (not correo_filtro or correo_filtro in usuario["correo"].lower()) and
               (not tipo_cuenta_filtro or tipo_cuenta_filtro == usuario["tipoUsuario"].lower())
        ]
        self.actualizarTabla(usuarios_filtrados)
#Aquí termina la ventana del gerente.

#5) Aquí empieza la ventana del operador
class ventana_operador(creacion_ventana):
    def __init__(self,usuario):
        super().__init__(titulo="Lavalimpia-Operador",icono="recursosImagenes/fondoL.ico")
        self.usuario = usuario  # Usuario autenticado
        self.archivo_pedidos="pedidostest.json"
        self.interfaz()
        
    def interfaz(self):
        self.crear_etiqueta(f"¡Bienvenido, {self.usuario['nombre']}!",fuente="Britannic Bold",tamano=28,x=40,y=30,bg="#188999")
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        self.crear_boton(text=" Cerrar sesión  ",font=("Arial", 10),x=840,y=8, command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25, bg= "red", fg="white")
        
        self.crear_boton(text="Ingresar pedido",font=("Arial",20),x=150,y=250,command=lambda: self.cambiarVentana(IngresoPedido_operador, self.usuario),width=260, height=40)
        self.crear_boton(text="Consultar pedido",font=("Arial",20),x=450,y=250,command=lambda: self.cambiarVentana(ConsultaPedido_operador,self.usuario),width=260, height=40)
        
class IngresoPedido_operador(creacion_ventana):
    def __init__(self, usuario):
        if not usuario:
            raise ValueError("El usuario no puede ser None")
        super().__init__(titulo="Lavalimpia-Operador (Ingreso de pedido)", icono="recursosImagenes/fondoL.ico")
        self.interfaz()
        self.archivo_pedidos = "pedidostest.json"
        self.archivo_usuarios = "usuariostest.json"
        self.usuario = usuario
    def interfaz(self):
        self.crear_etiqueta(texto="Creador de pedidos", fuente=("Britannic Bold"), tamano=28, x=40, y=30, bg="#188999")
        self.crear_boton("Volver", font=("Arial", 10), x=840, y=8, command=self.volver, width=100, height=25, bd=0, cursor="hand2", bg="white")

        self.crear_etiqueta(texto="Nombre del usuario", fuente=("Arial"), tamano=12, x=120, y=120, bg="#188999", fg="#ffffff")
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
    def volver(self):
        # Al hacer clic en Volver, se pasa el usuario correctamente a la ventana_operador
        self.cambiarVentana(ventana_operador, self.usuario)
    def guardar_pedido(self):
        # Obtener la fecha y hora actual
        fecha_actual = datetime.now()
        fecha_creacion = fecha_actual.strftime("%Y-%m-%d %H:%M") #convierte la fecha y hora actual en una cadena de texto con el formato AAAA-MM-DD HH:MM

        # Calcular la fecha de entrega sumando 2 días
        fecha_entrega = (fecha_actual + timedelta(days=2)).strftime("%Y-%m-%d %H:%M") #esta línea de código calcula una fecha que es 2 días posterior a la fecha y hora actuales y la formatea en una cadena de texto en el formato AAAA-MM-DD HH:MM

        # Obtener los datos de los campos de entrada
        nombre_usuario = self.entry_usuario.get().strip() #strip() se utiliza para eliminar cualquier espacio en blanco adicional al principio y al final de la entrada de texto.
        direccion = self.entry_direccion.get().strip()
        tarifa = self.entry_tarifa.get().strip()

        # Validaciones
        if not nombre_usuario:
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
            if tarifa_float <= 0:
                messagebox.showwarning("Valor inválido", "La tarifa debe ser un valor numérico positivo.")
                return
        except ValueError:
            messagebox.showwarning("Formato incorrecto", "La tarifa debe ser un valor numérico válido.")
            return

        # Leer archivo de usuarios
        try:
            with open(self.archivo_usuarios, "r", encoding="utf-8") as archivo_usuarios:
                usuarios = json.load(archivo_usuarios)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "No se encontró el archivo de usuarios o está vacío.")
            return

        # Comprobar si el código único del usuario existe
        usuario_existente = next((u for u in usuarios if u.get("nombre") == nombre_usuario), None)
        if not usuario_existente:
            messagebox.showwarning("Usuario no encontrado", "El código único ingresado no corresponde a ningún usuario registrado.")
            return
        # Obtener el ID del usuario
        id_usuario = usuario_existente.get("codigoUnico")
        # Generar un código único para el pedido
        codigo_unico_pedido = self.generar_CodigoUnico()

        # Crear un diccionario con los datos
        datos_pedido = {
        "codigoUnico": codigo_unico_pedido,
        "direccion": direccion,
        "usuario": id_usuario,  # ID del usuario
        "usuario_nombre": nombre_usuario,  # Nombre del usuario
        "tarifa": tarifa_float,
        "fechaCreacion": fecha_creacion,
        "estadoActual": "Recepcionado",
        "estadoHistorial": [
            [fecha_creacion, "Recepcionado", codigo_unico_pedido]
        ],
        "fechaPlazo": fecha_entrega
    }

        # Leer archivo de pedidos
        try:
            with open(self.archivo_pedidos, "r", encoding="utf-8") as archivo_pedidos:
                pedidos = json.load(archivo_pedidos)
        except (FileNotFoundError, json.JSONDecodeError):
            pedidos = []

        # Añadir el nuevo pedido
        pedidos.append(datos_pedido)

        # Guardar el archivo de pedidos actualizado
        with open(self.archivo_pedidos, "w", encoding="utf-8") as archivo_pedidos:
            json.dump(pedidos, archivo_pedidos, indent=4, ensure_ascii=False)

        # Actualizar el archivo de usuarios
        usuario_existente.setdefault("pedidos", []).append(codigo_unico_pedido)
        with open(self.archivo_usuarios, "w", encoding="utf-8") as archivo_usuarios:
            json.dump(usuarios, archivo_usuarios, indent=4, ensure_ascii=False)

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Pedido guardado exitosamente.")

        # Limpiar los campos después de guardar
        self.entry_usuario.delete(0, "end")
        self.entry_direccion.delete(0, "end")
        self.entry_tarifa.delete(0, "end")

    def generar_CodigoUnico(self):
        """
        Genera un código único alfanumérico de 8 caracteres que no se repite entre los pedidos existentes.

        Este método asegura que cada código generado sea único al verificarlo contra los códigos 
        ya registrados en un archivo JSON. Si el archivo no existe o tiene un formato inválido, 
        se asume que no hay códigos existentes.

        :return: Un código único de 8 caracteres.
        """
        try:
            # Intenta abrir el archivo de pedidos y cargar los códigos existentes
            with open(self.archivo_pedidos, "r", encoding="utf-8") as archivo_pedidos:
                pedidos = json.load(archivo_pedidos)
                # Extrae los códigos únicos existentes en un conjunto para una búsqueda eficiente
                codigos_existentes = {pedido["codigoUnico"] for pedido in pedidos}
        except (FileNotFoundError, json.JSONDecodeError):
            # Si el archivo no existe o tiene errores de formato, inicializa un conjunto vacío
            codigos_existentes = set()
        # Genera códigos hasta encontrar uno que no esté en el conjunto de códigos existentes
        while True:
            # Genera un código aleatorio de 8 caracteres alfanuméricos, une los caracteres seleccionados en una sola cadena de texto.
            codigo_unico = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) #string.ascii_letters + string.digits, que incluye todas las letras del alfabeto (mayúsculas y minúsculas) y todos los dígitos del 0 al 9.
            # Verifica si el código es único
            if codigo_unico not in codigos_existentes:
                return codigo_unico
              
class ConsultaPedido_operador(creacion_ventana):
    def __init__(self,usuario):
        super().__init__(titulo="Lavalimpia-Operador (consulta pedidos)", icono="recursosImagenes/fondoL.ico")
        self.interfaz()
        self.usuario = usuario
    def interfaz(self):
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        # Etiqueta principal
        self.crear_etiqueta(texto="Consulta de Pedidos por código único", fuente=("Britannic Bold"), tamano=20, x=40, y=30, bg="#188999")
        self.crear_boton("Volver", font=("Arial", 10), x=840, y=8, command=self.volver, width=100, height=25, bd=0, cursor="hand2", bg="white")

        # Etiqueta y entrada para el nombre del usuario
        self.crear_etiqueta(texto="Código único:", fuente=("Arial"), tamano=12, x=40, y=100, bg="#188999")
        self.entry_usuario = self.crear_entry(x=200, y=100, width=250, height=30)

        # Botón para buscar pedidos
        self.crear_boton(text="Buscar Pedidos", font=("Arial", 14), x=470, y=100,
                         command=lambda: self.buscar_pedidos(self.entry_usuario.get()), width=150, height=30)
    def volver(self):
        # Al hacer clic en Volver, se pasa el usuario correctamente a la ventana_operador
        self.cambiarVentana(ventana_operador, self.usuario)
    def buscar_pedidos(self, codigo_unico):
        """
        Busca pedidos en un archivo JSON según el código único proporcionado.
        """
        valor = codigo_unico.strip()  # Eliminar espacios en blanco innecesarios

        # Validar si el campo está vacío
        if not valor:
            messagebox.showwarning("Advertencia", "No se ingresó ningún código único. Por favor, ingrese uno.")
            return

        archivo_usuarios = "usuariostest.json"
        archivo_pedidos = "pedidostest.json"

        try:
            # Leer el archivo JSON de pedidos
            with open(archivo_pedidos, 'r', encoding='utf-8') as file_pedidos:
                pedidos = json.load(file_pedidos)

            # Leer el archivo JSON de usuarios
            with open(archivo_usuarios, 'r', encoding='utf-8') as file_usuarios:
                usuarios = json.load(file_usuarios)

            # Crear un diccionario para mapear código único de usuario a su nombre
            usuarios_dict = {u["codigoUnico"]: u["nombre"] for u in usuarios}

            # Buscar el pedido por su código único
            pedido_encontrado = next((pedido for pedido in pedidos if pedido.get("codigoUnico") == valor), None)

            if pedido_encontrado:
                # Buscar el nombre del usuario asociado al pedido
                usuario_id = pedido_encontrado.get("usuario", None)
                nombre_usuario = usuarios_dict.get(usuario_id, "Usuario desconocido")
                self.mostrar_info_pedido(pedido_encontrado, nombre_usuario)
            else:
                 messagebox.showinfo("Sin resultados", f"No se encontró ningún pedido con el código único '{codigo_unico}'.")

        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Archivo no encontrado: {str(e)}")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Uno de los archivos no contiene un formato JSON válido.")


    def mostrar_info_pedido(self, pedido,nombre_usuario):
        """
        Muestra la información de un pedido en una nueva ventana.
        Diccionario con los datos del pedido.
        """
        info_pedido = (
            f"Código Único: {pedido['codigoUnico']}\n"
            f"Dirección: {pedido['direccion']}\n"
            f"Usuario : {nombre_usuario}\n"
            f"Tarifa: {pedido['tarifa']}\n"
            f"Fecha Plazo: {pedido['fechaPlazo']}\n"
            f"Estado Actual: {pedido['estadoActual']}\n"
        )
        # Crear una ventana emergente para mostrar la información del pedido
        messagebox.showinfo("Información del Pedido", info_pedido)
#Aquí termina la ventana del operador.

#6) Aquí empieza la ventana del recaudador
class ventana_EmpleadoRecaudador(creacion_ventana):
    """
    Clase que representa la interfaz y funcionalidad para los empleados recaudadores en el sistema Lavalimpia.
    Permite realizar tareas como gestionar pedidos, procesar pagos y visualizar información relevante.
    
    Hereda de la clase `creacion_ventana`, que se utiliza para la creación de ventanas y elementos visuales.
    """
    def __init__(self, usuario):
        super().__init__(titulo="Lavalimpia-Recaudador", icono="recursosImagenes/fondoL.ico")
        self.usuario = usuario  # Usuario autenticado
        self.archivo_pedidos = "pedidostest.json"
        self.archivo_usuarios="usuariostest.json"
        self.interfaz()
        
    def interfaz(self):
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)

        self.crear_etiqueta(f"¡Bienvenido, {self.usuario['nombre']}!", fuente="Britannic Bold", tamano=28, x=40, y=30, bg="#188999")
        self.agregar_logo("recursosImagenes/Logo2.png", x=65, y=280)
        self.crear_boton(text=" Cerrar sesión ", font=("Arial", 10), x=840, y=8, command=lambda: self.cambiarVentana(ventanaPrincipal), width=100, height=25, bg="red", fg="white")
        
        self.crear_etiqueta("Para ver las entregas a domicilio cliquee aquí:", fuente="Arial", tamano=15, x=40, y=100, bg="#188999")
        self.boton_pedidos = self.crear_boton(text="Pedidos", font=("Arial", 18), x=40, y=150, command=lambda: self.cambiarVentana(pedidosVer, self.usuario),  width=250,height=30,)
        
        self.crear_etiqueta("Para proceder con el pago de la entrega cliquee aquí:", fuente="Arial", tamano=15, x=40, y=200, bg="#188999")
        self.botonPago = self.crear_boton(text="Pagar pedidos", font=("Arial", 18), x=40, y=250, command=self.pagar_pedidos,  width=250,height=30,)
    
    def cargar_pedidos(self, ruta_archivo):
        """
        Carga los datos de pedidos desde un archivo JSON.

        :param ruta_archivo: Ruta del archivo JSON.
        :return: Lista de pedidos.
        """
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        return datos

    def cargar_usuarios(self, ruta_archivo):
        """
        Carga los datos de usuarios desde un archivo JSON.

        :param ruta_archivo: Ruta del archivo JSON.
        :return: Lista de usuarios.
        """
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        return datos

    def mapear_usuarios_pedidos(self, usuarios):
        """
        Crea un diccionario que relaciona códigos únicos de pedidos con nombres de usuarios.

        :param usuarios: Lista de usuarios.
        :return: Diccionario con códigos únicos como claves y nombres de usuarios como valores.
        """
        usuario_dict = {}
        for usuario in usuarios:
            for pedido in usuario['pedidos']:
                usuario_dict[pedido] = usuario['nombre']
        return usuario_dict

    def encontrar_pedido(self, pedidos, codigo_unico):
        """
        Busca un pedido por su código único.

        :param pedidos: Lista de pedidos.
        :param codigo_unico: Código único a buscar.
        :return: El pedido encontrado o None si no existe.
        """
        for pedido in pedidos:
            if pedido['codigoUnico'] == codigo_unico:
                return pedido
        return None

    def actualizar_estado_pedido(self, pedidos, codigo_unico, ruta_archivo):
        """
        Actualiza el estado de un pedido a 'Entregado' y guarda los cambios en el archivo.

        :param pedidos: Lista de pedidos.
        :param codigo_unico: Código único del pedido.
        :param ruta_archivo: Ruta del archivo JSON.
        """
        for pedido in pedidos:
            if pedido['codigoUnico'] == codigo_unico:
                pedido['estadoActual'] = 'Entregado'
                pedido['estadoHistorial'].append([str(datetime.now()), 'Entregado', codigo_unico])
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(pedidos, archivo, ensure_ascii=False, indent=4)
        messagebox.showinfo("Éxito", f"El pedido {codigo_unico} ha sido entregado.")

    def mostrar_detalles(self, codigo_entry, tarifa_var, usuario_var, confirmar_pago_button):
        """
        Muestra los detalles de un pedido en función del código ingresado.

        :param codigo_entry: Entrada del código único.
        :param tarifa_var: Variable para mostrar la tarifa.
        :param usuario_var: Variable para mostrar el usuario.
        :param confirmar_pago_button: Botón para confirmar el pago.
        """
        codigo_unico = codigo_entry.get()
        pedido = self.encontrar_pedido(self.todos_pedidos, codigo_unico)
        if pedido and pedido['estadoActual'] == 'Listo para el retiro':
            usuario_nombre = self.usuario_dict.get(pedido['codigoUnico'], 'Desconocido')
            tarifa_var.set(f"Tarifa: {pedido['tarifa']} CLP")
            usuario_var.set(f"Usuario: {usuario_nombre}")
            confirmar_pago_button.config(state=tk.NORMAL) #(tk.NORMAL) puede ser interactuado por el usuario.
        else:
            tarifa_var.set("Tarifa: N/A")
            usuario_var.set("Usuario: N/A")
            confirmar_pago_button.config(state=tk.DISABLED)
            messagebox.showerror("Error", "Código único no válido o el pedido no está listo para el retiro.")

    def procesar_pago(self, codigo_entry, tarifa_var, usuario_var, confirmar_pago_button):
        """
        Procesa el pago de un pedido y actualiza su estado.

        :param codigo_entry: Entrada del código único.
        :param tarifa_var: Variable para mostrar la tarifa.
        :param usuario_var: Variable para mostrar el usuario.
        :param confirmar_pago_button: Botón para confirmar el pago.
        """
        codigo_unico = codigo_entry.get()
        self.actualizar_estado_pedido(self.todos_pedidos, codigo_unico, self.archivo_pedidos)
        tarifa_var.set("Tarifa: N/A")
        usuario_var.set("Usuario: N/A")
        codigo_entry.delete(0, tk.END)
        confirmar_pago_button.config(state=tk.DISABLED) #se utiliza para deshabilitar el botón confirmar_pago_button

    def pagar_pedidos(self):
        """
        Crea una ventana emergente para procesar el pago de pedidos.
        """
        pago = tk.Toplevel(self.ventana)
        pago.title("Pago de Pedidos")
        pago.geometry("400x300")
        pago.resizable(False, False)

        # Contenedor para alinear todo a la izquierda
        frame = tk.Frame(pago)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Etiqueta del código único
        tk.Label(frame, text="Código Único", anchor="w", justify="left").pack(fill=tk.X, pady=5)

        # Entrada para el código único
        codigo_entry = tk.Entry(frame)
        codigo_entry.pack(fill=tk.X, pady=5)

        # Etiquetas para mostrar detalles (tarifa y usuario)
        tarifa_var = tk.StringVar(value="Tarifa: N/A")
        usuario_var = tk.StringVar(value="Usuario: N/A")
    
        tk.Label(frame, textvariable=tarifa_var, anchor="w", justify="left").pack(fill=tk.X, pady=5)
        tk.Label(frame, textvariable=usuario_var, anchor="w", justify="left").pack(fill=tk.X, pady=5) #el parámetro anchor="w" se utiliza para controlar cómo se alinea el texto dentro del widget. #justify="left" alinea el texto a la izquierda en líneas múltiples.

        # Botón para confirmar pago
        confirmar_pago_button = tk.Button(
            frame,
            text="Confirmar Pago",
            state=tk.DISABLED,
            command=lambda: self.procesar_pago(codigo_entry, tarifa_var, usuario_var, confirmar_pago_button)
        )
        confirmar_pago_button.pack(fill=tk.X, pady=10) #fill=tk.X: Esto indica que el widget confirmar_pago_button debe expandirse horizontalmente para llenar todo el espacio disponible en su contenedor.

        # Botón para mostrar detalles
        tk.Button(
            frame,
            text="Mostrar Detalles",
            command=lambda: self.mostrar_detalles(codigo_entry, tarifa_var, usuario_var, confirmar_pago_button)
        ).pack(fill=tk.X, pady=5)

        # Cargar los pedidos y usuarios
        self.todos_pedidos = self.cargar_pedidos(self.archivo_pedidos)
        self.todos_usuarios = self.cargar_usuarios(self.archivo_usuarios)
        self.usuario_dict = self.mapear_usuarios_pedidos(self.todos_usuarios)

        # Configuración de la ventana emergente
        pago.transient(self.ventana)
        pago.grab_set()
        self.ventana.wait_window(pago)

class pedidosVer(creacion_ventana):
    '''
    La clase genera una interfaz gráfica que muestra los pedidos listos para ser entregados. 
    Además, incluye funcionalidades para copiar códigos únicos y filtrar los pedidos.
    '''
    def __init__(self, usuario):
        super().__init__(titulo="Lavalimpia-Recaudador (Pedidos a entregar)", usuario_actual=usuario, ancho=950, alto=550, color_fondo="#188999", icono="recursosImagenes/fondoL.ico")
        self.usuario = usuario  # Usuario autenticado
        self.archivo_pedidos = "pedidostest.json"
        self.archivo_usuarios = "usuariostest.json"  # Añadido para cargar usuarios
        self.interfaz()

    def volver(self):
        self.cambiarVentana(ventana_EmpleadoRecaudador, self.usuario)
    
    def interfaz(self):
        self.crear_etiqueta("¡Pedidos a entregar!", fuente="Britannic Bold", tamano=28, x=40, y=30, bg="#188999")
        self.crear_boton("Volver", font=("Arial", 10), x=840, y=8, command=self.volver, width=100, height=25, bd=0, cursor="hand2", bg="white")
        
        # Configuración de la tabla con el mismo fondo
        frame_tabla = tk.Frame(self.ventana, bg="#188999")
        frame_tabla.place(x=10, y=120, width=880, height=400)
        
        tabla = ttk.Treeview(frame_tabla, columns=('ID', 'Dirección', 'Usuario', 'Tarifa', 'Fecha Plazo'), show='headings')
        tabla.heading('ID', text='ID')
        tabla.heading('Dirección', text='Dirección')
        tabla.heading('Usuario', text='Usuario')
        tabla.heading('Tarifa', text='Tarifa')
        tabla.heading('Fecha Plazo', text='Fecha Plazo')
        
        # Ajustar el ancho de las columnas
        tabla.column('ID', width=100)
        tabla.column('Dirección', width=200)
        tabla.column('Usuario', width=150)
        tabla.column('Tarifa', width=100)
        tabla.column('Fecha Plazo', width=150)
        
        tabla.pack(side='left', fill='both', expand=True)
        
        scrollbar_vertical = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
        scrollbar_vertical.pack(side='right', fill='y')
        tabla.configure(yscrollcommand=scrollbar_vertical.set)

        # Menú contextual para copiar el código único
        menu = Menu(self.ventana, tearoff=0)
        menu.add_command(label="Copiar Código Único", command=lambda: copiar_codigo(None))
        
        # Función para mostrar el menú contextual
        def mostrar_menu(event):
            menu.post(event.x_root, event.y_root) #(.bind) posiciona y muestra el menú en la ubicación exacta del clic derecho del ratón, permitiendo que el usuario vea y seleccione opciones del menú contextual justo donde hizo clic.
            
        tabla.bind("<Button-3>", mostrar_menu)  # Vincula el clic derecho con el menú contextual
        
        # Función para cargar los pedidos desde un archivo JSON
        def cargar_pedidos(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
            return datos

        # Función para cargar los usuarios desde un archivo JSON
        def cargar_usuarios(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo: #Al usar 'utf-8', aseguras que los caracteres especiales y acentuados en el archivo se lean correctamente, evitando problemas de codificación 
                                                                       #abre el archivo en modo lectura ('r') sirve para indicar que el archivo se debe abrir en modo lectura.
                '''
                'r': Lectura - Abre un archivo para leerlo. El archivo debe existir.

                'w': Escritura - Abre un archivo para escribir. Si el archivo existe, su contenido será borrado. Si no existe, se crea uno nuevo.

                'a': Añadir - Abre un archivo para escribir en él sin borrar su contenido. Si el archivo no existe, se crea uno nuevo.

                'b': Binario - Abre un archivo en modo binario. Se usa junto con otros modos, por ejemplo, 'rb' para leer en binario o 'wb' para escribir en binario.
                '''
                datos = json.load(archivo)
            return datos
        
        # Función para filtrar los pedidos con el estado "Listo para el retiro"
        def filtrar_pedidos(pedidos):
            return [pedido for pedido in pedidos if pedido['estadoActual'] == 'Listo para el retiro' and pedido['estadoActual'] != 'Entregado']
        
        # Función para mapear los nombres de usuario a los pedidos
        def mapear_usuarios_pedidos(usuarios):
            usuario_dict = {}
            for usuario in usuarios:
                for pedido in usuario['pedidos']:
                    usuario_dict[pedido] = usuario['nombre']
            return usuario_dict
        
        # Función para actualizar la tabla con los pedidos filtrados
        def actualizar_tabla(tabla, pedidos, usuario_dict):
            for pedido in pedidos:
                usuario_nombre = usuario_dict.get(pedido['codigoUnico'], 'Desconocido')
                tabla.insert('', 'end', values=(pedido['codigoUnico'], pedido['direccion'], usuario_nombre, pedido['tarifa'], pedido['fechaCreacion'], pedido['fechaPlazo']))
        
        # Función para copiar el código único al portapapeles
        def copiar_codigo(event): #se establece una función para vincularla a un evento al cliquear un boton
            item = tabla.selection()[0] # obtiene el identificador del primer elemento seleccionado en la tabla.
            codigo_unico = tabla.item(item, 'values')[0] #extrae el primer valor asociado al elemento seleccionado. Este valor es lo que se copiará al portapapeles.
            self.ventana.clipboard_clear() #limpia el contenido actual del portapapeles.
            self.ventana.clipboard_append(codigo_unico) #añade el valor codigo_unico al portapapeles.
            self.ventana.update()  # Asegura que el portapapeles se actualice correctamente
            print(f"Código {codigo_unico} copiado al portapapeles")
        
        # Cargar y mostrar los pedidos
        todos_pedidos = cargar_pedidos(self.archivo_pedidos)
        todos_usuarios = cargar_usuarios(self.archivo_usuarios)
        usuario_dict = mapear_usuarios_pedidos(todos_usuarios)
        pedidos_filtrados = filtrar_pedidos(todos_pedidos)
        actualizar_tabla(tabla, pedidos_filtrados, usuario_dict)
#Aquí termina la ventana del recaudador.

"""
NOTA: Los usuarios y pedidos se manejan como diccionarios en lugar de instancias de clases.
Esto se decidió para facilitar la carga y manipulación de datos desde/para archivos JSON.
Los diccionarios permiten una implementación más sencilla y directa, adecuada para el tamaño y alcance del proyecto.
"""


###### FIN ########
print("Hola mundo")

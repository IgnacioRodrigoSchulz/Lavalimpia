import tkinter as tk #sirve para importar tkinter para poder  crear interfaces gráficas 
from tkinter import messagebox,ttk  # Importa herramientas específicas: messagebox para mensajes emergentes y ttk para widgets avanzados.
import funciones  # Importa un módulo externo llamado `funciones`

class creacion_ventana: #Esta clase es el origen de todas las otras ventanas de la aplicación, donde se establecen configuraciones en común
    def __init__(self,titulo, ancho=950, alto=550, color_fondo="#188999", icono=None, redimensionable=(False, False)): #__init__ es el método se llama automáticamente cuando se crea un objeto de una clase. (inicializa los atributos deacuerdo al objeto)
        self.ventana=tk.Tk() # crea la ventana principal
        self.ventana.geometry(f"{ancho}x{alto}") # defina las dimensiones de la ventana
        self.ventana.title(titulo) # establece el título que tendrá la ventana
        self.ventana.configure(bg=color_fondo) #cambia el color del fondo
        self.ventana.resizable(*redimensionable) #define si la ventana puede cambiar de tamaño
        if icono:
            self.ventana.iconbitmap(icono) # esto asigna un ícono a la venta si se le proporcionace uno
        
    def mostrarVentana(self):
        self.ventana.mainloop() # ejecuta el bucle principal para que la ventana se pueda mostrar.
    
    def cambiarVentana(self,nuevaVentana):
        self.ventana.destroy() #cierra la ventana actual
        nuevaVentana().mostrarVentana() # abre la nueva ventana 
    
    def agregar_logo(self,archivo,x,y):
        imagen = tk.PhotoImage(file=archivo) #carga la imagen desde un archivo proporcianado
        logo = tk.Label( self.ventana,image=imagen, bd=0) #crea una etiquetra para mostrar la imagen.
        logo.image = imagen  # Necesario para mantener la referencia a la imagen y así evitar que se elimine de la memoria 
        logo.place(x=x, y=y) #posiciona la imagen
    
    def crear_etiqueta(self,texto, fuente, tamano, x, y, **kwargs): # el parámetro **kwargs permite pasar un número de variables de argumentos con nombre a una función o método (flexibilidad y prevención de errores por argumentos no esperados)
     etiqueta = tk.Label(self.ventana, text=texto, font=(fuente, tamano), **kwargs) #crea una etiqueta con el texto y su fuente (cualquier fuente que se le quiera poner)
     width = kwargs.get('width', None) #obtiene el ancho si se le da uno
     height = kwargs.get('height', None) # obtiene el alto si se le da uno
    
     if width and height:
      etiqueta.place(x=x, y=y, width=width, height=height) #posiciona con ancho y alto específico
     else:
      etiqueta.place(x=x, y=y)
    
    def crear_entry(self,x,y,width,height,mostrar=None):
     entrada=tk.Entry(self.ventana,show=mostrar) if mostrar else tk.Entry(self.ventana) # Crea un campo de texto; si `mostrar` se especifica, oculta caracteres 
     entrada.place(x=x,y=y,width=width,height=height)
     return entrada # devuelve el entry para un uso posterior
 
    def crear_boton(self,text, font, x, y, command=None, **kwargs):
     boton = tk.Button(self.ventana, text=text, font=font, command=command, **kwargs)
     width = kwargs.get('width', None)
     height = kwargs.get('height', None)
    
     if width and height:
      boton.place(x=x, y=y, width=width, height=height)
     else:
      boton.place(x=x, y=y)
        
     return boton 
 
    def crear_tabla(self,parent, columnas, datos=None, ancho_columnas=None, expandir=True):
        
      tabla = ttk.Treeview(parent, columns=columnas, show="headings") #crea un widget de tabla con columnas definidas

      for idx, columna in enumerate(columnas):
       tabla.heading(columna, text=columna) #asigna nombres a las columnas
       ancho = ancho_columnas[idx] if ancho_columnas and idx < len(ancho_columnas) else 100 # establece el ancho de las columnas
       tabla.column(columna, width=ancho, anchor="center") #configura cada columna
    
      if datos:
        for fila in datos:
            tabla.insert("", tk.END, values=fila) #se inserta filas de datos en la tabla

      scrollbar = ttk.Scrollbar(parent, orient="vertical", command=tabla.yview) #se añade una barra de desplzamineto vertical
      tabla.configure(yscroll=scrollbar.set)
      scrollbar.pack(side=tk.RIGHT, fill=tk.Y) #posiciona la barra de desplazamiento

      if expandir:
        tabla.pack(expand=True, fill=tk.BOTH) #expande la tabla para ajustarse
      else:
        tabla.pack()

      return tabla
     
class ventanaPrincipal(creacion_ventana): #esta clase es la tiene una herencia con cracion_ventana.
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Inicio de sesión", icono="fondoL.ico") #con super.() se puede acceder a los métodos de la clase padre desde una subclase (ventanaPrincipal)
        self.interfaz() 
     
    def interfaz(self): #método donde se construye la interfaz o elementos gráficos de la ventana 
        self.agregar_logo("logoLavaLimpia.png",x=0,y=0)
        self.agregar_logo("Logo2.png", x=65, y=280)
        
        self.crear_etiqueta("Inicio de sesión", "Britannic Bold", 20, x=380, y=165,bg="#188999")
        self.crear_etiqueta("Ingrese usuario o e-mail", "Arial", 15, x=380, y=220,bg="#188999")
        self.crear_etiqueta("Ingrese contraseña:", "Arial", 15, x=380, y=275,bg="#188999")
        
        texto_ingreso =self.crear_entry(x=380, y=245, width=250, height=30) #texto ingreso usuario/e-mail
        texto_contrasena =self.crear_entry(x=380, y=300, width=250, height=30,mostrar="*") #texto ingreso contraseña
        
        boton1=self.crear_boton(text="Iniciar sesión",font=("Arial", 20),x=380, y=350, width=250, height=30,command=lambda: self.validar_credenciales(texto_ingreso.get(), texto_contrasena.get())) #boton de iniciar sesión dónde se llama a un método donde se validan los datos ingresados.
        boton_olvido=self.crear_boton(text="¿Olvidó su contraseña?", font=("Arial", 10),x=380, y=420,command=lambda: self.cambiarVentana(),bd=0, cursor="hand2",bg="#188999")
        boton_registro =self.crear_boton(text="Crear cuenta de usuario",font=("Arial", 15),x=380, y=450,command=lambda:self.cambiarVentana(ventanaRegistro),cursor="hand2") #boton que sirve para ir a la ventanad de registro
        
    def validar_credenciales(self,usuario, contrasena):
        if not usuario or not contrasena:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return
        if usuario == "Pancracio" and contrasena == "1234":  # Ejemplo de validación
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
            self.cambiarVentana(ventana_usuario)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas. Intente nuevamente.")
            
class ventana_usuario(creacion_ventana): #ventan que se muestra  tras iniciar sesión
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Usuario", icono=None)
        self.interfaz()
        
    def interfaz(self):
        self.agregar_logo("Logo2.png", x=65, y=280)
        self.crear_etiqueta("Información de pedido",fuente="Britannic Bold",tamano=28,x=40,y=30,bg="#188999")
        boton_salir=self.crear_boton("Cerrar sesión",font=("Arial", 10),x=840,y=8,command=lambda:self.cambiarVentana(ventanaPrincipal),width=100, height=25,bg="#e31414",fg="#ffffff",cursor="hand2")
        
        frame_tabla=ttk.Frame(self.ventana) #se crea un contenedor frame para posicionar la tabla
        frame_tabla.place(x=200, y=150, width=580, height=360)
        columnas = ["ID", "Nombre", "Fecha", "Estado"]
        datos = [
            (1, "Orden #1", "2024-12-03", "Completada"),
            (2, "Orden #2", "2024-12-01", "Pendiente"),
            (3, "Orden #3", "2024-11-29", "Cancelada"),]
        
        self.crear_tabla( #agrega kla tabla con los datos existentes
            parent=frame_tabla,
            columnas=columnas,
            datos=datos,
            ancho_columnas=[30, 30, 30, 30],
            expandir=True
        )
          
class ventanaRegistro(creacion_ventana): # ventana para registrar a los nuevos usuarios 
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Registro", icono="fondoL.ico")
        self.interfaz()
    
    def interfaz(self):
        self.agregar_logo("logoLavaLimpia.png", 0, 0)
        self.agregar_logo("Logo2.png", 65, 280)
        
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

class VentanaRecuperacion(ventanaPrincipal):
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Recuperación contraseña", icono="fondoL.ico")
        self.crear_interfaz()

    def crear_interfaz(self):
        self.agregar_logo("logoLavaLimpia.png", 0, 0)
        self.agregar_logo("Logo2.png", 65, 280)
        self.crear_etiqueta("Ingrese el código", "Arial", 12, 280, 165, bg="#188999")
        codigo = self.crear_entry(280, 190, 250, 30)
        self.crear_boton("Ingresar código", font=("Arial", 20), x=545, y=190, width=250, height=30,command=lambda: self.cambiarVentana(VentanaNuevaContrasena))

class VentanaNuevaContrasena(ventanaPrincipal):
    def __init__(self):
        super().__init__(titulo="Lavalimpia-Cambiar contraseña", icono="fondoL.ico")
        self.crear_interfaz()

    def crear_interfaz(self):
        self.agregar_logo("logoLavaLimpia.png", 0, 0)
        self.agregar_logo("Logo2.png", 65, 280)
        self.crear_etiqueta("Ingrese su nueva contraseña:", "Arial", 12, 280, 165, bg="#188999")
        nueva_contrasena = self.crear_entry(280, 190, 250, 30, mostrar="*")
        self.crear_etiqueta("Confirme su nueva contraseña:", "Arial", 12, 280, 225, bg="#188999")
        confirmar_contrasena = self.crear_entry(280, 250, 250, 30, mostrar="*")
        self.crear_boton("Cambiar contraseña", font=("Arial", 18), x=545, y=250, width=250, height=30)
        
if __name__ == "__main__":
    ventanaPrincipal().mostrarVentana()

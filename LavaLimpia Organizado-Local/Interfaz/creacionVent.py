import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.scrolledtext import ScrolledText
import json
from datetime import datetime
class creacion_ventana: #Esta clase es el origen de todas las otras ventanas de la aplicación, donde se establecen configuraciones en común
    def __init__(self,titulo,usuario_actual=None, ancho=950, alto=550, color_fondo="#188999", icono=None, redimensionable=(False, False)): #__init__ es el método se llama automáticamente cuando se crea un objeto de una clase. (inicializa los atributos deacuerdo al objeto)
        self.ventana=tk.Tk() # crea la ventana principal
        self.usuario_actual = usuario_actual
        self.ventana.geometry(f"{ancho}x{alto}") # defina las dimensiones de la ventana
        self.ventana.title(titulo) # establece el título que tendrá la ventana
        self.ventana.configure(bg=color_fondo) #cambia el color del fondo
        self.ventana.resizable(*redimensionable) #define si la ventana puede cambiar de tamaño
        if icono:
            self.ventana.iconbitmap(icono) # esto asigna un ícono a la venta si se le proporcionace uno
        
    def mostrarVentana(self):
        self.ventana.mainloop() # ejecuta el bucle principal para que la ventana se pueda mostrar.
    

    def cambiarVentana(self, nuevaVentana, *args):
        try:
            self.ventana.destroy()  # Cierra la ventana actual
        except AttributeError:
            pass  # Si no tiene la propiedad 'ventana' o ya está destruida, simplemente continúa
    
        try:
            nueva_ventana = nuevaVentana(*args)  # Pasa los argumentos a la clase nuevaVentana
            nueva_ventana.mostrarVentana()  # Muestra la nueva ventana
        except TypeError as e:
            messagebox.showerror("Error", f"Hubo un problema al instanciar la ventana: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error inesperado: {str(e)}")
    
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
 
    def crear_tabla(self, columnas, datos, x, y, ancho_columna=100):
        # Crear marco para la tabla
        frame_tabla = tk.Frame(self.ventana)
        frame_tabla.place(x=x, y=y, width=800, height=300)
        
        # Crear tabla (Treeview)
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)
        tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configurar columnas
        for columna in columnas:
            tabla.heading(columna, text=columna)
            tabla.column(columna, width=ancho_columna, anchor="center")

        # Insertar datos
        for fila in datos:
            tabla.insert("", tk.END, values=fila)

        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tabla.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tabla.configure(yscrollcommand=scrollbar.set)
        
        tabla.bind("<<TreeviewSelect>>", lambda event: self.abrir_ventana_emergente(tabla))

        return tabla
    
    def abrir_ventana_emergente(self, tabla):
    
      # Obtener el ID del elemento seleccionado
      seleccion = tabla.selection()
      if seleccion:
        valores = tabla.item(seleccion[0], "values")  # Obtener valores de la fila seleccionada
        
        # Crear la ventana emergente
        ventana_emergente = tk.Toplevel(self.ventana)
        ventana_emergente.title("Detalle del Pedido")
        ventana_emergente.geometry("400x300")
        ventana_emergente.resizable(False,False)
        # Mostrar detalles en la ventana emergente
        detalle = "\n".join(f"{columna}: {valor}" for columna, valor in zip(tabla["columns"], valores))
        etiqueta_detalle = tk.Label(ventana_emergente, text=detalle, font=("Arial", 12), justify="left")
        etiqueta_detalle.pack(padx=20, pady=20)

        # Botón para cerrar la ventana
        boton_cerrar = tk.Button(
            ventana_emergente, text="Cerrar", font=("Arial", 12),
            command=ventana_emergente.destroy, bg="#e31414", fg="white", cursor="hand2"
        )
        boton_cerrar.pack(pady=100)
        
    def agregar_busqueda(self, tabla, x, y):
        """
        Agrega un campo de búsqueda vinculado a una tabla.

        Args:
            tabla (ttk.Treeview): Tabla a la que se aplicará la búsqueda.
            x (int): Posición horizontal.
            y (int): Posición vertical.
        """
        # Crear entrada de búsqueda
        etiqueta = tk.Label(self.ventana, text="Buscar:", font=("Arial", 12))
        etiqueta.place(x=x, y=y)
        entrada_busqueda = tk.Entry(self.ventana, font=("Arial", 12))
        entrada_busqueda.place(x=x + 70, y=y, width=200)

        # Botón para ejecutar la búsqueda
        boton_buscar = tk.Button(
            self.ventana, text="Buscar", font=("Arial", 12),
            command=lambda: self.buscar_en_tabla(tabla, entrada_busqueda.get()),
            bg="#1b7fcc", fg="#ffffff", cursor="hand2"
        )
        boton_buscar.place(x=x + 280, y=y, width=100, height=25)

    def buscar_en_tabla(self, tabla, texto_buscar):
      # Intentar convertir el texto de búsqueda a un entero, si es posible
      try:
        texto_buscar_int = int(texto_buscar)
      except ValueError:
        texto_buscar_int = None  # No es un número válido

      texto_buscar = texto_buscar.lower()  # Convertir a minúsculas para búsquedas de texto

      for item in tabla.get_children():
        valores = tabla.item(item, "values")
        
        # Verificar coincidencias en las columnas
        if any(
            texto_buscar in str(valor).lower() or 
            (texto_buscar_int is not None and texto_buscar_int == valor)
            for valor in valores
        ):
            tabla.item(item, tags="match")
        else:
            tabla.item(item, tags="hide")

      # Estilos para las filas
      tabla.tag_configure("match", foreground="black")
      tabla.tag_configure("hide", foreground="white")  # Ocultar filas no coincidentes

    def crear_ventana_emergente(self, titulo, mensaje, ancho=600, alto=400, color_fondo="#f0f0f0"):
      # Crear una nueva ventana emergente
      ventana_terminos = tk.Toplevel(self.ventana)
      ventana_terminos.title(titulo)
      ventana_terminos.geometry(f"{ancho}x{alto}")
      ventana_terminos.configure(bg=color_fondo)
      ventana_terminos.transient(self.ventana)  # Mantenerlo sobre la ventana principal
      ventana_terminos.grab_set()  # Bloquear interacción con la ventana principal

      # Crear el widget ScrolledText
      texto_terminos = ScrolledText(
          ventana_terminos,
          wrap="word",
          width=60,
          height=15,
          font=("Arial", 12),
          bg=color_fondo
            )
      texto_terminos.insert("1.0", mensaje)  # Insertar el texto de los términos
      texto_terminos.configure(state="disabled")  # Hacer que sea solo lectura
      texto_terminos.place(x=10, y=10)  # Ubicar el widget en la ventana

        # Botón para cerrar la ventana
      cerrar_btn = tk.Button(
        ventana_terminos,
        text="Cerrar",
        command=ventana_terminos.destroy,
        font=("Arial", 12),
        bg="#188999",
        fg="white",
        relief="flat",
        cursor="hand2"
         )
      cerrar_btn.place(x=(ancho // 2) - 40, y=alto - 50)  # Centrar el botón en la parte inferior
        
    def crear_checkbox(self, texto, variable, x, y, command=None):
        """Crea un checkbox en la ventana."""
        checkbox = tk.Checkbutton(
            self.ventana, text=texto, variable=variable, bg="#188999", command=command
        )
        checkbox.place(x=x, y=y)
        return checkbox
    
    def ventanaE_InfoPedidoOperador(self, titulo, ruta_json,codigo_filtro, ancho=300, alto=120, color_fondo="#f0f0f0"):
        # Crear la ventana secundaria
        ventana_pedidos = tk.Toplevel(self.ventana)
        ventana_pedidos.title(titulo)
        ventana_pedidos.resizable(False,False)
        ventana_pedidos.geometry(f"{ancho}x{alto}")
        ventana_pedidos.configure(bg=color_fondo)
        
        ventana_pedidos.transient(self.ventana)  # Mantenerla sobre la ventana principal
        ventana_pedidos.grab_set()

        # Leer el archivo JSON
        try:
            with open(ruta_json, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except Exception as e:
            tk.Label(
            ventana_pedidos, 
            text=f"Error al cargar el archivo JSON: {e}", 
            bg=color_fondo, 
            fg="red", 
            wraplength=ancho).pack(pady=10)
            return
        
        pedido_filtrado=None
        for usuario in datos:
            for pedido in usuario.get("pedidos",[]):
                if pedido.get("Código único")==codigo_filtro:
                    pedido_filtrado=pedido
                    break
            if pedido_filtrado:
                break
      
        # Crear un widget para mostrar los pedidos
        marco = tk.Frame(ventana_pedidos, bg=color_fondo)
        marco.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        text_area = tk.Text(marco, wrap=tk.WORD, bg="white", fg="black", font=("Arial", 12))
        text_area.pack(fill=tk.BOTH, expand=True)

        if pedido_filtrado:
            # Formatear y mostrar los datos del usuario encontrado
            texto = (
            f"Usuario: {pedido_filtrado.get('Usuario', 'No disponible')}\n"
            f"Dirección: {pedido_filtrado.get('Dirección', 'No disponible')}\n"
            f"Tarifa pedido: ${pedido_filtrado.get('Tarifa pedido', 0):,.2f}\n"
            f"Estado: {pedido_filtrado.get('Estado', 'No disponible')}\n"
            f"Fecha entrega: {pedido_filtrado.get('Fecha entrega', 'No disponible')}\n"
        )
            text_area.insert(tk.END, texto)
        else:
            # Mostrar mensaje si no se encuentra el usuario
            texto = f"No se encontró información para el código único: {codigo_filtro}"
            text_area.insert(tk.END, texto)

        # Deshabilitar edición del Text
        text_area.config(state=tk.DISABLED)
        
    def ventanaE_InfoCodUnico(self, titulo, pedidos, ancho=None, alto=None, color_fondo="#f0f0f0"):
        # Crear la ventana secundaria
        ventana_pedidos = tk.Toplevel(self.ventana)
        ventana_pedidos.title(titulo)
        ventana_pedidos.resizable(False, False)
        ventana_pedidos.geometry(f"{ancho}x{alto}")
        ventana_pedidos.configure(bg=color_fondo)

        ventana_pedidos.transient(self.ventana)  # Mantenerla sobre la ventana principal
        ventana_pedidos.grab_set()

        # Marco principal
        marco = tk.Frame(ventana_pedidos, bg=color_fondo)
        marco.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Campo para filtrar por fecha
        filtro_frame = tk.Frame(marco, bg=color_fondo)
        filtro_frame.pack(fill=tk.X, pady=5)

        tk.Label(filtro_frame, text="Filtrar por fecha (YYYY-MM-DD):", bg=color_fondo).pack(side=tk.LEFT, padx=5)
        fecha_entry = tk.Entry(filtro_frame)
        fecha_entry.pack(side=tk.LEFT, padx=5)

        # Tabla para mostrar los códigos únicos
        columnas = ("#", "Código único", "Fecha creación")
        tree = ttk.Treeview(marco, columns=columnas, show="headings")
        tree.heading("#", text="#")
        tree.heading("Código único", text="Código único")
        tree.heading("Fecha creación", text="Fecha creación")

        tree.column("#", width=50, anchor=tk.CENTER)
        tree.column("Código único", width=300, anchor=tk.W)
        tree.column("Fecha creación", width=150, anchor=tk.CENTER)

        tree.pack(fill=tk.BOTH, expand=True, pady=10)

        # Función para cargar los datos en la tabla
        def cargar_datos(filtrados=None):
            tree.delete(*tree.get_children())
            datos=filtrados if filtrados else pedidos
            for i, pedido in enumerate(datos):
                tree.insert('', 'end', values=(i + 1, pedido['Código único'], pedido['Fecha creación']))

        # Cargar los datos iniciales
        cargar_datos(pedidos)

        # Función para filtrar por fecha
        def filtrar():
            fecha_filtro = fecha_entry.get().strip()
            try:
                fecha_filtro_dt = datetime.strptime(fecha_filtro,'%Y-%m-%d').date()
                datos_filtrados = []
                for pedido in pedidos:
                    fecha_creacion=pedido.get('Fecha creación')
                    if fecha_creacion:
                        fecha_creacion_dt=datetime.strptime(fecha_creacion,'%Y-%m-%d %H:%M:%S').date()
                        if fecha_creacion_dt==fecha_filtro_dt:
                            datos_filtrados.append(pedido)
                cargar_datos(datos_filtrados)
                if not datos_filtrados:
                    messagebox.showinfo("Filtro","No se encontraron pedidos para la fecha ingresada.")
            except ValueError:
                messagebox.showinfo("Error", "Por favor, ingrese una fecha válida en el formato YYYY-MM-DD.")
        
        tk.Button(filtro_frame, text="Filtrar", command=filtrar).pack(side=tk.LEFT, padx=5)
        # Función para refrescar la tabla
        def refrescar():
            fecha_entry.delete(0, tk.END)  # Borrar el contenido del campo de fecha
            cargar_datos()  # Restaurar los datos originales
        
        tk.Button(filtro_frame, text="Restablecer", command=refrescar).pack(side=tk.LEFT, padx=5)

        # Botón para copiar código único
        def copiar_codigo():
            selected_item = tree.focus()
            if selected_item:
                codigo = tree.item(selected_item, 'values')[1]
                self.ventana.clipboard_clear()
                self.ventana.clipboard_append(codigo)
                self.ventana.update()  # Actualizar el portapapeles
                messagebox.showinfo("Copiar", f"El código '{codigo}' ha sido copiado al portapapeles.")
            else:
                messagebox.showinfo("Error", "Por favor, seleccione un código para copiar.")

        # Añadir marco para botones inferiores
        boton_frame = tk.Frame(marco, bg=color_fondo)
        boton_frame.pack(fill=tk.X, pady=10)

        copiar_btn = tk.Button(boton_frame, text="Copiar código seleccionado", command=copiar_codigo)
        copiar_btn.pack(side=tk.RIGHT, padx=10, pady=5)

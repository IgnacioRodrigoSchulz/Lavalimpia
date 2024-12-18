import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Datos de ejemplo
usuarios = [
    {"nombre": "joaquin", "correo": "correo@pepi.to", "fechaCreacion": "2024-12-01 22:12"},
    {"nombre": "pedro", "correo": "pereira@mail.net", "fechaCreacion": "2024-12-01 22:12"},
    {"nombre": "Marco.1V", "correo": "marco@gmail.com", "fechaCreacion": "2024-12-02 12:12"},
    {"nombre": "gerente", "correo": "gerencia@general.com", "fechaCreacion": "2024-12-05 01:12"},
    {"nombre": "juan", "correo": "juan@mail.net", "fechaCreacion": "2024-12-10 09:12"}
]

pedidos = [
    {"codigoUnico": 1, "direccion": "Calle123", "usuario": 0, "tarifa": "1000", "fechaCreacion": "2024-12-10 00:12", "estadoActual": "Creado"},
    {"codigoUnico": 2, "direccion": "Avenida 12", "usuario": 1, "tarifa": "1500", "fechaCreacion": "2024-12-10 09:12", "estadoActual": "Creado"}
]

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Tabla de Pedidos")
ventana.geometry("1200x600")
ventana.configure(bg="#188999")  # Fondo de la ventana principal
ventana.resizable()

# Crear estilo para el Treeview
style = ttk.Style()
style.configure("Treeview",
                background="#188999",  # Fondo de la tabla
                foreground="black",     # Color negro para el texto
                fieldbackground="#188999",  # Fondo de las filas
                font=("Arial", 10),      # Fuente Arial para el texto
                rowheight=25)           # Altura de fila

style.configure("Treeview.Heading",
                background="#1a232a",  # Fondo del encabezado oscuro
                foreground="black",     # Color del texto del encabezado
                font=("Arial", 12, "bold"))  # Fuente más grande y negrita para encabezados

# Crear el Treeview para mostrar la tabla
columns = ("usuario", "correo", "id", "direccion", "tarifa", "fechaCreacion", "estadoActual")
tree = ttk.Treeview(ventana, columns=columns, show="headings", style="Treeview")

# Configurar los encabezados de la tabla
tree.heading("usuario", text="Usuario")
tree.heading("correo", text="Correo")
tree.heading("id", text="id")  # Cambié "ID" por "id"
tree.heading("direccion", text="Dirección")
tree.heading("tarifa", text="Tarifa")
tree.heading("fechaCreacion", text="Fecha Creación")
tree.heading("estadoActual", text="Estado Actual")

# Ajuste del ancho de las columnas para que se ajusten a la ventana
tree.column("usuario", width=120, anchor="w")
tree.column("correo", width=180, anchor="w")
tree.column("id", width=100, anchor="w")  # Cambié "ID" por "id"
tree.column("direccion", width=200, anchor="w")
tree.column("tarifa", width=100, anchor="w")
tree.column("fechaCreacion", width=160, anchor="w")
tree.column("estadoActual", width=120, anchor="w")

# Función para agregar los pedidos a la tabla
def mostrar_pedidos():
    # Limpiar la tabla antes de agregar los nuevos datos filtrados
    for item in tree.get_children():
        tree.delete(item)
    
    for pedido in pedidos:
        usuario = usuarios[pedido["usuario"]]  # Obtener el usuario asociado al pedido
        tree.insert("", tk.END, values=(usuario["nombre"], usuario["correo"], pedido["codigoUnico"],
                                       pedido["direccion"], pedido["tarifa"], pedido["fechaCreacion"],
                                       pedido["estadoActual"]))

# Función para filtrar la tabla según los criterios de búsqueda
def filtrar_tabla(event=None):
    # Obtener los valores de búsqueda de cada campo
    usuario_buscar = entry_usuario.get().lower()
    correo_buscar = entry_correo.get().lower()
    codigo_buscar = entry_codigo.get().lower()
    direccion_buscar = entry_direccion.get().lower()
    tarifa_buscar = entry_tarifa.get().lower()
    fecha_buscar = entry_fecha.get().lower()
    estado_buscar = entry_estado.get().lower()  # Campo de búsqueda para fecha de creación

    # Limpiar la tabla antes de agregar los datos filtrados
    for item in tree.get_children():
        tree.delete(item)
    
    # Filtrar y agregar solo los pedidos que coinciden con los filtros
    for pedido in pedidos:
        usuario = usuarios[pedido["usuario"]]  # Obtener el usuario asociado al pedido
        usuario_nombre = usuario["nombre"].lower()
        usuario_correo = usuario["correo"].lower()
        pedido_codigo = str(pedido["codigoUnico"]).lower()
        pedido_direccion = pedido["direccion"].lower()
        pedido_tarifa = str(pedido["tarifa"]).lower()
        pedido_fecha = pedido["fechaCreacion"].lower()
        pedido_estado = pedido["estadoActual"].lower() 

        if (usuario_buscar in usuario_nombre and
            correo_buscar in usuario_correo and
            codigo_buscar in pedido_codigo and
            direccion_buscar in pedido_direccion and
            tarifa_buscar in pedido_tarifa and
            fecha_buscar in pedido_fecha and
            estado_buscar in pedido_estado):  # Filtrado por fecha
            tree.insert("", tk.END, values=(usuario["nombre"], usuario["correo"], pedido["codigoUnico"],
                                           pedido["direccion"], pedido["tarifa"], pedido["fechaCreacion"],
                                           pedido["estadoActual"]))

# Crear el Frame para los campos de búsqueda y alinearlos con las columnas
frame_busqueda = tk.Frame(ventana, bg="#188999")
frame_busqueda.pack(pady=5, fill="x")

# Crear los campos de búsqueda y alinearlos sobre cada columna con grid
entry_usuario = tk.Entry(frame_busqueda, font=("Arial", 10), width=15)
entry_usuario.grid(row=0, column=0, padx=40, pady=5)  # Separación de 40 píxeles entre los campos
entry_usuario.bind("<KeyRelease>", filtrar_tabla)  # Filtrar cada vez que se suelta una tecla

entry_correo = tk.Entry(frame_busqueda, font=("Arial", 10), width=15)
entry_correo.grid(row=0, column=1, padx=40, pady=5)  # Separación de 40 píxeles entre los campos
entry_correo.bind("<KeyRelease>", filtrar_tabla)

entry_codigo = tk.Entry(frame_busqueda, font=("Arial", 10), width=15)
entry_codigo.grid(row=0, column=2, padx=40, pady=5)  # Separación de 40 píxeles entre los campos
entry_codigo.bind("<KeyRelease>", filtrar_tabla)

entry_direccion = tk.Entry(frame_busqueda, font=("Arial", 10), width=15)
entry_direccion.grid(row=0, column=3, padx=40, pady=5)  # Separación de 40 píxeles entre los campos
entry_direccion.bind("<KeyRelease>", filtrar_tabla)

entry_tarifa = tk.Entry(frame_busqueda, font=("Arial", 10), width=15)
entry_tarifa.grid(row=0, column=4, padx=40, pady=5)  # Separación de 40 píxeles entre los campos
entry_tarifa.bind("<KeyRelease>", filtrar_tabla)

entry_estado = tk.Entry(frame_busqueda, font=("Arial", 10), width=15)
entry_estado.grid(row=0, column=5, padx=30, pady=1)  # Separación de 40 píxeles entre los campos
entry_estado.bind("<KeyRelease>", filtrar_tabla)

# Nuevo campo de búsqueda para la fecha de creación
entry_fecha = tk.Entry(frame_busqueda, font=("Arial", 10), width=15)
entry_fecha.grid(row=0, column=6, padx=20, pady=5)  # Separación de 40 píxeles entre los campos
entry_fecha.bind("<KeyRelease>", filtrar_tabla)

# Mostrar todos los pedidos inicialmente
mostrar_pedidos()

# Crear el Treeview para mostrar la tabla
tree.pack(expand=True, fill="both", padx=20, pady=20)

# Iniciar la aplicación
ventana.mainloop()



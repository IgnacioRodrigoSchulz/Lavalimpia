import tkinter as tk
from tkinter import ttk

# Datos de ejemplo
usuarios = [
    {"nombre": "Joaquin", "correo": "correo@pepi.to", "fechaCreacion": "2024-12-01 22:12"},
    {"nombre": "Pedro", "correo": "pereira@mail.net", "fechaCreacion": "2024-12-01 22:12"},
    {"nombre": "Marco.1V", "correo": "marco@gmail.com", "fechaCreacion": "2024-12-02 12:12"},
    {"nombre": "gerente", "correo": "gerencia@general.com", "fechaCreacion": "2024-12-05 01:12"},
    {"nombre": "juan", "correo": "juan@mail.net", "fechaCreacion": "2024-12-10 09:12"}
]

pedidos = [
    {"codigoUnico": 1, "direccion": "Calle123", "usuario": 0, "tarifa": "1000", "fechaCreacion": "2024-12-10 00:12", "estadoActual": "Creado"},
    {"codigoUnico": 2, "direccion": "Avenida 12", "usuario": 1, "tarifa": "1500", "fechaCreacion": "2024-12-10 09:15", "estadoActual": "Entregado"},
    {"codigoUnico": 3, "direccion": "Avenida 23", "usuario": 2, "tarifa": "500", "fechaCreacion": "2024-12-10 10:10", "estadoActual": "Creado"},
    {"codigoUnico": 4, "direccion": "Avenida 18", "usuario": 3, "tarifa": "5500", "fechaCreacion": "2024-12-10 15:12", "estadoActual": "Procesado"},
    {"codigoUnico": 5, "direccion": "Avenida 109", "usuario": 4, "tarifa": "9500", "fechaCreacion": "2024-12-10 14:12", "estadoActual": "Creado"}
]

# Crear la ventana principal
def ventana_Empleadorecaudador():
    ventana = tk.Tk()
    ventana.title("Lavalimpia-Recaudador")
    ventana.geometry("1200x600")
    ventana.configure(bg="#188999")  # Fondo de la ventana principal
    ventana.resizable()
    ventana.iconbitmap("recursosImagenes/fondoL.ico")

    boton = tk.Button(ventana,text="Actualizar estado de pedido", font=("Arial",12),cursor="hand2",command=lambda:ventana_terminos())
    boton.configure(bg="blue",fg="#ffffff")
    boton.place(x=30,y=50)

    def ventana_terminos():
        ventana_terminos = tk.Toplevel(ventana)
        ventana_terminos.title("Estado del pedido")
        ventana_terminos.geometry("400x500")
        ventana_terminos.configure(bg="#f0f0f0")
        ventana_terminos.transient(ventana)  # Mantenerlo sobre la ventana principal
        ventana_terminos.grab_set() # Bloquear interacción con la ventana principal
        
        estado_eqt= tk.Label(
        ventana_terminos,
        text="Coloque id:", 
        font=("Arial", 15), 
        bg="#f0f0f0"
        )
        estado_eqt.place(x="91", y="70")
                
        estado_entry= tk.Entry(
        ventana_terminos, 
        font=("Arial", 15), 
        width=20 
        )
        estado_entry.place(x="90", y= "100")

        estado_eqt= tk.Label(
        ventana_terminos,
        text="Estado actual del pedido:", 
        font=("Arial", 15), 
        bg="#f0f0f0"
        )
        estado_eqt.place(x="91", y="210")
                
        estado_entry= tk.Entry(
        ventana_terminos, 
        font=("Arial", 15), 
        width=20 
        )
        estado_entry.place(x="90", y= "250")

        # Botón para actualizar la ventana
        actualizar_btn = tk.Button(
        ventana_terminos,
        text="Actualizar",
        command=ventana_terminos.destroy,
        font=("Arial", 12),
        bg="#188999",
        fg="white",
        relief="flat",
        cursor="hand2"
        )
        actualizar_btn.place(x="160", y="400")
    # Crear estilo para el Treeview
    style = ttk.Style()
    style.configure("Treeview",
                    background="#7ad1de",  # Fondo de la tabla
                    foreground="black",     # Color negro para el texto
                    fieldbackground="#7ad1de",  # Fondo de las filas
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
    tree.heading("id", text="Id")  # Cambié "ID" por "id"
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
    frame_busqueda.pack(fill="none",pady=20)

    # Crear los campos de búsqueda y alinearlos sobre cada columna con grid
    entry_usuario = tk.Entry(frame_busqueda, font=("Arial", 11),fg="Gray", width=15)
    entry_usuario.grid(row=0,column=0, padx=15, pady=0)  # Separación de 20 píxeles entre los campos
    entry_usuario.bind("<KeyRelease>", filtrar_tabla)

    entry_correo = tk.Entry(frame_busqueda, font=("Arial", 11),fg="Gray", width=20)
    entry_correo.grid(row=0,column=1, padx=15, pady=0)  # Separación de 20 píxeles entre los campos
    entry_correo.bind("<KeyRelease>", filtrar_tabla)
        
    entry_codigo = tk.Entry(frame_busqueda, font=("Arial", 11),fg="Gray", width=15)
    entry_codigo.grid(row=0, column=2, padx=15, pady=0)  # Separación de 20 píxeles entre los campos
    entry_codigo.bind("<KeyRelease>", filtrar_tabla)

    entry_direccion = tk.Entry(frame_busqueda, font=("Arial", 11),fg="Gray", width=20)
    entry_direccion.grid(row=0, column=3, padx=15, pady=0)  # Separación de 20 píxeles entre los campos
    entry_direccion.bind("<KeyRelease>", filtrar_tabla)
        
    entry_tarifa = tk.Entry(frame_busqueda, font=("Arial", 11),fg="Gray", width=15)
    entry_tarifa.grid(row=0, column=4, padx=15, pady=0)  # Separación de 20 píxeles entre los campos
    entry_tarifa.bind("<KeyRelease>", filtrar_tabla)
    
    # Nuevo campo de búsqueda para la fecha de creación
    entry_fecha = tk.Entry(frame_busqueda, font=("Arial", 11),fg="Gray", width=15)
    entry_fecha.grid(row=0, column=5, padx=15, pady=0)  # Separación de 20 píxeles entre los campos
    entry_fecha.bind("<KeyRelease>", filtrar_tabla)
        
    entry_estado = tk.Entry(frame_busqueda, font=("Arial", 11),fg="Gray", width=20)
    entry_estado.grid(row=0, column=6, padx=15, pady=0)  # Separación de 20 píxeles entre los campos
    entry_estado.bind("<KeyRelease>", filtrar_tabla)
    # Mostrar todos los pedidos inicialmente
    mostrar_pedidos()

    # Crear el Treeview para mostrar la tabla
    tree.pack(expand=True, fill="both", padx=30, pady=30)

    # Iniciar la aplicación
    ventana.mainloop()
ventana_Empleadorecaudador()

"""
def entry_focus_in(event):
    if entry_usuario.get()== "Usuario":
        entry_usuario.delete(0, 'end')
        entry_usuario.config(fg="Black")

def entry_focus_out(event):
    if entry_usuario.get()== "":
        entry_usuario.insert(0,"Usuario")
        entry_usuario.config(fg="gray")


entry_usuario.insert(0,"Usuario")
entry_usuario.bind("<FocusIn>",entry_focus_in)
entry_usuario.bind("<FocusOut>",entry_focus_out)  # Filtrar cada vez que se suelta una tecla

def entry_focus_in(event):
    if entry_correo.get()== "Correo":
        entry_correo.delete(0, 'end')
        entry_correo.config(fg="Black")

def entry_focus_out(event):
    if entry_correo.get()== "":
        entry_correo.insert(0,"Correo")
        entry_correo.config(fg="gray")entry_correo.insert(0,"Correo")
entry_correo.bind("<FocusIn>",entry_focus_in)
entry_correo.bind("<FocusOut>",entry_focus_out) 

def entry_focus_in(event):
    if entry_codigo.get()== "Codigo":
        entry_codigo.delete(0, 'end')
        entry_codigo.config(fg="Black")

def entry_focus_out(event):
    if entry_codigo.get()== "":
        entry_codigo.insert(0,"Codigo")
        entry_codigo.config(fg="gray")
entry_codigo.insert(0,"Codigo")
entry_codigo.bind("<FocusIn>",entry_focus_in)
entry_codigo.bind("<FocusOut>",entry_focus_out) 

def entry_focus_in(event):
    if entry_direccion.get()== "Dirección":
        entry_direccion.delete(0, 'end')
        entry_direccion.config(fg="Black")

def entry_focus_out(event):
    if entry_direccion.get()== "":
        entry_direccion.insert(0,"Dirección")
        entry_direccion.config(fg="gray")


entry_direccion.insert(0,"Dirección")
entry_direccion.bind("<FocusIn>",entry_focus_in)
entry_direccion.bind("<FocusOut>",entry_focus_out) 

def entry_focus_in(event):
    if entry_tarifa.get()== "Tarifa":
        entry_tarifa.delete(0, 'end')
        entry_tarifa.config(fg="Black")

def entry_focus_out(event):
    if entry_tarifa.get()== "":
        entry_tarifa.insert(0,"Tarifa")
        entry_tarifa.config(fg="gray")
entry_tarifa.insert(0,"Tarifa")
entry_tarifa.bind("<FocusIn>",entry_focus_in)
entry_tarifa.bind("<FocusOut>",entry_focus_out) 

def entry_focus_in(event):
    if entry_fecha.get()== "Fecha":
        entry_fecha.delete(0, 'end')
        entry_fecha.config(fg="Black")

def entry_focus_out(event):
    if entry_fecha.get()== "":
        entry_fecha.insert(0,"Fecha")
        entry_fecha.config(fg="gray")

entry_fecha.insert(0,"Fecha")
entry_fecha.bind("<FocusIn>",entry_focus_in)
entry_fecha.bind("<FocusOut>",entry_focus_out) 

def entry_focus_in(event):
    if entry_estado.get()== "Estado Actual":
        entry_estado.delete(0, 'end')
        entry_estado.config(fg="Black")

def entry_focus_out(event):
    if entry_estado.get()== "":
        entry_estado.insert(0,"Estado Actual")
        entry_estado.config(fg="gray")

entry_estado.insert(0,"Estado Actual")
entry_estado.bind("<FocusIn>",entry_focus_in)
entry_estado.bind("<FocusOut>",entry_focus_out) 
"""

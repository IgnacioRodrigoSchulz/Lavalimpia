import tkinter as tk
from tkinter import messagebox
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

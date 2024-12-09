import re 
from tkinter import messagebox


def verificarUsuario(usuario):
    """
    Verifica si un nombre de usuario cumple con los criterios de validación.
    
    Criterios:
    - Entre 4 y 20 caracteres.
    - Solo letras, números, guiones bajos (_) y puntos (.).
    - No puede comenzar ni terminar con un punto o guion bajo.
    - No debe tener puntos o guiones bajos consecutivos.
    
    Args:
        usuario (str): El nombre de usuario a verificar.
        
    Returns:
        bool: True si es válido, False si no.
    """
    if len(usuario) < 4 or len(usuario) > 20:
        messagebox.showwarning("Advertencia", "El nombre de usuario debe tener entre 4 y 20 caracteres.")
        return False
    if not re.match(r'^[a-zA-Z0-9_.]+$', usuario):
        messagebox.showwarning("Advertencia", "El nombre de usuario solo puede contener letras, números, guiones bajos (_) y puntos (.).")
        return False
    if usuario.startswith(('.', '_')) or usuario.endswith(('.', '_')):
        messagebox.showwarning("Advertencia", "El nombre de usuario no puede comenzar ni terminar con un punto o guion bajo.")
        return False
    if re.search(r'[._]{2,}', usuario):
        messagebox.showwarning("Advertencia", "El nombre de usuario no debe tener puntos o guiones bajos consecutivos.")
        return False
    return True

def verificarCorreo(correo):
    """
    Verifica si un correo electrónico es válido.

    Args:
        correo (str): El correo a verificar.

    Returns:
        bool: True si es válido, False si no.
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if not re.match(patron, correo):
        messagebox.showwarning("Advertencia","El correo electrónico no es válido. Asegúrate de usar un formato como 'usuario@dominio.com'.")
        return False
    return True
   
def verificarContrasena(contrasena, confirmar_contrasena):
    """
    Verifica si una contraseña cumple con los criterios de validación.

    Criterios:
    - Coincide con la contraseña de confirmación.
    - Al menos 8 caracteres.
    - Incluye al menos una letra mayúscula, una minúscula, un número y un carácter especial.

    Args:
        contrasena (str): La contraseña a verificar.
        confirmar_contrasena (str): La contraseña de confirmación.

    Returns:
        bool: True si es válida, False si no.
    """
    if contrasena != confirmar_contrasena:
        messagebox.showwarning("Advertencia","Las contraseñas no coinciden. Por favor, verifica ambas contraseñas.")
        return False
    if len(contrasena) < 8:
        messagebox.showwarning("Advertencia","La contraseña debe tener al menos 8 caracteres.")
        return False
    if not re.search(r'[A-Z]', contrasena):
        messagebox.showwarning("Advertencia","La contraseña debe incluir al menos una letra mayúscula.")
        return False
    if not re.search(r'[a-z]', contrasena):
        messagebox.showwarning("Advertencia","La contraseña debe incluir al menos una letra minúscula.")
        return False
    if not re.search(r'[0-9]', contrasena):
        messagebox.showwarning("Advertencia","La contraseña debe incluir al menos un número.")
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena):
        messagebox.showwarning("Advertencia","La contraseña debe incluir al menos un carácter especial (!@#$%^&*(),.?\":{}|<>).")
        return False
    return True




usuario = "usuario.ejemplo_123"
correo = "ejemplo@dominio.com"
contrasena = "Contraseña123!"
confirmar_contrasena = "Contraseña123!"


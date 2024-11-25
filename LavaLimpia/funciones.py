import re 
import funcionalidadServidor 

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
        return False
    if not re.match(r'^[a-zA-Z0-9_.]+$', usuario):
        return False
    if usuario.startswith(('.', '_')) or usuario.endswith(('.', '_')):
        return False
    if re.search(r'[._]{2,}', usuario):
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
    return bool(re.match(patron, correo))


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
        return False
    if len(contrasena) < 8:
        return False
    if not re.search(r'[A-Z]', contrasena):
        return False
    if not re.search(r'[a-z]', contrasena):
        return False
    if not re.search(r'[0-9]', contrasena):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena):
        return False
    return True




usuario = "usuario.ejemplo_123"
correo = "ejemplo@dominio.com"
contrasena = "Contraseña123!"
confirmar_contrasena = "Contraseña123!"


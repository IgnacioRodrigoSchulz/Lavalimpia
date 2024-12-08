from basededatosFunciones import *
from basededatosClases import *
import funcionLocutor


def recibir_nuevaCuenta(cliente, baseUsuarios, argumentos):
    nombreUsuario = argumentos[0]
    contrasena = argumentos[1]
    correo = argumentos[2]
    crearUsuario(baseUsuarios, "cliente", nombreUsuario, contrasena, correo)
    
    funcionLocutor.enviar_alerta(cliente, "Usuario creado exitosamente.")
    

def recibir_inicioSesion(cliente, baseUsuarios, argumentos):
    nombre = argumentos[0]
    contrasena = argumentos[1]
    #print(nombre)
    #print(contrasena)
    indice = baseUsuarios.buscarPor("nombre", nombre)[0]
    #print(indice)
    usuario = Usuario(baseUsuarios, indice)
    usuario.cargar()
    #print(usuario)
    usuario.iniciarSesion(contrasena)
    
    if usuario.sesionIniciada():
        funcionLocutor.enviar_alerta(cliente, "Inicio de sesion exitoso.")
    else:
        funcionLocutor.enviar_alerta(cliente, "Contraseña incorrecta.")
    return usuario
    
def recibir_solicitudInfoSesion(cliente, usuario):
    print(cliente)
    funcionLocutor.enviar_alerta(cliente, "Información de usuario")
    if usuario.sesionIniciada():
        funcionLocutor.enviar_alerta(cliente, "Información de usuario enviada")
    else:
        funcionLocutor.enviar_alerta(cliente, "Información de usuario no enviada")

def recibir_crearPedido():
    pass

def recibir_accesoPedido():
    pass

def recibir_buscarPedido():
    pass

def recibir_accesoUsuario():
    pass

def recibir_buscarUsuario():
    pass

def recibir_realizarPago():
    pass

def resivir_echo(cliente, argumentos):
    alerta = argumentos[0]
    funcionLocutor.enviar_alerta(cliente, alerta)

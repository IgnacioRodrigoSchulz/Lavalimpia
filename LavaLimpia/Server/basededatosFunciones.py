#import jsonLector

from basededatosClases import BaseDatos
from codigoUnico import fechaActual, codigoUnico



def crearUsuario(baseDatos, tipoUsuario, nombreUsuario, contrasena, correo):
    usuario = {}
    usuario["nombre"] = nombreUsuario
    usuario["contrasena"] = contrasena
    usuario["correo"] = correo
    
    usuario["pedidos"] = []
    usuario["tipoUsuario"] = tipoUsuario

    usuario["fechaCreacion"] = fechaActual()

    baseDatos.anadir(usuario)
    baseDatos.guardar()
    


def crearPedido(baseDatos, direccion, usuario, tarifa, empleadoAutor):
    pedido = {}

    pedido["codigoUnico"] = codigoUnico()
    
    pedido["direccion"] = direccion
    pedido["usuario"] = usuario
    pedido["tarifa"] = tarifa

    fecha = fechaActual()
    estado = "Creado"
    
    pedido["fechaCreacion"] = fecha
    pedido["estadoActual"] = estado

    accion = [fecha, estado, empleadoAutor]
    pedido["estadoHistorial"] = []
    pedido["estadoHistorial"].append(accion)
    
    baseDatos.anadir(pedido)
    baseDatos.guardar()


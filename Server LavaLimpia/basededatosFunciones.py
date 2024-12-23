#import jsonLector

from basededatosClases import BaseDatos, Usuario
from codigoUnico import fechaActual, codigoUnico, fecha_diasEnAdelante


# Dado los parametros dados, se crea un nuevo usuario y se guarda en
#el archivo JSON.
def crearUsuario(baseDatos, tipoUsuario, nombreUsuario, contrasena, correo):
    usuario = {}
    usuario["nombre"] = nombreUsuario
    usuario["contrasena"] = contrasena
    usuario["correo"] = correo
    
    usuario["pedidos"] = []
    usuario["tipoUsuario"] = tipoUsuario

    usuario["fechaCreacion"] = fechaActual()
    usuario["codigoUnico"] = codigoUnico(baseDatos)

    baseDatos.anadir(usuario)
    baseDatos.guardar()
    

# Dado los parametros dados, se crea un nuevo pedido y se guarda en
#el archivo JSON.
def crearPedido(basePedidos, baseUsuarios, direccion, usuario, tarifa, empleadoAutor):
    pedido = {}

    pedidoCodigoUnico = codigoUnico(basePedidos)
    pedido["codigoUnico"] = pedidoCodigoUnico
    
    pedido["direccion"] = direccion
    pedido["usuario"] = usuario
    pedido["tarifa"] = tarifa

    fecha = fechaActual()
    fechaFin = fecha_diasEnAdelante(5, "18:00")
    estado = "Creado"
    
    pedido["fechaCreacion"] = fecha
    pedido["estadoActual"] = estado

    accion = [fecha, estado, empleadoAutor]
    pedido["estadoHistorial"] = []
    pedido["estadoHistorial"].append(accion)

    pedido["fechaPlazo"] = fechaFin

    # Añade el pedido a la lista de los pedidos
    #del usuario, en el archivo JSON de los usuarios.
    baseUsuarios.cargar()
    usuarioIndice = baseUsuarios.buscarPor("codigoUnico", usuario)[0]
    usuarioInst = Usuario(baseUsuarios, usuarioIndice)
    usuarioInst.cargar()
    usuarioInst.anadirPedido(pedidoCodigoUnico)
    baseUsuarios.guardar()

    # Añade el pedido al archivo JSON de los pedidos.
    basePedidos.anadir(pedido)
    basePedidos.guardar()



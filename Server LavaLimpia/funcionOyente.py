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
    indice = baseUsuarios.buscarPor("nombre", nombre)[0]
    usuario = Usuario(baseUsuarios, indice)
    usuario.cargar()
    usuario.iniciarSesion(contrasena)
    
    if usuario.sesionIniciada():
        tipoDeUsuario = usuario.get_tipoUsuario()
        print(tipoDeUsuario)
        if tipoDeUsuario == "cliente":
            funcionLocutor.enviar_respuesta(cliente, '201')
        elif tipoDeUsuario == "gerente":
            funcionLocutor.enviar_respuesta(cliente, '202')
        elif tipoDeUsuario == "operador":
            funcionLocutor.enviar_respuesta(cliente, '203')
            
    else:
        funcionLocutor.enviar_alerta(cliente, "Contraseña incorrecta.")
    return usuario
    
def recibir_solicitudInfoSesion(cliente, usuario):
    funcionLocutor.enviar_alerta(cliente, "Información de usuario")
    informacionUsuario = usuario.get_datos()
    if usuario.sesionIniciada():
        funcionLocutor.enviar_alerta(cliente, "Información de usuario enviada")
        funcionLocutor.enviar_infoInicioSesion(cliente, informacionUsuario)
    else:
        funcionLocutor.enviar_alerta(cliente, "Información de usuario no enviada")

def recibir_crearPedido(cliente, basePedidos, baseUsuarios, usuario, argumentos):
    direccion = argumentos[0]
    usuarioID = argumentos[1]
    tarifa = int(argumentos[2])
    if usuario.sesionIniciada():
        tipoDeUsuario = usuario.get_tipoUsuario()
        if (tipoDeUsuario == "gerente") or (tipoDeUsuario == "operador"):
            crearPedido(basePedidos, baseUsuarios, direccion, usuarioID, tarifa, usuario.get_ID())
            funcionLocutor.enviar_respuesta(cliente, '001')
        else:
            funcionLocutor.enviar_respuesta(cliente, '002')
    else:
        funcionLocutor.enviar_respuesta(cliente, '003')        


def recibir_accesoPedido(cliente, basePedidos, usuario, argumentos):
    codigoUnico = argumentos[0]
    indice = basePedidos.buscarPor("codigoUnico", codigoUnico)[0]
    pedido = Pedido(basePedidos, indice)
    pedido.cargar()
    esUsuarioTitular = (pedido.usuario == usuario.get_ID())
    tipoDeUsuario = usuario.get_tipoUsuario()
    if usuario.sesionIniciada():
        if esUsuarioTitular or (tipoDeUsuario == "gerente"):            
            #print(codigoUnico)
            informacion = pedido.get_datos()
            #print(informacion)
            funcionLocutor.enviar_infoPedido(cliente, informacion)
            funcionLocutor.enviar_respuesta(cliente, '001')
        else:
            funcionLocutor.enviar_respuesta(cliente, '002')
    else:
        funcionLocutor.enviar_respuesta(cliente, '003')

def recibir_buscarPedido(cliente, basePedidos, usuario, argumentos):
    criterio = argumentos[0]
    valor = argumentos[1]
    print(criterio)
    print(valor)
    tipoDeUsuario = usuario.get_tipoUsuario()
    if usuario.sesionIniciada():
        if tipoDeUsuario == "gerente":
            basePedidos.cargar()
            baseData = basePedidos.getData()
            indices = basePedidos.buscarPor(criterio, valor)
            print(indices)
            resultados = []
            for i in indices:
                resultados.append(baseData[i])
                
            funcionLocutor.enviar_resultadosBusquedaPedido(cliente, resultados)
            funcionLocutor.enviar_respuesta(cliente, '001')
        else:
            funcionLocutor.enviar_respuesta(cliente, '002')
    else:
        funcionLocutor.enviar_respuesta(cliente, '003')
        

def recibir_accesoUsuario(cliente, baseUsuarios, usuario, argumentos):
    codigoUnico = argumentos[0]
    tipoDeUsuario = usuario.get_tipoUsuario()
    if usuario.sesionIniciada():
        if tipoDeUsuario == "gerente":
            indice = baseUsuarios.buscarPor("codigoUnico", codigoUnico)[0]
            usuarioSolicitado = Usuario(baseUsuarios, indice)
            usuarioSolicitado.cargar()
            informacion = usuarioSolicitado.get_datos()
            funcionLocutor.enviar_infoUsuario(cliente, informacion)
            funcionLocutor.enviar_respuesta(cliente, '001')
        else:
            funcionLocutor.enviar_respuesta(cliente, '002')
    else:
        funcionLocutor.enviar_respuesta(cliente, '003')
    
    

def recibir_buscarUsuario(cliente, baseUsuarios, usuario, argumentos):
    criterio = argumentos[0]
    valor = argumentos[1]
    tipoDeUsuario = usuario.get_tipoUsuario()
    if usuario.sesionIniciada():
        if tipoDeUsuario == "gerente":
            baseUsuarios.cargar()
            baseData = baseUsuarios.getData()
            
            indices = baseUsuarios.buscarPor(criterio, valor)
            resultados = []
            for i in indices:
                resultados.append(baseData[i])
                
            funcionLocutor.enviar_resultadosBusquedaUsuario(cliente, resultados)
            
            funcionLocutor.enviar_respuesta(cliente, '001')
        else:
            funcionLocutor.enviar_respuesta(cliente, '002')
    else:
        funcionLocutor.enviar_respuesta(cliente, '003')


def recibir_realizarPago(cliente, basePedidos, usuario, argumentos):
    codigoUnico = argumentos[0]
    usuario.cargar()
    tipoDeUsuario = usuario.get_tipoUsuario()
    tienePermiso = (tipoDeUsuario=="gerente") or (tipoDeUsuario=="recaudador")
    if usuario.sesionIniciada():
        if tienePermiso:
            indice = basePedidos.buscarPor("codigoUnico", codigoUnico)[0]
            pedido = Pedido(basePedidos, indice)
            pedido.cargar()
            AutorID = usuario.get_ID()
            pedido.cambiarEstado("Finalizado", AutorID)
            basePedidos.guardar()
            funcionLocutor.enviar_respuesta(cliente, '001')
        else:
            funcionLocutor.enviar_respuesta(cliente, '002')
    else:
        funcionLocutor.enviar_respuesta(cliente, '003')

def resivir_echo(cliente, argumentos):
    alerta = argumentos[0]
    funcionLocutor.enviar_alerta(cliente, alerta)

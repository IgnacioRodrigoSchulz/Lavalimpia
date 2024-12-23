from time import sleep

import protocolo_de_comandos as pdc

def echo(client, mensaje):
    comando = ["echo", mensaje]
    pdc.enviar_comandoUnificado(client, comando)
        

def exitt(client):
    sleep(0.05)
    client.send("exit".encode('UTF-8'))
    client.close()
    print("Disconnected from")
    

def solicitud_nuevaCuenta(client, nombreUsuario, contrasena, correo):
    comando = ["nuevaCuenta", str(nombreUsuario), str(contrasena), str(correo)]
    mensaje = pdc.comandoCodificador(comando)
    sleep(0.05)
    client.send(mensaje.encode('UTF-8'))
    

def solicitud_inicioSesion(client, nombreUsuario, contrasena):
    comando = ["iniciarSesion", str(nombreUsuario), str(contrasena)]
    mensaje = pdc.comandoCodificador(comando)
    sleep(0.05)
    client.send(mensaje.encode('UTF-8'))

def solicitud_infoSesion(client):
    comando = ["infoSesion"]
    mensaje = pdc.comandoCodificador(comando)
    sleep(0.05)
    client.send(mensaje.encode('UTF-8'))

def solicitud_crearPedido(client, direccion, usuarioID, tarifa):
    comando = ["crearPedido", str(direccion), str(usuarioID), str(tarifa)]
    mensaje = pdc.comandoCodificador(comando)
    sleep(0.05)
    client.send(mensaje.encode('UTF-8'))

def solicitud_accesoPedido(client, codigo):
    comando = ["accesoPedido", str(codigo)]
    mensaje = pdc.comandoCodificador(comando)
    sleep(0.05)
    client.send(mensaje.encode('UTF-8'))

def solicitud_buscarPedido(client, criterio, valor):
    comando = ["buscarPedido", criterio, valor]
    pdc.enviar_comandoUnificado(client, comando)


def solicitud_accesoUsuario(client, indice):
    comando = ["accesoUsuario", str(indice)]
    mensaje = pdc.comandoCodificador(comando)
    sleep(0.05)
    client.send(mensaje.encode('UTF-8'))

def solicitud_buscarUsuario(client, criterio, valor):
    comando = ["buscarUsuario", criterio, valor]
    pdc.enviar_comandoUnificado(client, comando)

def solicitud_realizarPago(client, codigoPedido):
    comando = ["realizarPago", str(codigoPedido)]
    mensaje = pdc.comandoCodificador(comando)
    sleep(0.05)
    client.send(mensaje.encode('UTF-8'))

from time import sleep

import protocolo_de_comandos as pdc
#from cicloRecibir import client as client

def echo(client, mensaje):

    comando = ["echo", str(mensaje)]
    mensaje = pdc.comandoCodificador(comando)
    sleep(0.05)
    client.send(mensaje.encode('UTF-8'))

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

def solicitud_crearPedido(client):
    pass

def solicitud_accesoPedido(client):
    pass

def solicitud_buscarPedido(client):
    pass

def solicitud_accesoUsuario(client):
    pass

def solicitud_buscarUsuario(client):
    pass

def solicitud_realizarPago(client):
    pass

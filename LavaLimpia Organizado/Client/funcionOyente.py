import socket

from protocolo_de_comandos import comandoDecodificador

host = '0.0.0.0'
port = 5000


def recibir_alerta(argumentos):
    alerta = argumentos[0]
    print(alerta)

def recibir_infoInicioSesion(argumentos):
    print(argumentos)

def recibir_infoPedido():
    pass

def recibir_resultadosBusquedaPedido():
    pass

def recibir_infoUsuario():
    pass

def recibir_resultadosBusquedaUsuario():
    pass




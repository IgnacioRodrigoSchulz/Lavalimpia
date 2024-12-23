import socket

from protocolo_de_comandos import comandoDecodificador
import funcionLocutor

host = '0.0.0.0'
port = 5000


def recibir_alerta(argumentos):
    alerta = argumentos[0]
    print(alerta)

def recibir_infoInicioSesion(argumentos):
    print(argumentos)

def recibir_infoPedido(argumentos):
    pedido = argumentos[0]
    print(pedido)
    #print(pedido["estadoActual"])

def recibir_resultadosBusquedaPedido(argumentos):
    print(argumentos)

def recibir_infoUsuario(argumentos):
    print(argumentos)

def recibir_resultadosBusquedaUsuario(argumentos):
    print(argumentos)


def recibir_respuesta(argumentos):
    codigoRespuesta = argumentos[0]
    print(codigoRespuesta)

    match codigoRespuesta:
        case '201':
            print("Sesión iniciada: usuario.")
        case '202':
            print("Sesión iniciada: gerente.")
        case '203':
            print("Sesión iniciada: operador.")
        case '204':
            print("Sesión iniciada: recaudador.")
        case '205':
            print("Se ha producido un error.")
    

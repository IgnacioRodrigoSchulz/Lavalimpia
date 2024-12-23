import socket
from time import sleep

import protocolo_de_comandos as pdc

def enviar_alerta(cliente, alerta):
    comando = ["alerta", alerta]
    pdc.enviar_comandoUnificado(cliente, comando)


def enviar_infoInicioSesion(cliente, informacion):
    comando = ["infoSesion", str(informacion)]
    pdc.enviar_comandoGeneral(cliente, comando)
    

def enviar_resultadosBusquedaPedido(cliente, resultados):
    comando = ["resultadoBusquedaPedido", resultados]
    pdc.enviar_comandoUnificado(cliente, comando)

def enviar_infoPedido(cliente, informacion):
    #comando = ["alerta", str(informacion)]
    comando = ["infoPedido", informacion]
    pdc.enviar_comandoUnificado(cliente, comando)
    

def enviar_resultadosBusquedaUsuario(cliente, informacion):
    comando = ["resultadoBusquedaUsuario", informacion]
    pdc.enviar_comandoUnificado(cliente, comando)


def enviar_infoUsuario(cliente, informacion):
    comando = ["infoUsuario", informacion]
    pdc.enviar_comandoUnificado(cliente, comando)


def enviar_respuesta(cliente, codigo):
    print(codigo)
    comando = pdc.comandoCodificador(["respuesta", str(codigo)])
    comando = comando.encode('UTF-8')
    cliente.send(comando)
    sleep(0.05)

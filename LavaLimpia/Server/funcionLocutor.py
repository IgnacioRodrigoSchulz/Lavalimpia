import socket
from time import sleep

import protocolo_de_comandos as pdc

def enviar_alerta(cliente, alerta):
    comando = pdc.comandoCodificador(["alerta", str(alerta)])
    comando = comando.encode('UTF-8')
    cliente.send(comando)
    sleep(0.05)

def enviar_infoInicioSesion(cliente, informacion):
    pass

def enviar_resultosBusquedaPedido(cliente, resultados):
    pass

def enviar_infoPedido(cliente, informacion):
    pass

def enviar_resultadosBusquedaUsuario(cliente, informacion):
    pass

def enviar_infoUsuario(cliente, informacion):
    pass

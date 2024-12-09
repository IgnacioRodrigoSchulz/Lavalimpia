import socket

from protocolo_de_comandos import comandoDecodificador
from funcionOyente import *

host = '0.0.0.0'
port = 5000

#client = None


def recibir(client):
    print(client)
    while True:
        try:         
            mensaje = client.recv(1024).decode('UTF-8')
            argumentos = comandoDecodificador(mensaje)
            comando = argumentos.pop(0)
            print(comando)
            if comando == "exit":
                client.close()
                print("Cliente desconectado")
                break

            match comando:
                case "alerta":
                    recibir_alerta(argumentos)

            
        except:
            print("Ocurrio un error")
            client.close()
            break

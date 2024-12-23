import socket

from protocolo_de_comandos import comandoDecodificador, recibir_comandoUnificado
from funcionOyente import *


def recibir(client):
    #print(client)
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

            if comando == "comandolargo":
                repeticiones = int(argumentos[0])
                print(repeticiones)
                mensaje = ""
                for i in range(repeticiones):
                    recibir = client.recv(1024).decode('UTF-8')
                    mensaje += recibir
                    
                argumentos = comandoDecodificador(mensaje)
                comando = argumentos.pop(0)

            if comando == "comandoUnificado":
                mensaje = recibir_comandoUnificado(argumentos[0])
                comando = mensaje[0]
                argumentos = mensaje[1]


            match comando:
                case "alerta":
                    recibir_alerta(argumentos)

                case "respuesta":
                    recibir_respuesta(argumentos)

                case "infoSesion":
                    recibir_infoInicioSesion(argumentos)

                case "infoPedido":
                    recibir_infoPedido(argumentos)

                case "resultadoBusquedaPedido":
                    recibir_resultadosBusquedaPedido(argumentos)                

                case "infoUsuario":
                    recibir_infoUsuario(argumentos)

                case "resultadoBusquedaUsuario":
                    recibir_resultadosBusquedaUsuario(argumentos)
            

            
        except:
            print("Ocurrio un error")
            client.close()
            break

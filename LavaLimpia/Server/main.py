import socket
import threading
from time import sleep

from protocolo_de_comandos import comandoDecodificador
from funcionOyente import *
from basededatosClases import *

##
baseUsuarios = BaseDatos("datatest.json")
baseUsuarios.cargar()
#basePedidos = 

###
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect(("8.8.8.8", 10000))
#host = s.getsockname()[0]
#print(host)
#s.close()


##
#host = '192.168.152.89'
host = '0.0.0.0'
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Crear socket
server.bind((host, port))  # Vincular dirección y puerto

server.listen() #Iniciar servidor

clients = []
###

def handle(client):
    while True:
        try:        #Ciclo de comunicación cliente y servidor
            mensaje = client.recv(1024).decode('UTF-8')
            argumentos = comandoDecodificador(mensaje)
            comando = argumentos.pop(0)
            #print(comando)
            #print(argumentos)
            
            if comando == "exit":
                client.send("exit".encode('UTF-8'))
                clients.remove(client)
                client.close()
                print("Cliente desconectado")
                break

            match comando:
#               case "comandoX":
#                   funcionOyenteX(argumentos)
                case "echo":
                    resivir_echo(client, argumentos)
                    
                case "nuevaCuenta":
                    recibir_nuevaCuenta(client, baseUsuarios, argumentos)

                case "iniciarSesion":
                    usuario = recibir_inicioSesion(client, baseUsuarios, argumentos)
                    print(usuario)
                case "infoSesion":
                    recibir_solicitudInfoSesion(client, usuario)
            
        except:     #Excepcion/fallo de comunicación
            clients.remove(client)
            client.close()
            print("Se ha producido un error en la comunicación")
            break


def receive():
    while True:
        client, address = server.accept() # Aceptar connección
        print(f"Client connected from "+ str(address))

        clients.append(client)

        thread = thread = threading.Thread(target=handle, args=(client,))
        # Empezar nuevo proceso para cada cliente connectado
        thread.start()


print("Server is listening...")
receive()


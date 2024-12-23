import socket
import threading
from time import sleep

from protocolo_de_comandos import comandoDecodificador, recibir_comandoUnificado
from funcionOyente import *
from basededatosClases import *

## Crea las instancias de las bases de datos
# y carga la información de los archivos JSON.
baseUsuarios = BaseDatos("usuariostest.json")
baseUsuarios.cargar()

basePedidos = BaseDatos("pedidostest.json")
basePedidos.cargar()


# Define la dirección del host y define el número del puerto
##
#host = '192.168.152.89'
host = '0.0.0.0'
port = 5000

# Crea instancia del socket que sera usado como server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
# AF_INET es la familia de direcciones IPv4 (Protocolo de internet versión 4)
# SOCK_STREAM tipo de socket para TCP (Protocolo de control de transmisión)


# Vincula dirección del host y número de puerto con el socket
server.bind((host, port))

# Inicia el socket, lo habilita para recibir conexiones.
server.listen()

# Clients es una lista de sockets
clients = []


# Ciclo de comunicación cliente y servidor
#Recibe como argumento la referencia al socket donde se envía y recibe información
def handle(client):
    while True:
        try:
            # Espera a recibir un mensaje del cliente
            #Este mensaje lo decodifica y separa,
            #El primer elemento sera considerado como un comando o instrucción
            #Los siguientes elementos seran considerados argumentos
            mensaje = client.recv(1024).decode('UTF-8')
            argumentos = comandoDecodificador(mensaje)
            comando = argumentos.pop(0)

            # A continuación los comandos reservados para la comunicación
            
            # Si el comando es exit, entonces se cerrara la comunicación.
            if comando == "exit":
                client.send("exit".encode('UTF-8'))
                clients.remove(client)
                client.close()
                print("Cliente desconectado")
                break

            # Este comando es para indicar que el mensaje enviado se trata
            #de un mensaje mayor a 1024, y debe ser recibido a través de un ciclo
            if comando == "comandolargo":
                repeticiones = int(argumentos[0])
                print(repeticiones)
                mensaje = ""
                for i in range(repeticiones):
                    recibir = client.recv(1024).decode('UTF-8')
                    mensaje += recibir
                    
                argumentos = comandoDecodificador(mensaje)
                comando = argumentos.pop(0)
                
            # Este comando indica que sus elementos estan en un string formato JSON.
            #El mensaje sera decodificado a datos trabajables en python.
            if comando == "comandoUnificado":
                mensaje = recibir_comandoUnificado(argumentos[0])
                comando = mensaje[0]
                argumentos = mensaje[1]

            print(comando)
            # A continuación los comandos referentes a las solicitudes del cliente
            
            match comando:
                
                #  La estructura es un string que es el comando
                # y una funcion oyente, que realiza operaciones en el sistema
               #case "comandoX":
                   #funcionOyenteX(argumentos)

                # El comando echo envía los mismos argumentos devuelta
                # al cliente, se utiliza principalmente para verificar
                # que la conexión es correcta.
                case "echo":
                    resivir_echo(client, argumentos)

                # Crea una cuenta nueva
                case "nuevaCuenta":
                    recibir_nuevaCuenta(client, baseUsuarios, argumentos)

                case "iniciarSesion":
                    usuario = recibir_inicioSesion(client, baseUsuarios, argumentos)

                case "infoSesion":
                    recibir_solicitudInfoSesion(client, usuario)
                case "crearPedido":
                    recibir_crearPedido(client, basePedidos, baseUsuarios, usuario, argumentos)

                case "accesoPedido":
                    recibir_accesoPedido(client, basePedidos, usuario, argumentos)
                    
                case "buscarPedido":
                    recibir_buscarPedido(client, basePedidos, usuario, argumentos)
                    
                case "accesoUsuario":
                    recibir_accesoUsuario(client, baseUsuarios, usuario, argumentos)
                    
                case "buscarUsuario":
                    recibir_buscarUsuario(client, baseUsuarios, usuario, argumentos)

                case "realizarPago":
                    recibir_realizarPago(client, basePedidos, usuario, argumentos)
                    
            
        except:     #Excepcion/fallo de comunicación
            clients.remove(client)
            client.close()
            print("Se ha producido un error en la comunicación")
            break


# Ciclo receive
#El programa esta esperando conexiones,
#Para las cuales crea un proceso separado
#Donde se comunican con el programa del servidor.
def receive():
    while True:
        client, address = server.accept() # Acepta la connección entrante
        #client es un objeto de tipo socket,
        #utilizado para enviar y recibir información
        print(f"Client connected from "+ str(address))

        #Añade el socket del cliente a la lista de sockets
        clients.append(client)

        # Crea un nuevo hilo por cada conexión
        thread = thread = threading.Thread(target=handle, args=(client,))
        # Empieza como proceso
        thread.start()
        # Cada proceso o hilo corre de manera asincrónica


print("Server is listening...")
receive()


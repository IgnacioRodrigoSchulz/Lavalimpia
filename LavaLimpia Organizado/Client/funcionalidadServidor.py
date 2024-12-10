import socket #sirve para establecer conexiones en procesos y transferir datos
import threading # módulo que permite gestionar y crear hilos un programa, un hilo es la unidad de ejecución que puede ejecutar una tarea independientemente del resto del programa 
import commandProtocol
from time import sleep #permite parar la ejecución del programa en un tiempo determinado 

host = '0.0.0.0'
port = 5000

def conectarServidor():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    #print("Connected to")


# Funciones para enviar comandos al servidor

def alert(arguments):
    print(arguments[0])

def salir():
    sleep(0.05)
    client.send("exit".encode('UTF-8')) # representa textos que contienen diferentes idiomas y alfabetos.
    client.close()
    print("Disconnected from")

def registrarUsuario(username,password):
#Cadena de strings, el primer string es la funcion, los siguientes son argumentos.
    command = ["add", str(username), str(password)]
    message = commandProtocol.commandEncoder(command)
    sleep(0.05)
    client.send(message.encode('UTF-8')) 

def iniciarSesion(username, password):
    command = ["login", str(username), str(password)]
    message = commandProtocol.commandEncoder(command)
    sleep(0.05)
    client.send(message.encode('UTF-8'))




def recibir():
    while True:
        try:         
            message = client.recv(1024).decode('UTF-8')
            arguments = commandProtocol.commandDecoder(message)
            command = arguments.pop(0) # .pop(0) elimina y devuelve el primer termimo de una lista
            if command == "exit": 
                client.close()
                print("Cliente desconectado")
                break

            match command:
                case "print":
                    print("server: " + arguments[0])

                case "alert":
                    alert(arguments)

            
        except:
            print("Ocurrio un error")
            client.close()
            break

#receive_thread = threading.Thread(target=receive)
#receive_thread.start()


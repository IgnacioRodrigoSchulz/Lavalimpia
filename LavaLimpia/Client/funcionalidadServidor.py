import socket
import threading
import commandProtocol
from time import sleep

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
    client.send("exit".encode('UTF-8'))
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
            command = arguments.pop(0)
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


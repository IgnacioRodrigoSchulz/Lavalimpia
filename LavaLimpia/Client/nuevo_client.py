import socket
import threading
import commandProtocol
from time import sleep

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 5000))
print("Connected to")



def alerta(arguments):
    print(arguments[0])



def exitt():
    sleep(0.05)
    client.send("exit".encode('UTF-8'))
    client.close()
    print("Disconnected from")

def registrarUsuario(username,password):
    command = ["add", str(username), str(password)]
    message = commandProtocol.commandEncoder(command)
    sleep(0.05)
    client.send(message.encode('UTF-8'))

def iniciarSesion(username, password):
    command = ["login", str(username), str(password)]
    message = commandProtocol.commandEncoder(command)
    sleep(0.05)
    client.send(message.encode('UTF-8'))

def echo(mensaje):
    command = ["echo", str(mensaje)]
    message = commandProtocol.commandEncoder(command)
    sleep(0.05)
    client.send(message.encode('UTF-8'))


def receive():
    while True:
        try:         
            message = client.recv(1024).decode('UTF-8')
            #print(message)
            arguments = commandProtocol.commandDecoder(message)
            command = arguments.pop(0)
            #print(command)
            if command == "exit":
                client.close()
                print("Client disconnected")
                break

            match command:
                case "print":
                    print("server:" + arguments[0])

                case "alerta":
                    alerta(arguments)


            
        except:
            print("An error ocurred!")
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

#registrarUsuario("Pepito", "Perez")

echo("Lechuga")
echo("Tomate")
echo("mesa")


sleep(1)
exitt()

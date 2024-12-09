import socket


def client_program():

    # Programa principal // Antes del ciclo
    host = '0.0.0.0'
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input
    
    # Ciclo principal
    while message.lower().strip() != 'bye': # El servidor terminara con la palabra clave
        client_socket.send(message.encode())  # Enviar request/mensaje (String)
        data = client_socket.recv(1024).decode()  # Recibir mensaje(String)

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

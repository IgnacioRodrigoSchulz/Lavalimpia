import socket
import threading
from time import sleep

from cicloRecibir import recibir
import funcionLocutor

# Define la dirección del host, y el número de puerto
host = '0.0.0.0'
port = 5000

# Crea instancia del socket que sera usado para comunicarse con el server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET es la familia de direcciones IPv4 (Protocolo de internet versión 4)
# SOCK_STREAM tipo de socket para TCP (Protocolo de control de transmisión)

# Vincula dirección del host y número de puerto con el socket
client.connect((host, port))
print("Connected to")
print(client)

#Crea el proceso del ciclo recibir que estara constantemente
# recibiendo mensajes del servidor
ciclo_recibir = threading.Thread(target=recibir, args=(client,))
#En este ciclo se realizara la comunicación desde el server hacia el cliente.
# Server --> Cliente

# Inicia el hilo de recibir, que sera distinto al hilo principal,
#Donde se enviaran mensajes hacia el servidor.
ciclo_recibir.start()


##########
# Hilo principal
# En este proceso se realizara la comunicación desde el cliente hacia el server
# Cliente --> Server

# En este proceso se ejecutan las funciones locutor,
# estas convierten los argumentos a un formato apto para enviar al servidor
# Como primer argumento toda función locutor debe recibir una referencia
# al socket donde se quiere enviar el mensaje.
sleep(1)


# La función echo recibe cualquier valor, lo envía al servidor y el servidor lo envía devuelta.
#sirve para verificar que la conexión esta correcta.
#funcionLocutor.echo(client, "Hola")


# La función solicitud_nuevaCuenta() debe recibir nombre, contraseña y correo.
#funcionLocutor.solicitud_nuevaCuenta(client, "gerente", "gerencia123", "gerencia@general.com")
#funcionLocutor.solicitud_nuevaCuenta(client, "juan", "perez123", "pereira@mail.net")

# La función solicitud_inicioSesion() debe recibir nombre y contraseña.
funcionLocutor.solicitud_inicioSesion(client, "gerente", "gerencia123")
#funcionLocutor.solicitud_inicioSesion(client, "juan", "perez123")

# La función solicitud_infoSesion() solo debe recibir el socket como argumento.
funcionLocutor.solicitud_infoSesion(client)


# La función solicitud_accesoUsuario() debe recibir el codigo único del usuario
# del que se quiere obtener la información
#funcionLocutor.solicitud_accesoUsuario(client, "3")


# La función solicitud_crearPedido() debe recibir dirección, codigo único del usuario y valor de la tarifa.
#funcionLocutor.solicitud_crearPedido(client, "avenida 12", "4", 3500)

# La función solicitud_accesoPedido() debe recibir el codigo único del pedido
# que se quiere obtener la información
#funcionLocutor.solicitud_accesoPedido(client, "0")

 
# La función solicitud_buscarPedido() debe recibir una llave y un valor para buscar en la base de pedidos.
#funcionLocutor.solicitud_buscarPedido(client, "direccion", "avenida 12")

# La función solicitud_buscarUsuario() debe recibir una llave y un valor para buscar en la base de usuarios.
#funcionLocutor.solicitud_buscarUsuario(client, "nombre", "alfonso")

# La función solicitud_buscarUsuario() debe recibir el codigo unico del pedido que se desea pagar.
#funcionLocutor.solicitud_realizarPago(client, "0")

sleep(1)


funcionLocutor.exitt(client)

import socket
import threading
from time import sleep

from cicloRecibir import recibir
#from cicloRecibir import client
import funcionLocutor

host = '0.0.0.0'
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print("Connected to")
print(client)

#recibir(client)

ciclo_recibir = threading.Thread(target=recibir, args=(client,))
ciclo_recibir.start()


##########
sleep(1)

#funcionLocutor.solicitud_nuevaCuenta(client, "joaquin", "pepito123", "correo@pepi.to")
#funcionLocutor.solicitud_nuevaCuenta(client, "pedro", "perez", "pereira@mail.net")
funcionLocutor.solicitud_inicioSesion(client, "joaquin", "pepito52")

sleep(1)

funcionLocutor.exitt(client)

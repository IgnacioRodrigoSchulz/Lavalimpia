from time import sleep
import json

# Recibe bytes de entrada y un tamaño de división,
#devuelve una lista de bytes,
# cada elemento de la lista es igual o menor en tamaño
#al tamaño de división.
def dividirBytes(bytesEntrada, tamanoDivision):
    tamano = len(bytesEntrada)
    repeticiones = tamano // tamanoDivision
    resto = tamano % tamanoDivision

    listaBytes = []
    for repeticion in range(repeticiones):
        baits = []
        for i in range(tamanoDivision):
            baits.append(bytesEntrada[(repeticion*tamanoDivision)+i])
        listaBytes.append(bytes(baits))

    baits = []
    for i in range(resto):
        baits.append(bytesEntrada[(repeticiones*tamanoDivision)+i])

    if len(baits) > 0:
        listaBytes.append(bytes(baits))

    return listaBytes

# Recibe un string
#Los separa de acuerdo a un carácter separador.
#devuelve una lista de todos los elementos
def comandoDecodificador(mensaje):
    separador = '𓂸'
    comando = mensaje.split(separador)
    return comando

# Recibe una lista
#Junta todos los elementos de la lista en un string
#dentro del string los elementos son separados por un carácter separador
#devuelve el string
def comandoCodificador(comando):
    separador = '𓂸'
    mensaje = separador.join(comando)
    return mensaje

# Dada una referencia a un socket, y dado un string.
#se envia la información a tráves del socket,
#separando el string en conjuntos de bytes menores a 1024,
#cada parte se envía por separado utilizando un ciclo
def enviar_comandoLargo(socket, comandoEntrada):
    comandoMensaje = comandoEntrada.encode('UTF-8')
    tamano = len(comandoMensaje)

    repeticiones = (tamano//1024)+1

    listaBytes = dividirBytes(comandoMensaje, 1024)

    comando = ["comandolargo", str(repeticiones)]
    mensaje = comandoCodificador(comando)
    socket.send(mensaje.encode('UTF-8'))
    sleep(0.05)

    for i in listaBytes:
        socket.send(i)
        sleep(0.05)

# Dada una referencia a un socket, y dado un string.
#Si el tamaño del string en bytes es menor a 1024,
#entonces se envía normalmente.
#De lo contrario, se envia utilizando enviar_comandoLargo()
def enviar_comandoGeneral(socket, comandoEntrada):
    comando = comandoCodificador(comandoEntrada)
    mensaje = comando.encode('UTF-8')
    if len(mensaje) <= 1024:
        socket.send(mensaje)
        sleep(0.05)
    else:
        enviar_comandoLargo(socket, comando)


# Dada una referencia a un socket, y dada una lista.
# El primer elemento de la lista debe ser un comando
#referente al ciclo de comunicación entre cliente y servidor
# El segundo elemento de la lista es otra lista, que contiene argumentos
#Los argumentos pueden ser cualquier objeto o dato válido:
#Número, cadena o string, booleano, lista, y diccionario.
# La función convierte los datos a JSON
#y envía el string del JSON a través del socket
def enviar_comandoUnificado(socket, comandoEntrada):
    argumentos = comandoEntrada
    comando = argumentos.pop(0)
    mensaje = json.dumps([comando, argumentos])
    enviar_comandoGeneral(socket, ["comandoUnificado" ,mensaje])

# Recibe un string JSON, y lo convierte en un dato trabajable en python
def recibir_comandoUnificado(argumentosEntrada):
    resultado = json.loads(argumentosEntrada)
    return resultado

# La ventaja de este metodo es que a diferencia de enviar_comandoGeneral() (Solo envía string),
# enviar_comandoUnificado(), es capaz de enviar todo tipo de dato,
# y ademas enviar estructuras de datos mas complejas, como listas y diccionarios.



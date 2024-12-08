#https://docs.python.org/3/library/json.html
#https://docs.python.org/3/library/functions.html#open

import json

def guardar(nombreArchivo, data):
    with open(nombreArchivo, 'w') as archivo:
        json.dump(data, archivo)


def cargar(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
        data = json.load(archivo)
    return data

#https://docs.python.org/3/library/json.html
#https://docs.python.org/3/library/functions.html#open

import json

#Dado el nombre de un archivo e información.
#Guarda la información en formato JSON dentro del archivo.
def guardar(nombreArchivo, data):
    with open(nombreArchivo, 'w') as archivo:        
        json.dump(data, archivo,indent=2)

#Dado el nombre de un archivo.
#Lo lee y devuelve la información
#El archivo debe estar en formato JSON.
def cargar(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
        try:
            data = json.load(archivo)
        except:
            data = []
       
    return data

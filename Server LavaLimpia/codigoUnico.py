#https://docs.python.org/3/library/json.html
#https://docs.python.org/3/library/datetime.html
#https://www.w3schools.com/python/python_datetime.asp
from time import sleep
from datetime import datetime, timedelta
from math import log

from basededatosClases import BaseDatos

# Dado un valor entero,
#devuelve un string del mismo número en base 32.
def decimal_a_base32(entero):
    enteroStr = str(entero)
    base32nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V')

    magnitud = int(log(entero, 32)//1)
    resto = entero
    base32 = ''
    for i in range(1, magnitud+2):
        num = resto//(32**(magnitud-i+1))
        resto = resto - num*(32**(magnitud-i+1))
        caracter = base32nums[num]
        base32 += caracter
    
    return base32

# Dado un string de un número en base 32,
#Devuelve el valor decimal del número.
def base32_a_decimal(base32):    
    base32nums = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31}
    base32str = base32.upper()
    largo = len(base32str)

    suma = 0    
    for i in range(largo):        
        char = base32str[largo-i-1]
        suma += base32nums[char]*(32**i)

    return suma

# Dado un número en base 32,
#devuelve su número sucesor en base 32.
def base32_sumar1(base32):    
    return decimal_a_base32(base32_a_decimal(base32)+1)

#Devuelve un string de la fecha actual
def fechaActual():
    fechaActual = datetime.now().strftime("%Y-%m-%d %H:%M")
    return(fechaActual)

#Dado un número entero de dias, y un string de una hora fija.
#devuelve un string de la fecha n dias adelante desde la fecha actual,
#y una hora fija dada por el usuario.
def fecha_diasEnAdelante(diasAdelante, horaLimite):
    fechaDespues = (datetime.now()+timedelta(days=diasAdelante)).strftime("%Y-%m-%d")
    fechaDespues += (' '+ horaLimite)
    return fechaDespues
    
# Dada una referencia a un objeto de clase BaseDatos.
#Busca el código único del ultimo elemento
#y devuelve el sucesor, resultando en un código nuevo.
def codigoUnico(database):
    database.cargar()
    data = database.getData()
    if len(data) > 0:
        ultimoCodigoBase32 = data[len(data)-1]["codigoUnico"]
        nuevoCodigo = base32_sumar1(ultimoCodigoBase32)
    else:
        nuevoCodigo = '0'
        
    return nuevoCodigo



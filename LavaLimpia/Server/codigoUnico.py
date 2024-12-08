#https://docs.python.org/3/library/json.html
from time import sleep
from datetime import datetime
from basededatosClases import BaseDatos

def entero_a_base32(num):
    if num == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUV"  # Caracteres para base 32
    base32_str = ""
    
    while num > 0:
        base32_str = digits[num % 32] + base32_str  # Obtiene el dígito correspondiente y lo agrega al inicio
        num = num // 32  # Divide el número por 32
    
    return base32_str

def base32_a_entero(base32_str):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUV"  # Caracteres para base 32
    base32_str = base32_str.upper()  # Asegurarse de que las letras sean mayúsculas
    num = 0
    
    for i, char in enumerate(base32_str):
        value = digits.index(char)  # Obtiene el valor numérico del carácter
        num = num * 32 + value  # Convierte a decimal
    
    return num

def sumar1(base32):
    return entero_a_base32(base32_a_entero(base32)+1)


def fechaActual():
    fechaActual = datetime.now().strftime("%Y-%m-%d %H:%m")
    return(fechaActual)


def codigoUnico():
    database = BaseDatos("codigoUnicoTest.json")
    database.cargar()

    data = database.getData()
    ultimoCodigo = data[len(data)-1]["codigoUnico"]

    nuevoCodigo = sumar1(ultimoCodigo)
    nuevoCodigo = (8-len(nuevoCodigo))*"0" + nuevoCodigo
    return nuevoCodigo


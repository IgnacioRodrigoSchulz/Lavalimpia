def comandoDecodificador(mensaje):
    separador = '𓂸'
    comando = mensaje.split(separador)
    return comando

def comandoCodificador(comando):
    separador = '𓂸'
    mensaje = separador.join(comando)
    return mensaje



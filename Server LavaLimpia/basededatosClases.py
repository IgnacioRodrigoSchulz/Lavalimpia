import jsonLector

from datetime import datetime
def fechaActual():
    fechaActual = datetime.now().strftime("%Y-%m-%d %H:%M")
    return fechaActual


# Clase general para las bases de datos
#Se utiliza tanto para la base de los usuarios como los pedidos.

class BaseDatos():
    #Se inicia con el nombre del archivo único argumento,
    #El archivo debe ser de tipo JSON.
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        self.data = []

    # Lee el archivo JSON y guarda su contenido en el atributo data.
    # El contenido es una lista de diccionarios.
    def cargar(self):
        self.data = jsonLector.cargar(self.nombreArchivo)
        
    # Guarda el la lista de diccionarios en el archivo JSON.
    def guardar(self):
        jsonLector.guardar(self.nombreArchivo, self.data)

    # Devuelve el atributo data (Lista de diccionarios).
    def getData(self):
        return self.data
    
    # Dado un numero entero como índice,
    # se devuelve el diccionario ubicado en tal índice.
    def getItem(self, indice):
        return self.data[indice]

    # Dado un string como llave o criterio de busqueda, y un valor
    # que debe coincidir.
    # Se realiza una busqueda sobre cada elemento de la lista.
    # Se devuelve una lista de índices de todos los diccionarios
    # que el valor de su llave coincidió con el valor dado.
    def buscarPor(self, llave, valor):
        listaIndices = []
        for itemIndice in range(len(self.data)):
            if self.data[itemIndice][llave] == valor:
                listaIndices.append(itemIndice)
        return listaIndices

    # Recibe un diccionario y lo añade al final de la lista de diccionarios
    def anadir(self, item):
        self.data.append(item)

    # Dado un índice y una llave,
    # se modifica el valor de la llave
    # del diccionario en el índice indicado
    # por el nuevo valor ingresado
    def modificarValor(self, indice, llave, valor):
        self.data[indice][llave] = valor

# Antes de realizar cualquier operación se debe utilizar el metodo "cargar"
#Para asegurarse de tener los datos actualizados desde el archivo JSON.
# Para utilizar el metodo "buscarPor" todos los diccionarios en la base de datos
#deben contener la llave que se esta buscando.
# Despues de realizar cualquier operación o modificacion se debe utilizar
#el metodo "guardar" para asegurarse que los datos se actualizen al archivo JSON.


# Clase del usuario.
#Se utiliza para hacer seguimiento de la sesión de un usuario
#y realizar modificaciones en la base de datos

class Usuario():
    #Debe iniciarse con una referencia a la base de datos
    #y el índice del usuario en la base de datos
    def __init__(self, baseDatos, indice):
        usuario = baseDatos.getItem(indice)
        
        self._baseDatos = baseDatos
        self._indice = indice
        self._id = usuario["codigoUnico"]
        
        self.nombre = ""
        self.contrasena = ""
        self.correo = ""

        self._pedidos = []
        self._tipoUsuario = ""

        self.fechaCreacion = ""
        
        self._sesionIniciada = False
        
    # Carga informacion desde los datos de la base de datos
    #y los guarda en los atributos del objeto usuario.
    def cargar(self):
        usuario = self._baseDatos.getItem(self._indice)
        self.nombre = usuario["nombre"]
        self.contrasena = usuario["contrasena"]
        self.correo = usuario["correo"]

        self._pedidos = usuario["pedidos"]
        self._tipoUsuario = usuario["tipoUsuario"]

        self.fechaCreacion = usuario["fechaCreacion"]

    # Devuelve el id o codigo único del usuario (un número en base32)
    def get_ID(self):
        return self._id

    # Guarda información modificada a los datos de la base de datos.
    def guardar(self):
        self._baseDatos.modificarValor(self._indice, "nombre", self.nombre)
        self._baseDatos.modificarValor(self._indice, "contrasena", self.contrasena)
        self._baseDatos.modificarValor(self._indice, "correo", self.correo)

    # Devuelve un diccionario con los datos del usuario
    def get_datos(self):
        usuario = {}

        usuario["nombre"] = self.nombre
        usuario["correo"] = self.correo

        usuario["pedidos"] = self._pedidos

        usuario["fechaCreacion"] = self.fechaCreacion
        usuario["tipoUsuario"] = self._tipoUsuario

        usuario["ID"] = self._id

        return usuario        

    # Cambia el tipo de usuario
    def set_tipoUsuario(self, tipo):
        esValido = False
        if tipo == "cliente":
            esValido = True
        elif tipo == "recaudador":
            esValido = True
        elif tipo == "operador":
            esValido = True
        elif tipo == "gerente":
            esValido = True

        if esValido:
            self._tipoUsuario = tipo
            self._baseDatos.modificarValor(self._indice, "tipoUsuario", tipo)

    # Devuelve el tipo de usuario
    def get_tipoUsuario(self):
        return self._tipoUsuario

    # Asocia un pedido al usuario
    #Añade el código único del pedido a la lista de pedidos del usuario
    #y lo guarda en los datos de la base de datos.
    def anadirPedido(self, pedidoCodigo):
        self._pedidos.append(pedidoCodigo)
        self._baseDatos.modificarValor(self._indice, "pedidos", self._pedidos)

    # Devuelve una lista que contiene el código único de los pedidos
    #asociados al usuario.
    def get_pedidos(self):
        return self._pedidos

    # Dada una contraseña,
    #si esta contraseña coincide con la del usuario se inicia sesión
    def iniciarSesion(self, contrasena):
        if self.contrasena == contrasena:
            self._sesionIniciada = True

    # Cierra la sesión
    #Cambia el estado de sesionIniciada a False.
    def cerrarSesion(self):
        self._sesionIniciada = False

    # Devuelve el booleano de sesionIniciada
    def sesionIniciada(self):
        return self._sesionIniciada

########


# Clase del pedido

class Pedido():
    def __init__(self, baseDatos, indice):
        self._baseDatos = baseDatos
        self._indice = indice

        self.direccion = ""

        self.codigoUnico = 0        
        self.usuario = 0
        self.tarifa = 0

        self.fechaCreacion = ""
        self.fechaPlazo = ""
        
        self.estadoActual = ""

        self._estadoHistorial = []
        
    def cargar(self):
        pedido = self._baseDatos.getItem(self._indice)
        
        self.direccion = pedido["direccion"]

        self.codigoUnico = pedido["codigoUnico"]
        self.usuario = pedido["usuario"]
        self.tarifa = pedido["tarifa"]

        self.fechaCreacion = pedido["fechaCreacion"]
        self.fechaPlazo = pedido["fechaPlazo"]
        
        self.estadoActual = pedido["estadoActual"]

        self._estadoHistorial = pedido["estadoHistorial"]

    def guardar(self):
        pass

    def get_datos(self):
        pedido = {}

        pedido["direccion"] = self.direccion

        pedido["codigoUnico"] = self.codigoUnico
        pedido["usuario"] = self.usuario
        pedido["tarifa"] = self.tarifa

        pedido["fechaCreacion"] = self.fechaCreacion
        pedido["fechaPlazo"] = self.fechaPlazo
        
        pedido["estadoActual"] = self.estadoActual

        pedido["estadoHistorial"] = self._estadoHistorial

        return pedido
    

    def cambiarEstado(self, nuevoEstado, usuarioAutor):
        fecha_actual = fechaActual()
        self.estadoActual = nuevoEstado
        accionRealizada = [fecha_actual, nuevoEstado, usuarioAutor]
        self._estadoHistorial.append(accionRealizada)

        self._baseDatos.modificarValor(self._indice, "estadoActual", nuevoEstado)
        self._baseDatos.modificarValor(self._indice, "estadoHistorial", self._estadoHistorial)

################
# Los metodos de las clases Usuario y pedido
#modifican los datos de la base de datos,
#y no el archivo JSON.

# Los datos de la base de datos son temporales
#y sus cambios no se ven reflejados en el archivo JSON.
#para esto se debe usar el metodo guardar de la clase BaseDatos.

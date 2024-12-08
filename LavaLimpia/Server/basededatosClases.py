import jsonLector


class BaseDatos():
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        self.data = []

    def cargar(self):
        self.data = jsonLector.cargar(self.nombreArchivo)
        
    def guardar(self):
        jsonLector.guardar(self.nombreArchivo, self.data)

    def getData(self):
        return self.data

    def getItem(self, indice):
        return self.data[indice]

    def buscarPor(self, llave, valor):
        listaIndices = []
        for itemIndice in range(len(self.data)):
            if self.data[itemIndice][llave] == valor:
                listaIndices.append(itemIndice)
        return listaIndices
    
    def anadir(self, item):
        self.data.append(item)
    
    def modificarValor(self, indice, llave, valor):
        self.data[indice][llave] = valor
        
    
class Usuario():
    def __init__(self, baseDatos, indice):
        self._baseDatos = baseDatos
        self._indice = indice
        
        self.nombre = ""
        self.contrasena = ""
        self.correo = ""

        self._pedidos = []
        self._tipoUsuario = ""

        self.fechaCreacion = ""
        
        self._sesionIniciada = False
        

    def cargar(self):
        usuario = self._baseDatos.getItem(self._indice)
        self.nombre = usuario["nombre"]
        self.contrasena = usuario["contrasena"]
        self.correo = usuario["correo"]

        self._pedidos = usuario["pedidos"]
        self._tipoUsuario = usuario["tipoUsuario"]

        self.fechaCreacion = usuario["fechaCreacion"]

    def guardar(self):
        usuario = {}

        self._baseDatos.modificarValor(self._indice, "nombre", self.nombre)
        self._baseDatos.modificarValor(self._indice, "contrasena", self.contrasena)
        self._baseDatos.modificarValor(self._indice, "correo", self.correo)
        

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
            

    def anadirPedido(self, pedidoIndice):
        self._pedidos.append(pedidoIndice)
        self._baseDatos.modificarValor(self._indice, "pedidos", self._pedidos)        

    def get_pedidos(self):
        return self._pedidos

    def iniciarSesion(self, contrasena):
        if self.contrasena == contrasena:
            self._sesionIniciada = True

    def cerrarSesion(self):
        self._sesionIniciada = False

    def sesionIniciada(self):
        return self._sesionIniciada


class Pedido():
    def __init__(self, baseDatos, indice):
        self._baseDatos = baseDatos
        self._indice = indice

        self.direccion = ""

        self.codigoUnico = 0        
        self.usuario = 0
        self.tarifa = 0

        self.fechaCreacion = ""
        self.estadoActual = ""

        self._estadoHistorial = []
        
    def cargar(self):
        pedido = self._baseDatos.getItem(self._indice)
        
        self.direccion = pedido["direccion"]

        self.codigoUnico = pedido["codigoUnico"]
        self.usuario = pedido["usuario"]
        self.tarifa = pedido["tarifa"]

        self.fechaCreacion = pedido["fechaCreacion"]
        self.estadoActual = pedido["estadoActual"]

        self._estadoHistorial = pedido["estadoHistorial"]

    def cambiarEstado(self, nuevoEstado, usuarioAutor):
        self.estadoActual = nuevoEstado
        accionRealizada = ["FechaActual/Hora", nuevoEstado, usuarioAutor]
        self._estadoHistorial.append(accionRealizada)

        self._baseDatos.modificarValor(self._indice, "estadoActual", nuevoEstado)
        self._baseDatos.modificarValor(self._indice, "estadoHistorial", self._estadoHistorial)

###########################


from abc import ABC, abstractmethod
from descuentos.descuento import DescuentoMembresia, DescuentoTemporada
from boutique.boutique import Boutique
class Cliente(ABC):
    """
        Clase abstracta que representa un cliente.
    """
    def __init__(self, nombre, email, telefono):
        # Inicializa los atributos del cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        # Crea una lista vacía para almacenar el carrito del cliente
        self.carrito = []
        # Crea un atributo para almacenar el descuento del cliente, que se define en las subclases
        self.descuento = 0 
        #self.boutique = Boutique

        @property
        def descuento(self):
            return self._descuento

        @descuento.setter
        def descuento(self, nuevo_descuento):
            self._descuento = nuevo_descuento

    def agregar_carrito(self, producto):
        self.carrito.append(producto)

    def mostrar_carrito(self):
        # Muestra el contenido del carrito del cliente y el total a pagar
        print(f"Carrito de {self.nombre}:")
        total = 0
        for producto, precio_base in self.carrito:
            print(f"- {producto.nombre}: {precio_base}")
            total += precio_base
        print(f"Total: {total}")
    
    def calcular_descuento(self):
        self.descuento = 0.0



class ClienteFiel:
    """
    Clase que representa a un cliente fiel.
    """
    def __init__(self, cliente,membresia):
        self.cliente = cliente
        # Asigna el atributo de membresía al cliente fiel
        self.membresia = membresia
        # Calcula el descuento que le corresponde al cliente fiel según su membresía
        self.calcular_descuento()

    def calcular_descuento(self):
        # Calcula el descuento que le corresponde al cliente fiel según su membresía
        if self.membresia.membresia == "nivel3":
            self.descuento = self.membresia.porcentaje
        elif self.membresia.membresia == "nivel2":
            self.descuento = self.membresia.porcentaje
        elif self.membresia.membresia == "nivel1":
            self.descuento = self.membresia.porcentaje
        
    #def agregar_carrito(self, producto):
    # self.cliente.agregar_carrito.append(producto)

class ClienteOcasional:
    """
    Clase que representa a un cliente ocasional.
    """
    def __init__(self,cliente=None, desc_temporada = None):
        self.cliente = cliente
        self.desc_temporada = desc_temporada
        self.calcular_descuento()

    def  calcular_descuento(self):
        if self.desc_temporada:
            self.descuento = self.desc_temporada.porcentaje
        else:
            self.descuento = 0.0

    #def agregar_carrito(self, producto):
        #self.carrito.append(producto)
        #ya en un futuro podria agregar funcionesque sirvan para clientes ocasionales




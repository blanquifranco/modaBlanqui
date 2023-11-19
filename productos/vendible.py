from abc import ABC, abstractmethod

class Vendible(ABC):
    """
    Clase abstracta que representa un producto vendible.
    """
    def __init__(self, nombre, precio):
        """
        Constructor de la clase Vendible.
        Args:
            nombre (str): Nombre del producto.
            precio_base (float): Precio base del producto.
        """
        # Inicializa los atributos del producto vendible
        self.nombre = nombre
        self.precio = precio
        # Crea un atributo para almacenar el descuento del producto, que se define en las subclases
        self.descuento = None

    def calcular_descuento(self):
        """
        Metodo paracalcular el precio decuento del producto.
        Debe ser implementado por las subclases.
        """
        # Calcula el descuento que le corresponde al producto según su tipo, se implementa en las subclases
        pass

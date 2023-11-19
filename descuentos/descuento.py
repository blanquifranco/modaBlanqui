from abc import ABC, abstractmethod

class Descuento(ABC):
    '''
    Clase abstracta que representa un descuento.'''
    def __init__(self, porcentaje):
        # Inicializa los atributos del descuento
        self.porcentaje = porcentaje

    def aplicar(self, producto):
        # Aplica el descuento a un producto, se implementa en las subclases
        pass

class DescuentoMembresia(Descuento):
    '''
    Clase que representa un descuento por membresía.'''
    def __init__(self,porcentaje, membresia):
        # Inicializa los atributos del descuento por membresía, llamando al constructor de la superclase
        super().__init__(porcentaje)
        # Asigna el atributo de membresía al descuento por membresía
        self.membresia = membresia

    def aplicar(self, producto):
        # Aplica el descuento por membresía a un producto, si el cliente tiene la misma membresia que el descuento
        if producto.cliente.membresia == self.membresia:
            # Asigna el porcentaje del descuento al atributo descuento del producto
            producto.descuento = self.porcentaje
        else:
            # No aplica el descuento al producto
            producto.descuento = 0


class DescuentoTemporada(Descuento):
    '''
    Clase que representa un descuento por temporada.'''
    def __init__(self,porcentaje, temporada):
        # Inicializa los atributos del descuento por temporada, llamando al constructor de la superclase
        super().__init__(porcentaje)
        # Asigna el atributo de temporada al descuento por temporada
        self.temporada = temporada

    def aplicar(self, producto):
    
            producto.descuento = porcentaje
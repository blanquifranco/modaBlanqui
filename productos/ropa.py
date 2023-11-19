from . import Vendible

class Ropa(Vendible):
    '''Clase que representa a una prenda que es vendible'''
    def __init__(self,codigo, nombre, precio, talla, color, material):
        # Inicializa los atributos de la ropa, llamando al constructor de la superclase
        super().__init__(nombre, precio)
        # Asigna los atributos específicos de la ropa
        self.talla = talla
        self.color = color
        self.material = material
        self.codigo = codigo
        self.descuento = None
    def mostrar(self):
        # Muestra la información de la ropa, incluyendo el nombre, el precio, la talla, el color y el material
        pass
        #return muestra


class Vestido(Ropa):
    '''Clase que representa a un vestido de la boutique'''
    def __init__(self,codigo, nombre, precio, talla, color, material, estilo):
        # Inicializa los atributos del vestido, llamando al constructor de la superclase
        super().__init__(codigo,nombre, precio, talla, color, material)
        # Asigna el atributo específico del vestido
        self.estilo = estilo
    
    def mostrar(self):
        muestra = f"codigo: {self.codigo} \n {self.nombre}: con precio base {self.precio} \n Talla: {self.talla} \n Color: {self.color} \n Material: {self.material}\n Estilo: {self.estilo}"
        return muestra 
        #return muestra


    def calcular_descuento(self):
        # Calcula el descuento que le corresponde al vestido según su estilo
        if self.estilo == "Casual":
            self.descuento = 0.1 # 10% de descuento
        elif self.estilo == "Formal":
            self.descuento = 0.05 # 5% de descuento
        elif self.estilo == "Fiesta":
            self.descuento = 0.15 # 15% de descuento

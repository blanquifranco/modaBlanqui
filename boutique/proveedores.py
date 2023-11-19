
# Crea una lista vacía para almacenar los objetos de tipo Proveedor
class Proveedor:
    """
    Clase para representar un proveedor.

    Atributos:
    - _nombre: El nombre del proveedor.
    - _direccion: La dirección del proveedor.
    - _telefono: El número de teléfono del proveedor.
    - _email: La dirección de correo electrónico del proveedor.
    - _productos: Una lista de productos que el proveedor ofrece.
    """

    def __init__(self, nombre, direccion, telefono, email, producto,cedula):
        # Inicializa los atributos del proveedor
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._email = email
        self._cedula = cedula
        # Asigna una lista de objetos de tipo Vendible al atributo productos del proveedor
        self._producto = producto

    def mostrar(self):
        # Muestra la información del proveedor, incluyendo el nombre, la dirección, el teléfono, el email y los productos que ofrece
        return (
            f"Nombre: {self._nombre}",
            f"Dirección: {self._direccion}",
            f"Teléfono: {self._telefono}",
            f"Email: {self._email}",
            f"{self._producto.mostrar()}\n",
        )


    def realizar_pedido(self):
        pass

#
    
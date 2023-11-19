
class Boutique:
    '''
    Clase que representa una tienda física.
    Esta clase gestiona ModaBlanqui, incluyendo su nombre, dirección, teléfono, email y un depósito asociado.
    Además, controla el stock de productos en la boutique, permite agregar y quitar productos, verificar la disponibilidad, vender productos a clientes y administrar proveedores.
    Atributos:
    nombre (str): El nombre de la boutique.
    direccion (str): La dirección de la boutique.
    telefono (str): El número de teléfono de la boutique.
    email (str): La dirección de correo electrónico de la boutique.
    deposito (Deposito): El depósito asociado a la boutique.
    stock (list): Lista de productos en el stock de la boutique.
    clientes (list): Lista de clientes de la boutique.
    codigos (dict): Diccionario que mapea códigos de productos a productos en el stock.
    proveedores (list): Lista de proveedores de la boutique.
    proveedores_id (dict): Diccionario que mapea cédulas de proveedores a objetos de proveedores.

    Métodos:
    agregar_stock(producto): Agrega un producto al stock de la boutique.
    quitar_stock(producto): Quita un producto del stock de la boutique.
    verificar_stock(producto): Verifica la disponibilidad de un producto en la boutique o el depósito.
    vender(cliente, producto): Vende un producto a un cliente, aplicando descuentos.
    agregar_proveedor(proveedor): Agrega un proveedor a la lista de proveedores de la boutique.
    eliminar_proveedor(proveedor): Elimina un proveedor de la lista de proveedores.
    mostrar_proveedores(): Muestra la información de los proveedores de la boutique.
    '''
    def __init__(self, nombre, direccion, telefono, email, deposito):
        '''Constructor de la clase Boutique'''
        # Inicializa los atributos de la boutique
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        # Asocia la boutique con un objeto de tipo Deposito
        self.deposito = deposito
        # Crea un diccionario vacio para almacenar el stock de la boutique
        self.stock = [] #seria stock dentro de la boutique, sin tener en cuenta el deposito
        self.clientes = []
        self.codigos = {}
        self.proveedores = []
        self.proveedores_id = {}
    def agregar_stock(self, producto):
        '''Método que se encarga de agregar un producto en la tienda'''
        codigo = producto.codigo
        if codigo not in self.codigos:
            # Si el código no existe en el diccionario, agrega el producto bajo ese código
            self.codigos[codigo] = producto
            self.stock.append(producto)
        else:
            # Si el código ya existe en el diccionario, muestra un mensaje de error
            print(f"El código {codigo} ya existe en la tienda. No se ha agregado el producto.")#las prendas tienen codigos unicos
        

    def quitar_stock(self, producto):
        '''Método que se encarga de sacar una prenda de la boutique, luego de que se realizó la venta'''
        if producto in self.stock:
            self.stock.remove(producto)
        else:
            # Si el producto no está en el stock, lanza una excepción
            raise ValueError(f"El producto {producto} no está en el stock de la boutique")

    def verificar_stock(self, producto):
        '''Un metodo que ayudará a verificar la existencia de stock'''
        # Verifica si hay disponibilidad de un producto en el stock de la boutique o del deposito
        
        if producto in self.stock:
            # Si el producto está en el stock de la boutique, devuelve True
            mensaje = f"Disponible dentro de la boutique{chr(0x1F929)}"
            return True,mensaje
        else:
            # Si el producto no está en el stock de la boutique, verifica si está en el depósito
            return self.deposito.verificar_stock(producto)

    def vender(self, cliente=None, producto = None):
        '''Funcion encargada de vender, tambien se agrega clientes a la lista de clientes y se agrega al carrito del cliente
        luego de haber calculado el precio final con los descuentos correspondientes'''
        # Vende un producto a un cliente, aplicando los descuentos correspondientes y actualizando el stock
        if self.verificar_stock(producto)[0]:
            # Si hay disponibilidad del producto, calcula el precio final con los descuentos
            if cliente:
                self.clientes.append(cliente)
                cliente.calcular_descuento()
                producto.calcular_descuento()
                precio_final = producto.precio * (1 - cliente.descuento) * (1 - producto.descuento)
            else:
                producto.calcular_descuento()
                precio_final = producto.precio * (1 - producto.descuento)
            try:
                cliente.cliente.agregar_carrito(producto)
                self.quitar_stock(producto)
            except ValueError:
                self.deposito.sacar_prenda(producto)
            # Devuelve el precio fin al del producto vendido
            venta = f"Vendido, Precio Final: {precio_final}Gs"
            return venta
        else:
            raise ValueError(f"Producto: {producto.codigo} {producto.nombre} no está disponible para la venta")
    
    def agregar_proveedor(self,proveedor):
        '''Funcionque se encarga de añadir un proveedor a lista de proveedores'''
        ci = proveedor._cedula
        if ci not in self.proveedores_id:
            # Si el código no existe en el diccionario, agrega el producto bajo ese código
            self.proveedores_id[ci] = proveedor
            self.proveedores.append(proveedor)
            return "proveedor agregado a la lista"

        else:
            # Si el código ya existe en el diccionario, muestra un mensaje de error
            return f"El proveedor  {ci} ya existe en la tienda. No se ha agregado el proveedor."
        

    def eliminar_proveedor(self, proveedor):
        '''Elimina un proveedor de la lista'''
        self.proveedores.remove(proveedor)

    def mostrar_proveedores(self):
        '''muestra el numero de proveedores y lista de proveedores'''
        lista = []
        # Recorre la lista de proveedores y muestra su información, llamando al método mostrar de cada uno
        for proveedor in self.proveedores:
            #print("-" * 20)
            lista.append(proveedor.mostrar())
        return lista


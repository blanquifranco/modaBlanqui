from boutique.boutique import Boutique
from boutique.deposito import Deposito
from boutique.proveedores import Proveedor
from productos.ropa import Vestido
from descuentos.descuento import DescuentoMembresia, DescuentoTemporada
from clientes.cliente import ClienteFiel, ClienteOcasional, Cliente

class Aplicacion:
    '''
    Clase que representa la aplicación de gestión de ModaBlanqui.
    Esta clase gestiona las operaciones de una boutique, como agregar proveedores, registrar clientes, vender productos y más.'''
    def __init__(self):
        '''Constructor encargado de inicializar los atributos de la aplicación'''
        self.deposito = Deposito()
        self.boutique = Boutique("ModaBlanqui", "San Lorenzo San Roque 245", "0987654321", "modablanqui@gmail.com", self.deposito)
        self.vestido1 = Vestido("100","Vestido Azul", 150000, "M", "Azul", "Algodon", "Formal")
        self.vestido2 = Vestido("102","Vestido Verde", 120000, "M", "Verde", "Lino", "Casual")
        self.vestido3 = Vestido("103","Vestido Azul", 120000, "P", "Verde", "Lino", "Fiesta")
        self.boutique.agregar_stock(self.vestido2)
        self.boutique.agregar_stock(self.vestido1)
        self.boutique.agregar_stock(self.vestido3)
        self.deposito.agregar_prenda(self.vestido1)
        self.deposito.agregar_prenda(self.vestido2)
        self.deposito.agregar_prenda(self.vestido3)
        self.cliente = None
        self.descuento_membresia = None
        self.descuento_temporada = None
        self.cliente_fiel = None
        self.cliente_ocasional = None
        self.cliente_elegido = None
        self.proveedores = None

    def mostrar_menu(self):
        '''
        Muestra el menú de opciones de la aplicación.
        '''
        print("Bienvenido/a ModaBlanqui")
        print("Seleccione una opción:")
        print("1. Vender")
        print("2. verificar stock de producto")
        print("3. Modificar descuento")
        print("4. Proveedores")  # Nueva opción
        print("5. Salir")

    def agregar_proveedor(self):
        '''
        Permite al usuario agregar un proveedor a la boutique.
        '''
        nombre = input("Ingrese el nombre del proveedor: ")
        direccion = input("Ingrese la dirección del proveedor: ")
        telefono = input("Ingrese el teléfono del proveedor: ")
        email = input("Ingrese el email del proveedor: ")
        cedula = input("Ingrese cedula de identidad: ")
        producto = Vestido("105","Vestido Azul", 150000, "M", "Azul", "Algodon", "Formal")
        proveedor = Proveedor(nombre, direccion, telefono,producto, email,cedula)
        self.boutique.agregar_proveedor(proveedor)

    def eliminar_proveedor(self):
        '''
        Permite al usuario eliminar un proveedor de la boutique.
        '''
        ci = input("Ingrese la cedula proveedor que desea eliminar: ")
        if ci in self.boutique.proveedores_id:
            self.boutique.eliminar_proveedor(self.boutique.proveedores_id[ci])
            print(f"Se ha eliminado el proveedor {self.boutique.proveedores_id[ci]._nombre} de la lista de proveedores.")
        else:
            print(f"No se ha encontrado el proveedor {self.boutique.proveedores_id[ci]._nombre} en la lista de proveedores.")


    #def mostrar_proveedores(self):
    # pass
    def gestionar_proveedores(self):
        '''
        Gestiona proveedores permitiendo agregar o eliminar proveedores.
        '''
        while True:
            print("Seleccione una opción:")
            print("1. Agregar proveedor")
            print("2. Eliminar proveedor")
            #print("3. Mostrar proveedores")
            print("4. Volver al menú principal")
            opcion = input("Opción: ")
            if opcion == "1":
                self.agregar_proveedor()
            elif opcion == "2":
                self.eliminar_proveedor()
            elif opcion == "3":
                self.mostrar_proveedores()
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
    def salir(self):
        '''
        Muestra un mensaje de despedida y cierra la aplicación.
        '''
        print("Buen Trabajo ModaBlanqui. Hasta pronto.")
        exit()

    def obtener_opcion(self):
        '''
        Obtiene la opción seleccionada por el usuario.

        Returns:
        str: La opción seleccionada.
        '''
        opcion = input("Ingrese la opción: ")
        return opcion
    def registrar_cliente(self):
        '''
        Permite al usuario registrar un cliente y asignarle un descuento.
        '''
        
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        email_cliente = input("Ingrese el email del cliente: ")
        cedula_cliente = input("Ingrese la cédula del cliente: ")
        self.cliente = Cliente(nombre_cliente, email_cliente, cedula_cliente)
        respuesta = input("1-cliente ocasional, 2- cliente fiel: ")
        self.cliente_elegido = self.cliente_fiel or self.cliente_ocasional
        if respuesta == "1":
            porcentaje_descuento2 = float(input("Ingrese el porcentaje del Descuento: "))
            temporada_descuento2 = input("Ingrese la temporada del Descuento: ")
            self.descuento_temporada = DescuentoTemporada(porcentaje_descuento2, temporada_descuento2)
            self.cliente_ocasional = ClienteOcasional(self.cliente,self.descuento_temporada)
            self.cliente_elegido = self.cliente_ocasional
        else:
            if respuesta == "2":
                porcentaje_membrecia = float(input("Ingrese el porcentaje del Descuento: "))
                opciones_validas = ["nivel1", "nivel2", "nivel3"]
                while True:
                    nombre_membrecia  = input("Ingrese nombre membresia(nivel1,nivel2,nivel3): ").lower()
                    if nombre_membrecia  in  opciones_validas:
                        break
                self.descuento_membresia = DescuentoMembresia(porcentaje_membrecia, nombre_membrecia)
                self.cliente_fiel = ClienteFiel(self.cliente,self.descuento_membresia)
                self.cliente_elegido = self.cliente_fiel

    def gestionar_venta(self):
        respuesta_cliente = input("Desea registrar cliente (SI/NO): ").lower()
        if respuesta_cliente == "si":
            self.registrar_cliente()
            self.vender_prenda(self.cliente_elegido)
        else:
            self.cliente = Cliente("sin nombre", "nada", "nada")
            self.cliente_ocasional = ClienteOcasional(self.cliente, 0.0)
            self.vender_prenda(self.cliente_ocasional)

    def vender_prenda(self, cliente):
        codigo_prenda = input("Ingrese código de la prenda: ")
        if codigo_prenda in self.boutique.codigos:
            self.boutique.vender(cliente, self.boutique.codigos[codigo_prenda])
        else:
            print(f"El código {codigo_prenda} no está dentro del stock de boutique")

    def verificar_stock(self):
        codigo_prenda = input("Ingrese código de la prenda: ")
        self.boutique.verificar_stock(self.boutique.codigos[codigo_prenda])

    #@staticmethod               
    def main(self):
        '''
        Punto de entrada de la aplicación donde se manejan las opciones del menú principal.
        '''
        while True:
            self.mostrar_menu()
            opcion_menu = self.obtener_opcion()

            if opcion_menu == "1":
                self.gestionar_venta()
            elif opcion_menu == "2":
                self.verificar_stock()
            elif opcion_menu == "4":
                self.gestionar_proveedores()
            elif opcion_menu == "5":
                self.salir()
            else:
                print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    app = Aplicacion()
    app.main()
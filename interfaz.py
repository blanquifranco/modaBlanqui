from boutique.boutique import Boutique
from boutique.deposito import Deposito
from boutique.proveedores import Proveedor
from productos.ropa import Vestido
from descuentos.descuento import DescuentoMembresia, DescuentoTemporada
from clientes.cliente import ClienteFiel, ClienteOcasional, Cliente
import tkinter as tk
from tkinter import simpledialog

class AplicacionGUI(tk.Tk):
    '''
    Clase que representa la aplicación de gestión de ModaBlanqui.
    Esta clase gestiona las operaciones de una boutique, como agregar proveedores, registrar clientes, vender productos y más.'''
    def __init__(self):
        '''Constructor encargado de inicializar los atributos de la aplicación'''
        super().__init__()

        self.title("ModaBlanqui - Aplicación de Boutique")
        self.geometry("400x300")

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

        self.crear_widgets()

    def crear_widgets(self):
        '''
        Muestra el menú de opciones de la aplicación.
        '''
        menu_label = tk.Label(self, text="Bienvenido/a ModaBlanqui", font=("Helvetica", 16))
        menu_label.pack(pady=10)

        vender_button = tk.Button(self, text="Vender", command=self.gestionar_venta)
        vender_button.pack(pady=10)

        stock_button = tk.Button(self, text="Verificar Stock", command=self.verificar_stock)
        stock_button.pack(pady=10)

        proveedores_button = tk.Button(self, text="Gestionar Proveedores", command=self.gestionar_proveedores)
        proveedores_button.pack(pady=10)

        salir_button = tk.Button(self, text="Salir", command=self.salir)
        salir_button.pack(pady=10)

    def gestionar_venta(self):
        while True:
            respuesta_cliente = simpledialog.askstring("Registro de Cliente", "¿Desea registrar un cliente? (SI/NO)").lower()
            if respuesta_cliente in ["si", "no"]:
                break
            else:
                tk.messagebox.showinfo("Error", "Por favor, ingrese 'SI' o 'NO'.")

        if respuesta_cliente == "si":
            if not self.registrar_cliente():
                tk.messagebox.showinfo("Error en el Registro", "Hubo un error en el registro.")
                return
            self.vender_prenda(self.cliente_elegido)
        else:
            self.cliente = Cliente("sin nombre", "nada", "nada")
            self.cliente_ocasional = ClienteOcasional(self.cliente, 0.0)
            self.vender_prenda(self.cliente_ocasional)

    def registrar_cliente(self):
        '''
        Permite al usuario registrar un cliente y asignarle un descuento.
        '''
        try:
            nombre_cliente = simpledialog.askstring("Registrar Cliente", "Ingrese el nombre del cliente:")
            email_cliente = simpledialog.askstring("Registrar Cliente", "Ingrese el email del cliente:")
            cedula_cliente = ""

            while not (cedula_cliente.isdigit() and len(cedula_cliente) > 0):
                cedula_cliente = simpledialog.askstring("Registrar Cliente", "Ingrese la cédula del cliente:")

            self.cliente = Cliente(nombre_cliente, email_cliente, cedula_cliente)
            respuesta = ""

            # Validar que la respuesta sea 1 o 2
            while respuesta not in ["1", "2"]:
                respuesta = simpledialog.askstring("Tipo de Cliente", "1-Cliente ocasional, 2-Cliente fiel:")

            self.cliente_elegido = self.cliente_fiel or self.cliente_ocasional

            if respuesta == "1":
                porcentaje_descuento2 = float(simpledialog.askstring("Descuento", "Ingrese el porcentaje del Descuento:"))
                temporada_descuento2 = simpledialog.askstring("Descuento", "Ingrese la temporada del Descuento:")
                self.descuento_temporada = DescuentoTemporada(porcentaje_descuento2, temporada_descuento2)
                self.cliente_ocasional = ClienteOcasional(self.cliente, self.descuento_temporada)
                self.cliente_elegido = self.cliente_ocasional
            elif respuesta == "2":
                porcentaje_membrecia = float(simpledialog.askstring("Descuento", "Ingrese el porcentaje del Descuento:"))
                opciones_validas = ["nivel1", "nivel2", "nivel3"]
                while True:
                    nombre_membrecia = simpledialog.askstring("Descuento", "Ingrese nombre membresía (nivel1, nivel2, nivel3):").lower()
                    if nombre_membrecia in opciones_validas:
                        break
                self.descuento_membresia = DescuentoMembresia(porcentaje_membrecia, nombre_membrecia)
                self.cliente_fiel = ClienteFiel(self.cliente, self.descuento_membresia)
                self.cliente_elegido = self.cliente_fiel
            return True
        except ValueError as e:
            tk.messagebox.showinfo("Error en el Registro", str(e))
            return False


    def vender_prenda(self, cliente):
        while True:
            codigo_prenda = simpledialog.askstring("Venta de Prenda", "Ingrese código de la prenda:")
            if codigo_prenda.isdigit() and len(codigo_prenda) <= 5:
                try:
                    if codigo_prenda in self.boutique.codigos:
                        mensaje = self.boutique.vender(cliente, self.boutique.codigos[codigo_prenda])
                        tk.messagebox.showinfo("Resultado de la Venta", mensaje)
                        break 
                    else:
                        tk.messagebox.showinfo("Error", f"El código {codigo_prenda} no está dentro del stock de boutique")
                except ValueError as e:
                    tk.messagebox.showinfo("Error", str(e))
            else:
                tk.messagebox.showinfo("Error", "Ingrese un código numérico de hasta 5 dígitos.")



    def verificar_stock(self):
        while True:
            codigo_prenda = simpledialog.askstring("Verificar Stock", "Ingrese código de la prenda:")
            if codigo_prenda.isdigit() and len(codigo_prenda) <= 5:
                try:
                    if codigo_prenda in self.boutique.codigos:
                        mensaje = self.boutique.verificar_stock(self.boutique.codigos[codigo_prenda])
                        tk.messagebox.showinfo("Resultado de la Verficacion de Stock", mensaje[1])
                        break 
                    else:
                        tk.messagebox.showinfo("Error", f"El código {codigo_prenda} no está dentro del stock de boutique")
                        return
                except ValueError as e:
                    tk.messagebox.showinfo("Error", str(e))
            else:
                tk.messagebox.showinfo("Error", "Ingrese un código numérico de hasta 5 dígitos.")


    def gestionar_proveedores(self):
        '''
        Gestiona proveedores permitiendo agregar, eliminar o mostrar proveedores.
        '''
        while True:
            opcion = simpledialog.askstring("Gestión de Proveedores", "Seleccione una opción:\n1. Agregar proveedor\n2. Eliminar proveedor\n3.Mostrar lista de Proveedores \n4. Volver al menú principal")

            if opcion == "1":
                self.agregar_proveedor()
            elif opcion == "2":
                self.eliminar_proveedor()
            elif opcion == "3":
                self.mostrar_proveedores()
            elif opcion == "4":
                break
            else:
                tk.messagebox.showinfo("Error", "Opción no válida. Por favor, seleccione una opción válida.")

    def mostrar_proveedores(self):
        try:
            proveedores = f"Se tienen {len(self.boutique.proveedores)} proveedores:",self.boutique.mostrar_proveedores()
            tk.messagebox.showinfo("Proveedores", proveedores)

        except AttributeError as e:
        # Si hay un error de atributo (por ejemplo, si _nombre o _producto no están definidos), muestra un mensaje de error
            tk.messagebox.showinfo("Error", str(e))


    def agregar_proveedor(self):
        '''
        Permite al usuario agregar un proveedor a la boutique.
        '''
        while True:
            try:
                nombre = simpledialog.askstring("Agregar Proveedor", "Ingrese el nombre del proveedor:")
                if nombre is None:
                    break

                direccion = simpledialog.askstring("Agregar Proveedor", "Ingrese la dirección del proveedor:")
                telefono = ""
                email = simpledialog.askstring("Agregar Proveedor", "Ingrese el email del proveedor:")
                cedula = ""

                while not telefono.isdigit():
                    telefono = simpledialog.askstring("Agregar Proveedor", "Ingrese el teléfono del proveedor:")

                while not (cedula.isdigit() and len(cedula) > 0):
                    cedula = simpledialog.askstring("Agregar Proveedor", "Ingrese cédula de identidad:")

                producto = Vestido("105", "Vestido Azul", 150000, "M", "Azul", "Algodon", "Formal")
                proveedor = Proveedor(nombre, direccion, telefono, email, producto, cedula)
                mensaje = self.boutique.agregar_proveedor(proveedor)
                tk.messagebox.showinfo("Proveedor", mensaje)

                break  # Sale del bucle si no hay errores y se agrega el proveedor correctamente

            except ValueError as e:
                tk.messagebox.showinfo("Error", str(e))

    def eliminar_proveedor(self):
        '''
        Permite al usuario eliminar un proveedor de la boutique.
        '''
        ci = ""
        while not (ci.isdigit() and len(ci) > 0):
            ci = simpledialog.askstring("Eliminar Proveedor", "Ingrese la cédula del proveedor que desea eliminar:")

        if ci in self.boutique.proveedores_id:
            self.boutique.eliminar_proveedor(self.boutique.proveedores_id[ci])
            tk.messagebox.showinfo("Eliminación Exitosa", f"Se ha eliminado el proveedor {self.boutique.proveedores_id[ci]._nombre} de la lista de proveedores.")
        else:
            tk.messagebox.showinfo("Error", f"No se ha encontrado el proveedor {ci} en la lista de proveedores.")


    def salir(self):
        '''
        Muestra un mensaje de despedida y cierra la aplicación.
        '''
        tk.messagebox.showinfo("Despedida", "Buen Trabajo ModaBlanqui. Hasta pronto.")
        self.destroy()


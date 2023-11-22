from boutique.boutique import Boutique
from boutique.deposito import Deposito
from boutique.proveedores import Proveedor
from productos.ropa import Vestido
from descuentos.descuento import DescuentoMembresia, DescuentoTemporada
from clientes.cliente import ClienteFiel, ClienteOcasional, Cliente
import tkinter as tk
from tkinter import simpledialog,messagebox
from tkinter.ttk import Combobox


class AplicacionGUI(tk.Tk):
    '''
    Clase que representa la aplicación de gestión de ModaBlanqui.
    Esta clase gestiona las operaciones de una boutique, como agregar proveedores, registrar clientes, vender productos y más.'''
    def __init__(self):
        '''Constructor encargado de inicializar los atributos de la aplicación'''
        super().__init__()

        self.title("ModaBlanqui - Aplicación de Boutique")
        self.configure(bg="blue")
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
        self.ventana_cliente = None

        self.crear_widgets()

    def crear_widgets(self):
        '''
        Muestra el menú de opciones de la aplicación.
        '''
        menu_label = tk.Label(self, text="ModaBlanqui", font=("Helvetica", 25, "bold"), fg="purple", bg="blue")
        menu_label.pack(pady=10)

        vender_button = BotonPersonalizado(self, text="Vender", command=self.gestionar_venta)
        vender_button.pack(pady=10)

        stock_button = BotonPersonalizado(self, text="Verificar Stock", command=self.verificar_stock)
        stock_button.pack(pady=10)

        proveedores_button = BotonPersonalizado(self, text="Gestionar Proveedores", command=self.gestionar_proveedores)
        proveedores_button.pack(pady=10)

        salir_button = BotonPersonalizado(self, text="Salir", command=self.salir)
        salir_button.pack(pady=10)

    def gestionar_venta(self):
        def callback_vender_prenda():
            if self.cliente_elegido:
                self.vender_prenda(self.cliente_elegido)
            else:
                tk.messagebox.showinfo("Error", "Hubo un problema al registrar el cliente.")
        while True:
            respuesta_cliente = simpledialog.askstring("Registro de Cliente", "¿Desea registrar un cliente? (SI/NO)").lower()

            if respuesta_cliente in ["si", "no"]:
                break
            else:
                tk.messagebox.showinfo("Error", "Por favor, ingrese 'SI' o 'NO'.")

        if respuesta_cliente == "si":
            self.registrar_cliente(callback_vender_prenda)
            self.vender_prenda(self.cliente_elegido)
        else:
            self.cliente = Cliente("sin nombre", "nada", "nada")
            self.cliente_ocasional = ClienteOcasional(self.cliente, 0.0)
            self.vender_prenda(self.cliente_ocasional)

    
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

    def registrar_cliente(self,callback=None):
        '''
        Permite al usuario registrar un cliente y asignarle un descuento.
        '''
        try:
            ventana_registro_cliente = tk.Toplevel(self)
            nombre_cliente_var = tk.StringVar()
            email_cliente_var = tk.StringVar()
            cedula_cliente_var = tk.StringVar()
            respuesta_var = tk.StringVar()
            temporada_descuento_var = tk.StringVar()
            ventana_registro_cliente.geometry("450x360")
            ventana_registro_cliente.configure(bg="#4A90E2")
            ventana_registro_cliente.option_add("*TEntry*background", "#87CEEB")
            ventana_registro_cliente.option_add("*TLabel*background", "#4A90E2")

            def solicitar_input_con_validacion(mensaje, validacion_func):
                while True:
                    valor = simpledialog.askstring("Descuento", mensaje)
                    if validacion_func(valor):
                        return valor
                    else:
                        messagebox.showinfo("Valor Incorrecto", "Por favor, ingrese un valor válido.")

            def obtener_porcentaje():
                def es_porcentaje_valido(valor):
                    try:
                        porcentaje_float = float(valor)
                        return 0 <= porcentaje_float <= 100
                    except ValueError:
                        return False
                return solicitar_input_con_validacion("Ingrese el porcentaje del Descuento:", es_porcentaje_valido)

            def obtener_membresia():
                opciones_validas = ["nivel1", "nivel2", "nivel3"]
                def es_membresia_valida(valor):
                    return valor.lower() in opciones_validas
                return solicitar_input_con_validacion("Ingrese nombre membresía (nivel1, nivel2, nivel3):", es_membresia_valida)
            

            def registrar_cliente_interno():
                nonlocal ventana_registro_cliente

                nombre_cliente = nombre_cliente_var.get()
                email_cliente = email_cliente_var.get()
                cedula_cliente = cedula_cliente_var.get()
                respuesta = respuesta_var.get()
                
                if not(nombre_cliente and email_cliente and cedula_cliente and respuesta):
                    messagebox.showinfo("Error en el Registro", "Ningun campo puede quedar vacio")
                    return

                if not (cedula_cliente.isdigit() and len(cedula_cliente) > 0):
                    messagebox.showinfo("Error en el Registro", "El campo cedula debe ser numero entero mayor a cero")
                    return
            
                self.cliente = Cliente(nombre_cliente, email_cliente, cedula_cliente)

                if respuesta == "1":
                    temporada_descuento_var.set(simpledialog.askstring("Descuento", "Ingrese la temporada del Descuento:"))
                    self.descuento_temporada = DescuentoTemporada(float(obtener_porcentaje()), temporada_descuento_var.get())
                    self.cliente_ocasional = ClienteOcasional(self.cliente, self.descuento_temporada)
                    self.cliente_elegido = self.cliente_ocasional
                elif respuesta == "2":
                    self.descuento_membresia = DescuentoMembresia(float(obtener_porcentaje()),obtener_membresia())
                    self.cliente_fiel = ClienteFiel(self.cliente, self.descuento_membresia)
                    self.cliente_elegido = self.cliente_fiel
                if callback:
                    callback()
                ventana_registro_cliente.destroy()
                
            # Crear y colocar widgets en la ventana de registro de cliente
            tk.Label(ventana_registro_cliente, text="Nombre del Cliente:").pack(pady=5)
            tk.Entry(ventana_registro_cliente, textvariable=nombre_cliente_var).pack(pady=5)

            tk.Label(ventana_registro_cliente, text="Email del Cliente:").pack(pady=5)
            tk.Entry(ventana_registro_cliente, textvariable=email_cliente_var).pack(pady=5)

            tk.Label(ventana_registro_cliente, text="Cédula del Cliente:").pack(pady=5)
            tk.Entry(ventana_registro_cliente, textvariable=cedula_cliente_var).pack(pady=5)

            tk.Label(ventana_registro_cliente, text="Tipo de Cliente:").pack(pady=5)
            tk.Radiobutton(ventana_registro_cliente, text="Cliente ocasional", variable=respuesta_var, value="1").pack(pady=5)
            tk.Radiobutton(ventana_registro_cliente, text="Cliente fiel", variable=respuesta_var, value="2").pack(pady=5)

            btn_registrar = BotonPersonalizado(ventana_registro_cliente, text="Registrar Cliente", command=registrar_cliente_interno)
            btn_registrar.pack(pady=10)

            # Mostrar la ventana de registro de cliente
            ventana_registro_cliente.mainloop()
        except ValueError as e:
            messagebox.showinfo("Error en el Registro", str(e))
            return False

    def salir(self):
        '''
        Muestra un mensaje de despedida y cierra la aplicación.
        '''
        tk.messagebox.showinfo("Despedida", "Buen Trabajo ModaBlanqui. Hasta pronto.")
        self.destroy()


class BotonPersonalizado(tk.Button):
    '''Clase para personalizar botones'''
    def __init__(self, master=None, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.config(bg="lightblue", padx=10, pady=5, font=("Helvetica", 12))
        self.bind("<Button-1>", self.cambiar_cursor)
        self.bind("<Enter>", self.cursor_sobre_boton)
        self.bind("<Leave>", self.cursor_fuera_boton)
    def cambiar_cursor(self, event):
        self.config(cursor="heart")

    def cursor_sobre_boton(self, event):
        self.config(cursor="heart")

        # Cambiar el color de fondo cuando el ratón está sobre el botón
        self.config(bg="lightcyan")

    def cursor_fuera_boton(self, event):
        # Restaurar el cursor y el color de fondo cuando el ratón sale del botón
        self.config(cursor="")
        self.config(bg="lightblue")




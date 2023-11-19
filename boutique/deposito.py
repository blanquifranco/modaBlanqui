from  boutique.proveedores  import Proveedor
class Deposito:
    def __init__(self):
        self.productos = []  # Usaremos un diccionario para rastrear las existencias
        self.historial_movimientos = []  # Lista para rastrear el historial de movimientos
        self.codigos = {}


    def agregar_prenda(self, producto):
        codigo = producto.codigo
        if codigo not in self.codigos:
            # Si el código no existe en el diccionario, agrega el producto bajo ese código
            self.codigos[codigo] = producto
            self.productos.append(producto)
        else:
            # Si el código ya existe en el diccionario, muestra un mensaje de error
            print(f"El código {codigo} ya existe en la tienda. No se ha agregado el producto.")#las prendas tienen codigos unicos
        
    def verificar_stock(self, producto):
        if producto in self.productos:
            mensaje = f"En el salon de boutique No se encuentra\nDisponible dentro del deposito!! {chr(0x1F60D)}"
            return True,mensaje

        else:
            mensaje =f"En el salon de boutique No se encuentra\nNo se encuentra en el deposito {chr(0x1F614)}"
            return False,mensaje

    def sacar_prenda(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            print(f"{producto.nombre} No se encuentra en el deposito.")

    def registrar_movimiento(self, prenda, tipo_movimiento, proveedor=None):
        if tipo_movimiento == "entrada":
            self.agregar_prenda(prenda)
        elif tipo_movimiento == "salida":
            self.sacar_prenda(prenda)
        else:
            print("Tipo de movimiento no válido.")

        # Registra el movimiento en el historial
        movimiento = {
            "prenda": prenda,
            "tipo": tipo_movimiento,
            "proveedor": proveedor,  # Almacena el proveedor en el movimiento
        }
        self.historial_movimientos.append(movimiento)

    def obtener_historial_movimientos(self):
        return self.historial_movimientos
    
    

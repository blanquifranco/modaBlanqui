from ZODB import FileStorage, DB
from persistent.mapping import PersistentMapping

class Conexion():
    def __init__(self):
        self.storage = FileStorage.FileStorage('database/modablanqui.fs')
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()
    def get_root(self):
        return self.root

    def confirmar(self):
        self.connection.transaction_manager.commit()

    
    def agregar_cliente(self, cliente):
        '''Agrega un cliente a la base de datos'''
        if 'clientes' not in self.get_root():
            self.get_root()['clientes'] = PersistentMapping()

        self.get_root()['clientes'][cliente.cliente.ci] = cliente
    
    def close(self):
        try:
            self.confirmar()
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir al confirmar la transacción, ( especificar el tipo de excepcion mas adelante)
            print(f"Error al confirmar la transacción: {e}")

        # Luego, cerrar la conexión
        self.storage.close()
        self.connection.close()
from clase_principio_encapsulacion import Producto

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__catalogo = set()
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def catalogo(self):
        return frozenset(self.__catalogo)
    
    def agregar_producto(self, producto: Producto):
        '''
        Agrega un producto al catálogo
        
        Sólo admite elementos de tipo Producto
        '''
        if not isinstance(producto, Producto):
            raise ValueError('Sólo se aceptan productos')
        
        self.__catalogo.add(producto)
    
    def quitar_producto(self, producto: Producto):
        '''
        Elimina un producto del catálogo
        '''
        self.__catalogo.discard(producto)  # No lanza error si el producto no existe

    def __str__(self):
        productos = ', '.join(str(prod) for prod in self.__catalogo)
        return f"Tienda: {self.nombre}\nProductos: {productos}"
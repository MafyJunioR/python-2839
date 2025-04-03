from clase_principio_encapsulacion import Producto

class Tienda:
    ultimo_id = 0

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__catalogo = dict()
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str):
            raise TypeError('Esperaba un valor str')
        
        self.__nombre = nombre
    
    @property
    def catalogo(self):
        return frozenset(self.__catalogo.values())
    
    def buscar_por_id(self, id: int) -> Producto:
        if not isinstance(id, int):
            raise TypeError('Esperaba un valor int')

        return self.__catalogo.get(id, None)

    def agregar_producto(self, producto: Producto) -> None:
        '''
        Agrega un producto al catálogo
        
        Sólo admite elementos de tipo Producto
        '''
        if not isinstance(producto, Producto):
            raise TypeError('Sólo se aceptan productos')

        id = None

        Tienda.ultimo_id += 1
        id = Tienda.ultimo_id

        self.__catalogo[id] = producto
    
    def quitar_producto(self, id: int) -> None:
        '''
        Elimina un producto del catálogo
        '''
        if not isinstance(id, int):
            raise TypeError('Esperaba un valor int')
        
        self.__catalogo.pop(id)

    def __str__(self) -> str:
        productos = ', '.join(str(prod) for prod in self.__catalogo)
        return f"Tienda: {self.nombre}\nProductos: {productos}"
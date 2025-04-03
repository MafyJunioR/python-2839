from datetime import date
from clase_principio_encapsulacion import Producto

class ProductoPerecedero(Producto):
    def __init__(self, nombre, precio, caducidad):
        super().__init__(nombre, precio)
        self.caducidad = caducidad
    
    @property
    def precio(self):
        if date.today() > self.caducidad:
            return 0
        
        return super().precio
    
    @precio.setter
    def precio(self, valor):
        Producto.precio.__set__(self, valor)

    @property
    def caducidad(self):
        return self.__caducidad
    
    @caducidad.setter
    def caducidad(self, valor):
        self.__caducidad = valor
    
    def __str__(self):
        return f'ProductoPerecedero(nombre={self.nombre}, precio={self.precio}, caducidad={self.caducidad})'
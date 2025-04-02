class Producto:
    def __init__(self, nombre = None, precio = None):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f'Producto({self.nombre=}, {self.precio=})'
    
    def iva(self):
        if self.precio is None:
            raise ValueError('No tiene precio')
        
        return self.precio * 0.21

p = Producto()

p.nombre = 'Prueba'

print(p)

try:
    print(p.iva())
except ValueError:
    print('No tiene IVA')

print(p.nombre)

p2 = Producto('Portátil', 1234.56)

print(p2, p2.iva())

p3 = Producto(precio = 234)

p3.nombre = 'Cambiado'
p3.descripcion = 'Descrito'

print(p3, p3.descripcion)

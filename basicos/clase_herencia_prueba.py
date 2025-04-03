from clase_principio_encapsulacion import Producto
from clase_con_diccionario import Tienda
from clase_herencia import ProductoPerecedero
from datetime import date

pp = ProductoPerecedero('Patatas', 12, date(2025, 4, 4))

print(pp.caducidad)

print(pp)

tienda = Tienda('Tiene de to')

tienda.agregar_producto(Producto('Cochecito de juguete', 2))
tienda.agregar_producto(pp)

print('Mostrando el catálogo')

for producto in tienda.catalogo:
    print(producto)
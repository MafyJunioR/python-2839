from clase_con_diccionario import *

t = Tienda('Bilbao')

t.nombre = 'Cambiado'

print(t.nombre)

t.agregar_producto(Producto('asdf', 1234)) #1
t.agregar_producto(Producto('zxcv', 5678)) #2
t.agregar_producto(Producto('ghjklhjk', 5678)) #3

t.quitar_producto(3) # Quitamos el 3

t.agregar_producto(Producto('Cuarto', 4444)) #4

producto3 = t.buscar_por_id(3)

if producto3 is not None:
    print(producto3)
else:
    print('No se ha encontrado el producto 3')

producto4 = t.buscar_por_id(4)

if producto4 is not None:
    print(producto4)
else:
    print('No se ha encontrado el producto 4')

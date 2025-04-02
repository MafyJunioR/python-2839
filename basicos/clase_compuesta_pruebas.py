from clase_compuesta import *
import pickle

t = Tienda('Bilbao')

t.agregar_producto(Producto('Portátil', 1234))
t.agregar_producto(Producto('Ratón', 12))
t.agregar_producto(Producto('   Portátil', 1234))

# t.agregar_producto(None)
# t.agregar_producto(5)
# t.agregar_producto('patata')

for producto in t.catalogo:
    print(producto)

with open('bilbao.tienda', 'wb') as f:
    pickle.dump(t, f)

tienda = None

with open('bilbao.tienda', 'rb') as f:
    tienda = pickle.load(f)

print('Datos cargados')

print(tienda.nombre)

for p in tienda.catalogo:
    print(p)

print(tienda)
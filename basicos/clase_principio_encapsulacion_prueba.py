from clase_principio_encapsulacion import Producto

p = Producto('  Portátil ', 1234)

print(p)

print(p.nombre)

p.nombre = '   Ratón    '

p.precio *= 1.1

print(p)

p1 = Producto('Producto', 1234)
p2 = Producto('Producto', 1234)

print(id(p1), id(p2))
print(p1 is p2) # Son el mismo?
print(p1 == p2) # Son iguales?

print(p1.__hash__(), p2.__hash__())

print(p + p2)

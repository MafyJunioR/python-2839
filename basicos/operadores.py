lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print(lista1 == lista2) # igualdad por contenido equals

print(lista1 is lista2) # son el mismo
print(id(lista1) == id(lista2))

print(not (lista1 is lista2))
print(lista1 is not lista2)

print(x := 5)

nombre = input('Dime tu nombre').strip() or 'Anónimo'

print('Hola ' + nombre)

for dato in ['asdfasd', '', 'asdfasd', 'asfasdf', '']:
    print(dato and 'Tiene dato' or 'No tiene dato')

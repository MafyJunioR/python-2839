lista = [ 1, 2, 3, 4, 5 ]

print(lista)

print(lista[3])

print(lista[2:5])

palabras = [ 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco' ]

print(palabras)

print(palabras[2:5])

print(lista + palabras)

palabras = palabras + ['Sis']

palabras += ['Siete']

palabras.append('Ocho')


print(palabras)

palabras[5] = 'Seis'

print(palabras)

palabras.insert(0, 'Cero')

print(palabras)

palabras2 = [] + palabras

palabras3 = palabras[:] # Prefiero esta forma

print(id(palabras), id(palabras2), id(palabras3))

palabras.append('Nueve')

print('ORIGINAL', palabras)
print('COPIA   ', palabras2)
print('COPIA2  ', palabras3)

palabras[3:6] = ['TRES', 'CUATRO', 'CINCO']

print(palabras)

print(len(palabras))

tablero = [
    ['t','c','a','k','q','a','c','t'],
    ['p'] * 8,
    ['x'] * 8,
    ['x'] * 8,
    ['x'] * 8,
    ['x'] * 8,
    ['P'] * 8,
    ['T','C','A','K','Q','A','C','T']
]

print(tablero)

print(tablero[0][5])

y = 0

while y < len(tablero):
    x = 0

    while x < len(tablero[y]):
        print(tablero[y][x], end=' ')
        x += 1
    
    print()
    y += 1

print(palabras)

i = 0
while i < len(palabras):
    palabra = palabras[i]
    print(palabra)
    i += 1

for palabra in palabras:
    print(palabra)

i = 2
while i < 11:
    numero = i
    print(numero)
    i += 2

for numero in range(2, 10 + 1, 2):
    print(numero)

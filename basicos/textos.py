nombre = 'Javier'

print('Hola ' + nombre) # Concatenación

print('El dijo: \t"Qué tal"') # Tabulador

# Texto multilínea
print('''
El dijo: 
'Qué tal'
''')

print("El dijo: \"Qué tal ☺️\" \\") # Uso de caracteres de emojis gracias a tener UTF-8

if nombre == 'Javier':
    print('Hombre... Si es el profe')
    print('Otro')

print('C:\\nuevos\\trabajos.txt')
print(r'C:\nuevos\trabajos.txt')

print('Hola' * 2 + ' vecinito')

print('asdfasdf' + ('-' * 25))

print('Una línea super larga en la que sueltas un rollo que te pasas'
      ' y sigue y sigue y sigue sin parar hasta el infinito y más allá')

print(nombre[0] + nombre[1])

print(nombre[-2] + nombre[-1])

dni = '12345678A'

print(dni[-1])

print(len(dni))

print(dni[len(dni)-1])

print(nombre[0:4])

print(nombre[:4] + nombre[4:])

# print(nombre[42])

print(1, 5, 3, 3, 4, 56, 76, sep=',', end=': ')
print('Después')

dias = 31
mes = 'Marzo'

print(mes + ' tiene ' + str(dias) + ' días')
print(f'{mes} tiene {dias} días')
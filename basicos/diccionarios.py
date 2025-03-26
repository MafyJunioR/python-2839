diccionario = { 
    'casa': 'house', 
    'perro': 'dog' 
}

print(diccionario['casa'])

for clave in diccionario:
    print(clave, diccionario[clave], sep='\t')

for clave, valor in diccionario.items():
    print(clave, valor, sep='\t')

for indice, clave in enumerate(diccionario):
    print(indice, clave, sep='\t')

claves = ['hola', 'adios']
valores = ['hello', 'bye']

diccionario_nuevo = zip(claves, valores)

for clave, valor in diccionario_nuevo:
    print(clave, valor, sep='\t')
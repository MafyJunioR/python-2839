coleccion = { 
    'casa': 'house', 
    'perro': 'dog' 
}

print(coleccion['casa'])

for clave in coleccion:
    print(clave, coleccion[clave], sep='\t')
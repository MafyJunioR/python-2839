# No se repiten
conjunto = { 1, 5, 6, 8, 3, 2, 3, 4 }
print(conjunto)

print(5 in conjunto)
print(7 in conjunto)

conjunto1 = set('34567890')
conjunto2 = set('123456')

print(conjunto1, conjunto2)

print(conjunto1 - conjunto2) # Resta
print(conjunto1 | conjunto2) # Unión
print(conjunto1 & conjunto2) # Intersección
print(conjunto1 ^ conjunto2) # Excluye los comunes

import re

re_dni = r'[XYZ\d]\d{7}[A-Z]'

texto = '''
Este texto contiene 12345678A en varias partes del mismo.
Ya sé que es una X7654321Z de ejemplo, pero bueno
'''

resultado = re.findall(re_dni, texto)

print(resultado)

resultado = re.sub(re_dni, '*' * 9, texto)

print(resultado)

re_tacos = '(puta|mierda|culo|caca|culo|pedo|pis)'

texto = '''
Este juego es una puta mierda.
La verdad es que los desarrolladores se pueden ir a tomar por el culo.
'''

resultado = re.sub(re_tacos, '******', texto)

print(resultado)
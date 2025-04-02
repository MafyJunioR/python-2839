with open('fichero.txt', 'a', encoding='utf-8') as f:
    while True:
        linea = input('Dame una línea para el fichero: ')

        if linea == '':
            break

        f.write(linea + '\n')

texto = None

with open('fichero.txt', 'r', encoding='utf-8') as f:
    texto = f.read()

print(texto)

numero_linea = 1

with open('fichero.txt', 'r', encoding='utf-8') as f:
    for linea in f:
        print(f'{numero_linea:4d}: {linea}', end='')
        numero_linea += 1

lista = []

with open('fichero.txt', 'r', encoding='utf-8') as f:
    lista = list(f)

print(lista)

lista_sin_enter = []

with open('fichero.txt', 'r', encoding='utf-8') as f:
    for linea in f:
        lista_sin_enter.append(linea[:-1])

print(lista_sin_enter)


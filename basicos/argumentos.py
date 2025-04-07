import sys

if len(sys.argv) != 3:
    print('Argumentos incorrectos')
    print('Formato de llamada:')
    print(f'{sys.argv[0]} origen destino')
else:
    print(f'Copiando fichero {sys.argv[1]} a {sys.argv[2]}')
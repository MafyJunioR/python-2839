for numero in range(1, 10):
    print(numero % 4, end=',')

print()

for numero in range(1, 10):
    if numero % 3 == 0:
        print(numero, end=',')

print()

print('Búsqueda')

lista = [ 1, 56, 7, 8, 6, 4, 45,7 ,8 , 76, 45, 34 ]

for numero in lista:
    print(numero, end=',')

    if numero == 6:
        print('ENCONTRADO')
        break
        
else:
    print('NO ENCONTRADO')

print('Versión while')

i = 0
encontrado = False

while i < len(lista) and not encontrado:
    print(lista[i], end=',')
    
    if lista[i] == 6:
        print('ENCONTRADO')
        encontrado = True
    else:
        pass
    
    i += 1

for mes in range(1, 12 + 1):
    match mes:
        case 2:
            dias = 28
        case 4 | 6 | 9 | 11:
            dias = 30
        case _:
            dias = 31

    print('El mes', mes, 'tiene', dias, 'días')

x = 5
y = 2

punto = (x, y)

print(punto)

match punto:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("No es un punto")
    
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

punto = Punto(5, 5)

print(punto.x, punto.y)

match punto:
    case Punto(x=0, y=0):
        print('No tiene valor')
    case Punto(x=x, y=0):
        print('x = ', x)
    case Punto(x=x, y=y) if x == y:
        print('Diagonal')
    case Punto(x=x, y=y):
        print(punto.x, punto.y)

from enum import Enum
class Color(Enum):
    ROJO = 'rojo'
    VERDE = 'verde'
    AZUL = 'azul'

mi_color = Color.AZUL

match mi_color:
    case Color.ROJO:
        print('El primero')
    case Color.VERDE:
        print('El segundo')
    case _:
        print(mi_color.value)


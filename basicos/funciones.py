def sumar(a, b):
    ''' Función que suma dos valores recibidos '''
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

dividir = lambda a, b: a / b

print(sumar(5, 6))

print(dividir(10, 5))

def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(1000)

f = fib

f(500)

operacion = restar

print(operacion(6, 7))

def calculadora(a = 0, operacion = sumar, b = 0):
    return operacion(a, b)

print(calculadora(7, sumar, 3))

print('Valor devuelto por f', f(1))

def fib2(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fib2(10))

print(calculadora(4, restar, 5))

nombre = input('Dime tu nombre: ')

print(nombre)

def calc(operacion, *operandos):
    if len(operandos) < 2:
        raise ValueError('Necesito al menos dos operandos')
    
    op1 = operandos[0]

    for operando in operandos[1:]:
        op2 = operando

        op1 = operacion(op1, op2)
    
    return op1

print(calc(multiplicar, 3, 5, 6, 7, 8))

def traductor(palabra, **traducciones):
    return traducciones[palabra]

print(traductor('casa', perro = 'dog', casa = 'house', mascota = 'pet'))

rango = [3, 7]

print(list(range(*rango))[0])

valores = [2, 3, 4];

print(calc(lambda x, y: x ** y, *valores))

diccionario = { 'perro': 'dog', 'casa': 'house', 'mascota': 'pet' }

print(traductor('casa', **diccionario))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[0], reverse=True)

print(pairs)

print(sumar.__doc__)

def concatenar(texto1: str, texto2: str) -> str:
    return texto1 + ', ' + texto2

print(concatenar(1, 2))


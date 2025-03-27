import random

print('Bienvenido a adivina el número')

pensado = random.randint(1, 100)

print(pensado)

while True:
    numero = int(input('Dime un número de 1 a 100: '))

    if pensado == numero:
        print('Has acertado')
        break
    elif pensado > numero:
        print('ES MAYOR')
    else:
        print('Es menor')
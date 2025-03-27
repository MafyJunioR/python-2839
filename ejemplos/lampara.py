enchufada = input('¿La lámpara está enchufada?')

if enchufada == 'si':
    quemada = input('¿La bombilla está quemada?')

    if quemada == 'si':
        print('Reemplaza la bombilla')
    else:
        print('Repara la lámpara')
else:
    print('Enchufa la lámpara')

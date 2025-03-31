def input_str(mensaje):
    return input(mensaje + ": ")

def input_int(mensaje):
    correcto = False

    numero = None

    while not correcto:
        texto = input_str(mensaje)
        
        try:
            numero = int(texto)
            correcto = True
        except ValueError:
            print('Debe ser un número')

    return numero
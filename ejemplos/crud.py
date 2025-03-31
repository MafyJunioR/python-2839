from dependencias.crud_modulo import *
from bibliotecas.consola import *

# PROGRAMA PRINCIPAL

consultar = True

while consultar:
    menu()

    opcion = input_int('Elige una opción')

    consultar = procesar(opcion)

# FUNCIONES

def menu():
    '''Mostrar menú en pantalla'''
    
    print('''
1. Listado
2. Buscar por id
3. Añadir
4. Modificar
5. Borrar
0. Salir
    ''')

def procesar(opcion):
    '''Procesar la opción seleccionada'''
    
    global contactos
    global consultar

    match opcion:
        case 1:
            listado()
        case 2:
            print('Buscar por id')
        case 3:
            insertar()
        case 4:
            print('Modificar')
        case 5:
            print('Borrar')
        case 0:
            print('Salir')
            consultar = False
        case _:
            print('OPCIÓN NO RECONOCIDA')
    
    input('Dale a enter para continuar')

def insertar():
    global contactos
    
    print('Añadir')

    nombre = input('Nombre: ')
    apellido = input('Apellido: ')

    id = list(contactos.keys())[-1] + 1

    contactos[id] = { 'nombre': nombre, 'apellido': apellido }

def listado():
    global contactos

    print('Listado')

    formato = '%3s %-10s %-10s'

    print(formato % ('Id', 'Nombre', 'Apellido'))

    for id in contactos:
        print(formato % (id, contactos[id]['nombre'], contactos[id]['apellido']))

# PROGRAMA PRINCIPAL

contactos = { 
    1: { 'nombre': 'Javier', 'apellido': 'Lete' },
    2: { 'nombre': 'Pepe', 'apellido': 'Pérez' } 
}

consultar = True

while consultar:
    menu()

    opcion = int(input('Elige una opción: '))

    procesar(opcion)

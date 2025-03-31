from bibliotecas.consola import *

# VARIABLES GLOBALES

contactos = { 
    1: { 'nombre': 'Javier', 'apellido': 'Lete' },
    2: { 'nombre': 'Pepe', 'apellido': 'Pérez' } 
}

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

    match opcion:
        case 1:
            listado()
        case 2:
            buscar_por_id()
        case 3:
            insertar()
        case 4:
            modificar()
        case 5:
            borrar()
        case 0:
            print('Salir')
            return False
        case _:
            print('OPCIÓN NO RECONOCIDA')
    
    input('Dale a enter para continuar')

    return True

def listado():
    global contactos

    print('Listado')

    formato = '%3s %-10s %-10s'

    print(formato % ('Id', 'Nombre', 'Apellido'))

    for id in contactos:
        print(formato % (id, contactos[id]['nombre'], contactos[id]['apellido']))

def buscar_por_id():
    global contactos

    print('Buscar por id')

    id = input_int('Dime el id a buscar')

    contacto = contactos[id]

    print(f'''
id: {id}
nombre: {contacto['nombre']}
apellido: {contacto['apellido']}
    ''')

def insertar():
    global contactos
    
    print('Añadir')

    nombre = input_str('Nombre')
    apellido = input_str('Apellido')

    id = list(contactos.keys())[-1] + 1

    contactos[id] = { 'nombre': nombre, 'apellido': apellido }

def modificar():
    global contactos
    
    print('Modificar')

    id = input_int('Id')
    nombre = input_str('Nombre')
    apellido = input_str('Apellido')

    contactos[id] = { 'nombre': nombre, 'apellido': apellido }

def borrar():
    global contactos

    print('Borrar')

    id = input_int('Dime el id a borrar')

    del contactos[id]

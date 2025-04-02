import json

contactos = { 
    1: { 'nombre': 'Javier', 'apellido': 'Lete' },
    2: { 'nombre': 'Pepe', 'apellido': 'Pérez' } 
}

print(json.dumps(contactos))

with open('contactos.json', 'w', encoding='utf-8') as f:
    json.dump(contactos, f)

contactos_cargados = None

with open('contactos.json', 'r', encoding='utf-8') as f:
    contactos_cargados = json.load(f)

print(contactos_cargados)

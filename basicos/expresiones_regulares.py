import re

dni = input('Dime el DNI: ')

dni_ok = re.match(r'^[XYZ\d]\d{7}[A-Z]$', dni)

print(dni_ok)

if dni_ok:
    print('DNI OK')
else:
    print('DNI INCORRECTO')

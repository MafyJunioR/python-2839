from datetime import *
from dateutil.relativedelta import relativedelta

ahora = datetime.now()

print(ahora)

print(ahora.strftime('%d/%m/%Y, %H:%M:%S'))

hoy = date.today()

print(hoy)

hora = time(1, 2, 3)

print(hora)

fecha_nacimiento = datetime.strptime(input('Dime tu fecha de nacimiento: '), '%d-%m-%Y') # date(1990, 3, 31)

edad = hoy.year - fecha_nacimiento.year

if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

print(edad)
print(relativedelta(hoy, fecha_nacimiento).years)
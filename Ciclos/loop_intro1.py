import re
from unittest import result


mascotas =  ['gatos', 'perros', 'peces', 'loros']

result = len(mascotas)

m1 = mascotas[0]

m2 = mascotas[2]

print(result)

print(m2)
print(m1)

for index, mascota in enumerate (mascotas):
    print(index, mascota)

pocision_peces = 0
for index, mascota in enumerate (mascotas):
    if mascota == 'peces':
        pocision_peces = index

print('Hay un pez en la pocision', pocision_peces)
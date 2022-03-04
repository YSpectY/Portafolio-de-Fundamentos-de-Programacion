# 1.8. Un año es bisiesto si es divisible por 4 y no es por 100, 
# o si es divisible por 400. Escribe un programa que lea un año
# y devuelva si es bisiesto o no.

year = int(input('Escriba un año:'))

if year % 4 == 0 and (not(year % 100 == 0) or year % 400 == 0):
    print(year, 'es un año bisiesto :D')
else:
    print(year, 'no es un año bisiesto')
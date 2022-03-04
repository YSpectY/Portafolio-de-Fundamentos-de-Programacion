# Solicitar al usuario una fecha(dd:mm:aaaa)
# y comprobar si es correcta 
# Para que la fecha sea correcta es necesario que:
# El año sea mayor a 0
# El mes este entre 1 y 12
# Dependiendo del mes que sea, el día debe estar 
# dentro de los limites válidos.
# Los meses que tienen 31 días son:
# 1,3,5,7,8,10,12.
# Los meses que tienen 30 días son:
# 4,6,9,11.
# El mes de 28 días es 2, excepto en un año bisiesto
# que es 29 días.

f=input("Introduce fecha (dd:mm:aaaa) ")
d=int(f[:2])
m=int(f[3:5])
a=int(f[6:])

if m <= 0 or m > 12 or d <= 0 or d > 31 or a <= 0:
    print('fecha no valida')
elif m in [1, 3, 5, 7, 8, 10, 12]:
    if d <= 31 and d >= 1:
        print ('La fecha ', d, ':', m ,':', a, "es valida")
    else:
        print ('La fecha ', d, ':', m ,':', a, "no es valida")
elif m in [4, 6, 9, 11]:
    if d <= 30 and d >= 1:
        print ('La fecha ', d, ':', m ,':', a, "es valida")
    else:
        print ('La fecha ', d, ':', m ,':', a, "no es valida")

elif m == 2 and a % 4 == 0 and (not(a % 100 == 0) or a % 400 == 0):
    if d <= 29 and d >= 1:
        print ('La fecha ', d, ':', m ,':', a, "es valida")
    else:
        print ('La fecha ', d, ':', m ,':', a, "no es valida")
elif m == 2:
    if d <= 28 and d >= 1:
        print ('La fecha ', d, ':', m ,':', a, "es valida")
    else:
        print ('La fecha ', d, ':', m ,':', a, "no es valida")
else:
    print ('La entrada ', d, ':', m ,':', a, "no es valida")
# Dada la fecha de hoy calcular el dia siguiente
# Suponer que el año no es Bisiesto

d= int(input('Escriba un dia:'))
m= int(input('Escriba un mes:'))
a= int(input('Escriba un año:'))


if m <= 0 or m > 12 or d <= 0 or d > 31 or a < 0:
    print('fecha no valida')
elif m in [1, 3, 5, 7, 8, 10, 12]:
    if d == 31 and m == 12:
        a += 1
        m = 1
        d = 1
    elif d == 31 and m != 12:
        m += 1
        d = 1
    else:
        d += 1
    print ('El siguiente dia es el', d, '/', m ,'/', a)
elif m in [4, 6, 9, 11] and d <= 30:
    if d == 30:
        m += 1
        d = 1
    else:
        d += 1
    print ('El siguiente dia es el', d, '/', m ,'/', a)
#Esta linea habilita el calculo de años bisiestos.
elif m == 2 and a % 4 == 0 and (not(a % 100 == 0) or a % 400 == 0):
    if d == 29:
        m += 1
        d =1
    else:
        d += 1
    print ('El siguiente dia es el', d, '/', m ,'/', a)
elif m == 2 and d <= 28:
    if d == 28:
        m += 1
        d = 1
    else:
        d += 1
    print ('El siguiente dia es el', d, '/', m ,'/', a)
else:
    print('fecha no valida')
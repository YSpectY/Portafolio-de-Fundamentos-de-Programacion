# calcular el promedio de un alumno que tiene 7  calificaciones de calculo 


n = 7
suma = 0
for i in range(n):
    nota = float(input('Ingrese nota ' + str(i+1) + ':'))
    suma = suma + nota

promedio = suma/n

print('Promedio:', promedio)
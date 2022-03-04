# suponga que se tiene un conjunto de calificaciones de un grupo de 10 alumnos.
# realize un programa para calcular la calificacion media y la calificacion mas baja.
import sys
N=3
calif_media = 0
calif_baja = sys.maxsize
for i in range(N):
    suma = float(input('Ingrese nota del estudiante #' + str(i+1) + ':'))
    calif_media += suma
    if suma < calif_baja:
         calif_baja = suma
        

print('La media aritmetica de', calif_media, 'es:', calif_media/N)

print('La calificacion mas baja es:', calif_baja)
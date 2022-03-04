# calcularde la suma  y media aritmetica de N numeros reales.
# Solicitar el valor de N al usuario y cada uno de los N numeros reales

N= int(input('ingrese cuantos valores va a calcular:'))
media = 0
for i in range(N):
    suma = int(input('Ingrese un numero real:'))
    media += suma
    

print('La media aritmetica de', media, 'es:', media/N)


# 2.- Escribir un programa que solicite un valor entero al usuario 
# y determine si es positivo o negativo.

num =int(input('Ingrese un numero entero:'))

if num > 0:
    print(num, 'es positivo')
elif num < 0:
    print(num,'es negativo')
else:
    print ('el numero es =', num)
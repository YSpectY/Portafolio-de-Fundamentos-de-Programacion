# 5.- Calcular el mayor de tres números enteros introducidos por teclado.

# entrada
num1 = int(input('Numero#1:'))
num2 = int(input('Numero#2:'))
num3 = int(input('Numero#3:'))

if num1 >= num2 and num1 >= num3:
    print(num1, 'es el mayor')
elif num2 >= num1 and num2 >= num3:
    print(num2, 'es el mayor')
elif num3 >= num1 and num3 >= num2:
    print(num3, 'es el mayor')
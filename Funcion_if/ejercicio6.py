# Calcular el mayor de cuatro numeros enteros intruducidos por teclado
num1 = int(input('Ingrese un numero:'))
num2 = int(input('Ingrese un segundo numero:'))
num3 = int(input('Ingrese un tercer numero:'))
num4 = int(input('Ingrese un cuarto numero:'))

if num3 < num4:
    num3, num4 = num4, num3

if num2 < num4:
    num2, num4 = num4, num2

if num2 < num3:
    num2, num3 = num3, num2

if num1 < num2:
    num1, num2 = num2, num1

if num2 < num3:
    num2, num3 = num3, num2

if num3 < num4:
    num3, num4 = num4, num3


print(num1)
print(num2)
print(num3)
print(num4)
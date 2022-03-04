# calcular el mayor de dor numero enteros intrudocidos por teclado

num1 = int(input('Ingrese un numero:'))
num2 = int(input('Ingrese un segundo numero:'))

if num1 > num2:
    print('el numero mayor es:', num1)
elif num2 > num1:
    print('el numero mayor es:', num2)
else:
    print('los numeros son iguales')
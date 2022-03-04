# pedir al usuario un valor. si es positivo
# pedir un segundo valor y calcular la suma, resta y producto de ambos

num1 = int(input('Ingrese un numero:'))
if num1 > 0:
    num2 = int(input('ingrese un segfundo valor:'))
    print('la suma de los valores es:', num1 + num2)
    print('la resta de los valores es:', num1 - num2)
    print('el producto de los valores es:', num1 * num2)
else:
    print('el numero es negativo o cero')
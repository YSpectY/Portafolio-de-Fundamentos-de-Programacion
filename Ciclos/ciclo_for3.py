# Calcular e imprimir la tabla de multiplicar de un numero cualquiera.
# Imprimir el, el multiplicado y el producto

numero = int (input ('Ingrese un numero:'))

for i in range (1, 13):
    resultado = i * numero
    print( i, '*', numero,'=',resultado)
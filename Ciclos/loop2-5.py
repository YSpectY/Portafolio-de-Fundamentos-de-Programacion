# leer 10 numeros e imprimir solamente los  numeros positivos.

n = 10
for i in range(n):
    result = int(input('Ingrese numero:' ))
    if result > 0:
        print(result)
    else:
        print (result, 'No es positivo')

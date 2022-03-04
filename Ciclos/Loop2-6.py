# leer 5 numeros e imprimir cuantos son positivos , negativos y neutros

positivo=0; negativo=0; neutro=0
n=5
for i in range(n):
    if i > 0:
        positivo += 1
    elif i < 0:
        negativo += 1
    else:
        neutro += 1

print('Total de positivos:', positivo)
print('Total de negativos:', negativo)
print('Total de neutros:', neutro)
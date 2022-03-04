# 1.7. Determinar en que estado está el agua en función de su temperatura. 
# Si es negativa el estado será sólido, si es menor que 100 será líquido
# y si es mayor que 100 será gas. Pedir al usuario el valor de la temperatura.

agua_temp = int(input('Ingrese la temperatura:'))

if agua_temp < 0:
    print('El agua esta en estado solido')
elif agua_temp >= 0 and agua_temp <= 100:
    print('El agua esta en estado liquido')
elif agua_temp > 100:
    print('El agua esta en estado gaseoso')
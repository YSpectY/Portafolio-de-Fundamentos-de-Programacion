a = 4; b = 3

#  a^2 + b^2
result = (a ** 2) + (b ** 2)
print('a^2 + b^2=', result)

#  (a+b)^2
result = (a+b) ** 2
print('(a+b)^2=', result)

# b^1/3 + 34
def resultado_raiz_cubica(x):
    if x < 0:
        x = abs(x)
        raiz_cubica = pow(x,1/3)*(-1)
    else:
        raiz_cubica = pow(x,1/3)

    return raiz_cubica
result = resultado_raiz_cubica(b) + 34

print('b^1/3 + 34=', result)

# (b + 34a)^1/3
result = (b + 34 * a)

print('(b + 34a)^1/3=',resultado_raiz_cubica(result))
a = 2; b = -3; c= 0
r1 = a > b and a > c
r2 = (a == 2 and b > 0) or (c == a or a >= 2)
r2 = not not r2
print(r1)
print(r2)
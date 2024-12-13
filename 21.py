from math import exp, cos, sin

x, y, z = map(float, input().split())  
a = (1 + y) * (x + y / (x ** 2 + 4)) / (exp(-x - 2) + 1 / (x ** 2 + 4))  
b = (1 + cos(y - 2)) / (x ** 4 / 2 + sin(z))  
print(a, b)

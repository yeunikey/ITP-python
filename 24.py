from math import sin, cos, atan

x, y, z = map(float, input().split())  
a = (1 + sin(x + y) ** 2) / (2 + abs(x - 2 * x / (1 + x ** 2 * y ** 2))) + x  
b = cos(atan(1 / z)) ** 2  
print(a, b)

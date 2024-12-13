from math import cos, sin

x, y, z = map(float, input().split())  
a = (2 * cos(x - 3.14159 / 6)) / (0.5 + sin(y) ** 2)  
b = 1 + z ** 2 / (3 + z ** 2 / 5)  
print(a, b)

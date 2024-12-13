from math import tan

x, y, z = map(float, input().split())  
a = y + x / (y ** 2 + x ** 3 / 3)  
b = 1 + tan(z / 2) ** 2  
print(a, b)

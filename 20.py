from math import exp

x, y, z = map(float, input().split())  
a = (3 + exp(y - 1)) / (1 + x ** 2 * abs(y - z))  
b = 1 + abs(y - x) * ((y - x) / 2 + abs(y - x) ** 3)  
print(a, b)

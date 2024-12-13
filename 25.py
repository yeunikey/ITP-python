from math import log, sqrt

x, y, z = map(float, input().split())  
a = log(abs(y - sqrt(abs(x)))) * (x - y / (z + x ** 2 / 4))  
b = x - x ** 2 / 6 + x ** 5 / 120  
print(a, b)

from math import sqrt

x1, y1, x2, y2, x3, y3 = map(float, input().split())  
a = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  
b = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)  
c = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)  
P = a + b + c  
print(P)

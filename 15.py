x, y = map(float, input().split())  
result = (abs(x) + abs(y)) / (1 + abs(x * y))  
print(result)

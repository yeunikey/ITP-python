n = int(input())  
D = n // 86400  
n %= 86400  
HH = n // 3600  
n %= 3600  
MM = n // 60  
SS = n % 60  
print(D, HH, MM, SS)

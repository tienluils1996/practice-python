import math
n = int(input("nhap n:"))
S = 0
i = n
while(i >=1):
    S = math.sqrt(i + S)
    i = i-1
print(S)

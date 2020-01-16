import math
n = int(input("nhap n:"))
S = 0
i = 1
while(i <= n):
    S = math.sqrt(2+S)
    i = i+1
print(S)

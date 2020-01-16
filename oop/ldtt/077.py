import math
n = int(input("nhap n:"))
k = int(input("nhap k:"))
S = 0
i = 1
while(i <= n):
    S = S + math.pow(i, k)
    i = i+1
print(S)

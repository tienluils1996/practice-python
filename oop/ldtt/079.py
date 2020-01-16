import math
n = int(input("nhap n:"))
S = 0
T = 1
i = 1
while(i <= n):
    T = T*i
    S = S + i*T
    i = i+1
print(S)

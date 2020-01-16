import math
n = int(input("nhap n:"))
x = int(input("nhap x:"))
S = 0
T = 1
i = 1
while(i <= n):
    T = T*math.sin(x)
    S = S + T
    i = i+1
print(S)

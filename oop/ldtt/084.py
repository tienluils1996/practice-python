import math
n = int(input("nhap n:"))
x = int(input("nhap x:"))
S = 0
T = x
i = 1
while(i <= n):
    T = math.sin(T)
    S = S + T
    i = i+1
print(S)

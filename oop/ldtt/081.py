import math
n = int(input("nhap n:"))
x = int(input("nhap x:"))
S = 1/x
M = x
i = 1
while(i <= n):
    M = M*(x+1)
    S = S+1/M
    i = i+1
print(S)

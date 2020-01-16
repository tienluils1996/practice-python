n = int(input("nhap n:"))
x = int(input("nhap x:"))
S = 1 + x
T = x
M = 1
i = 3
while(i <= 2*n + 1):
    T = T*x*x
    M = M * i * (i-1)
    S = S + T/M
    i = i+2
print(S)

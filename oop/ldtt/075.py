n = int(input("nhap n:"))
x = int(input("nhap x:"))
S = 1
T = 1
M = 1
i = 2
while(i <= 2*n):
    T = T*x
    M = M * i * (i-1)
    S = S + T/M
    i = i+2
print(S)
